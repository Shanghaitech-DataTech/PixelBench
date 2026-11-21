from pixelbench_api import new_canvas, view, finish

W = H = 64
c = new_canvas(W, H, background="#081225", name="pixel_quest_title")

# Palette: deep arcade-night backdrop with restrained jewel tones.
NAVY = "#081225"
NAVY2 = "#0d1c38"
BLUE = "#132b4d"
INK = "#020711"
OUTLINE = "#311b52"
PURPLE = "#6b3f8f"
GOLD_DARK = "#b65a35"
GOLD = "#f3a83b"
GOLD_HI = "#ffe06a"
CYAN_DARK = "#167a91"
CYAN = "#35c6c9"
CYAN_HI = "#9bf6db"
WHITE = "#f5f2d0"
PINK = "#ef6f91"
GREEN = "#70d36b"

# Subtle horizontal bands establish depth without competing with the title.
c.rect(0, 0, 64, 64, NAVY)
c.rect(0, 7, 64, 49, NAVY2)
c.rect(0, 9, 64, 45, BLUE)
c.rect(0, 11, 64, 41, NAVY2)

# Sparse stars and corner sparks.
for x, y, col in [
    (4,5,WHITE),(11,8,CYAN_HI),(20,4,GOLD_HI),(42,5,WHITE),(54,8,PINK),(60,4,CYAN_HI),
    (3,27,CYAN),(60,25,GOLD),(5,50,PINK),(58,51,GREEN)
]:
    c.set(x, y, col)
for x, y, col in [(7,7,GOLD_HI),(56,6,CYAN_HI)]:
    c.set(x,y,col); c.set(x-1,y,col); c.set(x+1,y,col); c.set(x,y-1,col); c.set(x,y+1,col)

FONT = {
    "P":["11110","10001","10001","11110","10000","10000","10000"],
    "I":["11111","00100","00100","00100","00100","00100","11111"],
    "X":["10001","10001","01010","00100","01010","10001","10001"],
    "E":["11111","10000","10000","11110","10000","10000","11111"],
    "L":["10000","10000","10000","10000","10000","10000","11111"],
    "Q":["01110","10001","10001","10001","10101","10010","01101"],
    "U":["10001","10001","10001","10001","10001","10001","01110"],
    "S":["01111","10000","10000","01110","00001","00001","11110"],
    "T":["11111","00100","00100","00100","00100","00100","00100"],
}

def make_mask(text, x0, y0, scale=2, gap=2):
    pts = set()
    x = x0
    for ch in text:
        glyph = FONT[ch]
        for gy, row in enumerate(glyph):
            for gx, bit in enumerate(row):
                if bit == "1":
                    for yy in range(scale):
                        for xx in range(scale):
                            pts.add((x + gx*scale + xx, y0 + gy*scale + yy))
        x += 5*scale + gap
    return pts

def draw_title(text, x, y, fill, hi):
    pts = make_mask(text, x, y)
    # Chunky diagonal drop shadow.
    for px, py in pts:
        c.set(px+2, py+3, INK)
    # One-pixel silhouette outline.
    edge = set()
    for px, py in pts:
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            if (px+dx, py+dy) not in pts:
                edge.add((px+dx, py+dy))
    for p in edge:
        c.set(p[0], p[1], OUTLINE)
    for px, py in pts:
        c.set(px, py, fill)
    # Consistent top-edge shine gives the block letters carved volume.
    for px, py in pts:
        if (px, py-1) not in pts:
            c.set(px, py, hi)

# Five 10px-wide letters + four 2px gaps = 58px, centered.
draw_title("PIXEL", 3, 13, GOLD, GOLD_HI)
draw_title("QUEST", 3, 34, CYAN, CYAN_HI)

# Divider gem and tiny quest markers between title rows.
c.line(20, 30, 27, 30, PURPLE)
c.line(37, 30, 44, 30, PURPLE)
c.set(31,29,PINK); c.set(32,29,PINK); c.set(30,30,PINK); c.set(31,30,WHITE); c.set(32,30,WHITE); c.set(33,30,PINK); c.set(31,31,PINK); c.set(32,31,PINK)

# Ground-line ornament anchors the composition like a game-title plaque.
c.rect(7, 53, 50, 1, PURPLE)
c.rect(12, 55, 40, 1, "#263c5d")
c.set(5,53,GOLD); c.set(6,53,GOLD_HI); c.set(57,53,CYAN_HI); c.set(58,53,CYAN)

# Small centered prompt, readable but clearly subordinate.
c.text(4, 57, "PRESS START", WHITE, spacing=0, font="5x7")

view(c, scale=8, margin=0)
finish(c)
