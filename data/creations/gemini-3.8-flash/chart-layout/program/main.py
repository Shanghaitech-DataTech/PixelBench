from pixelbench_api import *

def draw_apple(c, ox, oy):
    stem = "#5a2e12"
    leaf_dk = "#1b5e20"
    leaf_md = "#2e7d32"
    leaf_lt = "#66bb6a"
    red_dk = "#7d0b0b"
    red_md = "#d91e1e"
    red_lt = "#ff6b6b"
    shine  = "#ffffff"

    # Stem and leaf
    c.set(ox + 4, oy + 0, stem)
    c.set(ox + 4, oy + 1, stem)
    c.set(ox + 5, oy + 1, leaf_dk)
    c.set(ox + 6, oy + 1, leaf_lt)
    c.set(ox + 5, oy + 2, leaf_md)
    c.set(ox + 6, oy + 2, leaf_lt)
    c.set(ox + 7, oy + 2, leaf_md)

    # Apple top lobes
    c.set(ox + 2, oy + 2, red_dk)
    c.set(ox + 3, oy + 2, red_md)
    c.set(ox + 4, oy + 2, red_dk)

    # Apple body
    c.set(ox + 1, oy + 3, red_dk)
    c.set(ox + 2, oy + 3, red_md)
    c.set(ox + 3, oy + 3, red_lt)
    c.set(ox + 4, oy + 3, red_lt)
    c.set(ox + 5, oy + 3, red_md)
    c.set(ox + 6, oy + 3, red_md)
    c.set(ox + 7, oy + 3, red_md)
    c.set(ox + 8, oy + 3, red_dk)

    c.set(ox + 1, oy + 4, red_dk)
    c.set(ox + 2, oy + 4, red_lt)
    c.set(ox + 3, oy + 4, shine)
    c.set(ox + 4, oy + 4, red_lt)
    c.set(ox + 5, oy + 4, red_md)
    c.set(ox + 6, oy + 4, red_md)
    c.set(ox + 7, oy + 4, red_md)
    c.set(ox + 8, oy + 4, red_dk)

    c.set(ox + 1, oy + 5, red_dk)
    c.set(ox + 2, oy + 5, red_md)
    c.set(ox + 3, oy + 5, red_lt)
    c.set(ox + 4, oy + 5, red_md)
    c.set(ox + 5, oy + 5, red_md)
    c.set(ox + 6, oy + 5, red_md)
    c.set(ox + 7, oy + 5, red_dk)
    c.set(ox + 8, oy + 5, red_dk)

    c.set(ox + 1, oy + 6, red_dk)
    c.set(ox + 2, oy + 6, red_md)
    c.set(ox + 3, oy + 6, red_md)
    c.set(ox + 4, oy + 6, red_md)
    c.set(ox + 5, oy + 6, red_md)
    c.set(ox + 6, oy + 6, red_dk)
    c.set(ox + 7, oy + 6, red_dk)
    c.set(ox + 8, oy + 6, red_dk)

    c.set(ox + 2, oy + 7, red_dk)
    c.set(ox + 3, oy + 7, red_md)
    c.set(ox + 4, oy + 7, red_md)
    c.set(ox + 5, oy + 7, red_dk)
    c.set(ox + 6, oy + 7, red_dk)
    c.set(ox + 7, oy + 7, red_dk)

    c.set(ox + 2, oy + 8, red_dk)
    c.set(ox + 3, oy + 8, red_md)
    c.set(ox + 4, oy + 8, red_dk)
    c.set(ox + 5, oy + 8, red_dk)
    c.set(ox + 6, oy + 8, red_md)
    c.set(ox + 7, oy + 8, red_dk)

    # Bottom lobes
    c.set(ox + 3, oy + 9, red_dk)
    c.set(ox + 6, oy + 9, red_dk)

