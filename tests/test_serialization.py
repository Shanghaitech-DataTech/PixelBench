from pixelbench.core.canvas import PixelCanvas
from pixelbench.core.serialization import from_pixel_json, loads_pixel_json, to_pixel_json


def test_pixel_json_roundtrip():
    c = PixelCanvas(12, 8)
    c.register_color("outline", "#181818")
    c.register_color("skin", "#e8b98a")
    c.paint_rect(2, 2, 6, 4, "skin")
    c.stroke_rect(2, 2, 6, 4, "outline")
    d = to_pixel_json(c, id_="test_01", metadata={"asset_type": "sprite"})
    assert d["version"] == "pixelbench-v0"
    assert d["id"] == "test_01"
    assert d["width"] == 12 and d["height"] == 8
    assert d["canvas"][3][3] == c.palette._resolve_id("skin")  # interior pixel
    c2 = from_pixel_json(d)
    assert c2.width == 12 and c2.height == 8
    assert c2.palette.names() == c.palette.names()
    assert c2.matrix.tolist() == c.matrix.tolist()


def test_loads_dumps():
    c = PixelCanvas(4, 4)
    c.register_color("red", "#ff0000")
    c.paint_rect(0, 0, 2, 2, "red")
    s = to_pixel_json(c)
    import json

    c2 = loads_pixel_json(json.dumps(s))
    assert c2.matrix.tolist() == c.matrix.tolist()
