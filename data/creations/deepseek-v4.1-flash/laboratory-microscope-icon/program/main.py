from pixelbench_api import *

W = H = 32
c = new_canvas(W, H, name="microscope")

OUT = c.color('#0e1520', 'out')      # outline / deepest shadow
DK  = c.color('#1a2432', 'dk')       # dark metal
MD  = c.color('#2d3e52', 'md')       # body metal
LT  = c.color('#4b6580', 'lt')       # lit metal
HI  = c.color('#7c99b5', 'hi')       # highlights / top faces
WH  = c.color('#bdd2e3', 'wh')       # glass, bright rims
GL  = c.color('#46bfd7', 'gl')       # lens glass
GL2 = c.color('#a5eaf7', 'gl2')      # lens glass shine

# ================= BASE (horseshoe foot) =================
c.poly([(4, 27), (23, 27), (25, 30), (6, 30)], MD)          # front face
c.line(4, 27, 23, 27, LT)                                   # lit top of front
c.poly([(5, 25), (24, 25), (23, 27), (4, 27)], HI)          # top face
c.line(5, 29, 25, 29, DK)                                   # floor shade
c.rect(14, 28, 4, 2, OUT)                                   # horseshoe notch

# ================= ARM (stand pillar, right) =================
c.path("M19 26 L18 15 Q16 8 20 7 L23.5 7 L25 12 L25 26 Z", MD)
c.path("M23.5 7 L25 12 L25 26 L23.5 26 Z", DK)              # shaded side face
c.line(18, 16, 18, 25, LT)                                  # lit left edge
c.line(18, 26, 24, 26, DK)                                  # contact shadow

# ================= STAGE (with slide) =================
c.poly([(5, 20), (17, 20), (16, 22), (4, 22)], HI)          # top face
c.poly([(4, 22), (16, 22), (16, 23), (4, 23)], MD)          # front edge
c.line(4, 23, 16, 23, DK)                                   # under lip
c.poly([(7, 20), (14, 20), (13, 22), (6, 22)], WH)          # glass slide
c.set(10, 20, GL)                                           # specimen

# ================= BODY TUBE =================
c.poly([(9, 8), (14, 5), (17, 11), (12, 14)], MD)
c.line(9, 8, 12, 14, LT)                                    # lit left edge
c.line(10, 9, 12, 13, HI)
c.line(14, 5, 17, 11, DK)                                   # shaded right edge

# ================= REVOLVING NOSEPIECE =================
c.poly([(12, 10), (18, 10), (19, 12), (17, 14), (13, 14), (11, 12)], LT)
c.line(12, 10, 18, 10, HI)                                  # lit top rim
c.line(18, 10, 19, 12, DK)
c.line(19, 12, 17, 14, DK)

# ================= OBJECTIVE LENS =================
c.poly([(12, 14), (16, 14), (17, 19), (14, 19)], DK)
c.line(14, 18, 17, 18, HI)                                  # lens front
c.set(13, 15, LT)
c.set(13, 16, LT)

# ================= EYEPIECE =================
c.poly([(9, 8), (15, 5), (14, 2), (8, 5)], MD)
c.line(8, 5, 9, 8, LT)                                      # lit left side
c.line(14, 2, 15, 5, DK)                                    # shaded right side
c.line(8, 5, 14, 2, WH)                                     # bright rim
c.line(9, 6, 14, 3, GL2)                                    # glass
c.set(10, 6, GL)
c.set(11, 5, GL)
c.set(12, 4, GL)
c.line(9, 8, 15, 5, DK)                                     # collar

# ================= FOCUS KNOB =================
c.circle(25, 19, 3, DK)
c.circle(25, 19, 2, LT)
c.set(24, 18, HI)
c.set(24, 19, HI)


# ---------------- finishing passes ----------------
def visible_mask(canvas):
    w, h, data = canvas.to_rgba()
    return [[data[(y * w + x) * 4 + 3] > 0 for x in range(w)] for y in range(h)], w, h


def plug_holes(canvas):
    """Fill single-pixel rasteriser gaps so no stray dark dot lands inside a part."""
    on, w, h = visible_mask(canvas)
    for y in range(h):
        for x in range(w):
            if on[y][x]:
                continue
            full = True
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < h and 0 <= nx < w) or not on[ny][nx]:
                        full = False
            if full:
                canvas.set(x, y, canvas.get(max(0, x - 1), y))


def add_outline(canvas, colour):
    """Grow a one-pixel dark rim outward so the sprite reads on any background."""
    on, w, h = visible_mask(canvas)
    for y in range(h):
        for x in range(w):
            if on[y][x]:
                continue
            hit = False
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < h and 0 <= nx < w and on[ny][nx]:
                        hit = True
            if hit:
                canvas.set(x, y, colour)


plug_holes(c)
add_outline(c, OUT)

print(c.stats_text())
save("microscope", c)
finish(c)