def draw_banana(c, ox, oy):
    stem = "#5a2e12"
    tip_grn = "#736a10"
    ban_hi = "#fff176"
    ban_shine = "#ffffff"
    ban_md = "#f5c010"
    ban_dk = "#996300"

    # Smooth crescent banana
    c.set(ox + 7, oy + 0, stem)
    c.set(ox + 6, oy + 1, tip_grn)
    c.set(ox + 7, oy + 1, stem)

    c.set(ox + 5, oy + 2, ban_hi)
    c.set(ox + 6, oy + 2, ban_md)
    c.set(ox + 7, oy + 2, ban_dk)

    c.set(ox + 4, oy + 3, ban_hi)
    c.set(ox + 5, oy + 3, ban_md)
    c.set(ox + 6, oy + 3, ban_dk)

    c.set(ox + 3, oy + 4, ban_shine)
    c.set(ox + 4, oy + 4, ban_hi)
    c.set(ox + 5, oy + 4, ban_dk)

    c.set(ox + 2, oy + 5, ban_hi)
    c.set(ox + 3, oy + 5, ban_md)
    c.set(ox + 4, oy + 5, ban_dk)

    c.set(ox + 2, oy + 6, ban_hi)
    c.set(ox + 3, oy + 6, ban_md)
    c.set(ox + 4, oy + 6, ban_dk)

    c.set(ox + 3, oy + 7, ban_hi)
    c.set(ox + 4, oy + 7, ban_md)
    c.set(ox + 5, oy + 7, ban_dk)

    c.set(ox + 4, oy + 8, ban_md)
    c.set(ox + 5, oy + 8, ban_dk)
    c.set(ox + 6, oy + 8, stem)

    c.set(ox + 6, oy + 9, stem)

def draw_orange(c, ox, oy):
    stem = "#5a2e12"
    leaf_dk = "#1b5e20"
    leaf_lt = "#66bb6a"
    ora_dk = "#a33600"
    ora_md = "#ff7700"
    ora_hi = "#ffa834"
    shine  = "#fff0db"

    # Leaf angled to right
    c.set(ox + 4, oy + 0, leaf_dk)
    c.set(ox + 5, oy + 0, leaf_lt)
    c.set(ox + 3, oy + 1, stem)
    c.set(ox + 4, oy + 1, leaf_dk)
    c.set(ox + 5, oy + 1, leaf_lt)
    c.set(ox + 6, oy + 1, leaf_dk)

    # Orange body
    for x in range(2, 8):
        c.set(ox + x, oy + 2, ora_dk if x in (2, 7) else ora_md)
    c.set(ox + 1, oy + 3, ora_dk)
    c.set(ox + 2, oy + 3, ora_md)
    c.set(ox + 3, oy + 3, ora_hi)
    c.set(ox + 4, oy + 3, ora_hi)
    c.set(ox + 5, oy + 3, ora_md)
    c.set(ox + 6, oy + 3, ora_md)
    c.set(ox + 7, oy + 3, ora_md)
    c.set(ox + 8, oy + 3, ora_dk)

    c.set(ox + 1, oy + 4, ora_dk)
    c.set(ox + 2, oy + 4, ora_hi)
    c.set(ox + 3, oy + 4, shine)
    c.set(ox + 4, oy + 4, ora_hi)
    c.set(ox + 5, oy + 4, ora_md)
    c.set(ox + 6, oy + 4, ora_md)
    c.set(ox + 7, oy + 4, ora_dk)
    c.set(ox + 8, oy + 4, ora_dk)

    c.set(ox + 1, oy + 5, ora_dk)
    c.set(ox + 2, oy + 5, ora_hi)
    c.set(ox + 3, oy + 5, ora_hi)
    c.set(ox + 4, oy + 5, ora_md)
    c.set(ox + 5, oy + 5, ora_md)
    c.set(ox + 6, oy + 5, ora_md)
    c.set(ox + 7, oy + 5, ora_dk)
    c.set(ox + 8, oy + 5, ora_dk)

    c.set(ox + 1, oy + 6, ora_dk)
    c.set(ox + 2, oy + 6, ora_md)
    c.set(ox + 3, oy + 6, ora_md)
    c.set(ox + 4, oy + 6, ora_md)
    c.set(ox + 5, oy + 6, ora_md)
    c.set(ox + 6, oy + 6, ora_dk)
    c.set(ox + 7, oy + 6, ora_dk)
    c.set(ox + 8, oy + 6, ora_dk)

    c.set(ox + 2, oy + 7, ora_dk)
    c.set(ox + 3, oy + 7, ora_md)
    c.set(ox + 4, oy + 7, ora_md)
    c.set(ox + 5, oy + 7, ora_dk)
    c.set(ox + 6, oy + 7, ora_dk)
    c.set(ox + 7, oy + 7, ora_dk)

    for x in range(3, 7):
        c.set(ox + x, oy + 8, ora_dk)

