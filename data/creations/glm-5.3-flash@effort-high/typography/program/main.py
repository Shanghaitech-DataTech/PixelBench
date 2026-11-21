# "PIXEL QUEST" 64x64 title screen
BG      = '#141230'   # deep night blue
FRAME   = '#d9a441'   # frame gold
FRAME_D = '#7a5a1e'   # dark gold accents
CREAM   = '#f6f0dc'   # QUEST letters
GOLD    = '#f2c14e'   # PIXEL letters
OUT     = '#0a0918'   # letter outline (black)
SHAD    = '#7a5a1e'   # drop shadow (dark gold)
STAR    = '#7f8cc9'   # faint stars
WHITE   = '#ffffff'

c = new_canvas(64, 64, background=BG, name='pixel_quest_title')

# ---------- decorative frame: outer border + corner brackets ----------
c.rect(0, 0, 64, 64, FRAME, fill=False)

def bracket(x, y, sx, sy):
    c.line(x, y, x + 7 * sx, y, FRAME)
    c.line(x, y, x, y + 7 * sy, FRAME)
    c.set(x + 8 * sx, y, FRAME_D)
    c.set(x, y + 8 * sy, FRAME_D)

bracket(3, 3, 1, 1)
bracket(60, 3, -1, 1)
bracket(3, 60, 1, -1)
bracket(60, 60, -1, -1)

# ---------- stars / sparkles ----------
for (x, y) in [(16, 7), (26, 5), (38, 6), (50, 6), (12, 58), (52, 57), (45, 59), (18, 53)]:
    c.set(x, y, STAR)

def sparkle(x, y, col):
    c.set(x, y, col)
    c.set(x - 1, y, col)
    c.set(x + 1, y, col)
    c.set(x, y - 1, col)
    c.set(x, y + 1, col)

sparkle(21, 8, WHITE)
sparkle(43, 8, GOLD)

# ---------- glyph mask: 5x7 font scaled 2x ----------
t = new_canvas(30, 16, name='glyphs')
t.text(0, 0, 'PIXEL', GOLD, font='5x7')   # rows 0-6, 29 px wide
t.text(0, 8, 'QUEST', CREAM, font='5x7')  # rows 8-14

m = new_canvas(64, 64, name='mask')
t.select(0, 0, 29, 7).resize(58, 14).copy_to(3, 14, m)   # PIXEL  y 14-27
t.select(0, 8, 29, 7).resize(58, 14).copy_to(3, 35, m)   # QUEST  y 35-48

# ---------- recoloured copies of the mask (shadow + outline) ----------
def recolor(src, colour):
    w, h, buf = src.to_rgba()
    d = new_canvas(64, 64)
    idx = d.color(colour)
    for yy in range(h):
        for xx in range(w):
            if buf[(yy * w + xx) * 4 + 3] > 0:
                d.set(xx, yy, idx)
    return d

shad_m = recolor(m, SHAD)
out_m = recolor(m, OUT)

# drop shadow (bottom-right, 2 px)
for dx, dy in [(2, 2), (3, 2), (2, 3), (3, 3)]:
    c.blit(shad_m, dx, dy)

# 1 px outline around the letters
for dx, dy in [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]:
    c.blit(out_m, dx, dy)

# letters on top
c.blit(m, 0, 0)

# ---------- divider ornament under the title ----------
c.line(8, 54, 26, 54, FRAME_D)
c.line(38, 54, 55, 54, FRAME_D)
c.set(8, 54, GOLD)
c.set(55, 54, GOLD)
# centre diamond
c.set(32, 52, GOLD)
c.set(31, 53, GOLD); c.set(33, 53, GOLD)
c.set(30, 54, CREAM); c.set(31, 54, GOLD); c.set(32, 54, CREAM); c.set(33, 54, GOLD); c.set(34, 54, CREAM)
c.set(31, 55, GOLD); c.set(33, 55, GOLD)
c.set(32, 56, GOLD)

print(c.stats_text())
print(c.matrix_text(region=(0, 10, 63, 52)))
finish(c)
