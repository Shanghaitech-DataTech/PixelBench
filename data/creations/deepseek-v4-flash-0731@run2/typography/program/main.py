from pixelbench_api import new_canvas, finish

W = H = 64
c = new_canvas(W, H, background="#141034", name="title")

# 5x7 pixel font (1 = filled)
F5 = {
    'A': ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    'D': ["11110", "10001", "10001", "10001", "10001", "10001", "11110"],
    'E': ["11111", "10000", "10000", "11110", "10000", "10000", "11111"],
    'I': ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    'L': ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    'N': ["10001", "11001", "10101", "10011", "10001", "10001", "10001"],
    'P': ["11110", "10001", "10001", "11110", "10000", "10000", "10000"],
    'Q': ["01110", "10001", "10001", "10001", "10010", "10101", "01001"],
    'R': ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    'S': ["01111", "10000", "10000", "01110", "00001", "00001", "11110"],
    'T': ["11111", "00100", "00100", "00100", "00100", "00100", "00100"],
    'U': ["10001", "10001", "10001", "10001", "10001", "10001", "01110"],
    'V': ["10001", "10001", "10001", "10001", "10001", "01010", "00100"],
    'X': ["10001", "10001", "01010", "00100", "01010", "10001", "10001"],
    ' ': ["00000", "00000", "00000", "00000", "00000", "00000", "00000"],
}


def draw_text(x, y, s, scale, color, outline=None, shadow=None, dx=2, dy=2, gap=None):
    if gap is None:
        gap = scale
    pitch = 5 * scale + gap
    for ch in s:
        rows = F5.get(ch, ["00000"] * 7)
        if shadow is not None:
            for r, row in enumerate(rows):
                for col, v in enumerate(row):
                    if v == '1':
                        for sy in range(scale):
                            for sx in range(scale):
                                c.set(x + col * scale + sx + dx, y + r * scale + sy + dy, shadow)
        if outline is not None:
            for r, row in enumerate(rows):
                for col, v in enumerate(row):
                    if v == '1':
                        for oy in range(-1, scale + 1):
                            for ox in range(-1, scale + 1):
                                if ox or oy:
                                    c.set(x + col * scale + ox, y + r * scale + oy, outline)
        for r, row in enumerate(rows):
            for col, v in enumerate(row):
                if v == '1':
                    for sy in range(scale):
                        for sx in range(scale):
                            c.set(x + col * scale + sx, y + r * scale + sy, color)
        x += pitch


def plus(cx, cy, color):
    for ax, ay in ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)):
        c.set(cx + ax, cy + ay, color)


def sparkle(cx, cy, arm, core):
    plus(cx, cy, arm)
    c.set(cx, cy, core)


# ---------------- composition ----------------
# double frame
c.rect(1, 1, 62, 62, "#ffd23f", fill=False)          # gold outer frame
c.rect(3, 3, 58, 58, "#6a4fae", fill=False)          # purple inner frame
# centre panel behind the title
c.rect(5, 8, 54, 33, "#231b4d")

# main title: two big stacked words, 1px letter gaps so both fit the panel
draw_text(5, 9, "PIXEL", 2, "#ffd94a", outline="#170d33", shadow="#07051c", gap=1)
draw_text(5, 26, "QUEST", 2, "#53d8ff", outline="#170d33", shadow="#07051c", gap=1)

# small subtitle
draw_text(5, 48, "ADVENTURE", 1, "#c9b0ff", outline="#170d33")

# corner accents
for cx, cy in ((6, 6), (57, 6), (6, 57), (57, 57)):
    plus(cx, cy, "#ffd23f")

# sparkles framing the subtitle
sparkle(9, 45, "#ffe36b", "#ffffff")
sparkle(54, 45, "#ffe36b", "#ffffff")
# small gem dots on the accent line row
c.line(9, 57, 23, 57, "#4f3f94")
c.line(40, 57, 54, 57, "#4f3f94")

print(c.stats_text())
finish(c)
