"""
Tavern Interior 64x64 Pixel Art - Final Polish
"""
from pixelbench_api import new_canvas, view, save, finish

def build_tavern():
    c = new_canvas(64, 64, name="tavern")

    # Curated palette of cohesive colors
    P = {
        # Darks & Outlines
        "black": "#0c0812",
        "dark1": "#160f1b",
        "dark2": "#221726",
        "dark3": "#322338",

        # Stone wall & mortar
        "stone_dark": "#3d3047",
        "stone_mid": "#564563",
        "stone_hi": "#735f82",

        # Tavern Timber & Wood (dark to bright)
        "wood_1": "#261317",
        "wood_2": "#3d1e1f",
        "wood_3": "#592c25",
        "wood_4": "#783d2e",
        "wood_5": "#9c5237",
        "wood_6": "#be6b42",
        "wood_7": "#de8852",

        # Polished Bar Counter mahogany
        "bar_rich": "#853628",
        "bar_warm": "#aa472f",
        "bar_bright": "#cc5e36",
        "bar_sheen": "#f09a56",

        # Floor Planks
        "floor_base": "#362029",
        "floor_warm": "#4d2d34",
        "floor_lit": "#6e4143",

        # Wrought Iron / Steel Hoops
        "iron_dark": "#24252e",
        "iron_mid": "#424552",
        "iron_light": "#686c7d",
        "iron_hi": "#989cae",

        # Brass / Gold / Taps / Coins
        "brass_dark": "#573c14",
        "brass_mid": "#946b20",
        "brass_bright": "#cf9e30",
        "brass_hi": "#f7cb4d",

        # Warm Lantern Glow & Lighting
        "glow_core": "#ffffff",
        "glow_yellow": "#ffeb5c",
        "glow_amber": "#f5b025",
        "glow_orange": "#dc6714",
        "glow_red": "#9c3518",

        # Crimson Velvet Stool Cushions
        "cushion_dark": "#47101b",
        "cushion_mid": "#7e192c",
        "cushion_bright": "#b5243c",
        "cushion_hi": "#e84860",

        # Glassware, Beer & Foam
        "glass_body": "#567994",
        "glass_hi": "#b8e2fa",
        "ale_amber": "#9e5210",
        "ale_gold": "#e3861b",
        "foam_mid": "#e8ce82",

        # Bottle Jewel Liquors
        "ruby_dark": "#520c1d",
        "ruby_bright": "#be2044",
        "green_dark": "#0e361d",
        "green_bright": "#24ad55",
        "blue_dark": "#122947",
        "blue_bright": "#2b7ad4",

        # Smoke & Haze
        "smoke_1": "#4c3e52",
        "smoke_2": "#74627a",
        "smoke_3": "#a08ba6",
        "smoke_4": "#ccbcd1",

        # Tavern Cat
        "cat_mid": "#a35824",
        "cat_bright": "#d97d36",
        "cat_light": "#f5b578",
    }

    for name, hexcode in P.items():
        c.color(hexcode, name)

    # ----------------------------------------------------
    # 1. BASE BACKGROUND WALL & CEILING TIMBERS
    # ----------------------------------------------------
    c.rect(0, 0, 64, 64, "dark1")

    # Stone wall back area (y: 3 to 35)
    for y in range(3, 36, 4):
        c.line(0, y, 63, y, "stone_dark")
    for row, y in enumerate(range(4, 35, 4)):
        x_shift = 6 if row % 2 == 1 else 0
        for x in range(x_shift, 64, 12):
            c.line(x, y, x, y+2, "stone_dark")
            if x+1 < 64:
                c.set(x+1, y, "stone_mid")

    # Heavy ceiling beams
    c.rect(0, 0, 64, 4, "wood_1")
    c.line(0, 1, 63, 1, "wood_3")
    c.line(0, 2, 63, 2, "wood_2")
    c.line(0, 3, 63, 3, "black")

    # Left timber pillar (x: 0..3)
    c.rect(0, 0, 4, 64, "wood_1")
    c.line(1, 0, 1, 63, "wood_3")
    c.line(2, 0, 2, 63, "wood_2")
    c.line(3, 0, 3, 63, "black")

    # Right timber pillar (x: 60..63)
    c.rect(60, 0, 4, 64, "wood_1")
    c.line(61, 0, 61, 63, "wood_3")
    c.line(62, 0, 62, 63, "wood_2")
    c.line(60, 0, 60, 63, "black")

    # Timber brackets at ceiling corners
    for i in range(7):
        c.set(4+i, 4+i//2, "wood_2")
        c.set(59-i, 4+i//2, "wood_2")

    # ----------------------------------------------------
    # 2. BACK-BAR ALCOVE & BOTTLE SHELVES (x: 5 to 43, y: 5 to 34)
    # ----------------------------------------------------
    c.rect(5, 5, 38, 29, "black")
    c.rect(6, 6, 36, 27, "wood_1")

    # Vertical wood panel lines inside alcove
    for px in range(10, 42, 5):
        c.line(px, 6, px, 32, "wood_2")

    # Arch decorative moulding at top of alcove (y: 5..7)
    c.line(6, 6, 41, 6, "wood_3")
    c.line(8, 5, 39, 5, "wood_4")
    c.line(10, 5, 37, 5, "wood_5")

    # 3 Sturdy Wooden Shelves
    for sy in [14, 22, 30]:
        c.rect(6, sy, 36, 2, "wood_3")
        c.line(6, sy, 41, sy, "wood_5")
        c.line(7, sy, 40, sy, "wood_6")
        c.line(6, sy+2, 41, sy+2, "black")

    # Central vertical shelf divider (x: 23..24)
    c.rect(23, 7, 2, 24, "wood_2")
    c.line(24, 7, 24, 30, "wood_4")

    # Bottle drawing function
    def draw_bottle(bx, by, btype, c_dark, c_bright):
        if btype == "wine":
            c.rect(bx, by-4, 3, 4, c_bright)
            c.line(bx, by-4, bx, by-1, c_dark)
            c.set(bx+1, by-3, "glow_core")
            c.line(bx+1, by-6, bx+1, by-5, c_dark)
            c.set(bx+1, by-6, "brass_dark")
            c.set(bx, by, "black")
            c.set(bx+2, by, "black")
        elif btype == "round":
            c.rect(bx, by-3, 3, 3, c_bright)
            c.set(bx+1, by-4, c_dark)
            c.set(bx+1, by-5, "brass_dark")
            c.set(bx, by-1, c_dark)
            c.set(bx+1, by-2, "glow_core")
        elif btype == "flask":
            c.rect(bx, by-4, 4, 4, c_bright)
            c.line(bx, by-4, bx, by-1, c_dark)
            c.line(bx+3, by-4, bx+3, by-1, c_dark)
            c.set(bx+1, by-2, "glow_core")
            c.line(bx+1, by-5, bx+2, by-5, c_dark)
            c.set(bx+1, by-6, "brass_dark")
        elif btype == "jug":
            c.rect(bx, by-4, 4, 5, "wood_5")
            c.line(bx, by-4, bx, by, "wood_2")
            c.set(bx+2, by-3, "wood_7")
            c.line(bx+1, by-5, bx+2, by-5, "brass_dark")
            c.set(bx+4, by-3, "wood_1")
            c.set(bx+4, by-2, "wood_1")
        elif btype == "vial":
            c.rect(bx, by-2, 2, 3, c_bright)
            c.set(bx, by-2, "glow_core")
            c.set(bx, by-3, "brass_dark")

    # POPULATE SHELF 1 (y=13)
    draw_bottle(7, 13, "wine", "ruby_dark", "ruby_bright")
    draw_bottle(11, 13, "round", "green_dark", "green_bright")
    draw_bottle(19, 13, "flask", "ale_amber", "ale_gold")
    draw_bottle(26, 13, "jug", "wood_2", "wood_5")
    draw_bottle(31, 13, "round", "blue_dark", "blue_bright")
    draw_bottle(35, 13, "wine", "green_dark", "green_bright")
    draw_bottle(41, 13, "vial", "ruby_dark", "ruby_bright")

    # POPULATE SHELF 2 (y=21)
    draw_bottle(7, 21, "flask", "ale_amber", "ale_gold")
    draw_bottle(12, 21, "wine", "ruby_dark", "ruby_bright")
    draw_bottle(16, 21, "round", "green_dark", "green_bright")
    draw_bottle(20, 21, "vial", "blue_dark", "blue_bright")
    draw_bottle(26, 21, "round", "ruby_dark", "ruby_bright")
    draw_bottle(30, 21, "flask", "ale_amber", "ale_gold")
    draw_bottle(35, 21, "jug", "wood_2", "wood_5")
    draw_bottle(40, 21, "vial", "green_dark", "green_bright")

    # POPULATE SHELF 3 (y=29: Tumblers, Goblets & Pewter Mugs)
    # Hanging wine glasses under shelf 2
    for hx in [8, 12, 16, 20]:
        c.set(hx, 24, "glass_body")
        c.line(hx, 25, hx, 26, "glass_body")
        c.set(hx, 26, "glass_hi")

    # Pewter mugs at x=7..9, 12..14
    for mx in [7, 12]:
        c.rect(mx, 26, 3, 4, "iron_mid")
        c.line(mx, 26, mx, 29, "iron_dark")
        c.set(mx+1, 26, "iron_hi")
        c.set(mx+3, 27, "iron_dark")
        c.set(mx+3, 28, "iron_dark")
    # Amber tumblers at x=17, 26, 31, 36
    for gx in [17, 26, 31, 36]:
        c.rect(gx, 27, 3, 3, "glass_body")
        c.rect(gx, 28, 3, 2, "ale_amber")
        c.set(gx+1, 27, "glass_hi")
        c.set(gx+1, 28, "ale_gold")

    # ----------------------------------------------------
    # 3. WOODEN BARRELS ON RACK BEHIND THE BAR (RIGHT SIDE: x: 44 to 59)
    # ----------------------------------------------------
    c.rect(44, 6, 2, 26, "wood_2")
    c.rect(58, 6, 2, 26, "wood_2")
    c.line(44, 18, 59, 18, "wood_1")
    c.line(44, 30, 59, 30, "wood_1")

    def draw_rack_barrel(bx, by, w, h):
        cx = bx + w // 2
        cy = by + h // 2
        rx = w // 2
        ry = h // 2
        c.ellipse(cx, cy, rx, ry, "black")
        c.ellipse(cx, cy, rx-1, ry-1, "wood_2")
        c.ellipse(cx, cy, rx-2, ry-2, "wood_3")
        c.ellipse(cx, cy, rx-3, ry-3, "wood_4")
        # Vertical stave lines
        c.line(cx-2, by+2, cx-2, by+h-3, "wood_2")
        c.line(cx+2, by+2, cx+2, by+h-3, "wood_2")
        # Directional light from lantern
        c.line(cx-3, cy-1, cx-1, cy-2, "wood_6")
        c.set(cx-2, cy-1, "wood_7")
        # Central wooden bung
        c.set(cx, cy-1, "black")
        c.set(cx, cy, "brass_dark")
        # Iron hoops
        c.set(bx+1, cy, "iron_mid")
        c.set(bx+w-2, cy, "iron_mid")

    draw_rack_barrel(45, 8, 13, 10)
    draw_rack_barrel(45, 20, 13, 10)

    # Brass Spigot / Tap on Lower Barrel
    c.line(49, 26, 52, 26, "brass_mid")
    c.set(52, 25, "brass_bright")
    c.line(52, 26, 52, 28, "brass_bright")
    c.set(52, 27, "brass_hi")
    c.set(52, 29, "ale_gold") # dripping ale!

    # Tasting cup
    c.rect(51, 30, 3, 2, "iron_dark")
    c.set(52, 30, "foam_mid")

    # STURDY STORAGE CRATE UNDER BARREL RACK (x: 44 to 59, y: 32 to 44)
    # Rich warm wood storage base
    c.rect(44, 32, 16, 12, "wood_2")
    c.rect(45, 33, 14, 10, "wood_3")
    c.line(44, 36, 59, 36, "black")
    c.line(44, 40, 59, 40, "black")
    c.line(44, 32, 59, 32, "wood_5")
    c.line(44, 37, 59, 37, "wood_5")
    c.line(44, 41, 59, 41, "wood_5")
    # Left corner iron strap only (keeping right clean behind foreground barrel)
    c.rect(44, 32, 2, 12, "iron_dark")
    c.set(44, 34, "iron_light")
    c.set(44, 39, "iron_light")
    c.line(58, 32, 58, 43, "wood_2")
    c.line(59, 32, 59, 43, "wood_1")

    # ----------------------------------------------------
    # 4. WARM YELLOW HANGING LAMPS (x: 16 and x: 39)
    # ----------------------------------------------------
    # WARM NIGHTTIME LIGHTING GLOW (drawn behind lanterns onto stone wall)
    def apply_clean_glow(lx, ly):
        for dy in range(-5, 6):
            for dx in range(-5, 6):
                d2 = dx*dx + dy*dy
                gx = lx + dx
                gy = ly + dy
                if 4 <= gx < 60 and 3 <= gy < 33:
                    cur = c.get(gx, gy)
                    # Only glow over stone wall or deep dark background
                    if cur in [c.color("dark1"), c.color("stone_dark")]:
                        if d2 <= 14:
                            c.set(gx, gy, "glow_amber" if (gx+gy)%2==0 else "glow_orange")
                        elif d2 <= 26 and (gx+gy)%2 == 0:
                            c.set(gx, gy, "glow_red")

    apply_clean_glow(16, 10)
    apply_clean_glow(39, 10)

    def draw_lantern(lx, ly):
        for cy in range(3, ly):
            c.set(lx, cy, "iron_light" if cy % 2 == 0 else "iron_mid")
        c.set(lx, ly-1, "iron_light")
        c.line(lx-2, ly, lx+2, ly, "brass_dark")
        c.line(lx-3, ly+1, lx+3, ly+1, "brass_mid")
        c.line(lx-2, ly+1, lx+2, ly+1, "brass_bright")
        c.set(lx, ly, "brass_hi")

        # Glass chamber with glowing warm flame
        c.rect(lx-2, ly+2, 5, 5, "glow_amber")
        c.rect(lx-1, ly+2, 3, 5, "glow_yellow")
        c.rect(lx-1, ly+3, 3, 3, "glow_core")
        c.set(lx, ly+3, "glow_core")
        c.set(lx, ly+4, "glow_core")

        # Outer dark frame / cage ribs
        c.line(lx-3, ly+2, lx-3, ly+6, "black")
        c.line(lx+3, ly+2, lx+3, ly+6, "black")
        c.set(lx-1, ly+2, "brass_mid")
        c.set(lx+1, ly+2, "brass_mid")

        # Lantern bottom cap & drop finial
        c.line(lx-3, ly+7, lx+3, ly+7, "brass_dark")
        c.line(lx-2, ly+7, lx+2, ly+7, "brass_bright")
        c.set(lx, ly+8, "brass_dark")
        c.set(lx, ly+9, "black")

    draw_lantern(16, 7)
    draw_lantern(39, 7)

    # ----------------------------------------------------
    # 5. POLISHED WOODEN BAR COUNTER (x: 0 to 52, y: 34 to 52)
    # ----------------------------------------------------
    c.rect(0, 34, 51, 6, "wood_3")
    c.line(4, 34, 50, 34, "wood_2")
    c.line(4, 35, 50, 35, "bar_rich")
    c.line(4, 36, 50, 36, "bar_warm")
    c.line(4, 37, 50, 37, "bar_bright")

    # Specular reflections under left lamp (x: 12..20)
    c.line(12, 35, 20, 35, "bar_sheen")
    c.line(13, 36, 19, 36, "bar_sheen")
    c.line(15, 36, 17, 36, "glow_yellow")
    c.line(13, 37, 19, 37, "bar_bright")

    # Specular reflections under right lamp (x: 35..43)
    c.line(35, 35, 43, 35, "bar_sheen")
    c.line(36, 36, 42, 36, "bar_sheen")
    c.line(38, 36, 40, 36, "glow_yellow")
    c.line(36, 37, 42, 37, "bar_bright")

    # Front bullnose molding
    c.line(0, 38, 50, 38, "bar_sheen")
    c.line(0, 39, 50, 39, "bar_bright")
    c.set(51, 36, "bar_bright")
    c.set(51, 37, "bar_sheen")
    c.set(51, 38, "bar_bright")
    c.set(51, 39, "wood_3")
    c.line(52, 36, 52, 39, "black")

    # Shadow groove
    c.line(0, 40, 51, 40, "wood_1")

    # Counter front face (y: 41 to 52)
    c.rect(0, 41, 51, 11, "wood_3")

    # Wainscot wood panels
    panels = [(5, 17), (19, 31), (33, 47)]
    for p_left, p_right in panels:
        pw = p_right - p_left + 1
        c.rect(p_left, 42, pw, 9, "wood_2")
        c.rect(p_left+1, 43, pw-2, 7, "wood_3")
        c.line(p_left+1, 43, p_right-1, 43, "wood_4")
        c.line(p_left+1, 43, p_left+1, 49, "wood_4")
        c.line(p_left+2, 49, p_right-1, 49, "wood_2")
        c.line(p_right-1, 44, p_right-1, 49, "wood_2")

    c.line(51, 40, 51, 52, "wood_2")
    c.line(52, 40, 52, 52, "black")

    # Brass Foot Rail along base of counter - visible between stools
    rail_segments = [(3, 8), (19, 23), (33, 37), (47, 50)]
    for rx0, rx1 in rail_segments:
        c.line(rx0, 50, rx1, 50, "brass_bright")
        c.line(rx0, 51, rx1, 51, "brass_dark")
    for bx in [6, 21, 35, 49]:
        c.rect(bx, 49, 2, 4, "brass_mid")
        c.set(bx, 49, "brass_hi")

    # ----------------------------------------------------
    # 6. ITEMS ON THE BAR COUNTER (y: 31 to 39)
    # ----------------------------------------------------
    # ITEM 1: Pewter Beer Stein with frothy foam at x: 8..13, y: 32..36
    c.rect(9, 33, 4, 4, "iron_mid")
    c.line(9, 33, 9, 36, "iron_dark")
    c.line(10, 33, 10, 36, "iron_light")
    c.set(11, 33, "iron_hi")
    c.set(11, 34, "iron_hi")
    c.line(8, 33, 8, 36, "iron_dark")
    c.set(9, 33, "iron_dark")
    c.set(9, 36, "iron_dark")
    c.rect(9, 31, 5, 2, "foam_mid")
    c.line(10, 30, 13, 30, "glow_core")
    c.set(11, 30, "glow_core")
    c.set(12, 31, "glow_core")
    c.set(12, 33, "glow_core")
    c.set(12, 34, "foam_mid")

    # ITEM 2: Whiskey Tumbler with Amber Liquid at x: 22..25, y: 33..36
    c.rect(22, 33, 4, 4, "glass_body")
    c.rect(23, 34, 2, 3, "ale_amber")
    c.set(23, 34, "ale_gold")
    c.set(24, 35, "ale_gold")
    c.line(22, 33, 25, 33, "glass_hi")
    c.set(23, 33, "glow_core")

    # ITEM 3: Tavern Pipe & Ashtray with smoke at x: 29..33, y: 35..37
    c.line(29, 37, 33, 37, "brass_dark")
    c.line(30, 36, 32, 36, "brass_mid")
    c.rect(30, 34, 3, 3, "wood_4")
    c.line(30, 34, 30, 36, "wood_2")
    c.set(31, 34, "glow_orange")
    c.set(32, 34, "glow_yellow")
    c.line(33, 36, 35, 37, "wood_2")
    c.set(35, 37, "wood_1")

    # ITEM 4: Wine Goblet & Gold coins at x: 43..48, y: 33..37
    c.rect(43, 33, 3, 3, "glass_body")
    c.line(43, 34, 45, 34, "ruby_bright")
    c.set(44, 34, "ruby_dark")
    c.set(43, 33, "glass_hi")
    c.set(44, 35, "glass_body")
    c.set(44, 36, "glass_body")
    c.line(43, 37, 45, 37, "glass_hi")
    c.line(46, 37, 48, 37, "brass_dark")
    c.line(46, 36, 47, 36, "brass_bright")
    c.set(47, 36, "brass_hi")

    # ----------------------------------------------------
    # 7. FOREGROUND WOODEN BARREL (RIGHT SIDE: x: 52 to 62, y: 44 to 62)
    # ----------------------------------------------------
    c.ellipse(57, 45, 5, 2, "black")
    c.ellipse(57, 45, 4, 1, "wood_4")
    c.line(54, 45, 60, 45, "wood_5")
    c.set(56, 45, "wood_6")

    for by in range(47, 63):
        if by in [47, 48, 61, 62]:
            x0, x1 = 52, 62
        elif by in [49, 50, 59, 60]:
            x0, x1 = 51, 63
        else:
            x0, x1 = 50, 63
        c.line(x0, by, x1, by, "wood_4")
        c.set(x0, by, "black")
        c.set(x1, by, "black")
        c.set(x0+1, by, "wood_5")
        c.set(x0+2, by, "wood_6")
        c.set(x0+3, by, "wood_7")
        c.line(x0+4, by, x1-2, by, "wood_4")
        c.set(x1-1, by, "wood_2")

    for hy in [49, 50, 57, 58]:
        c.line(51, hy, 63, hy, "iron_dark")
        c.line(52, hy, 56, hy, "iron_light")
        c.set(53, hy, "iron_hi")
        c.set(54, hy, "glow_core")
        c.set(58, hy, "iron_mid")

    for by in range(47, 63):
        c.set(55, by, "black")
        c.set(59, by, "wood_2")

    # Mug on foreground barrel
    c.rect(55, 42, 3, 3, "glass_body")
    c.line(55, 43, 57, 43, "ale_amber")
    c.set(56, 43, "ale_gold")
    c.set(55, 42, "glow_core")
    c.set(56, 41, "glow_core")
    c.set(57, 42, "foam_mid")
    c.set(58, 42, "glass_hi")

    # ----------------------------------------------------
    # 8. FLOOR (y: 52 to 63)
    # ----------------------------------------------------
    floor_breaks = [52, 55, 58, 61, 64]
    for i in range(len(floor_breaks)-1):
        y0 = floor_breaks[i]
        y1 = floor_breaks[i+1] - 1
        for fy in range(y0, y1+1):
            c.line(0, fy, 50, fy, "floor_base")
            # Pools of light
            for fx in range(8, 22):
                dist = abs(fx - 15)
                if dist <= 2:
                    c.set(fx, fy, "floor_lit")
                elif dist <= 6:
                    c.set(fx, fy, "floor_warm")
            for fx in range(31, 46):
                dist = abs(fx - 39)
                if dist <= 2:
                    c.set(fx, fy, "floor_lit")
                elif dist <= 6:
                    c.set(fx, fy, "floor_warm")
        c.line(0, y1, 50, y1, "wood_1")
        joint_x = (i * 17 + 11) % 46 + 4
        c.line(joint_x, y0, joint_x, y1, "black")

    # Sleeping Cat on Rug (x: 4 to 11, y: 58 to 62)
    c.ellipse(7, 60, 4, 2, "wood_1")
    c.ellipse(7, 60, 3, 1, "floor_warm")
    c.ellipse(7, 60, 3, 1, "cat_mid")
    c.ellipse(7, 60, 2, 1, "cat_bright")
    c.set(8, 59, "cat_light")
    c.set(6, 60, "glow_core")
    c.set(5, 59, "cat_bright")
    c.set(5, 58, "cat_light")
    c.set(9, 60, "cat_mid")

    # ----------------------------------------------------
    # 9. BAR STOOLS (x: 14, x: 28, x: 42)
    # ----------------------------------------------------
    def draw_bar_stool(cx):
        # Shadow behind cushion
        c.line(cx-4, 40, cx+4, 40, "black")

        # Crimson leather cushion
        c.ellipse(cx, 42, 5, 2, "black")
        c.ellipse(cx, 42, 4, 1, "cushion_mid")
        c.line(cx-2, 41, cx+2, 41, "cushion_bright")
        c.set(cx, 41, "cushion_hi")
        c.set(cx-1, 41, "cushion_hi")
        c.line(cx-4, 43, cx+4, 43, "cushion_dark")

        # Wooden rim ring with brass studs
        c.line(cx-4, 44, cx+4, 44, "wood_2")
        c.line(cx-4, 45, cx+4, 45, "black")
        c.line(cx-3, 44, cx+3, 44, "wood_4")
        for sx in [cx-4, cx-2, cx, cx+2, cx+4]:
            c.set(sx, 44, "brass_bright")

        # Stool legs
        # Back legs
        c.line(cx-2, 46, cx-3, 56, "wood_1")
        c.line(cx+2, 46, cx+3, 56, "wood_1")

        # Circular footrest rung at y: 52
        c.line(cx-4, 52, cx+4, 52, "wood_2")
        c.line(cx-3, 52, cx+3, 52, "wood_5")
        c.set(cx-1, 52, "brass_bright")

        # Front legs
        c.line(cx-3, 46, cx-5, 58, "black")
        c.line(cx-2, 46, cx-4, 58, "wood_4")
        c.line(cx-3, 50, cx-4, 58, "wood_6")

        c.line(cx+3, 46, cx+5, 58, "black")
        c.line(cx+2, 46, cx+4, 58, "wood_4")
        c.line(cx+3, 50, cx+4, 58, "wood_6")

        c.set(cx-4, 59, "black")
        c.set(cx+4, 59, "black")

        c.ellipse(cx, 59, 4, 1, "floor_base")
        c.ellipse(cx, 59, 2, 1, "black")

    draw_bar_stool(14)
    draw_bar_stool(28)
    draw_bar_stool(42)

    # ----------------------------------------------------
    # 10. SMOKY ATMOSPHERE
    # ----------------------------------------------------
    # Billowing, curling plume of pipe smoke
    pipe_smoke = [
        (31, 33, "smoke_4"), (31, 32, "smoke_4"),
        (32, 31, "smoke_3"), (32, 30, "smoke_4"), (33, 30, "smoke_3"),
        (33, 29, "smoke_3"), (33, 28, "smoke_2"), (34, 28, "smoke_3"),
        (34, 27, "smoke_3"), (34, 26, "smoke_2"),
        (33, 25, "smoke_2"), (32, 25, "smoke_2"),
        (31, 24, "smoke_3"), (32, 24, "smoke_2"),
        (31, 23, "smoke_3"), (30, 23, "smoke_2"),
        (31, 22, "smoke_2"), (30, 22, "smoke_1"),
        (31, 21, "smoke_2"), (32, 21, "smoke_1"),
        (32, 20, "smoke_2"), (33, 20, "smoke_1"),
        (33, 19, "smoke_1"), (34, 19, "smoke_1"),
        (34, 18, "smoke_2"), (35, 18, "smoke_1"),
        (35, 17, "smoke_1"), (36, 17, "smoke_1"),
        (35, 16, "smoke_1"), (34, 15, "smoke_1"),
    ]
    for sx, sy, scol in pipe_smoke:
        c.set(sx, sy, scol)

    # Ceiling smoke haze
    ceiling_smoke = [
        (10, 5, "smoke_1"), (11, 5, "smoke_2"), (12, 5, "smoke_1"),
        (13, 6, "smoke_1"), (14, 5, "smoke_2"), (15, 6, "smoke_1"),
        (20, 5, "smoke_1"), (21, 6, "smoke_2"), (22, 5, "smoke_1"),
        (26, 5, "smoke_1"), (27, 6, "smoke_2"), (28, 5, "smoke_1"),
        (32, 5, "smoke_2"), (33, 6, "smoke_1"), (34, 5, "smoke_1"),
        (43, 5, "smoke_1"), (44, 6, "smoke_2"), (45, 5, "smoke_1"),
        (51, 5, "smoke_1"), (52, 6, "smoke_1"), (53, 5, "smoke_2"),
    ]
    for sx, sy, scol in ceiling_smoke:
        c.set(sx, sy, scol)

    # ----------------------------------------------------
    # 11. CRISP DARK OUTLINE BORDER
    # ----------------------------------------------------
    c.rect(0, 0, 64, 1, "black")
    c.rect(0, 63, 64, 1, "black")
    c.rect(0, 0, 1, 64, "black")
    c.rect(63, 0, 1, 64, "black")

    print("Stats:", c.stats_text())
    print("Distinct colors used:", len(c.palette()))
    view(c)
    finish(c)
    return c

c = build_tavern()
