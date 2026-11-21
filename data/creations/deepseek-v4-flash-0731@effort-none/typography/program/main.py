from pixelbench_api import *

c = new_canvas(64, 64)

# ---------- Palette ----------
NAVY   = c.color((10, 14, 42))     # background
NAVY2  = c.color((16, 22, 56))     # darker accents
SHADOW = c.color((5, 6, 20))       # letter shadow / outline
CYAN   = c.color((64, 224, 255))   # PIXEL main
CYAN_D = c.color((20, 120, 160))   # PIXEL dark accent
GOLD   = c.color((255, 204, 51))   # QUEST main
GOLD_D = c.color((180, 120, 10))   # QUEST dark accent
WHITE  = c.color((235, 240, 255))  # stars
PURPLE = c.color((150, 90, 220))   # accent
RED    = c.color((255, 90, 90))    # accent gem
ORANGE = c.color((255, 160, 60))   # accent

# ---------- Background ----------
c.rect(0, 0, 64, 64, NAVY)

# subtle vertical banding for depth
for i in range(64):
    if i % 8 == 5:
        c.rect(0, i, 64, 1, (14, 19, 48))
    if i % 8 == 2:
        c.rect(0, i, 64, 1, (8, 11, 34))

# ---------- Border frame ----------
c.rect(2, 2, 60, 60, None, fill=False)
c.rect(3, 3, 58, 58, None, fill=False)
# draw frame lines
for x in range(2, 62):
    c.set(x, 2, WHITE)
    c.set(x, 61, WHITE)
for y in range(2, 62):
    c.set(2, y, WHITE)
    c.set(61, y, WHITE)
for x in range(3, 61):
    c.set(x, 3, CYAN_D)
    c.set(x, 60, CYAN_D)
for y in range(3, 61):
    c.set(3, y, CYAN_D)
    c.set(60, y, CYAN_D)

# ---------- Star field ----------
stars = [(6,6),(13,5),(22,11),(33,5),(48,7),(57,9),(26,4),(41,12),(9,13),(52,21),
         (8,55),(17,60),(28,58),(39,55),(53,57),(60,43),(12,50),(45,59),(8,42),(58,53)]
for (sx, sy) in stars:
    c.set(sx, sy, WHITE)
# some dimmer stars
for (sx, sy) in [(18,7),(29,14),(40,6),(55,14),(5,24),(47,48),(22,55),(35,61),(57,31),(15,44)]:
    c.set(sx, sy, (120, 140, 190))

# ---------- Font (7x9 block letters) ----------
FONT = {
 'P': ["XXXXX..","X....X.","X....X.","X....X.","XXXXX..","X......","X......","X......","X......"],
 'I': ["..XXX..","..XXX..","..XXX..","..XXX..","..XXX..","..XXX..","..XXX..","..XXX..","..XXX.."],
 'X': ["X....X.","X....X.",".X..X..","..XX...","..XX...",".X..X..","X....X.","X....X.","X....X."],
 'E': ["XXXXX..","X......","X......","XXXXX..","X......","X......","X......","X......","XXXXX.."],
 'L': ["X......","X......","X......","X......","X......","X......","X......","X......","XXXXX.."],
 'Q': [".XXXX..","X....X.","X....X.","X....X.","X....X.","X....X.","X..X.X.",".XX..X.","....XX."],
 'U': ["X....X.","X....X.","X....X.","X....X.","X....X.","X....X.","X....X.","X....X.",".XXXX.."],
 'S': [".XXXX..","X....X.","X......","X......",".XXXX..",".....X.",".....X.","X....X.",".XXXX.."],
 'T': ["XXXXX..","..XX...","..XX...","..XX...","..XX...","..XX...","..XX...","..XX...","..XX..."],
}

def draw_glyph(gx, gy, glyph, color):
    for row in range(9):
        for col in range(7):
            if glyph[row][col] == 'X':
                c.set(gx + col, gy + row, color)

def draw_word(x, y, word, main, accent, shadow_col):
    """Draw a word with a drop shadow + thin outline (accent) around the main fill."""
    ADV = 8
    start_x = x
    for i, ch in enumerate(word):
        glyph = FONT[ch]
        gx = start_x + i * ADV
        for row in range(9):
            for col in range(7):
                if glyph[row][col] == 'X':
                    # drop shadow
                    c.set(gx + col + 1, y + row + 2, SHADOW)
                    # accent outline around the pixel
                    for dy in (-1, 0, 1):
                        for dx in (-1, 0, 1):
                            if dx or dy:
                                c.set(gx + col + dx, y + row + dy, accent)
        # main fill painted over the outline
        draw_glyph(gx, y, glyph, main)

# Layout
# "PIXEL" word
draw_word(12, 13, "PIXEL", CYAN, CYAN_D, SHADOW)

# "QUEST" word
draw_word(12, 35, "QUEST", GOLD, GOLD_D, SHADOW)

# ---------- Decorative gem between words ----------
gx, gy = 26, 27
c.set(gx+2, gy, RED)
c.set(gx+1, gy+1, RED); c.set(gx+2, gy+1, ORANGE); c.set(gx+3, gy+1, RED)
c.set(gx, gy+2, RED); c.set(gx+1, gy+2, RED); c.set(gx+2, gy+2, ORANGE); c.set(gx+3, gy+2, RED); c.set(gx+4, gy+2, RED)
c.set(gx, gy+3, RED); c.set(gx+1, gy+3, WHITE); c.set(gx+2, gy+3, WHITE); c.set(gx+3, gy+3, RED); c.set(gx+4, gy+3, RED)
c.set(gx+1, gy+4, RED); c.set(gx+2, gy+4, RED); c.set(gx+3, gy+4, RED)
c.set(gx+2, gy+5, RED)

# small sparkles beside gem
c.set(13, 26, WHITE)
c.set(50, 26, WHITE)
c.set(22, 25, CYAN_D)
c.set(41, 25, CYAN_D)

# ---------- Small pixel blocks at bottom corners ----------
for bx, by, col in [(6,54,CYAN_D),(49,54,GOLD_D)]:
    c.rect(bx, by, 3, 3, None, fill=False)
    for i in range(3):
        for j in range(3):
            c.set(bx+i, by+j, col)

c.set(6, 54, CYAN); c.set(7,54,CYAN); c.set(8,54,CYAN)
c.set(6,54,CYAN); c.set(6,55,CYAN); c.set(6,56,CYAN)
c.set(49,54,GOLD); c.set(50,54,GOLD); c.set(51,54,GOLD)
c.set(49,54,GOLD); c.set(49,55,GOLD); c.set(49,56,GOLD)

# corner notches
for (px, py) in [(4,4),(59,4),(4,59),(59,59)]:
    c.set(px, py, PURPLE)
    c.set(px+1, py+1, WHITE)

print(c.stats_text())
finish(c)
