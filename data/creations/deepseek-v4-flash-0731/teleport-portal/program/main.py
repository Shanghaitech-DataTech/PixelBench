import math
from pixelbench_api import *

W = H = 48
c = new_canvas(W, H, name="teleport_portal")

# --- palette (purple family) ---
deep   = c.color((18, 4, 42), "deep")
dark   = c.color((44, 13, 82), "dark")
vio    = c.color((90, 30, 152), "violet")
purple = c.color((145, 62, 232), "purple")
bright = c.color((190, 122, 250), "bright")
mag    = c.color((226, 152, 252), "magenta")
light  = c.color((242, 224, 255), "light")
white  = c.color((255, 252, 255), "white")
glo1   = c.color((198, 145, 252, 150), "glow1")
glo2   = c.color((226, 192, 252, 90), "glow2")
glo3   = c.color((244, 228, 255, 55), "glow3")

grad = [deep, dark, vio, purple, bright, mag]


def draw_swirl(cv, cx, cy, rx, ry, rot):
    arms = 3
    steps = 120
    turns = 1.7
    for arm in range(arms):
        for k in range(steps + 1):
            t = k / steps
            th = rot + arm * (2 * math.pi / arms) + t * turns * 2 * math.pi
            f = 0.14 + 0.86 * t
            x = cx + rx * f * math.cos(th)
            y = cy + ry * f * math.sin(th)
            rad = 1 if t < 0.45 else 2
            ci = min(len(grad) - 1, int(t * len(grad)))
            cv.circle(int(round(x)), int(round(y)), rad, grad[ci])
    cv.ellipse(cx, cy, 3, 5, deep)
    cv.circle(cx, cy, 1, white)


# --- frame 1: purple energy vortex (left half) ---
f1 = new_canvas(24, 48, name="frame1_vortex")
draw_swirl(f1, 12, 24, 7, 11, 0.0)

# --- frame 2: vortex rotated + glowing halo (right half) ---
f2 = new_canvas(24, 48, name="frame2_vortex_halo")
draw_swirl(f2, 12, 24, 7, 11, 1.9)
f2.ellipse(12, 24, 9, 15, purple, fill=False)
f2.ellipse(12, 24, 10, 16, glo1, fill=False)
f2.ellipse(12, 24, 10, 17, glo2, fill=False)
f2.ellipse(12, 24, 11, 18, glo3, fill=False)
for i in range(8):
    a = i * math.pi / 4 + 0.4
    f2.circle(int(round(12 + 9.5 * math.cos(a))), int(round(24 + 16.5 * math.sin(a))), 1, light)
    f2.circle(int(round(12 + 10.5 * math.cos(a + 0.5))), int(round(24 + 17.5 * math.sin(a + 0.5))), 1, white)

c.blit(f1, 0, 0)
c.blit(f2, 24, 0)

print(c.stats_text())
save("teleport_portal", c)
finish(c)
