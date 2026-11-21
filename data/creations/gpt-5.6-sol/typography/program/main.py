# Pixel-art title screen: PIXEL QUEST
W, H = 64, 64
result = new_canvas(W, H, background="#071126", name="pixel_quest_title")

# Palette
sky = "#071126"
sky2 = "#0d1d3b"
blue = "#17345a"
blue_hi = "#24517a"
ink = "#020817"
shadow = "#351d47"
gold_dark = "#d57a2a"
gold = "#ffd45a"
gold_hi = "#fff3a1"
cyan_dark = "#238fb0"
cyan = "#62dddf"
cyan_hi = "#c5ffff"
white = "#f2f5d0"

# Layered night-sky backdrop.
result.rect(0, 0, 64, 64, sky)
result.rect(0, 31, 64, 33, sky2)
result.dither(0, 24, 64, 22, [sky, sky2], pattern="bayer4")

# Sparse stars and tiny spark crosses.
for x, y, c in [
    (5, 7, blue_hi), (13, 4, white), (24, 8, blue_hi), (37, 4, white),
    (50, 9, blue_hi), (59, 5, white), (4, 22, white), (60, 25, blue_hi),
    (8, 50, blue_hi), (56, 48, white)
]:
    result.set(x, y, c)
for x, y in [(8, 12), (55, 16)]:
    result.set(x, y, white).set(x-1, y, blue_hi).set(x+1, y, blue_hi)
    result.set(x, y-1, blue_hi).set(x, y+1, blue_hi)

# Distant angular landscape under the title.
result.poly([(0, 51), (7, 44), (12, 49), (20, 40), (28, 50), (37, 43),
             (44, 49), (53, 41), (63, 51), (63, 63), (0, 63)], blue)
result.poly([(0, 57), (10, 51), (17, 56), (26, 49), (35, 57), (45, 50),
             (54, 55), (63, 48), (63, 63), (0, 63)], "#0c2443")
# Ridge highlights.
result.line(7, 44, 12, 49, blue_hi)
result.line(20, 40, 25, 47, blue_hi)
result.line(53, 41, 58, 46, blue_hi)

FONT = {
    "P": ["11110","10001","10001","11110","10000","10000","10000"],
    "I": ["11111","00100","00100","00100","00100","00100","11111"],
    "X": ["10001","10001","01010","00100","01010","10001","10001"],
    "E": ["11111","10000","10000","11110","10000","10000","11111"],
    "L": ["10000","10000","10000","10000","10000","10000","11111"],
    "Q": ["01110","10001","10001","10001","10101","10010","01101"],
    "U": ["10001","10001","10001","10001","10001","10001","01110"],
    "S": ["01111","10000","10000","01110","00001","00001","11110"],
    "T": ["11111","00100","00100","00100","00100","00100","00100"],
}

def pixel_cells(word, x0, y0, scale=2, gap=2):
    cells = []
    x = x0
    for ch in word:
        for gy, row in enumerate(FONT[ch]):
            for gx, bit in enumerate(row):
                if bit == "1":
                    for yy in range(scale):
                        for xx in range(scale):
                            cells.append((x + gx*scale + xx, y0 + gy*scale + yy))
        x += 5*scale + gap
    return set(cells)

def draw_title(word, x, y, dark, mid, hi):
    cells = pixel_cells(word, x, y)
    # Chunky one-pixel outline around the complete bitmap.
    outline_cells = set()
    for px, py in cells:
        for ox, oy in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(1,-1),(-1,1),(1,1)]:
            if (px+ox, py+oy) not in cells:
                outline_cells.add((px+ox, py+oy))
    # Purple offset shadow gives depth while preserving the dark keyline.
    for px, py in outline_cells:
        result.set(px+1, py+2, shadow)
    for px, py in outline_cells:
        result.set(px, py, ink)
    for px, py in cells:
        # Horizontal two-tone bands within each 2px source row.
        local_y = py - y
        colour = hi if local_y % 2 == 0 else mid
        if local_y >= 10:
            colour = mid if local_y % 2 == 0 else dark
        result.set(px, py, colour)

# Both rows are 58 px wide, centered with a 5 px vertical overlap between keylines.
draw_title("PIXEL", 3, 14, gold_dark, gold, gold_hi)
draw_title("QUEST", 3, 34, cyan_dark, cyan, cyan_hi)

# Framing ornaments: gem-like corner brackets and a centered quest marker.
for x, flip in [(2, 1), (61, -1)]:
    result.set(x, 11, gold).set(x, 12, gold_hi).set(x, 13, gold)
    result.set(x + flip, 12, gold)
for x in range(24, 40):
    result.set(x, 57, blue_hi)
result.set(23, 57, cyan_dark).set(40, 57, cyan_dark)
result.poly([(32, 54), (35, 57), (32, 60), (29, 57)], ink)
result.poly([(32, 55), (34, 57), (32, 59), (30, 57)], gold)
result.set(32, 56, gold_hi)

# Crisp lower border.
result.rect(0, 62, 64, 2, ink)
result.line(0, 61, 63, 61, blue_hi)

view(result, scale=8, margin=0)
finish(result)
