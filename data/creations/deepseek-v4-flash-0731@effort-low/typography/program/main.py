from pixelbench_api import *

c = new_canvas(64, 64, background=(14, 16, 38))  # deep indigo night

bg      = c.color((14, 16, 38))
outline = c.color((10, 8, 24))
shadow  = c.color((0, 0, 10))
gold    = c.color((245, 197, 24))
gold_hi = c.color((255, 236, 130))
cyan    = c.color((122, 218, 255))
white   = c.color((240, 248, 255))
mount   = c.color((30, 26, 74))
mount2  = c.color((42, 38, 94))
horizon = c.color((255, 190, 30))
red     = c.color((224, 64, 96))

# ---- star field ----
stars = [
    (6, 3, white), (14, 2, (150,170,255)), (22, 4, (255,220,130)),
    (34, 2, white), (45, 4, (150,170,255)), (53, 2, (255,220,130)),
    (59, 5, white), (28, 1, (150,170,255)), (3, 9, white),
    (59, 12, (255,220,130)), (48, 13, white), (10, 15, (150,170,255)),
    (8, 20, (255,220,130)), (55, 20, white), (4, 25, (150,170,255)),
    (5, 31, white), (58, 27, (255,220,130)),
]
for x, y, col in stars:
    c.set(x, y, col)
def sparkle(cx, cy, col):
    c.set(cx, cy, col); c.set(cx-1, cy, col); c.set(cx+1, cy, col)
    c.set(cx, cy-1, col); c.set(cx, cy+1, col)
sparkle(60, 8, white)
sparkle(3, 14, (255,220,130))

# ---- custom 5x8 block font (1 = ink) ----
FONT = {
    'P': ["####","#..#","#..#","#..#","###.","#...","#...","#..."],
    'I': ["#####","..#..","..#..","..#..","..#..","..#..","..#..","#####"],
    'X': ["#...#",".#.#.","..#..","..#..",".#.#.","#...#","#...#","#...#"],
    'E': ["#####","#....","#....","####.","#....","#....","#....","#####"],
    'L': ["#....","#....","#....","#....","#....","#....","#....","#####"],
    'Q': [".###.","#...#","#...#","#...#","#...#","#...#","#..##",".###."],
    'U': ["#...#","#...#","#...#","#...#","#...#","#...#","#...#",".###."],
    'S': ["#####","#....","#....","####.","....#","....#","....#","#####"],
    'T': ["#####","..#..","..#..","..#..","..#..","..#..","..#..","..#.."],
}

def build_word(word, color, scale=2):
    """Return a temp canvas (and its dims) with the word filled in `color`."""
    grid_w = len(word) * 5 + (len(word) - 1)  # grid cells across
    w = grid_w * scale
    h = 8 * scale
    t = new_canvas(w, h)
    for k, ch in enumerate(word):
        rows = FONT[ch]
        for gy, row in enumerate(rows):
            for gx, px in enumerate(row):
                if px == '#':
                    t.rect((k * 5 + k + gx) * scale, gy * scale, scale, scale, color)
    return t, w, h

def outlined(t):
    """Add a 1px rim of `outline` colour around every ink pixel."""
    w, h = t.size
    tmp = t.copy()
    # a playing field of indices: first re-register ink colour must not be zero.
    ink_idx = t.get(0, 0)
    outpix = tmp.color(outline)
    for yy in range(h):
        for xx in range(w):
            if tmp.get(xx, yy) == 0:
                continue  # transparent
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = xx+dx, yy+dy
                if nx < 0 or ny < 0 or nx >= w or ny >= h or tmp.get(nx, ny) == 0:
                    t.set(nx, ny, outpix)
    return t

def draw_word(c, x, y, word, color, scale=2, shadow_off=(2, 2)):
    t, sw, sh = build_word(word, color, scale)
    # drop shadow silhouette offset down-right
    shc = t.copy()
    for yy in range(sh):
        for xx in range(sw):
            if shc.get(xx, yy) != 0:
                shc.set(xx, yy, shadow)
    c.blit(shc, x + shadow_off[0], y + shadow_off[1])
    # 1px outline on an overdraw copy, then stamp
    ot = t.copy()
    outpix = ot.color(outline)
    for yy in range(sh):
        for xx in range(sw):
            if t.get(xx, yy) == 0:
                continue
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = xx+dx, yy+dy
                if (0 <= nx < sw and 0 <= ny < sh) and t.get(nx, ny) == 0:
                    ot.set(nx, ny, outpix)
    c.blit(ot, x, y)

# ---- title lines ----
draw_word(c, 3, 6, "PIXEL", gold)
draw_word(c, 3, 34, "QUEST", cyan)
# crown highlight on PIXEL's top ink row
def tint_top(c, x, y, word, scale=2, tint=gold_hi):
    for k, ch in enumerate(word):
        rows = FONT[ch]
        for gx, px in enumerate(rows[0]):
            if px == '#':
                c.rect(x + (k * 5 + k + gx) * scale, y, scale, scale, tint)
tint_top(c, 3, 6, "PIXEL")

# ---- emblem divider (ruby diamond) between the words ----
c.rect(30, 24, 4, 4, outline)
c.rect(31, 26, 2, 2, red)
c.set(33, 28, gold_hi)
c.set(28, 30, white)

# ---- horizon + mountains at bottom ----
c.rect(0, 50, 64, 1, horizon)
c.poly([(0, 51), (63, 51), (63, 63), (0, 63)], mount)
c.poly([(0, 63), (12, 53), (26, 63)], mount2)
c.poly([(38, 63), (52, 52), (64, 63)], mount2)

# ---- tagline ----
c.text(18, 54, "BEGIN", (250, 250, 240), font="5x7")
c.rect(14, 52, 36, 1, outline)
c.rect(14, 61, 36, 1, outline)

print(c.stats_text())
finish(c)
