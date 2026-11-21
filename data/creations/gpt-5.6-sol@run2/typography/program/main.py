# Pixel Quest title screen, 64x64
result = new_canvas(64, 64, background="#090b24", name="pixel_quest")

# Palette
bg2 = "#11133a"
bg3 = "#1b1b50"
ink = "#050718"
outline = "#342060"
shadow = "#7a285f"
gold_dark = "#c84b45"
gold = "#f28b42"
gold_hi = "#ffd866"
blue_dark = "#16758f"
blue = "#27b7c6"
blue_hi = "#8cf4de"
white = "#fff3c4"

# Recessed stone-panel background.
result.rect(2, 2, 60, 60, bg2)
result.rect(3, 3, 58, 58, "#0c0e2d")
result.line(4, 11, 59, 11, bg3)
result.line(4, 52, 59, 52, bg3)
# Block joints and sparse texture.
for x in (10, 27, 45):
    result.set(x, 4, bg3)
    result.set(x + 1, 4, bg3)
for x in (16, 38, 54):
    result.set(x, 58, bg3)
for x, y, c in [
    (7,8,white),(56,7,"#7466a8"),(12,12,"#4a3b79"),(50,13,white),
    (5,31,"#7466a8"),(59,28,"#4a3b79"),(9,50,white),(55,48,"#7466a8")]:
    result.set(x,y,c)
# Tiny four-point stars.
for x, y in [(6,16),(57,19),(7,42),(58,39)]:
    result.set(x,y,"#7466a8")
    result.set(x-1,y,"#312a67")
    result.set(x+1,y,"#312a67")
    result.set(x,y-1,"#312a67")
    result.set(x,y+1,"#312a67")

# Crown-like quest gem above the title.
result.poly([(27,8),(29,5),(32,4),(35,5),(37,8),(34,11),(30,11)], ink)
result.poly([(29,8),(31,6),(33,6),(35,8),(33,10),(31,10)], "#e44f6f")
result.set(32,6,"#ffb56b")
result.set(30,7,"#ff7890")
result.set(32,3,"#ffd866")
result.set(25,7,"#7466a8")
result.set(39,7,"#7466a8")

font = {
    "P":["11110","10001","10001","11110","10000","10000","10000"],
    "I":["11111","00100","00100","00100","00100","00100","11111"],
    "X":["10001","10001","01010","00100","01010","10001","10001"],
    "E":["11111","10000","10000","11110","10000","10000","11111"],
    "L":["10000","10000","10000","10000","10000","10000","11111"],
    "Q":["01110","10001","10001","10001","10101","10010","01101"],
    "U":["10001","10001","10001","10001","10001","10001","01110"],
    "S":["01111","10000","10000","01110","00001","00001","11110"],
    "T":["11111","00100","00100","00100","00100","00100","00100"],
    "A":["01110","10001","10001","11111","10001","10001","10001"],
    "R":["11110","10001","10001","11110","10100","10010","10001"],
}

def title_mask(word, x0, y0, scale=2, spacing=2):
    pts = set()
    x = x0
    for ch in word:
        for gy, row in enumerate(font[ch]):
            for gx, bit in enumerate(row):
                if bit == "1":
                    for yy in range(scale):
                        for xx in range(scale):
                            pts.add((x + gx*scale + xx, y0 + gy*scale + yy))
        x += 5*scale + spacing
    return pts

def paint_title(word, y, dark, mid, hi):
    pts = title_mask(word, 3, y)
    # Deep drop shadow first.
    for x, py in pts:
        result.set(x+2, py+3, shadow)
    # One-pixel dark keyline around each glyph.
    border = set()
    for x, py in pts:
        for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
            if (x+dx,py+dy) not in pts:
                border.add((x+dx,py+dy))
    for x, py in border:
        result.set(x, py, ink)
    # Three-band face colors with a bright upper edge.
    for x, py in pts:
        rel = py-y
        col = hi if rel < 3 else (mid if rel < 9 else dark)
        result.set(x, py, col)
    # Sparse shine pixels keep the chunky letter faces lively.
    for x, py in pts:
        if py == y and (x % 4 in (0,1)):
            result.set(x, py, white)

paint_title("PIXEL", 15, gold_dark, gold, gold_hi)
paint_title("QUEST", 35, blue_dark, blue, blue_hi)

# Bottom prompt and small brackets.
result.text(17, 55, "START", "#b7a7d9", font="5x7")
result.set(14,57,"#e44f6f"); result.set(14,58,"#e44f6f")
result.set(48,57,"#e44f6f"); result.set(48,58,"#e44f6f")
result.set(15,56,"#7a285f"); result.set(47,56,"#7a285f")

# Bright corner rivets.
for x, y in [(3,3),(60,3),(3,60),(60,60)]:
    result.set(x,y,"#51448a")

view(result, scale=8, margin=0)
finish(result)
