"""Two-level palette symbol mapping for the "character art" text format.

Design:
  Level A (<= 86 colors): single chars 0-9 a-z A-Z + lowercase Greek
                          -> 1 char per pixel
  Level B (87-256 colors): two-char lowercase hex 00-ff -> 2 chars per pixel

The two levels share one id->symbol mapping (id<86 single char, id>=86 hex),
so a palette row's symbol length (1 or 2) tells the parser which level a
`````image````` block uses.  Level A is a strict superset of the legacy
36-symbol format (0-9 a-z), so old data keeps working unchanged.

Note: lowercase Greek letters are appended after the 62 ASCII symbols so
Level A covers up to 86 colors with one char per pixel.  Caveat: some Greek
glyphs resemble Latin (omicron o, iota i) and a few (zeta/xi/psi) tokenize
to 2 tokens in older tokenizers (cl100k); widths are still fixed per level.

Everything here is width-fixed per level (ASCII + Greek are all 1 codepoint).
"""
from __future__ import annotations

from typing import Dict, Iterable, List, Sequence, Tuple

# id 0..61 -> ASCII single characters (most frequent colors first); id 62..85
# -> lowercase Greek, so common palettes stay in single-char form.
_GREEK_LOWER = "αβγδεζηθικλμνξοπρστυφχψω"  # 24 letters, no final sigma
SINGLE_SYMBOLS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + _GREEK_LOWER
MAX_SINGLE = len(SINGLE_SYMBOLS)  # 86
MAX_COLORS = 256

# Level A single-char symbol -> id
_SINGLE_TO_ID: Dict[str, int] = {ch: i for i, ch in enumerate(SINGLE_SYMBOLS)}


def symbol_for_id(cid: int) -> str:
    """Return the text symbol for a palette id (0..255)."""
    if cid < 0 or cid >= MAX_COLORS:
        raise ValueError(f"palette id {cid} out of range [0, {MAX_COLORS})")
    if cid < MAX_SINGLE:
        return SINGLE_SYMBOLS[cid]
    return f"{cid:02x}"


def id_for_symbol(sym: str) -> int:
    """Inverse of :func:`symbol_for_id` (accepts either level)."""
    if len(sym) == 1:
        if sym not in _SINGLE_TO_ID:
            raise ValueError(f"unknown single-char symbol {sym!r}")
        return _SINGLE_TO_ID[sym]
    if len(sym) == 2:
        try:
            v = int(sym, 16)
        except ValueError:
            raise ValueError(f"invalid hex symbol {sym!r}") from None
        if v >= MAX_COLORS:
            raise ValueError(f"hex symbol {sym!r} out of range")
        return v
    raise ValueError(f"symbol must be 1 or 2 chars, got {sym!r}")


def palette_block(rgba_colors: Sequence[Tuple[int, int, int, int]]) -> str:
    """Format a palette as ``symbol=#RRGGBBAA`` lines (transparent id 0 first).

    ``rgba_colors`` is the ordered palette (index = palette id).

    Level is uniform per palette: <= 86 colors -> single chars (ASCII +
    lowercase Greek), > 86 colors -> two-char hex for *every* id
    (``00``..``ff``), so the palette width always matches the image block
    width.  The parser detects the level from the first symbol's length.
    """
    wide = len(rgba_colors) > MAX_SINGLE
    lines = []
    for cid, rgba in enumerate(rgba_colors):
        r, g, b, a = (int(v) for v in rgba)
        sym = f"{cid:02x}" if wide else SINGLE_SYMBOLS[cid]
        lines.append(f"{sym}={r:02X}{g:02X}{b:02X}{a:02X}")
    return "\n".join(lines)


def image_block(matrix_rows: Sequence[Sequence[int]], wide: bool | None = None) -> str:
    """Format a canvas as character-art lines.

    ``wide``: True -> two-char hex for every id; False -> single chars;
    None -> auto-detect from the largest id in the matrix.  Callers with a
    known palette level must pass ``wide`` so the image width always matches
    the palette (an 87-color palette with no id>=86 in the matrix must still
    be encoded wide).
    """
    if wide is None:
        wide = any(v >= MAX_SINGLE for row in matrix_rows for v in row)
    lines = []
    for row in matrix_rows:
        if wide:
            lines.append("".join(f"{v:02x}" for v in row))
        else:
            lines.append("".join(SINGLE_SYMBOLS[v] for v in row))
    return "\n".join(lines)


def parse_palette_block(text: str) -> Tuple[List[Tuple[int, int, int, int]], Dict[str, int]]:
    """Parse `````color````` lines into (ordered rgba palette, symbol->id map)."""
    rgba: List[Tuple[int, int, int, int]] = []
    sym_map: Dict[str, int] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("```") or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        sym, _, hexv = line.partition("=")
        sym = sym.strip()
        hexv = hexv.strip().lstrip("#")
        if len(hexv) not in (6, 8):
            raise ValueError(f"bad hex {hexv!r} in palette line {line!r}")
        if len(hexv) == 6:
            hexv += "FF"
        rgba.append(tuple(int(hexv[i : i + 2], 16) for i in (0, 2, 4, 6)))  # type: ignore[return-value]
        sym_map[sym] = id_for_symbol(sym)
    return rgba, sym_map


def parse_image_block(text: str, sym_map: Dict[str, int]) -> List[List[int]]:
    """Parse `````image````` lines into an id matrix, auto-detecting the level.

    Level is determined by the palette symbol width (uniform per palette).
    """
    if not sym_map:
        raise ValueError("empty symbol map")
    width = len(next(iter(sym_map)))
    if any(len(s) != width for s in sym_map):
        raise ValueError("palette symbols have mixed widths; use palette_block() "
                         "which keeps the level uniform")
    matrix = []
    for line in text.splitlines():
        line = line.rstrip()
        if not line or line.startswith("```"):
            continue
        if len(line) % width != 0:
            raise ValueError(f"row length {len(line)} not multiple of symbol width {width}")
        row = []
        for i in range(0, len(line), width):
            sym = line[i : i + width]
            if sym not in sym_map:
                raise ValueError(f"unknown symbol {sym!r} in image block")
            row.append(sym_map[sym])
        matrix.append(row)
    return matrix


def encode_canvas(palette_rgba: Sequence[Tuple[int, int, int, int]],
                  matrix: Sequence[Sequence[int]]) -> str:
    """Full `````color````` + `````image````` text for a palette+matrix.

    The level is determined by the palette size (<=86 single, >86 hex) and
    applied to both blocks so their widths always agree.
    """
    wide = len(palette_rgba) > MAX_SINGLE
    return "```color\n" + palette_block(palette_rgba) + "\n```\n\n```image\n" + \
        image_block(matrix, wide=wide) + "\n```"


def decode_canvas(text: str):
    """Parse a full `````color`````+`````image````` block into (rgba, matrix)."""
    color_part, _, image_part = text.partition("```image")
    rgba, sym_map = parse_palette_block(color_part)
    matrix = parse_image_block(image_part, sym_map)
    return rgba, matrix
