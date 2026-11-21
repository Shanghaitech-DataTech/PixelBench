from pixelbench_api import *

W = H = 48
c = new_canvas(W, H, background=None, name="staff")

# ---------- palette ----------
OUT   = c.color("#1c0f07")        # wood outline
WD    = c.color("#3a2414")        # wood dark shade
WB    = c.color("#5b3a20")        # wood base
WH    = c.color("#7d4f2a")        # wood highlight
WL    = c.color("#9a6534")        # lightest
PD    = c.color("#5a1fa8")        # purple dark
PM    = c.color("#8a3ff0")        # purple mid
PL    = c.color("#b473ff")        # purple light
PG    = c.color("#e0bcff")        # purple glow

# ---------- staff path (shaft then curved crook head) ----------
way = [(25,46),(25,29),(25,27),(26,25),(28,24),(30,23),(31.5,22),
       (32,20.5),(31.5,19),(30,18),(28,17.5),(26,18),(25,19),(24.5,20.5)]

def sample_path(pts, step=0.5):
    out=[]
    for i in range(len(pts)-1):
        (x0,y0)=pts[i]; (x1,y1)=pts[i+1]
        d=max(abs(x1-x0),abs(y1-y0))
        n=int(d/step)+1
        for k in range(n+1):
            t=k/n
            out.append((x0+(x1-x0)*t, y0+(y1-y0)*t))
    return out

pts = sample_path(way, 0.45)
for (x,y) in pts:
    cx=int(round(x)); cy=int(round(y))
    # outline
    c.circle(cx, cy, 2, OUT)
# base (inner) wood
for (x,y) in pts:
    cx=int(round(x)); cy=int(round(y))
    c.circle(cx, cy, 1, WB)

# shading on straight shaft: dark east side, highlight west side
for y in range(27, 47):
    for (dx,col) in ((1,WD),(-1,WH)):
        c.set(25+dx, y, col)
# lightest touch on straight shaft
for y in range(28,44,2):
    c.set(24, y, WL)

# highlight along outer (top-left) edge of the head
for (x,y) in [(26,24),(28,23.2),(30,22),(31.6,20.6),(31,19.2),(30,18.2),
              (28.2,17.6),(26.4,17.8),(25.2,18.6)]:
    c.set(int(round(x)), int(round(y)), WH)
# dark lower/inner edge of the head
for (x,y) in [(27,25.5),(29,24),(32,21.5),(32,19.5),(29.5,19),(27,18.4),
              (25.5,19.6)]:
    c.set(int(round(x)), int(round(y)), WD)

# ---------- purple gem at the staff tip ----------
gx, gy = 24, 21
c.set(gx, gy, PM); c.set(gx+1, gy, PL); c.set(gx, gy+1, PL); c.set(gx-1, gy, PD); c.set(gx, gy-1, PG)

# ---------- purple particles ----------
parts = [
    (16,13,PM),(17,12,PL),(18,10,PG),(15,16,PM),(14,14,PG),
    (32,13,PM),(34,12,PL),(35,10,PG),(33,16,PD),(36,15,PL),
    (20,8,PM),(22,7,PG),(13,19,PD),(16,20,PL),(37,19,PM),
    (28,9,PL),(33,9,PD),(12,11,PG),(38,13,PL),(19,22,PD),
    (30,7,PG),(15,8,PM),(36,21,PD),(26,6,PL),(10,16,PM),
    (39,18,PG),(21,24,PL),(18,17,PM),
]
for (x,y,col) in parts:
    c.set(x,y,col)

# brighten a few particles (glow centers)
for (x,y) in [(18,10),(14,14),(35,10),(22,7),(12,11),(30,7),(39,18)]:
    c.set(x,y,PG)
    c.set(x+1,y,PG)

print(c.stats_text())
finish(c)
