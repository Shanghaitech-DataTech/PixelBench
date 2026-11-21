import math

W, H = 48, 48
c = new_canvas(W, H, background=None, name="result")

# Cool white / cyan slash palette
GLOW = "#2FA8E0"      # outer cyan-blue edge
MID = "#9FE8FF"       # pale cyan
CORE = "#FFFFFF"      # hot white core
TRAIL_OUT = "#2A9FD6" # trailing streak edge
TRAIL_IN = "#BFF4FF"  # trailing streak highlight
SPARK = "#EAFBFF"


def _rot(x, y, ang):
    ca, sa = math.cos(ang), math.sin(ang)
    return x * ca - y * sa, x * sa + y * ca


def _arc_frame(cx, cy, rx, ry, theta, rot):
    x = rx * math.cos(theta)
    y = ry * math.sin(theta)
    x, y = _rot(x, y, rot)
    return cx + x, cy + y


def _cross_section(cx, cy, rx, ry, theta, rot):
    """Return center point and unit normal of the ellipse at theta."""
    eps = 1e-4
    x0, y0 = _arc_frame(cx, cy, rx, ry, theta - eps, rot)
    x1, y1 = _arc_frame(cx, cy, rx, ry, theta + eps, rot)
    tx, ty = x1 - x0, y1 - y0
    tl = math.hypot(tx, ty)
    if tl < 1e-9:
        return (cx, cy), (0.0, 1.0)
    tx, ty = tx / tl, ty / tl
    # normal
    nx, ny = -ty, tx
    x, y = _arc_frame(cx, cy, rx, ry, theta, rot)
    return (x, y), (nx, ny)


def draw_band(c, cx, cy, rx, ry, a0, a1, rot, thick, colour,
              samples=280, profile="symmetric", t0=0.0, t1=1.0,
              dash=None):
    """Draw a smoothly tapered arc band along an ellipse.

    a0/a1/rot are radians.  thick is the maximum total width in pixels.
    dash may be a list of (start,end) fractions within t0..t1.
    """
    for i in range(samples + 1):
        t = i / samples
        if t < t0 or t > t1:
            continue
        if dash is not None:
            keep = False
            for d0, d1 in dash:
                if d0 <= t <= d1:
                    keep = True
                    break
            if not keep:
                continue
        theta = a0 + (a1 - a0) * t
        (x, y), (nx, ny) = _cross_section(cx, cy, rx, ry, theta, rot)
        if profile == "symmetric":
            w = thick * (math.sin(math.pi * t) ** 0.62)
        elif profile == "trail":
            # grows from the outer tail toward the main arc
            w = thick * (t ** 0.55)
        elif profile == "lead":
            # thick near the start, tapering to the end
            w = thick * ((1.0 - t) ** 0.55)
        elif profile == "flat":
            w = thick * min(1.0, 3.0 * min(t, 1.0 - t))
        else:
            w = thick
        if w < 0.18:
            continue
        x0 = int(round(x - nx * w * 0.5))
        y0 = int(round(y - ny * w * 0.5))
        x1 = int(round(x + nx * w * 0.5))
        y1 = int(round(y + ny * w * 0.5))
        # Keep the rasteriser inside the canvas without losing the band shape.
        x0 = max(0, min(W - 1, x0))
        y0 = max(0, min(H - 1, y0))
        x1 = max(0, min(W - 1, x1))
        y1 = max(0, min(H - 1, y1))
        c.line(x0, y0, x1, y1, colour)


def draw_slash(c, cx, cy, rx, ry, a0_deg, a1_deg, rot_deg, T,
               sample_n=300, trailing=False):
    a0 = math.radians(a0_deg)
    a1 = math.radians(a1_deg)
    rot = math.radians(rot_deg)

    if trailing:
        # Long faint continuation of the arc beyond the upper tip.
        # This is the motion streak left behind by the expanding slash.
        draw_band(c, cx, cy, rx, ry, math.radians(-110), a0, rot,
                  T * 0.38, TRAIL_OUT, samples=130, profile="trail")
        draw_band(c, cx, cy, rx, ry, math.radians(-110), a0, rot,
                  T * 0.17, TRAIL_IN, samples=130, profile="trail")
        # A couple of broken speed dashes further along the same path.
        draw_band(c, cx, cy, rx, ry, math.radians(-130), math.radians(-119), rot,
                  T * 0.18, TRAIL_OUT, samples=30, profile="trail")
        draw_band(c, cx, cy, rx, ry, math.radians(-142), math.radians(-135), rot,
                  T * 0.12, TRAIL_IN, samples=20, profile="trail")

    # Main crescent: dark edge, pale inner band, hot white core.
    draw_band(c, cx, cy, rx, ry, a0, a1, rot, T, GLOW, samples=sample_n)
    draw_band(c, cx, cy, rx, ry, a0, a1, rot, T * 0.78, MID, samples=sample_n)
    draw_band(c, cx, cy, rx, ry, a0, a1, rot, T * 0.52, CORE, samples=sample_n,
              t0=0.055, t1=0.945)


# ---------------------------------------------------------------------------
# Frame 1 (left half): small, simple white arc slash.
# Canvas is treated as two 24x48 frames side by side.
# ---------------------------------------------------------------------------
draw_slash(c, cx=8.8, cy=24.0, rx=5.4, ry=11.2,
           a0_deg=-58, a1_deg=58, rot_deg=-15,
           T=4.0, sample_n=220, trailing=False)

# ---------------------------------------------------------------------------
# Frame 2 (right half): larger arc slash with a trailing streak.
# ---------------------------------------------------------------------------
draw_slash(c, cx=34.5, cy=24.0, rx=7.9, ry=17.4,
           a0_deg=-65, a1_deg=65, rot_deg=-15,
           T=5.8, sample_n=340, trailing=True)

print(c.stats_text())
finish(c)