def draw_lemon(c, ox, oy):
    stem = "#5a2e12"
    leaf_dk = "#1b5e20"
    leaf_lt = "#66bb6a"
    lem_dk = "#8f8b00"
    lem_md = "#e8e517"
    lem_hi = "#ffff7a"
    shine  = "#ffffe8"

    # Leaf
    c.set(ox + 4, oy + 0, leaf_dk)
    c.set(ox + 5, oy + 0, leaf_lt)
    c.set(ox + 3, oy + 1, stem)
    c.set(ox + 4, oy + 1, leaf_dk)
    c.set(ox + 5, oy + 1, leaf_lt)
    c.set(ox + 6, oy + 1, leaf_dk)

    # Plump Lemon body with pointed nips
    c.set(ox + 2, oy + 2, lem_dk)
    c.set(ox + 3, oy + 2, lem_hi)
    c.set(ox + 4, oy + 2, lem_hi)
    c.set(ox + 5, oy + 2, lem_md)
    c.set(ox + 6, oy + 2, lem_md)
    c.set(ox + 7, oy + 2, lem_dk)

    c.set(ox + 1, oy + 3, lem_dk)
    c.set(ox + 2, oy + 3, lem_hi)
    c.set(ox + 3, oy + 3, lem_hi)
    c.set(ox + 4, oy + 3, shine)
    c.set(ox + 5, oy + 3, lem_md)
    c.set(ox + 6, oy + 3, lem_md)
    c.set(ox + 7, oy + 3, lem_md)
    c.set(ox + 8, oy + 3, lem_dk)

    c.set(ox + 1, oy + 4, lem_dk)
    c.set(ox + 2, oy + 4, lem_hi)
    c.set(ox + 3, oy + 4, shine)
    c.set(ox + 4, oy + 4, lem_hi)
    c.set(ox + 5, oy + 4, lem_md)
    c.set(ox + 6, oy + 4, lem_md)
    c.set(ox + 7, oy + 4, lem_dk)
    c.set(ox + 8, oy + 4, lem_dk)

    c.set(ox + 0, oy + 5, lem_dk)
    c.set(ox + 1, oy + 5, lem_md)
    c.set(ox + 2, oy + 5, lem_hi)
    c.set(ox + 3, oy + 5, lem_md)
    c.set(ox + 4, oy + 5, lem_md)
    c.set(ox + 5, oy + 5, lem_md)
    c.set(ox + 6, oy + 5, lem_md)
    c.set(ox + 7, oy + 5, lem_dk)
    c.set(ox + 8, oy + 5, lem_md)
    c.set(ox + 9, oy + 5, lem_dk)

    c.set(ox + 1, oy + 6, lem_dk)
    c.set(ox + 2, oy + 6, lem_md)
    c.set(ox + 3, oy + 6, lem_md)
    c.set(ox + 4, oy + 6, lem_md)
    c.set(ox + 5, oy + 6, lem_md)
    c.set(ox + 6, oy + 6, lem_dk)
    c.set(ox + 7, oy + 6, lem_dk)
    c.set(ox + 8, oy + 6, lem_dk)

    c.set(ox + 1, oy + 7, lem_dk)
    c.set(ox + 2, oy + 7, lem_md)
    c.set(ox + 3, oy + 7, lem_md)
    c.set(ox + 4, oy + 7, lem_dk)
    c.set(ox + 5, oy + 7, lem_dk)
    c.set(ox + 6, oy + 7, lem_dk)
    c.set(ox + 7, oy + 7, lem_dk)
    c.set(ox + 8, oy + 7, lem_dk)

    for x in range(2, 8):
        c.set(ox + x, oy + 8, lem_dk)

