from pixelbench_api import new_canvas, finish, view

# Transparent sprite sheet; restrained palette keeps all four icons cohesive.
result = new_canvas(64, 64, background=None, name="battery-status-set")

INK = "#111827"
DEEP = "#1f2937"
STEEL = "#64748b"
RIM = "#cbd5e1"
INNER = "#0b1220"
GREEN_D = "#15803d"
GREEN = "#22c55e"
GREEN_HI = "#86efac"
AMBER_D = "#b45309"
AMBER = "#f59e0b"
AMBER_HI = "#fde68a"
RED_D = "#b91c1c"
RED = "#ef4444"
RED_HI = "#fca5a5"
CYAN_D = "#0891b2"
CYAN = "#22d3ee"
CYAN_HI = "#a5f3fc"
BOLT = "#fff7ae"


def battery_shell(x):
    # Terminal and beveled, identical 12x26 casing.
    result.rect(x + 3, 16, 6, 5, INK)
    result.rect(x + 4, 17, 4, 3, RIM)
    result.rect(x + 1, 20, 10, 1, INK)
    result.rect(x, 21, 12, 23, INK)
    result.rect(x + 1, 20, 10, 24, INK)
    result.set(x, 20, None)
    result.set(x + 11, 20, None)
    result.set(x, 43, None)
    result.set(x + 11, 43, None)
    result.rect(x + 2, 22, 8, 20, STEEL)
    result.rect(x + 3, 23, 6, 18, INNER)
    # Metallic glint and grounded bottom edge.
    result.set(x + 2, 22, RIM)
    result.set(x + 3, 22, RIM)
    result.rect(x + 2, 42, 8, 1, DEEP)
    result.rect(x + 10, 23, 1, 19, DEEP)


def fill_level(x, height, dark, main, highlight):
    top = 41 - height
    result.rect(x + 3, top, 6, height, main)
    result.rect(x + 3, top, 1, height, highlight)
    result.rect(x + 8, top, 1, height, dark)
    result.rect(x + 4, top, 4, 1, highlight)


xs = [2, 17, 32, 47]
for px in xs:
    battery_shell(px)

# 100%, 60%, 20% and an energized charging state.
fill_level(xs[0], 18, GREEN_D, GREEN, GREEN_HI)
fill_level(xs[1], 11, AMBER_D, AMBER, AMBER_HI)
fill_level(xs[2], 4, RED_D, RED, RED_HI)
fill_level(xs[3], 12, CYAN_D, CYAN, CYAN_HI)

# White separators make the three numeric levels countable at sprite scale.
# 100: four bars; 60: three bars; 20: one bar.
for dx in (0, 3, 6, 9):
    result.rect(2 + dx, 50, 2, 2, GREEN)
for dx in (0, 3, 6):
    result.rect(18 + dx, 50, 2, 2, AMBER)
result.rect(35, 50, 2, 2, RED)

# A high-contrast lightning glyph crosses both empty and filled portions.
result.poly([(53, 25), (58, 25), (56, 30), (59, 30),
             (53, 39), (54, 33), (51, 33)], INK)
result.poly([(54, 26), (57, 26), (55, 31), (58, 31),
             (54, 37), (55, 32), (52, 32)], BOLT)
# Small live-current sparks below the charger.
result.set(52, 49, CYAN_HI)
result.rect(54, 48, 1, 3, CYAN)
result.set(56, 49, CYAN_HI)

view(result, scale=8, margin=0)
finish(result)
