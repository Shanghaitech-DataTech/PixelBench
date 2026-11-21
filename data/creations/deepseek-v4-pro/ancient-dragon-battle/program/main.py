c = new_canvas(256, 256, background=None, name="battle")

OUT = "#120e12"

def rblock(x, y, w, h, color, outline=OUT, o=1):
    c.rect(x - o, y - o, w + 2 * o, h + 2 * o, outline)
    c.rect(x, y, w, h, color)

def thick_line(x0, y0, x1, y1, r, color):
    steps = max(abs(x1 - x0), abs(y1 - y0)) // 2 + 1
    for i in range(steps + 1):
        t = i / steps
        x = round(x0 + (x1 - x0) * t)
        y = round(y0 + (y1 - y0) * t)
        c.circle(x, y, r, color)

# ---------------------------------------------------------------
# Sky gradient with dithered transitions
# ---------------------------------------------------------------
stops = [
    (0, "#241a42"),
    (30, "#3a2860"),
    (60, "#5c3470"),
    (88, "#8a3f70"),
    (112, "#b85260"),
    (132, "#d96e4c"),
    (146, "#ef9a52"),
    (158, "#f7c06a"),
]
for i in range(len(stops) - 1):
    y0, col0 = stops[i]
    y1, col1 = stops[i + 1]
    c.rect(0, y0, 256, y1 - y0, col0)
    if i < len(stops) - 2:
        c.dither(0, y1 - 2, 256, 4, [col0, col1], "checker")

# sun low on the left horizon
c.circle(60, 124, 24, "#e89a54")
c.circle(60, 124, 18, "#f4bd76")
c.circle(60, 124, 11, "#fbe0a4")

# high thin clouds
c.ellipse(40, 46, 26, 3, "#5c2a50")
c.ellipse(128, 28, 24, 3, "#4c2448")
c.ellipse(206, 40, 28, 3, "#5c2a50")
c.ellipse(88, 66, 22, 2, "#5c2a50")
c.ellipse(176, 62, 18, 2, "#4c2448")

# ---------------------------------------------------------------
# Distant mountains
# ---------------------------------------------------------------
c.poly([(0, 158), (0, 124), (22, 112), (40, 130), (58, 104), (76, 126),
        (96, 116), (120, 132), (142, 108), (162, 128), (184, 112),
        (206, 132), (228, 116), (244, 128), (255, 120), (255, 158)],
       "#33204e")
c.poly([(0, 158), (0, 134), (30, 120), (54, 138), (78, 124), (104, 142),
        (128, 126), (150, 140), (176, 128), (200, 144), (224, 130),
        (244, 142), (255, 136), (255, 158)],
       "#261a38")

# ---------------------------------------------------------------
# Ground
# ---------------------------------------------------------------
c.rect(0, 156, 256, 22, "#5c3a2c")
c.dither(0, 174, 256, 4, ["#5c3a2c", "#4a2e24"], "checker")
c.rect(0, 178, 256, 30, "#4a2e24")
c.dither(0, 204, 256, 4, ["#4a2e24", "#38221c"], "checker")
c.rect(0, 208, 256, 30, "#38221c")
c.dither(0, 234, 256, 4, ["#38221c", "#241510"], "checker")
c.rect(0, 238, 256, 18, "#241510")

# rocky hill under the castle
c.poly([(70, 200), (112, 156), (150, 136), (188, 156), (232, 200),
        (232, 212), (70, 212)], "#3a2620")
c.poly([(70, 200), (112, 156), (150, 136), (188, 156), (232, 200)],
       "#4a3024")

# ---------------------------------------------------------------
# Castle (center-right)
# ---------------------------------------------------------------
STONE_MID = "#6a5a60"
STONE_DARK = "#4c4048"
STONE_LIGHT = "#8a7a7e"
WINDOW = "#e8843a"
WINDOW_HI = "#f7c26a"

# main keep
rblock(118, 66, 64, 86, STONE_MID)
rblock(122, 60, 56, 8, STONE_DARK)
# lit / shadowed faces
c.rect(118, 66, 5, 86, STONE_LIGHT)
c.rect(172, 66, 10, 86, "#3c343c")
# crenellations on keep top
for mx in range(122, 176, 8):
    rblock(mx, 54, 5, 6, STONE_MID)
    c.set(mx, 54, STONE_LIGHT)
    c.set(mx, 58, STONE_DARK)

