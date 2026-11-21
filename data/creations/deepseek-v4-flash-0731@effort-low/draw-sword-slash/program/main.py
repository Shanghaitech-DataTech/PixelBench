from pixelbench_api import *
import math

c = input_canvas
W, H = 62, 72
BLACK = c.color("#020202")

f1 = c.copy(name="f1")
f2 = c.copy(name="f2")

def taper_draw(cv, p0, p1, ctrl, steps=120, r0=3.0, r1=0.8):
    for i in range(steps + 1):
        t = i / steps
        u = 1 - t
        x = u*u*p0[0] + 2*u*t*ctrl[0] + t*t*p1[0]
        y = u*u*p0[1] + 2*u*t*ctrl[1] + t*t*p1[1]
        r = r0 + (r1 - r0) * t
        cv.circle(int(round(x)), int(round(y)), max(1, int(round(r))), BLACK, fill=True)

# main sweeping trail: from left-hand grip (lower area) -> upper right
taper_draw(f2, (28, 52), (59, 6), (24, 28), r0=2.3, r1=0.7)

print(f2.matrix_text(region=(24,0,61,60)))
print("f1", f1.stats_text())
print("f2", f2.stats_text())
finish([f1, f2])
