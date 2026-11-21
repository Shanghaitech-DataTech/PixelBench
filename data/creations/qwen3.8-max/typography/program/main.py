# PIXEL QUEST - 64x64 pixel art game title screen
W = H = 64
c = new_canvas(W, H, name="pixel_quest")

# ---------------------------------------------------------------- custom font
FONT = {
    'P': ("11110", "10001", "10001", "11110", "10000", "10000", "10000"),
    'I': ("11111", "00100", "00100", "00100", "00100", "00100", "11111"),
    'X': ("10001", "10001", "01010", "00100", "01010", "10001", "10001"),
    'E': ("11111", "10000", "10000", "11110", "10000", "10000", "11111"),
    'L': ("10000", "10000", "10000", "10000", "10000", "10000", "11111"),
    'Q': ("01110", "10001", "10001", "10001", "10101", "10010", "01101"),
    'U': ("10001", "10001", "10001", "10001", "10001", "10001", "01110"),
    'S': ("01110", "10001", "10000", "01110", "00001", "10001", "01110"),
    'T': ("11111", "00100", "00100", "00100", "00100", "00100", "00100"),
    'R': ("11110", "10001", "10001", "11110", "10100", "10010", "10001"),
    'A': ("01110", "10001", "10001", "11111", "10001", "10001", "10001"),
    ' ': ("00000", "00000", "00000", "00000", "00000", "00000", "00000"),
}


def word_w(s, scale, gap):
    return len(s) * 5 * scale + (len(s) - 1) * gap * scale


def render_word(t, s, x, y, scale, gap, colors):
    """colors: single colour or a 7-entry list (one per glyph row)."""
    cx = x
    for ch in s:
        for ry, row in enumerate(FONT[ch]):
            col = colors[ry] if isinstance(colors, (list, tuple)) else colors
            for rx, b in enumerate(row):
                if b == '1':
                    t.rect(cx + rx * scale, y + ry * scale, scale, scale, col)
        cx += (5 + gap) * scale


def dilated(word, x, y, scale, gap, color, r=2):
    tmp = new_canvas(W, H)
    render_word(tmp, word, x, y, scale, gap, color)
    out = new_canvas(W, H)
    for dx in range(-r, r + 1):
        for dy in range(-r, r + 1):
            out.blit(tmp, dx, dy)
    return out


# ------------------------------------------------------------------ sky / bg
SKY = [
    (0, 9, '#140E2C'),
    (10, 19, '#1B1339'),
    (20, 29, '#231846'),
    (30, 39, '#2D1C55'),
    (40, 47, '#3A2264'),
    (48, 52, '#4C2B72'),
    (53, 55, '#66357A'),
    (56, 56, '#8A4A76'),
    (57, 63, '#7A4478'),
]
for y0, y1, col in SKY:
    c.rect(0, y0, W, y1 - y0 + 1, col)

# ------------------------------------------------------------------- stars
STARS = [
    (15, 2, '#C9BEF0'), (17, 5, '#6E62A8'),
    (22, 1, '#FFFFFF'), (27, 4, '#9A8CD0'), (33, 0, '#C9BEF0'), (36, 3, '#F2ECFF'),
    (41, 5, '#7A6CB4'), (45, 1, '#C9BEF0'), (49, 4, '#FFFFFF'), (58, 5, '#8C7FC8'),
    (62, 1, '#C9BEF0'), (63, 4, '#6E62A8'), (19, 0, '#6E62A8'), (25, 5, '#8C7FC8'),
    (39, 0, '#6E62A8'), (56, 1, '#9A8CD0'), (60, 0, '#F2ECFF'), (30, 2, '#7A6CB4'),
    (1, 55, '#6E62A8'), (62, 52, '#8C7FC8'), (2, 51, '#7A6CB4'), (61, 55, '#6E62A8'),
    (0, 49, '#8C7FC8'), (63, 49, '#6E62A8'),
    (9, 26, '#5E5296'), (31, 27, '#6E62A8'), (52, 26, '#5E5296'),
]
for x, y, col in STARS:
    c.set(x, y, col)

# crescent moon
c.circle(10, 3, 2, '#FFF6D5')
c.circle(12, 3, 2, '#140E2C')
c.set(9, 4, '#EFE3BC')

# small 4-point sparkle in the sky
c.path("M52 0 L53 2 L55 3 L53 4 L52 6 L51 4 L49 3 L51 2 Z", '#F2ECFF')
c.set(52, 3, '#FFFFFF')

# ------------------------------------------------------------------- ground
TOP = [(0, 59), (7, 58), (14, 60), (22, 58), (30, 59), (38, 57),
       (46, 59), (54, 58), (60, 60), (63, 59)]
c.poly(TOP + [(63, 63), (0, 63)], '#1A1030')
for i in range(len(TOP) - 1):
    c.line(TOP[i][0], TOP[i][1], TOP[i + 1][0], TOP[i + 1][1], '#3A2464')
for x, y, col in [(4, 61, '#241640'), (18, 62, '#241640'), (33, 61, '#2A1A48'),
                  (49, 62, '#241640'), (58, 61, '#2A1A48'), (26, 60, '#241640')]:
    c.set(x, y, col)

# ------------------------------------------------------------------- title
ICE = ['#FFFFFF', '#E8F7FF', '#B4E4FF', '#7CCBFF', '#4FA9F2', '#2F7FD1', '#1E5CA8']
GOLD = ['#FFF8D2', '#FFE684', '#FFCB3D', '#F7A325', '#E2781C', '#BE521A', '#963C1A']


def draw_title(word, x, y, grad, outline_col, extrude_col):
    sil_e = dilated(word, x, y, 2, 1, extrude_col)
    sil_o = dilated(word, x, y, 2, 1, outline_col)
    c.blit(sil_e, 2, 2)
    c.blit(sil_o, 0, 0)
    render_word(c, word, x, y, 2, 1, grad)


TX = (W - word_w('PIXEL', 2, 1)) // 2 - 1     # 2 -> leaves room for extrude
draw_title('PIXEL', TX, 8, ICE, '#0A1A2E', '#14395E')
draw_title('QUEST', TX, 30, GOLD, '#2A1208', '#6B2A11')

# (left sky kept calm: the crescent moon is its only feature)

# ---------------------------------------------------------------- subtitle
SUB = 'PRESS START'
sx = (W - word_w(SUB, 1, 0)) // 2
render_word(c, SUB, sx + 1, 50, 1, 0, '#150E28')
render_word(c, SUB, sx, 49, 1, 0, '#DCD2F7')

# small gold diamonds flanking the subtitle
for dx in (sx - 3, sx + word_w(SUB, 1, 0) + 2):
    c.set(dx, 50, '#FFCB3D')
    c.set(dx - 1, 51, '#F7A325')
    c.set(dx + 1, 51, '#F7A325')
    c.set(dx, 52, '#BE521A')
    c.set(dx, 51, '#FFE684')

print("TX", TX, "sx", sx, "wordw", word_w('PIXEL', 2, 1), word_w(SUB, 1, 0))
print(c.stats_text())
view(c)
save("pixel_quest", c, indexed=True)
finish(c)
