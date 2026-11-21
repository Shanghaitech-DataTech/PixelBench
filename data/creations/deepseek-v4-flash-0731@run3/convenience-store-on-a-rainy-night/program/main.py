# Convenience store on a rainy night, 64x64, one output canvas.
c = new_canvas(64, 64, background="#141934", name="store")

# ---------- ground ----------
c.rect(0, 43, 64, 11, "#555560")   # sidewalk y43..53
c.rect(0, 52, 64, 2, "#6a6a74")    # curb
c.rect(0, 54, 64, 10, "#23232f")    # road

# ---------- distant silhouettes ----------
c.rect(0, 9, 9, 5, "#0d1128")
c.rect(55, 4, 9, 10, "#0d1128")

# ---------- building ----------
c.rect(8, 13, 47, 32, "#3d3d47")   # front wall x8..54, y13..44
c.rect(8, 13, 47, 2, "#23232c")     # roof cap
c.rect(55, 13, 2, 31, "#2b2b36")    # side wall x55..56, y13..43

# sign band
c.rect(10, 16, 43, 10, "#f5e6b8")   # sign panel y16..25
c.rect(9, 15, 45, 1, "#23232c")
c.rect(9, 26, 45, 1, "#23232c")
c.text(23, 17, "24H", "#c03030", font="5x7")

# glass frame + window
c.rect(9, 27, 46, 15, "#33333c")    # frame y27..41, x9..54
c.rect(10, 28, 35, 4, "#ffdc7a")    # bright window top
c.rect(27, 28, 1, 13, "#33333c")    # mullion
c.rect(10, 32, 35, 8, "#d99a3a")    # lower interior
# shelves
c.rect(11, 34, 16, 1, "#7a4a1a")
c.rect(28, 34, 16, 1, "#7a4a1a")
c.rect(11, 37, 16, 1, "#7a4a1a")
c.rect(28, 37, 16, 1, "#7a4a1a")
# product dots
prods = ["#c8503a", "#3a70c8", "#45a04f", "#e8eef6", "#f2c94c", "#8a5a3a"]
for r, cols in ((35, [12, 15, 18, 21, 24, 29, 32, 35, 38, 41]),
               (36, [13, 17, 20, 23, 30, 33, 36, 39]),
               (38, [11, 14, 16, 28, 31, 34, 37, 40]),
               (39, [29, 33, 37])):
    for k, x in enumerate(cols):
        c.set(x, r, prods[k % len(prods)])
# glass sheen
for x, y in ((14, 28), (13, 29), (12, 30), (48, 28), (47, 29), (46, 30)):
    c.set(x, y, "#fff2b8")

# door (bright glass) + handle
c.rect(46, 28, 8, 12, "#ffe89a")
c.set(53, 33, "#8a8a94")

# ---------- light spill on sidewalk ----------
c.rect(45, 43, 12, 1, "#ffcf5e")    # doorway glow
c.rect(47, 44, 9, 1, "#c98f42")
c.rect(49, 45, 7, 1, "#8a6a3a")
c.rect(50, 46, 5, 1, "#6b5430")
c.rect(13, 44, 31, 1, "#b8863a")    # window spill
c.rect(14, 45, 29, 1, "#8a6a3a")

# ---------- umbrella rack ----------
c.rect(57, 40, 4, 5, "#3e4a5c")     # rack body x57..60, y40..44
c.rect(57, 40, 4, 1, "#5a6a82")     # rim
c.circle(58, 37, 1, "#d04a3a")       # red umbrella
c.set(58, 39, "#23232c")
c.circle(59, 36, 1, "#3a6ac8")       # blue umbrella
c.set(59, 38, "#23232c")
c.set(60, 35, "#45a04f")             # green umbrella tip
c.set(60, 36, "#45a04f")
c.set(60, 37, "#45a04f")

# ---------- parked bicycle ----------
c.circle(15, 43, 2, "#1e1e26")
c.circle(23, 43, 2, "#1e1e26")
c.set(15, 43, "#8a8a94")
c.set(23, 43, "#8a8a94")
c.line(15, 43, 19, 40, "#d24a34")
c.line(23, 43, 19, 40, "#d24a34")
c.line(19, 40, 17, 39, "#d24a34")
c.set(16, 39, "#1e1e26")             # seat
c.set(20, 38, "#1e1e26")             # handlebar
c.set(21, 38, "#1e1e26")
c.set(22, 39, "#1e1e26")

# ---------- person in raincoat entering ----------
c.circle(50, 31, 2, "#f2c94c")       # hood
c.set(50, 32, "#c89318")
c.rect(47, 32, 6, 8, "#e8b41e")     # coat
c.set(47, 33, "#c89318")
c.set(52, 33, "#c89318")
c.set(48, 38, "#d9a81d")
c.set(51, 38, "#d9a81d")
c.set(47, 40, "#332f1e")             # boots
c.set(50, 40, "#332f1e")
c.set(51, 40, "#332f1e")
c.set(49, 41, "#332f1e")

# ---------- puddles ----------
c.ellipse(20, 58, 6, 2, "#15151f")
c.ellipse(40, 59, 5, 2, "#15151f")
c.ellipse(53, 57, 4, 1, "#15151f")
c.ellipse(8, 61, 3, 1, "#15151f")

# reflections in puddles
for x in (16, 20, 24):
    for y in (56, 57, 58, 59):
        c.set(x, y, "#8a5a22" if y < 58 else "#6b4520")
for x in (49, 51, 53):
    c.set(x, 57, "#c8842e")
    c.set(x, 58, "#c8842e")
    c.set(x, 59, "#a06a26")
c.set(14, 59, "#2e3a6a")
c.set(45, 57, "#2e3a6a")
c.set(22, 57, "#8aa0d8")
c.set(38, 59, "#8aa0d8")
c.set(52, 58, "#8aa0d8")

# ---------- rain ----------
for j in range(0, 63):
    for i in range(1, 63):
        if (i * 5 + j * 11) % 19 == 0:
            if 9 <= i <= 55 and 14 <= j <= 45:
                continue
        else:
            continue
        col = "#8aa0e0" if j < 42 else "#a8bcf0"
        c.set(i, j, col)
        c.set(i - 1, j + 1, col)

print(c.stats_text())
finish(c)