# side towers
rblock(84, 86, 32, 66, STONE_MID)
rblock(184, 86, 32, 66, STONE_MID)
rblock(86, 80, 28, 8, STONE_DARK)
rblock(186, 80, 28, 8, STONE_DARK)
c.rect(84, 86, 4, 66, STONE_LIGHT)
c.rect(184, 86, 4, 66, STONE_LIGHT)
c.rect(112, 86, 4, 66, "#3c343c")
c.rect(212, 86, 4, 66, "#3c343c")
# left tower crenellations
for mx in range(86, 116, 7):
    rblock(mx, 74, 4, 6, STONE_MID)
    c.set(mx, 74, STONE_LIGHT)
# right tower: burning conical roof
c.poly([(182, 84), (200, 40), (218, 84)], STONE_DARK)
c.poly([(184, 82), (200, 44), (200, 82)], STONE_MID)
c.poly([(200, 40), (196, 62), (200, 66), (204, 62)], "#e85a30")
c.poly([(200, 42), (198, 56), (200, 60), (202, 56)], "#f9c860")
# flames above the keep roof
c.poly([(150, 56), (146, 36), (152, 46), (154, 30), (160, 44), (162, 34), (168, 52)], "#e85a30")
c.poly([(154, 44), (153, 36), (157, 42), (158, 34), (163, 44)], "#f9c860")

# gatehouse
rblock(130, 140, 40, 30, STONE_DARK)
c.rect(140, 150, 20, 20, "#0e0a0c")
# portcullis lines
for gy in range(152, 168, 3):
    c.line(140, gy, 159, gy, "#2a2024")

# lit windows
for wy in (84, 104):
    for wx in (126, 138, 150, 162, 174):
        rblock(wx, wy, 4, 6, WINDOW, o=0)
        c.set(wx + 1, wy + 1, WINDOW_HI)
for wx in (92, 102, 192, 202):
    rblock(wx, 102, 4, 6, WINDOW, o=0)
    c.set(wx + 1, 103, WINDOW_HI)

# ---------------------------------------------------------------
# Knights on the ramparts
# ---------------------------------------------------------------
def knight(x, y, body="#5a4a52", spear="#c8a878", shield="#7a4a3a"):
    # y is the feet line (top of wall)
    c.rect(x - 1, y - 8, 3, 8, OUT)
    c.rect(x, y - 7, 3, 7, body)
    c.rect(x, y - 9, 3, 2, "#9a8a88")
    c.line(x + 1, y - 9, x + 1, y - 16, spear)
    c.rect(x - 2, y - 7, 2, 4, shield)

def banner(x, y, col="#b03030"):
    c.line(x, y, x, y - 13, OUT)
    c.line(x + 1, y, x + 1, y - 13, OUT)
    c.poly([(x + 1, y - 13), (x + 10, y - 11), (x + 1, y - 7)], col)
    c.line(x + 1, y - 13, x + 1, y - 7, OUT)

def bird(x, y):
    c.line(x, y, x + 3, y - 2, "#1a1220")
    c.line(x + 3, y - 2, x + 6, y, "#1a1220")

# (knight figures are drawn after the dragon so they stay visible)

# ---------------------------------------------------------------
# Dragon silhouette flying above, breathing fire
# ---------------------------------------------------------------
DRAGON = "#120c1e"
WING_MEM = "#2c2040"
RIM = "#f0a050"

# left (far) wing
c.poly([(128, 60), (28, 10), (54, 26), (74, 20), (96, 38), (116, 32), (124, 56)],
       DRAGON)
# right (near) wing
c.poly([(154, 60), (228, 10), (202, 26), (182, 20), (160, 38), (140, 32), (146, 56)],
       DRAGON)

# tail
thick_line(130, 62, 86, 78, 4, DRAGON)
thick_line(86, 78, 58, 90, 3, DRAGON)
thick_line(58, 90, 42, 96, 2, DRAGON)
c.poly([(32, 98), (44, 90), (38, 104)], DRAGON)

