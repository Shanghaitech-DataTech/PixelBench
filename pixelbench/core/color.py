"""Palette and color handling.

PixelBench's primary format is ``palette + integer-id matrix``: every
cell of the canvas stores a palette *id*, never raw RGB.  This makes
palette discipline, color replacement, pick-color and region
consistency checks straightforward.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Tuple, Union

HEX_RE = re.compile(r"^#?(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")


def parse_hex(value: str) -> Tuple[int, int, int, int]:
    """Parse ``#rgb``, ``#rrggbb`` or ``#rrggbbaa`` into an RGBA tuple."""
    v = str(value).strip().lstrip("#")
    if len(v) == 3:
        v = "".join(c * 2 for c in v) + "FF"
    elif len(v) == 6:
        v += "FF"
    if len(v) != 8:
        raise ValueError(f"invalid hex color: {value!r}")
    return tuple(int(v[i : i + 2], 16) for i in (0, 2, 4, 6))  # type: ignore[return-value]


def hex_of(rgba: Tuple[int, int, int, int]) -> str:
    r, g, b, a = rgba
    return f"#{r:02x}{g:02x}{b:02x}{a:02x}"


@dataclass(frozen=True)
class Color:
    id: int
    name: str
    rgba: Tuple[int, int, int, int] = (0, 0, 0, 0)

    def to_hex(self) -> str:
        return hex_of(self.rgba)

    def __str__(self) -> str:  # noqa: D105
        return f"{self.name}@{self.to_hex()}"


TRANSPARENT_NAME = "transparent"


class Palette:
    """Ordered, name-indexed palette of :class:`Color`."""

    def __init__(self, colors: Optional[Iterable[Color]] = None, max_colors: Optional[int] = None) -> None:
        self._by_id: Dict[int, Color] = {}
        self._by_name: Dict[str, int] = {}
        self._next_id = 0
        self.max_colors = int(max_colors) if max_colors is not None else None
        if colors:
            for c in colors:
                self._add(c)
        if self.max_colors is not None and len(self._by_id) > self.max_colors:
            raise ValueError(
                f"palette already has {len(self._by_id)} colors, exceeding max_colors={self.max_colors}"
            )

    # -- construction ---------------------------------------------------
    def _add(self, color: Color) -> None:
        if color.id in self._by_id:
            raise ValueError(f"duplicate palette id {color.id}")
        if color.name in self._by_name:
            raise ValueError(f"duplicate palette name {color.name!r}")
        self._by_id[color.id] = color
        self._by_name[color.name] = color.id
        self._next_id = max(self._next_id, color.id + 1)

    def _check_limit(self, name: str) -> None:
        """Raise before registering a *new* color past ``max_colors``."""
        if self.max_colors is None:
            return
        if len(self._by_id) >= self.max_colors:
            raise ValueError(
                f"palette limit reached: max {self.max_colors} colors "
                f"(already registered {len(self._by_id)}); cannot register {name!r} — "
                f"reuse an existing color or replace_color() an existing one"
            )

    def register(self, name: str, rgba: Tuple[int, int, int, int]) -> int:
        """Add a color and return its new id.  Names must be unique."""
        name = name.strip()
        if not name:
            raise ValueError("color name must not be empty")
        if name in self._by_name:
            raise ValueError(
                f"color name {name!r} already exists (id {self._by_name[name]}); "
                "use replace_color() or a different name"
            )
        self._check_limit(name)
        cid = self._next_id
        self._add(Color(id=cid, name=name, rgba=tuple(rgba)))
        return cid

    def replace(self, old: Union[int, str], rgba: Tuple[int, int, int, int]) -> Color:
        cid = self._resolve_id(old)
        new = Color(id=cid, name=self._by_id[cid].name, rgba=tuple(rgba))
        self._by_id[cid] = new
        self._by_name[new.name] = cid
        return new

    # -- lookup ---------------------------------------------------------
    def _resolve_id(self, ref: Union[int, str, Tuple[int, int, int, int]]) -> int:
        """Resolve a color reference (id, name, or rgba/hex string) to an id."""
        if isinstance(ref, bool):
            raise ValueError(f"invalid color reference: {ref!r}")
        if isinstance(ref, int):
            if ref not in self._by_id:
                raise ValueError(f"unknown palette id {ref}; known ids: {sorted(self._by_id)}")
            return ref
        if isinstance(ref, str):
            if ref in self._by_name:
                return self._by_name[ref]
            # allow hex if it matches an existing color's value
            try:
                rgba = parse_hex(ref)
            except ValueError:
                raise ValueError(
                    f"unknown color name {ref!r}; registered names: {sorted(self._by_name)}"
                )
            for c in self._by_id.values():
                if c.rgba == rgba:
                    return c.id
            raise ValueError(
                f"color {ref!r} is not registered; use register_color(name, '{ref}') first"
            )
        if isinstance(ref, (tuple, list)) and len(ref) in (3, 4):
            rgba = tuple(int(c) for c in ref)
            if len(rgba) == 3:
                rgba = (rgba[0], rgba[1], rgba[2], 255)
            for c in self._by_id.values():
                if c.rgba == rgba:
                    return c.id
            raise ValueError(
                f"color {ref!r} is not registered; use register_color(name, ...) first"
            )
        raise ValueError(f"invalid color reference: {ref!r}")

    def color(self, ref: Union[int, str, Tuple[int, int, int, int]]) -> Color:
        return self._by_id[self._resolve_id(ref)]

    def __getitem__(self, cid: int) -> Color:
        return self._by_id[cid]

    def __contains__(self, ref: object) -> bool:
        try:
            self._resolve_id(ref)  # type: ignore[arg-type]
            return True
        except ValueError:
            return False

    def __len__(self) -> int:
        return len(self._by_id)

    def __iter__(self):
        return iter(self._by_id.values())

    def copy(self) -> "Palette":
        """Deep copy: independent dicts and Color entries."""
        return Palette(
            (Color(id=c.id, name=c.name, rgba=c.rgba) for c in self._by_id.values()),
            max_colors=self.max_colors,
        )

    def ids(self) -> List[int]:
        return sorted(self._by_id)

    def names(self) -> List[str]:
        return sorted(self._by_name)

    def add_if_absent(self, name: str, rgba: Tuple[int, int, int, int]) -> int:
        if name in self._by_name:
            return self._by_name[name]
        return self.register(name, rgba)

    # -- views ----------------------------------------------------------
    def summary(self) -> str:
        lines = [f"palette ({len(self)} colors):"]
        for cid in self.ids():
            c = self._by_id[cid]
            lines.append(f"  {cid:>3}  {c.name:<16} {c.to_hex()}")
        return "\n".join(lines)

    def to_dict(self) -> List[dict]:
        return [{"id": c.id, "name": c.name, "rgba": list(c.rgba)} for c in self._by_id.values()]

    @classmethod
    def from_dict(cls, entries: Iterable[dict]) -> "Palette":
        pal = cls()
        for e in entries:
            rgba = tuple(int(v) for v in e["rgba"])
            pal._add(Color(id=int(e["id"]), name=str(e["name"]), rgba=rgba))
        return pal
