import math

c = new_canvas(48, 48)

CX, CY = 23.5, 23.5

def circle(rx, ry, colour, fill=True):
    c.ellipse(CX, CY, rx, ry, colour, fill=fill)

# --- layered glow from outer to inner ---
glow = [
    (23, (50, 12, 110, 14)),
    (22, (72, 22, 150, 26)),
    (21, (95, 34, 180, 42)),
    (20, (118, 48, 205, 66)),
    (19, (140, 62, 228, 96)),
    (18, (158, 80, 242, 132)),
    (17, (172, 98, 250, 170)),
    (16, (120, 40, 205, 255)),
    (15, (135, 52, 222, 255)),
    (14, (152, 70, 238, 255)),
    (13, (170, 92, 248, 255)),
    (12, (188, 116, 255, 255)),
    (11, (205, 145, 255, 255)),
    (10, (221, 175, 255, 255)),
    (9,  (236, 208, 255, 255)),
    (8,  (245, 230, 255, 255)),
]
for r, col in glow:
    circle(r, r, col, fill=True)

# --- bright halo ring (thin outline) ---
circle(21.5, 21.5, (205, 145, 255, 200), fill=False)
circle(20.0, 20.0, (236, 208, 255, 120), fill=False)

# --- spiral vortex arms ---
def spiral_arm(offset_deg, sweep_deg, r0, r1, n, colour):
    off = math.radians(offset_deg)
    sweep = math.radians(sweep_deg)
    # start point
    th0 = off
    x0 = CX + r0 * math.cos(th0)
    y0 = CY + r0 * math.sin(th0)
    d = f"M {x0:.3f} {y0:.3f}"
    for i in range(1, n + 1):
        t = i / n
        ri = r0 + (r1 - r0) * t
        th = off + sweep * t
        x = CX + ri * math.cos(th)
        y = CY + ri * math.sin(th)
        d += f" A {ri:.3f} {ri:.3f} 0 0 1 {x:.3f} {y:.3f}"
    c.path(d, colour, fill=False)

# soft darker swirls first, then bright swirls, then inner white threads
for k in range(3):
    spiral_arm(k * 120, 215, 15.5, 3.5, 14, (70, 16, 150, 255))
for k in range(3):
    spiral_arm(k * 120 + 18, 200, 13, 2.5, 14, (220, 150, 255, 255))
for k in range(3):
    spiral_arm(k * 120 + 55, 150, 7, 1.2, 8, (255, 240, 255, 255))

# --- bright core ---
circle(4.5, 4.5, (240, 200, 255, 255), fill=True)
circle(3.0, 3.0, (255, 250, 255, 255), fill=True)
circle(1.5, 1.5, (255, 255, 255, 255), fill=True)

# --- sparkles around the rim ---
sparks = [
    (8.0, 6.0), (38.5, 7.5), (40.0, 23.0), (37.0, 40.5),
    (9.5, 40.0), (7.0, 23.5), (23.5, 4.5), (23.0, 43.0),
]
for sx, sy in sparks:
    c.ellipse(sx, sy, 0.8, 0.8, (255, 255, 255, 235), fill=True)
    c.ellipse(sx, sy, 0.4, 0.4, (255, 255, 255, 255), fill=True)

finish(c)