# body
c.ellipse(148, 58, 20, 11, DRAGON)
# neck
thick_line(160, 54, 198, 38, 5, DRAGON)
# head
c.ellipse(206, 38, 10, 7, DRAGON)
# snout and jaw
c.poly([(208, 34), (224, 38), (208, 42)], DRAGON)
c.poly([(206, 42), (216, 45), (206, 48)], DRAGON)
# horn
c.poly([(202, 33), (194, 22), (200, 30)], DRAGON)

# wing membrane detail
c.line(120, 50, 74, 26, WING_MEM)
c.line(116, 52, 96, 40, WING_MEM)
c.line(160, 50, 182, 26, WING_MEM)
c.line(164, 52, 160, 40, WING_MEM)

# warm rim light on sun-facing edges
c.line(126, 58, 30, 12, RIM)
c.line(156, 58, 226, 12, RIM)
c.line(130, 48, 168, 48, RIM)
c.line(160, 52, 196, 36, RIM)
c.line(128, 60, 42, 96, RIM)

# eye
c.set(208, 36, "#ffb040")

# fire breath toward castle
c.poly([(212, 38), (226, 46), (204, 80), (176, 64), (192, 46)], "#e85a30")
c.poly([(212, 38), (222, 46), (202, 74), (188, 60), (198, 46)], "#f9c860")
c.poly([(212, 38), (218, 42), (204, 64), (194, 52), (200, 42)], "#fbe8a8")

# knights on the ramparts (drawn after the dragon so they stay visible)
for kx in (124, 132, 140, 172):
    knight(kx, 54)
for kx in (90, 99, 108):
    knight(kx, 74)

# war banners on the battlements
banner(86, 74)
banner(114, 74)
banner(120, 54)
banner(180, 54)

# distant birds
bird(30, 30)
bird(42, 24)
bird(222, 26)
bird(236, 34)
bird(18, 48)
bird(248, 56)

# ---------------------------------------------------------------
# Siege towers
# ---------------------------------------------------------------
def siege_tower(x, y_base, w, h, wood="#7a5232", plank="#5c3c24"):
    c.rect(x - 4, y_base - h - 8, w + 8, h + 12, OUT)
    c.rect(x, y_base - h, w, h, wood)
    # diagonal bracing
    c.line(x, y_base - h, x + w, y_base, plank)
    c.line(x + w, y_base - h, x, y_base, plank)
    # platform and crenellations
    c.rect(x - 5, y_base - h - 7, w + 10, 6, plank)
    for mx in range(x - 5, x + w + 4, 6):
        c.rect(mx, y_base - h - 11, 4, 4, wood)
    # wheels
    c.circle(x + 6, y_base + 4, 4, OUT)
    c.circle(x + 6, y_base + 4, 2, plank)
    c.circle(x + w - 6, y_base + 4, 4, OUT)
    c.circle(x + w - 6, y_base + 4, 2, plank)

siege_tower(36, 200, 30, 82)
siege_tower(212, 206, 22, 58)

# ladders leaning toward the castle
thick_line(58, 120, 104, 152, 1, "#3a2418")
thick_line(232, 150, 206, 176, 1, "#3a2418")

# ---------------------------------------------------------------
# Soldiers in formation (foreground)
# ---------------------------------------------------------------
def soldier(x, y, body="#4a3430", spear="#c8a878", shield="#7a4a3a"):
    c.rect(x - 1, y - 8, 3, 8, OUT)
    c.rect(x, y - 7, 3, 7, body)
    c.rect(x, y - 9, 3, 2, "#8a6a58")
    c.line(x + 1, y - 9, x + 1, y - 16, spear)
    c.rect(x - 2, y - 7, 2, 4, shield)

row1 = list(range(34, 222, 14))
row2 = list(range(42, 222, 14))
for x in row1:
    soldier(x, 224)
for x in row2:
    soldier(x, 238)

# scattered battlefield rocks and a small foreground fire
c.rect(16, 240, 8, 5, OUT)
c.rect(17, 241, 6, 3, "#2c1c16")
c.rect(176, 248, 10, 5, OUT)
c.rect(177, 249, 8, 3, "#2c1c16")
c.rect(232, 236, 7, 4, OUT)
c.rect(233, 237, 5, 2, "#2c1c16")
c.poly([(12, 246), (10, 234), (14, 238), (16, 230), (20, 238), (22, 234), (26, 246)], "#e85a30")
c.poly([(14, 240), (14, 236), (18, 240)], "#f9c860")

