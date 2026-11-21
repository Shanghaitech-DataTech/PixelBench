import numpy as np
import pytest

from pixelbench.core import shapes


def m():
    return np.zeros((16, 16), dtype=np.int32)


def test_bresenham_horizontal_vertical_diagonal():
    assert shapes.bresenham(0, 0, 5, 0) == [(i, 0) for i in range(6)]
    assert shapes.bresenham(0, 0, 0, 5) == [(0, i) for i in range(6)]
    assert len(shapes.bresenham(0, 0, 5, 5)) == 6


def test_draw_line_endpoints():
    a = m()
    n = shapes.draw_line(a, 2, 3, 8, 3, 7)
    assert n == 7
    assert a[3, 2] == 7 and a[3, 8] == 7
    assert a[3, 4] == 7


def test_fill_rect_clips():
    a = m()
    n = shapes.fill_rect(a, -2, -2, 6, 6, 1)  # partially off-canvas
    assert n == 4 * 4
    assert a[0, 0] == 1


def test_circle_symmetry():
    a = m()
    shapes.draw_circle(a, 8, 8, 4, 1)
    pts = shapes.circle_points(8, 8, 4)
    for x, y in pts:
        assert a[y, x] == 1
    # axis-aligned points of radius 4 are on the ring
    assert a[8 + 4, 8] == 1 and a[8 - 4, 8] == 1
    assert a[8, 8 + 4] == 1 and a[8, 8 - 4] == 1
    # every painted pixel lies within ~1px of the ideal radius
    for x, y in pts:
        d = abs((x - 8) ** 2 + (y - 8) ** 2 - 16)
        assert d <= 8, (x, y, d)


def test_filled_circle():
    a = m()
    n = shapes.draw_circle(a, 8, 8, 5, 1, filled=True)
    assert n == a[a == 1].size
    # center filled
    assert a[8, 8] == 1


def test_ellipse_filled_area():
    a = m()
    shapes.draw_ellipse(a, 8, 8, 6, 3, 1, filled=True)
    assert a[8, 8] == 1
    assert a.sum() > 0


def test_polygon_fill_even_odd():
    a = m()
    pts = [(3, 3), (12, 3), (12, 12), (3, 12)]
    shapes.draw_polygon(a, pts, 1, filled=True)
    assert a[5, 5] == 1
    assert a[3, 3] == 1
    assert a[0, 0] == 0


def test_flood_fill_4conn():
    a = m()
    a[2:8, 2:8] = 1
    n = shapes.flood_fill(a, 3, 3, 9)
    assert n == 36
    assert (a[2:8, 2:8] == 9).all()
    assert a[1, 2] == 0
    with pytest.raises(ValueError):
        shapes.flood_fill(a, 99, 99, 9)


# ------------------------------------------------------------------ paths
def test_parse_path_absolute():
    segs = shapes.parse_path("M 1 2 L 3 4 H 5 V 6 Z")
    assert segs[0] == ("M", 1.0, 2.0)
    assert segs[1] == ("L", 3.0, 4.0)
    assert segs[2] == ("H", 5.0)
    assert segs[3] == ("V", 6.0)
    assert segs[4] == ("Z",)


def test_parse_path_relative():
    segs = shapes.parse_path("m 1 2 l 3 4 h 5 v 6")
    assert segs[0] == ("m", 1.0, 2.0)
    assert segs[2] == ("h", 5.0)
    assert segs[3] == ("v", 6.0)


def test_parse_path_errors():
    with pytest.raises(shapes.PathError):
        shapes.parse_path("")
    with pytest.raises(shapes.PathError):
        shapes.parse_path("M 1")


def test_flatten_path_relative_and_curves():
    pts = shapes.flatten_path("m 0 0 l 10 0 l 0 10 z")
    assert pts[0] == (0.0, 0.0)
    assert pts[1] == (10.0, 0.0)
    assert pts[-1] == (0.0, 0.0)  # closed
    cubic = shapes.flatten_path("M 0 0 C 5 0, 5 10, 10 10", curve_steps=10)
    assert len(cubic) == 11
    assert cubic[0] == (0.0, 0.0) and cubic[-1] == (10.0, 10.0)


def test_flatten_arc():
    pts = shapes.flatten_path("M 0 0 A 5 5 0 0 1 10 0", curve_steps=16)
    assert len(pts) == 17
    assert pts[0] == (0.0, 0.0)
    assert pts[-1] == pytest.approx((10.0, 0.0))


def test_draw_path_rect():
    a = m()
    n = shapes.draw_path(a, "M 2 2 L 10 2 L 10 8 L 2 8 Z", 1, filled=True, origin=(0, 0))
    assert n > 0
    assert a[5, 5] == 1
    assert a[0, 0] == 0
