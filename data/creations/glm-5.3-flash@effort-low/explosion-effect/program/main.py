from pixelbench_api import *
import math

cx, cy = 32, 32

# Frame 1: bright yellow fireball at center (built for reference/preview)
f1 = new_canvas(64, 64, name="frame1")
f1.circle(cx, cy, 9, "#ff6a00")
f1.circle(cx, cy, 7, "#ffcc00")
f1.circle(cx, cy, 4, "#fff8b0")
for dx, dy in [(0,-14),(10,-9),(14,2),(9,12),(-3,14),(-13,7),(-14,-4),(-8,-12)]:
    f1.line(cx, cy, cx+dx, cy+dy, "#ff9900")
f1.circle(cx, cy, 7, "#ffcc00")
f1.circle(cx, cy, 4, "#fff8b0")
for p in [(18,18),(46,20),(44,44),(20,45),(32,12),(12,32),(52,32),(32,52)]:
    f1.set(p[0], p[1], "#ffdd55")

# Frame 2: expanding orange-red blast with sparks -> the delivered 64x64 frame
f2 = new_canvas(64, 64, name="frame2")
f2.circle(cx, cy, 20, "#cc2200")
f2.circle(cx, cy, 16, "#ff5500")
f2.circle(cx, cy, 11, "#ff9900")
f2.circle(cx, cy, 6, "#ffdd55")
f2.circle(cx, cy, 3, "#ffffcc")
for i in range(12):
    a = i * math.pi / 6
    x1 = cx + int(20*math.cos(a)); y1 = cy + int(20*math.sin(a))
    x2 = cx + int(26*math.cos(a)); y2 = cy + int(26*math.sin(a))
    f2.line(x1, y1, x2, y2, "#cc2200")
for a, r1, r2 in [(0.2,28,38),(1.1,30,40),(2.0,27,36),(2.9,29,39),(3.8,28,37),
                  (4.7,30,41),(5.5,27,36),(0.7,26,33),(2.4,25,32),(4.2,26,34)]:
    x1 = cx + int(r1*math.cos(a)); y1 = cy + int(r1*math.sin(a))
    x2 = cx + int(r2*math.cos(a)); y2 = cy + int(r2*math.sin(a))
    f2.line(x1, y1, x2, y2, "#ffcc33")
    f2.set(x2, y2, "#ffff99")
for p in [(14,14),(50,16),(48,50),(15,49)]:
    f2.circle(p[0], p[1], 2, "#662200")

print(f1.stats_text())
print(f2.stats_text())
save("explosion-frame1", f1)
save("explosion-frame2", f2)
# Single required 64x64 output: the explosion effect frame
finish(f2)
