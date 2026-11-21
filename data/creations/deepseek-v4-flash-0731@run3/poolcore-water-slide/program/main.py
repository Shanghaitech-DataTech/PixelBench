from pixelbench_api import new_canvas, finish
import random

c = new_canvas(128, 128)

# ---- palette constants (indexes registered on first use) ----
CEIL     = "#e7eef2"
LIGHT    = "#ffffff"
LIGHT_D  = "#cddbe3"
SIDE     = "#9db8c6"
WALLBASE = "#a9c2cc"
TILE_W   = "#edf4f6"
TILE_B   = "#a3c9d8"
WALL_SH  = "#8aa6b4"
HAZE     = "#e6f2f8"
WT_LINE  = "#aee6f4"
RIP1     = "#b6e8f4"
RIP2     = "#d4f4fc"
S_MID    = "#e4ebee"
S_WHT    = "#fbfdfe"
S_DK     = "#b5c4cc"
S_SH     = "#91a8b4"
S_IN     = "#6f9aae"
SUB      = "#7fb8cc"
YEL      = "#f2c014"
YEL_H    = "#ffe866"
YEL_D    = "#d3a20c"
YEL_M    = "#c8ac58"
HAIR     = "#3a2313"
SKIN     = "#eab891"
SUIT     = "#26446e"
SUIT_H   = "#3f6396"
SHAD     = "#2c6688"

# ---- ceiling ----
c.rect(0, 0, 128, 16, CEIL)
c.rect(0, 15, 128, 1, LIGHT_D)
c.rect(0, 0, 5, 15, SIDE)
c.rect(123, 0, 5, 15, SIDE)
for px in (20, 52, 84):
    c.rect(px - 2, 1, 28, 12, "#d8e8f0")
for px in (20, 52, 84):
    c.rect(px, 3, 24, 8, LIGHT)

# ---- far wall, tiled ----
c.rect(0, 16, 128, 48, WALLBASE)
for row in range(6):
    y = 16 + row * 8
    for col in range(10):
        x = col * 12
        tcol = TILE_W if (col + row) % 2 == 0 else TILE_B
        c.rect(x, y, 11, 7, tcol)
c.rect(0, 16, 128, 10, HAZE)
for (px, pw) in [(20, 24), (52, 24), (84, 14)]:
    c.rect(px, 17, pw, 5, "#eef6fa")
c.rect(0, 16, 5, 48, SIDE)
c.rect(123, 16, 5, 48, SIDE)
c.rect(0, 61, 128, 3, WALL_SH)

# ---- tiled columns ----
for bx in (18, 98):
    c.rect(bx, 0, 12, 64, WALLBASE)
    c.rect(bx, 1, 12, 62, TILE_B)
    c.rect(bx, 0, 2, 63, "#e0f0f8")
    c.rect(bx + 9, 1, 2, 62, "#8fb0bf")
    for g in (8, 16, 24, 32, 40, 48, 56):
        c.rect(bx, g, 12, 1, WALLBASE)

# ---- water ----
for (y0, y1, col) in [(64, 70, "#3d88ab"), (71, 77, "#4794b6"), (78, 84, "#51a2c2"),
                     (85, 91, "#5caece"), (92, 98, "#66b8d8"), (99, 105, "#70c2de"),
                     (106, 112, "#7acae4"), (113, 119, "#84d2ea"), (120, 127, "#8edaf0")]:
    c.rect(0, y0, 128, y1 - y0 + 1, col)
c.rect(0, 64, 128, 2, WT_LINE)

# ---- light reflections on water ----
for px in (20, 52, 84):
    cx = px + 12
    c.rect(cx - 6, 66, 12, 1, RIP2)
    c.rect(cx - 5, 68, 10, 1, RIP2)
    c.rect(cx - 4, 70, 8, 1, RIP2)
    c.rect(cx - 3, 72, 7, 1, RIP1)
    c.rect(cx - 3, 74, 6, 1, RIP1)
    c.rect(cx - 3, 76, 6, 1, RIP1)
    c.rect(cx - 3, 78, 6, 1, RIP1)

# ---- gentle ripples ----
random.seed(13)
for i in range(130):
    x = random.randint(2, 112)
    y = random.randint(80, 122)
    w = random.choice([2, 3, 4, 5])
    col = RIP1 if i % 3 else RIP2
    c.rect(x, y, w, 1, col)

# ---- water slide descending into the pool (right) ----
slide = [(126, 26), (113, 33), (101, 45), (91, 59), (87, 70), (90, 76),
        (94, 72), (102, 58), (112, 47), (122, 39), (126, 34)]
c.poly(slide, S_MID, fill=True)
c.line(90, 74, 126, 34, S_WHT)
c.line(91, 72, 115, 45, S_WHT)
c.line(87, 69, 101, 46, S_SH)
c.line(101, 46, 113, 34, S_DK)
c.ellipse(91, 72, 6, 3, S_IN)          # trough mouth
c.line(85, 70, 95, 71, S_DK)
c.poly([(88, 72), (86, 80), (90, 86), (95, 82), (95, 73)], SUB)  # submerged tip
c.rect(84, 74, 15, 1, RIP2)
c.rect(87, 77, 11, 1, WT_LINE)
c.rect(89, 80, 7, 1, RIP2)
c.rect(86, 83, 5, 1, RIP1)

# ---- girl floating in the middle, seen from behind ----
cx, cy = 66, 97
c.ellipse(cx, cy + 6, 8, 3, SHAD)          # shadow beneath
c.ellipse(cx, cy, 14, 3, RIP2, fill=False)  # ripples
c.ellipse(cx, cy, 10, 2, RIP1, fill=False)
c.circle(cx, cy, 7, YEL)                    # swim ring
c.circle(cx, cy, 5, "#66b8d8")               # hole -> water
c.ellipse(cx, cy - 1, 4, 2, SUIT)           # back
c.rect(cx - 2, cy - 2, 5, 1, SUIT_H)
c.rect(cx - 2, cy - 5, 5, 3, SKIN)          # neck
c.circle(cx, cy - 7, 2, HAIR)                # back of head
c.set(cx - 1, cy - 6, "#5a3d26")             # hair shine
c.rect(cx - 8, cy - 4, 3, 2, SKIN)          # arms over the ring
c.rect(cx + 5, cy - 4, 3, 2, SKIN)
c.set(cx - 5, cy - 4, YEL_H)
c.set(cx - 3, cy - 5, YEL_H)
c.set(cx + 4, cy - 5, YEL_H)
c.set(cx + 6, cy - 4, YEL_H)
c.set(cx - 3, cy - 4, YEL_D)
c.set(cx + 4, cy - 4, YEL_D)
c.set(cx, cy + 6, YEL_D)

# ---- ring reflection streaks on the water ----
for (y, w) in [(105, 9), (107, 7), (109, 6), (111, 5), (113, 4)]:
    c.rect(cx - w // 2, y, w, 1, YEL_M)

print(c.stats_text())
print(c.matrix_text(region=(54, 84, 82, 114)))
print(c.matrix_text(region=(82, 22, 128, 90)))

finish(c)