def draw_grape(c, ox, oy):
    stem = "#5a2e12"
    leaf_dk = "#1b5e20"
    leaf_lt = "#66bb6a"
    grp_dk = "#380d6b"
    grp_md = "#8a2be2"
    grp_hi = "#c471ed"
    shine  = "#f0d6ff"

    c.set(ox + 4, oy + 0, stem)
    c.set(ox + 3, oy + 1, leaf_dk)
    c.set(ox + 4, oy + 1, stem)
    c.set(ox + 5, oy + 1, leaf_lt)
    c.set(ox + 6, oy + 1, leaf_dk)

    c.set(ox + 2, oy + 2, grp_hi)
    c.set(ox + 5, oy + 2, grp_hi)
    c.set(ox + 7, oy + 2, grp_hi)

    c.set(ox + 1, oy + 3, grp_hi)
    c.set(ox + 2, oy + 3, shine)
    c.set(ox + 3, oy + 3, grp_dk)
    c.set(ox + 4, oy + 3, grp_hi)
    c.set(ox + 5, oy + 3, shine)
    c.set(ox + 6, oy + 3, grp_dk)
    c.set(ox + 7, oy + 3, grp_hi)
    c.set(ox + 8, oy + 3, grp_dk)

    c.set(ox + 1, oy + 4, grp_md)
    c.set(ox + 2, oy + 4, grp_dk)
    c.set(ox + 3, oy + 4, grp_dk)
    c.set(ox + 4, oy + 4, grp_md)
    c.set(ox + 5, oy + 4, grp_dk)
    c.set(ox + 6, oy + 4, grp_dk)
    c.set(ox + 7, oy + 4, grp_md)
    c.set(ox + 8, oy + 4, grp_dk)

    c.set(ox + 2, oy + 5, grp_hi)
    c.set(ox + 3, oy + 5, grp_hi)
    c.set(ox + 4, oy + 5, grp_dk)
    c.set(ox + 5, oy + 5, grp_hi)
    c.set(ox + 6, oy + 5, grp_hi)
    c.set(ox + 7, oy + 5, grp_dk)

    c.set(ox + 2, oy + 6, grp_hi)
    c.set(ox + 3, oy + 6, shine)
    c.set(ox + 4, oy + 6, grp_dk)
    c.set(ox + 5, oy + 6, grp_md)
    c.set(ox + 6, oy + 6, grp_dk)
    c.set(ox + 7, oy + 6, grp_dk)

    c.set(ox + 2, oy + 7, grp_dk)
    c.set(ox + 3, oy + 7, grp_dk)
    c.set(ox + 4, oy + 7, grp_hi)
    c.set(ox + 5, oy + 7, grp_dk)
    c.set(ox + 6, oy + 7, grp_dk)

    c.set(ox + 3, oy + 8, grp_hi)
    c.set(ox + 4, oy + 8, grp_md)
    c.set(ox + 5, oy + 8, grp_dk)

    c.set(ox + 4, oy + 9, grp_dk)

def draw_digit(c, x, y, d, col):
    patterns = {
        '0': ["111", "101", "101", "101", "111"],
        '1': ["010", "110", "010", "010", "111"],
        '2': ["111", "001", "111", "100", "111"],
        '4': ["101", "101", "111", "001", "001"],
        '5': ["111", "100", "111", "001", "111"],
        '7': ["111", "001", "010", "010", "010"],
    }
    pat = patterns[d]
    for row_idx, row in enumerate(pat):
        for col_idx, ch in enumerate(row):
            if ch == '1':
                c.set(x + col_idx, y + row_idx, col)

