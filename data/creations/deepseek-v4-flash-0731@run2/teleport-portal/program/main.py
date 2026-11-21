import math
from pixelbench_api import new_canvas, flatten, finish

S = 48
glow = new_canvas(S, S, name="halo")
v = new_canvas(S, S, name="vortex")

CX = CY = 24


def pos(r, a):
    return CX + r * math.cos(a), CY + r * math.sin(a)


# ---------- halo (frame 2: glowing halo) ----------
glow.circle(CX, CY, 22, (168, 108, 255, 55))
glow.circle(CX, CY, 20, (184, 128, 255, 90))
glow.circle(CX, CY, 18, (198, 148, 255, 130))

# ---------- vortex body ----------
v.circle(CX, CY, 17, "#1d0939")            # dark void disc
v.circle(CX, CY, 15, "#4a1a8c", fill=False)
v.circle(CX, CY, 13, "#6a27c9", fill=False)
v.circle(CX, CY, 11, "#8f45e0", fill=False)
v.circle(CX, CY, 9, "#b26ef2", fill=False)
v.circle(CX, CY, 7, "#cf9fff", fill=False)


def arm(offset, r0, r1, turns, color, thin):
    N = 140
    pts = []
    for i in range(N + 1):
        t = offset + (i / N) * turns * 2 * math.pi
        r = r0 + (i / N) * (r1 - r0)
        pts.append(pos(r, t))
    for i in range(N):
        a = pts[i]
        b = pts[i + 1]
        if thin:
            v.line(int(round(a[0])), int(round(a[1])), int(round(b[0])), int(round(b[1])), color)
        else:
            v.line(int(round(a[0])), int(round(a[1])), int(round(b[0])), int(round(b[1])), color)
            v.circle(int(round(b[0])), int(round(b[1])), 1, color)


# two main swirling arms with a hint of width
arm(0.0, 2.0, 14.5, 1.75, "#8a3ad9", False)
arm(math.pi, 2.0, 14.5, 1.75, "#8a3ad9", False)
# lighter trailing arms
arm(0.9, 2.0, 11.5, 1.35, "#cd9dff", False)
arm(math.pi + 0.9, 2.0, 11.5, 1.35, "#cd9dff", False)
# bright thin sweeps near the core
arm(0.45, 1.5, 7.5, 1.0, "#f2e7ff", True)
arm(math.pi + 0.45, 1.5, 7.5, 1.0, "#f2e7ff", True)

# ---------- core ----------
v.circle(CX, CY, 4, "#bf8fff")
v.circle(CX, CY, 2, "#efe0ff")
v.set(CX, CY, "#ffffff")

# ---------- sparkles ----------
for a, r in [(0.5, 18.5), (1.9, 19.0), (3.2, 18.2), (4.4, 19.3), (5.6, 18.6)]:
    x, y = pos(r, a)
    v.set(int(round(x)), int(round(y)), "#e6ccff")
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        v.set(int(round(x)) + dx, int(round(y)) + dy, "#f5ecff")

result = flatten([glow, v], name="teleport_portal")
print(result.stats_text())
finish(result)