# ---------------------------------------------------------------
# Arrows flying toward the castle
# ---------------------------------------------------------------
def arrow(x0, y0, x1, y1):
    c.line(x0, y0, x1, y1, OUT)
    c.line(x0 + 1, y0 - 1, x1 + 1, y1 - 1, OUT)
    c.line(x0, y0, x1 - 4, y1 - 4, "#c8a878")
    c.line(x0 + 1, y0 - 1, x1 - 3, y1 - 5, "#c8a878")
    c.poly([(x1, y1), (x1 - 6, y1 - 3), (x1 - 6, y1 + 3)], OUT)
    c.line(x0 - 1, y0 - 1, x0 - 4, y0 - 4, OUT)
    c.line(x0 + 2, y0 - 1, x0 + 5, y0 - 4, OUT)

arrow(10, 84, 44, 50)
arrow(22, 74, 60, 36)
arrow(46, 92, 82, 56)
arrow(6, 104, 40, 70)
arrow(34, 66, 74, 26)
arrow(240, 60, 200, 34)
arrow(250, 82, 212, 50)

# ---------------------------------------------------------------
# Smoke and embers
# ---------------------------------------------------------------
SMOKE_D = "#4c4452"
SMOKE_M = "#6e6474"
SMOKE_L = "#948a98"

def smoke_puff(cx, cy, r, col):
    c.circle(cx, cy, r, col)
    c.circle(cx - r, cy - r // 2, max(1, r // 2), col)
    c.circle(cx + r, cy - r // 2, max(1, r // 2), col)

# plume from burning right tower
smoke_puff(200, 60, 6, SMOKE_D)
smoke_puff(196, 48, 8, SMOKE_M)
smoke_puff(190, 34, 10, SMOKE_L)
smoke_puff(206, 40, 6, SMOKE_M)
# plume from keep fire
smoke_puff(160, 46, 6, SMOKE_D)
smoke_puff(156, 34, 8, SMOKE_M)
smoke_puff(150, 22, 9, SMOKE_L)
# plume from a burning siege tower (left)
smoke_puff(52, 104, 5, SMOKE_D)
smoke_puff(48, 92, 7, SMOKE_M)
smoke_puff(42, 78, 8, SMOKE_L)

# embers
for ex, ey in [(168, 52), (184, 44), (196, 28), (204, 50), (150, 36),
               (176, 56), (158, 58), (192, 62), (180, 70), (206, 32),
               (140, 44), (166, 40), (54, 86), (60, 98), (46, 66),
               (214, 60), (226, 40), (186, 30), (174, 34)]:
    c.set(ex, ey, "#f7c26a")
for ex, ey in [(172, 46), (190, 38), (200, 56), (152, 50), (184, 62), (162, 52),
               (50, 96), (58, 84), (44, 74), (210, 46), (196, 36), (188, 58)]:
    c.set(ex, ey, "#e85a30")

# ---------------------------------------------------------------
# Preview and stats
# ---------------------------------------------------------------
def preview(step=4, region=None):
    pal = c.palette()
    idx_rgba = {p["index"]: p["rgba"] for p in pal}
    ramp = " .,:;irsXA253hMHGS#9B&@"
    x0, y0, x1, y1 = region if region else (0, 0, 255, 255)
    out = []
    for y in range(y0, y1 + 1, step):
        row = []
        for x in range(x0, x1 + 1, step):
            idx = c.get(x, y)
            if idx is None:
                row.append(" ")
                continue
            r, g, b, a = idx_rgba.get(idx, (0, 0, 0, 0))
            if a < 32:
                row.append(" ")
                continue
            lum = (r * 299 + g * 587 + b * 114) / 1000 / 255
            if r > 160 and g > 100 and b < 120 and r > b + 60:
                row.append("F")
            elif r > 170 and g > 140 and b < 130:
                row.append("Y")
            else:
                row.append(ramp[min(len(ramp) - 1, int(lum * (len(ramp) - 1)))])
        out.append("".join(row))
    print("\n".join(out))

print(c.stats_text())
preview(4)
print("---- SKY/DRAGON (step 2) ----")
preview(2, (0, 0, 255, 96))
print("---- CASTLE (step 2) ----")
preview(2, (70, 50, 235, 165))

finish(c)
