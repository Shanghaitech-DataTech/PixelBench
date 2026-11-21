import math
from pixelbench_api import new_canvas, finish

OUTLINE = "#1b1f24"


def build_sword():
    c = new_canvas(32, 32)
    steel = "#c9d4df"
    steel_dark = "#9fadbc"
    steel_hi = "#eef3f8"
    gold = "#e0a82e"
    gold_dark = "#b8860b"
    gold_hi = "#f5cf6e"
    grip = "#7a4a24"
    # blade (diagonal, tip upper right)
    c.line(22, 5, 6, 21, steel_hi)
    c.line(23, 6, 7, 22, steel)
    c.line(25, 8, 9, 24, steel_dark)
    # guard
    c.rect(4, 24, 13, 1, gold_hi)
    c.rect(4, 25, 13, 1, gold)
    c.rect(4, 26, 12, 1, gold_dark)
    # grip
    c.rect(7, 27, 5, 3, grip)
    # pommel
    c.circle(9, 30, 1, gold)
    c.outline(OUTLINE)
    return c


def build_bow():
    c = new_canvas(32, 32)
    wood = "#8b5a2b"
    wood_dark = "#6b4421"
    wood_hi = "#a9763d"
    steel = "#c9d4df"
    shaft = "#a9723a"
    fletch = "#c0392b"
    string = "#ddd6c6"
    n = 46
    for i in range(n):
        a = -1.55 + 3.1 * i / (n - 1)
        x = round(15 + 10 * math.cos(a))
        y = round(16 + 10 * math.sin(a))
        c.circle(x, y, 2, wood)
    # grip on the belly
    c.rect(21, 14, 5, 4, wood_dark)
    # string
    c.line(12, 5, 12, 27, string)
    # arrow (horizontal, pointing right)
    c.line(4, 16, 23, 16, shaft)
    c.set(24, 15, steel)
    c.set(24, 16, steel)
    c.set(24, 17, steel)
    c.set(25, 16, steel)
    c.set(26, 16, steel)
    c.set(4, 15, fletch)
    c.set(5, 15, fletch)
    c.set(6, 15, fletch)
    c.set(5, 16, fletch)
    c.set(4, 17, fletch)
    c.set(5, 17, fletch)
    c.outline(OUTLINE)
    return c


def build_shield():
    c = new_canvas(32, 32)
    red = "#c0392b"
    red_hi = "#d95c4e"
    steel = "#c9d4df"
    steel_dark = "#9fadbc"
    steel_hi = "#eef3f8"
    body = "M 8 7 Q 8 3 16 3 Q 24 3 24 7 L 24 13 L 16 28 L 8 13 Z"
    c.path(body, red)
    c.path("M 9 8 Q 9 5 16 5 Q 17 5 18 7 L 10 11 Z", red_hi)
    c.circle(16, 12, 3, steel_dark)
    c.circle(16, 12, 2, steel)
    c.set(15, 11, steel_hi)
    c.outline(OUTLINE)
    return c


def build_axe():
    c = new_canvas(32, 32)
    steel = "#c9d4df"
    steel_dark = "#9fadbc"
    steel_hi = "#eef3f8"
    wood = "#7a4a24"
    wood_dark = "#5c3719"
    head = "M 20 5 L 9 5 Q 3 8 3 13 Q 3 18 9 21 L 20 21 Z"
    c.rect(17, 4, 3, 26, wood)
    c.rect(17, 4, 2, 26, wood)
    c.rect(19, 4, 1, 26, wood_dark)
    c.path(head, steel)
    c.path("M 9 6 Q 4 9 4 13 L 9 13 Z", steel_hi)
    c.outline(OUTLINE)
    return c


result = new_canvas(64, 64)
sw = build_sword()
bw = build_bow()
sh = build_shield()
ax = build_axe()
result.blit(sw, 0, 0)
result.blit(bw, 32, 0)
result.blit(sh, 0, 32)
result.blit(ax, 32, 32)

print(sw.stats_text())
print(bw.stats_text())
print(sh.stats_text())
print(ax.stats_text())
print(sw.matrix_text())
print(bw.matrix_text())
print(sh.matrix_text())
print(ax.matrix_text())
print(result.stats_text())

finish(result)
