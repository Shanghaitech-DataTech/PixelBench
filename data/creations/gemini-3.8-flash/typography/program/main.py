from pixelbench_api import *

def build_complete_title_screen():
    # -------------------------------------------------------------
    # 1. Background Canvas
    # -------------------------------------------------------------
    bg = new_canvas(64, 64, name="bg")
    
    # Atmospheric twilight sky gradient (y = 0 to 63)
    sky_palette = [
        "#09081a", "#0b0a1f", "#0d0c24", "#100f2a",
        "#131131", "#171438", "#1c1741", "#211b4a",
        "#271f54", "#2d235f", "#332669", "#392873",
        "#3c2875", "#3c2673", "#38226b", "#321d61",
        "#2a1754", "#221146", "#1a0b38", "#13072b"
    ]
    for y in range(64):
        idx = min(len(sky_palette) - 1, int(y / 64.0 * len(sky_palette)))
        bg.line(0, y, 63, y, sky_palette[idx])
        
    # Distant mountain silhouettes at the horizon (y = 52 to 63)
    mountain_back = "#1a0e36"
    mountain_front = "#100724"
    
    # Mountain peak profiles
    back_heights = [
        57, 56, 55, 54, 53, 52, 53, 54, 55, 56, 57, 56, 55, 54, 55, 56,
        57, 58, 57, 56, 55, 54, 53, 52, 51, 52, 53, 54, 55, 56, 55, 54,
        53, 54, 55, 56, 57, 56, 55, 54, 53, 52, 53, 54, 55, 56, 57, 58,
        57, 56, 55, 54, 53, 52, 53, 54, 55, 56, 55, 54, 53, 52, 53, 54
    ]
    front_heights = [
        60, 60, 59, 58, 57, 58, 59, 60, 61, 60, 59, 58, 57, 56, 57, 58,
        59, 60, 60, 59, 58, 57, 56, 55, 56, 57, 58, 59, 60, 61, 60, 59,
        58, 57, 56, 57, 58, 59, 60, 60, 59, 58, 57, 56, 57, 58, 59, 60,
        61, 60, 59, 58, 57, 56, 55, 56, 57, 58, 59, 60, 61, 61, 62, 62
    ]
    for x in range(64):
        bg.line(x, back_heights[x], x, 63, mountain_back)
        bg.line(x, front_heights[x], x, 63, mountain_front)
        
    # Stars in the sky
    def draw_star(c, cx, cy, core_col, ray_col=None):
        c.set(cx, cy, core_col)
        if ray_col:
            c.set(cx - 1, cy, ray_col)
            c.set(cx + 1, cy, ray_col)
            c.set(cx, cy - 1, ray_col)
            c.set(cx, cy + 1, ray_col)

    # Sparkling 4-point cross stars
    draw_star(bg, 8, 5, "#ffffff", "#7af4ff")
    draw_star(bg, 55, 5, "#ffffff", "#ffe538")
    draw_star(bg, 3, 22, "#ffffff", "#7af4ff")
    draw_star(bg, 60, 22, "#ffffff", "#ffe538")
    
    # Smaller twinkling stars
    stars_small = [
        (16, 3, "#ffffff"), (23, 7, "#7af4ff"), (38, 2, "#fffbb5"), (48, 6, "#ffffff"),
        (5, 12, "#7af4ff"), (58, 13, "#fffbb5"), (2, 38, "#6a5b9e"), (61, 36, "#6a5b9e"),
        (4, 46, "#7af4ff"), (59, 45, "#ffe538"), (12, 50, "#6a5b9e"), (52, 49, "#6a5b9e"),
    ]
    for sx, sy, scol in stars_small:
        bg.set(sx, sy, scol)

    # -------------------------------------------------------------
    # 2. Main Title Canvas ("PIXEL QUEST")
    # -------------------------------------------------------------
    title_canvas = new_canvas(64, 64, name="title")
    title_pixels = set()

    # Color Gradients
    pixel_gradient = [
        "#ffffff", # row 0: specular highlight
        "#c2f9ff", # row 1: pale ice
        "#6befff", # row 2: bright neon cyan
        "#2ad8f8", # row 3: vivid electric cyan
        "#0ab8e8", # row 4: vibrant azure
        "#009cd6", # row 5: deep sky blue
        "#0082be", # row 6: royal blue
        "#006aa6", # row 7: ocean blue
        "#00538e", # row 8: deep cobalt
        "#063d72", # row 9: navy blue
        "#082b58", # row 10: midnight blue base
    ]
    
    quest_gradient = [
        "#ffffff", # row 0: specular highlight
        "#fffbb5", # row 1: pale cream gold
        "#ffe538", # row 2: bright pure yellow
        "#ffd020", # row 3: brilliant gold
        "#f5b610", # row 4: warm gold
        "#e89d06", # row 5: radiant golden amber
        "#d48200", # row 6: amber orange
        "#bf6900", # row 7: rich amber
        "#a85300", # row 8: warm bronze
        "#944000", # row 9: deep bronze
        "#823000", # row 10: bronze rust
        "#732500", # row 11: burnished bronze
        "#661d00", # row 12: deep bronze base
        "#591700", # row 13: warm dark base
        "#4e1200", # row 14: dark rim base
    ]

    # Letter Bitmaps for PIXEL (height 11)
    P = [
        "1111110",
        "1111111",
        "1100011",
        "1100011",
        "1111111",
        "1111110",
        "1100000",
        "1100000",
        "1100000",
        "1100000",
        "1100000",
    ]
    I = [
        "11111",
        "11111",
        "01110",
        "01110",
        "01110",
        "01110",
        "01110",
        "01110",
        "01110",
        "11111",
        "11111",
    ]
    X = [
        "1100011",
        "1100011",
        "0110110",
        "0011100",
        "0011100",
        "0001000",
        "0011100",
        "0011100",
        "0110110",
        "1100011",
        "1100011",
    ]
    E = [
        "111111",
        "111111",
        "110000",
        "110000",
        "111110",
        "111110",
        "110000",
        "110000",
        "111111",
        "111111",
        "111111",
    ]
    L = [
        "110000",
        "110000",
        "110000",
        "110000",
        "110000",
        "110000",
        "110000",
        "110000",
        "111111",
        "111111",
        "111111",
    ]

    # Render PIXEL
    # Total width: 7+2 + 5+2 + 7+2 + 6+2 + 6 = 39.
    px = 12
    py = 10
    for let in [P, I, X, E, L]:
        lw = len(let[0])
        for y, row in enumerate(let):
            base_col = pixel_gradient[y]
            for x, ch in enumerate(row):
                if ch == '1':
                    col = base_col
                    if y == 0:
                        col = "#ffffff"
                    title_canvas.set(px + x, py + y, col)
                    title_pixels.add((px + x, py + y))
        px += lw + 2

    # Letter Bitmaps for QUEST (height 15)
    Q = [
        "0011111100",
        "0111111110",
        "1110000111",
        "1100000011",
        "1100110011", # ruby gem
        "1100110011", # ruby gem
        "1100000011",
        "1100000011",
        "1100000011",
        "1110000111",
        "0111001110",
        "0011111111", # tail begins
        "0000001111",
        "0000000111",
        "0000000011",
    ]
    U = [
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11000011",
        "11100111",
        "01100110",
        "01111110",
        "00111100",
        "00011000",
    ]
    E_Q = [
        "11111111",
        "11111111",
        "11111111",
        "11000000",
        "11000000",
        "11000000",
        "11111100",
        "11111100",
        "11000000",
        "11000000",
        "11000000",
        "11000000",
        "11111111",
        "11111111",
        "11111111",
    ]
    S = [
        "01111110",
        "11111111",
        "11000011",
        "11000000",
        "11110000",
        "01111100",
        "00011110",
        "00001111",
        "00000011",
        "00000011",
        "11000011",
        "11111111",
        "01111110",
        "00111100",
        "00011000",
    ]
    T = [
        "111111111",
        "111111111",
        "111111111",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "000111000",
        "00001000",
    ]

    # Render QUEST
    # Total width: 10+2 + 8+2 + 8+2 + 8+2 + 9 = 51.
    qx = 6
    qy = 24
    for l_idx, let in enumerate([Q, U, E_Q, S, T]):
        lw = len(let[0])
        for y, row in enumerate(let):
            base_col = quest_gradient[y]
            for x, ch in enumerate(row):
                if ch == '1':
                    col = base_col
                    if y == 0:
                        col = "#ffffff"
                    # Ruby core in Q
                    if l_idx == 0 and (y == 4 or y == 5) and (x == 4 or x == 5):
                        if y == 4 and x == 4:
                            col = "#ffffff"
                        elif y == 4 and x == 5:
                            col = "#ff2255"
                        else:
                            col = "#990022"
                    # Golden shiny tail of Q
                    if l_idx == 0 and y >= 11 and x >= 6:
                        if y == 11:
                            col = "#ffd020"
                        elif y == 12:
                            col = "#f5b610"
                        elif y == 13:
                            col = "#e89d06"
                        else:
                            col = "#d48200"
                    title_canvas.set(qx + x, qy + y, col)
                    title_pixels.add((qx + x, qy + y))
        qx += lw + 2

    # Star glints on title lettering
    def add_glint(c, cx, cy, c_core, c_arm):
        c.set(cx, cy, c_core)
        title_pixels.add((cx, cy))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            c.set(cx + dx, cy + dy, c_arm)
            title_pixels.add((cx + dx, cy + dy))
            
    # Glint on top-left of 'P'
    add_glint(title_canvas, 12, 10, "#ffffff", "#bbf8ff")
    # Glint on top-right of 'T'
    add_glint(title_canvas, 57, 24, "#ffffff", "#fffbb5")

    # -------------------------------------------------------------
    # 3. Outline & 3D Shadow Layers (for Title only)
    # -------------------------------------------------------------
    shadow = new_canvas(64, 64, name="shadow")
    outline = new_canvas(64, 64, name="outline")
    shadow_col = "#040310"
    outline_col = "#060416"
    
    # 3D Drop shadow (2 px down, 1 px right)
    for x, y in title_pixels:
        for sx, sy in [(0, 1), (0, 2), (1, 1), (1, 2)]:
            nx, ny = x + sx, y + sy
            if 0 <= nx < 64 and 0 <= ny < 64:
                shadow.set(nx, ny, shadow_col)

    # 1-pixel tight outline around title lettering
    for x, y in title_pixels:
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < 64 and 0 <= ny < 64:
                    outline.set(nx, ny, outline_col)

    # -------------------------------------------------------------
    # 4. Foreground UI / Decorations Layer
    # -------------------------------------------------------------
    ui = new_canvas(64, 64, name="ui")
    
    # Golden ornamental divider bar below QUEST (y = 42)
    div_y = 42
    # Filigree wings with shadow
    ui.line(16, div_y + 1, 47, div_y + 1, "#070414") # shadow
    ui.line(16, div_y, 47, div_y, "#d48200")
    ui.line(20, div_y, 43, div_y, "#f5b610")
    ui.line(26, div_y, 37, div_y, "#ffe538")
    
    # Center diamond crest with ruby gem
    ui.set(31, div_y - 1, "#ffe538")
    ui.set(32, div_y - 1, "#ffffff")
    ui.set(31, div_y + 1, "#d48200")
    ui.set(32, div_y + 1, "#d48200")
    ui.set(30, div_y, "#ffe538")
    ui.set(33, div_y, "#ffe538")
    ui.set(31, div_y, "#ffffff") # ruby gleam
    ui.set(32, div_y, "#ff2255") # ruby gem

    # "PRESS START" Text at y = 47..51
    font_3x5 = {
        'P': ["111", "101", "111", "100", "100"],
        'R': ["111", "101", "110", "101", "101"],
        'E': ["111", "100", "111", "100", "111"],
        'S': ["111", "100", "111", "001", "111"],
        'T': ["111", "010", "010", "010", "010"],
        'A': ["111", "101", "111", "101", "101"],
        ' ': ["00", "00", "00", "00", "00"],
    }
    
    ps_text = "PRESS START"
    # Measure width
    ps_w = 0
    for ch in ps_text:
        ps_w += len(font_3x5[ch][0]) + 1
    ps_w -= 1
    
    ps_x = (64 - ps_w) // 2
    ps_y = 47
    
    # Draw crisp 1px drop shadow for PRESS START
    cur_x = ps_x
    for ch in ps_text:
        glyph = font_3x5[ch]
        gw = len(glyph[0])
        for y, row in enumerate(glyph):
            for x, bit in enumerate(row):
                if bit == '1':
                    ui.set(cur_x + x, ps_y + y + 1, "#070414")
        cur_x += gw + 1
        
    # Draw PRESS START lettering
    cur_x = ps_x
    for ch in ps_text:
        glyph = font_3x5[ch]
        gw = len(glyph[0])
        for y, row in enumerate(glyph):
            for x, bit in enumerate(row):
                if bit == '1':
                    col = "#ffffff" if y == 0 else ("#ffe538" if y < 3 else "#e89d06")
                    ui.set(cur_x + x, ps_y + y, col)
        cur_x += gw + 1

    # Bottom subtitle / prompt: subtle retro arcade copyright
    # "- 2026 -" centered at y = 56
    sub_text = "- 2026 -"
    sub_font = {
        '-': ["000", "000", "111", "000", "000"],
        '2': ["111", "001", "111", "100", "111"],
        '0': ["111", "101", "101", "101", "111"],
        '6': ["111", "100", "111", "101", "111"],
        ' ': ["0", "0", "0", "0", "0"],
    }
    sub_w = 0
    for ch in sub_text:
        sub_w += len(sub_font[ch][0]) + 1
    sub_w -= 1
    sub_x = (64 - sub_w) // 2
    sub_y = 56
    
    for ch in sub_text:
        glyph = sub_font[ch]
        gw = len(glyph[0])
        for y, row in enumerate(glyph):
            for x, bit in enumerate(row):
                if bit == '1':
                    ui.set(sub_x + x, sub_y + y, "#8092bd")
        sub_x += gw + 1

    # -------------------------------------------------------------
    # 5. Composite Final Image
    # -------------------------------------------------------------
    result = flatten([bg, shadow, outline, title_canvas, ui])
    return result

c = build_complete_title_screen()
view(c)
finish(c)
