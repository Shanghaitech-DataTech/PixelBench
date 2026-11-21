from pixelbench_api import *
import math

src = input_canvas

def rotated(angle_deg):
    return src.select(0, 0, 93, 128).rotate(angle_deg, algorithm="rotsprite").preview(f"k{angle_deg}")

def tip_of(rot):
    W, H = rot.stats()['size']
    pts = []
    for y in range(H):
        for x in range(W):
            idx = rot.get(x, y)
            if idx is not None:
                for e in rot.palette():
                    if e['index'] == idx and e['rgba'][3] > 0:
                        pts.append((x, y))
                        break
    mx = max(p[0] for p in pts)
    tp = [p for p in pts if p[0] >= mx - 5]
    return (mx, sum(p[1] for p in tp) / len(tp))

def place(rot, tx, ty, alpha, canvas):
    mx, my = tip_of(rot)
    dx = int(round(tx - mx))
    dy = int(round(ty - my))
    W, H = rot.stats()['size']
    for y in range(H):
        for x in range(W):
            idx = rot.get(x, y)
            if idx is not None:
                for e in rot.palette():
                    if e['index'] == idx and e['rgba'][3] > 0:
                        canvas.set(x + dx, y + dy, (e['rgba'][0], e['rgba'][1], e['rgba'][2], alpha))
                        break

W, H = 265, 170
out = new_canvas(W, H, name="out")

# --- semi-transparent afterimages trailing behind the thrust (blade angled as it swings in) ---
ghost_tips = [(92, 62), (132, 58), (172, 52), (210, 47)]
ghost_angles = [68, 76, 84, 92]
ghost_alphas = [52, 92, 138, 182]
for (tx, ty), ang, al in zip(ghost_tips, ghost_angles, ghost_alphas):
    g = rotated(ang)
    place(g, tx, ty, al, out)

# --- main knife: horizontal thrust to the right, cutting edge facing down ---
main = rotated(90)
place(main, 240, 44, 255, out)

# --- white slash effect ---
def arc(cx, cy, rx, ry, a0, a1, color, step=0.035, width=1):
    n = max(4, int(abs(a1 - a0) / step))
    for w in range(width):
        for i in range(n):
            x0 = cx + (rx + w) * math.cos(a0 + (a1 - a0) * i / n)
            y0 = cy + (ry + w) * math.sin(a0 + (a1 - a0) * i / n)
            x1 = cx + (rx + w) * math.cos(a0 + (a1 - a0) * (i + 1) / n)
            y1 = cy + (ry + w) * math.sin(a0 + (a1 - a0) * (i + 1) / n)
            out.line(round(x0), round(y0), round(x1), round(y1), color)

WHITE = (255, 255, 255, 255)
arc(214, 26, 46, 36, math.radians(-22), math.radians(86), WHITE, width=3)
arc(214, 26, 59, 47, math.radians(-26), math.radians(82), (255, 255, 255, 235), width=2)
arc(214, 26, 72, 58, math.radians(-30), math.radians(76), (255, 255, 255, 200), width=2)
arc(214, 26, 34, 25, math.radians(-14), math.radians(80), WHITE, width=2)
# speed streaks along the motion line (behind the blade)
for yy in (40, 52, 64, 76, 88, 100):
    out.line(12, yy - 6, 48, yy, (255, 255, 255, 150))
# bright sparks at the tip
for (sx, sy) in [(248, 28), (254, 40), (246, 14), (240, 60), (258, 22), (244, 4), (232, 72)]:
    out.set(sx, sy, WHITE)

print(out.stats_text())
finish(out)
