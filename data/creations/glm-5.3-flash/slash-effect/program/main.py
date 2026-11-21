import math

W = H = 48
c = new_canvas(W, H, background=None, name="slash_effect")

WHITE = "#FFFFFF"
PALE = "#CFE6FF"
MID = "#9CC3EA"
DIM = "#5E86AD"


def band(canvas, cx, cy, r, a0, a1, tmax, col_fn, min_t=1.1):
    """Crescent band around radius r sweeping a0..a1 degrees (screen angles,
    y down). Thick in the middle, tapering toward both tips. col_fn(u, frac)
    picks the colour; u = 0 inner edge -> 1 outer edge."""
    pad = tmax / 2 + 2
    x0 = max(0, int(cx - r - pad)); x1 = min(W - 1, int(cx + r + pad))
    y0 = max(0, int(cy - r - pad)); y1 = min(H - 1, int(cy + r + pad))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            dx = x - cx
            dy = y - cy
            d = math.hypot(dx, dy)
            if abs(d - r) > tmax / 2:
                continue
            a = math.degrees(math.atan2(dy, dx)) % 360.0
            if not (a0 <= a <= a1):
                continue
            frac = (a - a0) / float(a1 - a0)
            t = tmax * (0.30 + 0.70 * math.sin(math.pi * frac))
            if t < min_t:
                continue
            if abs(d - r) > t / 2:
                continue
            u = (d - (r - t / 2)) / t
            col = col_fn(u, frac)
            if col is not None:
                canvas.set(x, y, col)
    return canvas


def streak(canvas, px, py, ang, length, t0, col_fn):
    """Tapering capsule from (px, py) along ang degrees, thinning and fading
    toward the tail."""
    dx = math.cos(math.radians(ang))
    dy = math.sin(math.radians(ang))
    nx, ny = -dy, dx
    xs = [px, px + dx * length]
    ys = [py, py + dy * length]
    x0 = max(0, int(min(xs) - t0 - 2)); x1 = min(W - 1, int(max(xs) + t0 + 2))
    y0 = max(0, int(min(ys) - t0 - 2)); y1 = min(H - 1, int(max(ys) + t0 + 2))
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            rx = x - px
            ry = y - py
            s = rx * dx + ry * dy
            if s < -0.5 or s > length + 0.5:
                continue
            v = rx * nx + ry * ny
            frac = min(1.0, max(0.0, s / length))
            t = max(1.4, t0 * (1.0 - 0.75 * frac))
            if abs(v) > t / 2:
                continue
            col = col_fn(frac)
            if col is not None:
                canvas.set(x, y, col)
    return canvas


# ---- frame 1 (rows 0-23): small white arc slash ----
band(c, 24, 18, 10, 205, 335, 4.2,
     lambda u, f: WHITE if u >= 0.22 else PALE)

# ---- frame 2 (rows 24-47): larger arc slash + trailing streak ----
band(c, 24, 46, 15, 210, 330, 6.0,
     lambda u, f: WHITE if u >= 0.45 else (PALE if u >= 0.18 else MID))
# streak whipping off the leading tip, fading as it travels
streak(c, 37.0, 38.5, 60, 9.0, 2.6,
       lambda f: WHITE if f < 0.15 else (PALE if f < 0.45 else (MID if f < 0.72 else DIM)))

print(c.stats_text())
print("FRAME 1:")
print(c.matrix_text(region=(0, 0, 47, 23)))
print("FRAME 2:")
print(c.matrix_text(region=(0, 24, 47, 47)))

save("slash_effect", c)
finish(c)