def draw_num(c, x, y, s, col):
    cur_x = x
    for ch in s:
        draw_digit(c, cur_x, y, ch, col)
        cur_x += 4

def create_fruit_chart():
    bg = "#11141c"
    card_bg = "#181d28"
    card_border = "#2a3346"
    card_bevel = "#3a4660"
    axis_color = "#4c5c7d"
    grid_major = "#273248"
    grid_minor = "#1c2434"
    num_color = "#8294b0"

    c = new_canvas(128, 64, background=bg)

    # Outer frame / card
    c.rect(1, 1, 126, 62, card_border, fill=False)
    c.rect(2, 2, 124, 60, card_bg, fill=True)

    # Chamfer corners for a sleek UI look
    c.set(1, 1, bg)
    c.set(1, 62, bg)
    c.set(126, 1, bg)
    c.set(126, 62, bg)
    c.set(2, 2, card_bevel)
    c.set(125, 2, card_bevel)
    c.set(2, 61, card_border)
    c.set(125, 61, card_border)

    x_axis = 19
    y_axis = 54
    x_start = 20
    scale = 6

    # Draw grid lines first (behind bars)
    for val in range(16):
        gx = x_start + val * scale
        if val in (0, 5, 10, 15):
            c.line(gx, 4, gx, y_axis, grid_major)
            # Major tick mark below axis (3 px)
            c.line(gx, y_axis, gx, y_axis + 2, axis_color)
        elif val in (2, 4, 6, 8, 12, 14):
            c.line(gx, 4, gx, y_axis, grid_minor)
            # Medium tick mark (2 px)
            c.line(gx, y_axis, gx, y_axis + 1, axis_color)
        else:
            # Minor tick mark (1 px)
            c.set(gx, y_axis + 1, grid_major)

    # Axis lines
    c.line(x_axis, 4, x_axis, y_axis, axis_color)
    c.line(x_axis, y_axis, x_start + 15 * scale + 2, y_axis, axis_color)

    # Bottom axis scale numbers: 0, 5, 10, 15
    draw_num(c, 19, 57, "0", num_color)
    draw_num(c, 49, 57, "5", num_color)
    draw_num(c, 77, 57, "10", num_color)
    draw_num(c, 107, 57, "15", num_color)

    # Fruit data: (name, value, base_color, highlight_color, shadow_color)
    fruits = [
        ("apple",  10, "#e02222", "#ff6b6b", "#8f1111"),
        ("banana",  5, "#f5c010", "#ffe55c", "#a67300"),
        ("orange",  7, "#ff7700", "#ffa633", "#b34400"),
        ("lemon",  14, "#e8e517", "#ffff7a", "#969400"),
        ("grape",   2, "#8a2be2", "#c471ed", "#4a148c"),
    ]

    row_y = [5, 15, 25, 35, 45]

    for idx, (name, val, col_base, col_hi, col_sh) in enumerate(fruits):
        by = row_y[idx]
        bar_len = val * scale
        bx0 = x_start
        bx1 = bx0 + bar_len

        # Bar height = 5 px: by+1 to by+5
        c.rect(bx0, by + 1, bar_len, 1, col_hi)
        c.rect(bx0, by + 2, bar_len, 3, col_base)
        c.rect(bx0, by + 5, bar_len, 1, col_sh)
        c.line(bx1 - 1, by + 1, bx1 - 1, by + 5, col_sh)
        c.set(bx1 - 1, by + 1, col_hi)

        # Right-aligned value indicators in matching color
        val_str = str(val)
        vx = 117 if len(val_str) == 2 else 121
        draw_num(c, vx, by + 1, val_str, col_hi)

    # Draw the mini fruit icons beside each bar
    draw_apple(c, 5, 3)
    draw_banana(c, 5, 13)
    draw_orange(c, 5, 23)
    draw_lemon(c, 5, 33)
    draw_grape(c, 5, 43)

    return c

c = create_fruit_chart()
finish(c)
view(c)
