import pytest

from pixelbench.core.color import Color, Palette, parse_hex


def test_parse_hex_variants():
    assert parse_hex("#f00") == (255, 0, 0, 255)
    assert parse_hex("#ff0000") == (255, 0, 0, 255)
    assert parse_hex("#ff000080") == (255, 0, 0, 128)
    assert parse_hex("ff0000") == (255, 0, 0, 255)
    with pytest.raises(ValueError):
        parse_hex("not-a-color")


def test_palette_register_and_resolve():
    p = Palette()
    cid = p.register("red", (255, 0, 0, 255))
    assert cid == 0
    assert p._resolve_id("red") == 0
    assert p._resolve_id(0) == 0
    assert p._resolve_id("#ff0000") == 0
    assert p._resolve_id((255, 0, 0, 255)) == 0
    assert p._resolve_id((255, 0, 0)) == 0  # 3-tuple padded
    with pytest.raises(ValueError):
        p._resolve_id("nope")
    with pytest.raises(ValueError):
        p._resolve_id("#00ff00")  # different value, not registered


def test_palette_duplicate_names_rejected():
    p = Palette()
    p.register("red", (255, 0, 0, 255))
    with pytest.raises(ValueError):
        p.register("red", (0, 0, 255, 255))


def test_palette_replace():
    p = Palette()
    cid = p.register("red", (255, 0, 0, 255))
    p.replace("red", (0, 0, 255, 255))
    assert p.color("red").rgba == (0, 0, 255, 255)
    assert p.color(cid).name == "red"


def test_palette_serialization_roundtrip():
    p = Palette()
    p.register("outline", (18, 18, 18, 255))
    p.register("transparent", (0, 0, 0, 0))
    p2 = Palette.from_dict(p.to_dict())
    assert p2.names() == p.names()
    assert p2.color("outline").rgba == (18, 18, 18, 255)
