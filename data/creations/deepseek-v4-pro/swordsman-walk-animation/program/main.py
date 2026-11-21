from pixelbench_api import *

# Palette: 16-bit RPG style, limited colours
PAL = {
    '.': None,            # transparent
    'O': (24, 18, 16),    # outline
    'H': (198, 58, 38),   # red hair
    'h': (150, 40, 30),   # hair shade
    'S': (232, 184, 136), # skin
    'E': (30, 30, 30),    # eye
    'T': (58, 130, 70),   # tunic green
    'K': (90, 60, 34),    # belt / leather
    'C': (32, 48, 96),    # cape dark blue
    'L': (70, 56, 44),    # pants
    'B': (92, 62, 34),    # boots
    'W': (216, 224, 232), # blade light
    'w': (168, 180, 196), # blade shade
    'G': (216, 164, 40),  # gold guard
    'b': (110, 70, 40),   # hilt brown
}

W, H = 32, 32

def new_rows():
    return [['.'] * W for _ in range(H)]

def put(rows, y, x, s):
    for i, ch in enumerate(s):
        xx = x + i
        if 0 <= xx < W and 0 <= y < H:
            rows[y][xx] = ch

def draw_rows(c, ox, oy, rows):
    for y in range(H):
        for x in range(W):
            ch = rows[y][x]
            if ch == '.':
                continue
            c.set(ox + x, oy + y, PAL[ch])
    return c

def outline_expand(rows):
    """Add a 1px dark outline around all opaque shapes (8-neighbour expansion)."""
    out = [row[:] for row in rows]
    for y in range(H):
        for x in range(W):
            if rows[y][x] != '.':
                continue
            found = False
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < H and 0 <= nx < W and rows[ny][nx] != '.':
                        found = True
                        break
                if found:
                    break
            if found:
                out[y][x] = 'O'
    return out

def upper_body(rows, dy=0):
    """Cape, head, torso, sword and sword arm."""
    # cape behind body
    put(rows, 9 + dy, 7, "CCCCC")
    put(rows, 10 + dy, 7, "CCCCC")
    put(rows, 11 + dy, 7, "CCCCC")
    put(rows, 12 + dy, 7, "CCCCC")
    put(rows, 13 + dy, 7, "CCCCC")
    put(rows, 14 + dy, 7, "CCCC")
    put(rows, 15 + dy, 6, "CCCC")
    put(rows, 16 + dy, 6, "CCCC")
    put(rows, 17 + dy, 5, "CCC")
    put(rows, 18 + dy, 5, "CCC")
    put(rows, 19 + dy, 4, "CC")
    put(rows, 20 + dy, 4, "CC")

    # head / hair (facing right, face at front/right)
    put(rows, 1 + dy, 13, "HHHHH")
    put(rows, 2 + dy, 12, "HHHHHHH")
    put(rows, 3 + dy, 11, "HHHHHHHHH")
    put(rows, 4 + dy, 11, "HHHHHHHHS")
    put(rows, 5 + dy, 11, "HHHHHHHES")
    put(rows, 6 + dy, 11, "HHHHHHSSS")
    put(rows, 7 + dy, 11, "HHHHHSSSS")
    put(rows, 8 + dy, 11, "HHHHSSSS")
    put(rows, 5 + dy, 10, "h")
    put(rows, 6 + dy, 10, "h")
    put(rows, 7 + dy, 10, "h")

    # neck
    put(rows, 9 + dy, 14, "SSS")

    # torso tunic
    for yy in range(10, 16):
        put(rows, yy + dy, 12, "TTTTTTTT")
    # belt + gold buckle
    put(rows, 16 + dy, 12, "KKKKKKKK")
    put(rows, 16 + dy, 15, "G")

    # sword (long blade, upright, tip at top)
    put(rows, 2 + dy, 22, "W")
    for yy in range(3, 13):
        put(rows, yy + dy, 21, "wW")
    put(rows, 13 + dy, 20, "GGGG")
    put(rows, 14 + dy, 21, "bb")
    put(rows, 15 + dy, 21, "bb")
    put(rows, 16 + dy, 21, "G")

    # sword arm (front)
    put(rows, 11 + dy, 19, "T")
    put(rows, 12 + dy, 19, "T")
    put(rows, 13 + dy, 20, "T")
    put(rows, 14 + dy, 20, "S")

def leg_back_frame1(rows, dy):
    """Back (left) leg, planted behind."""
    put(rows, 17 + dy, 12, "LL")
    put(rows, 18 + dy, 11, "LL")
    put(rows, 19 + dy, 10, "LL")
    put(rows, 20 + dy, 10, "LL")
    put(rows, 21 + dy, 9, "LL")
    put(rows, 22 + dy, 9, "LL")
    put(rows, 23 + dy, 9, "LL")
    put(rows, 24 + dy, 9, "LL")
    put(rows, 25 + dy, 9, "BB")
    put(rows, 26 + dy, 8, "BBB")

def leg_front_frame1(rows, dy):
    """Front (right) leg, planted forward."""
    put(rows, 17 + dy, 15, "LL")
    put(rows, 18 + dy, 16, "LL")
    put(rows, 19 + dy, 17, "LL")
    put(rows, 20 + dy, 18, "LL")
    put(rows, 21 + dy, 18, "LL")
    put(rows, 22 + dy, 19, "LL")
    put(rows, 23 + dy, 19, "LL")
    put(rows, 24 + dy, 19, "LL")
    put(rows, 25 + dy, 19, "BB")
    put(rows, 26 + dy, 18, "BBB")

def leg_back_frame2(rows, dy):
    """Back (left) leg lifted, knee bent (passing pose)."""
    put(rows, 16 + dy, 12, "LL")
    put(rows, 17 + dy, 12, "LL")
    put(rows, 18 + dy, 11, "LL")
    put(rows, 19 + dy, 11, "LL")
    put(rows, 20 + dy, 12, "LL")
    put(rows, 21 + dy, 12, "BB")
    put(rows, 22 + dy, 12, "BB")

def leg_front_frame2(rows, dy):
    """Front (right) support leg, straight down to the ground."""
    put(rows, 16 + dy, 15, "LL")
    put(rows, 17 + dy, 15, "LL")
    put(rows, 18 + dy, 15, "LL")
    put(rows, 19 + dy, 15, "LL")
    put(rows, 20 + dy, 15, "LL")
    put(rows, 21 + dy, 15, "LL")
    put(rows, 22 + dy, 15, "LL")
    put(rows, 23 + dy, 15, "LL")
    put(rows, 24 + dy, 15, "LL")
    put(rows, 25 + dy, 15, "LL")
    put(rows, 26 + dy, 15, "BB")
    put(rows, 27 + dy, 14, "BBB")

def build_frame(pose):
    rows = new_rows()
    if pose == 1:
        dy = 1   # head top at row 2, feet on ground at row 27
        leg_back_frame1(rows, dy)
        upper_body(rows, dy)
        leg_front_frame1(rows, dy)
    else:
        dy = 0   # head top at row 1 (1px bob), feet still on ground at row 27
        leg_back_frame2(rows, dy)
        upper_body(rows, dy)
        leg_front_frame2(rows, dy)
    return outline_expand(rows)

c = new_canvas(64, 32, background=None, name="swordsman-walk")

rows1 = build_frame(1)
rows2 = build_frame(2)
draw_rows(c, 0, 0, rows1)
draw_rows(c, 32, 0, rows2)

print(c.stats_text())

finish(c)
