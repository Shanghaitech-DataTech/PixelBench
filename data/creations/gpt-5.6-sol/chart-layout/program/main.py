# 128x64 pixel-art fruit bar chart
result = new_canvas(128, 64, background="#101827", name="fruit_chart")

# Palette
bg = "#101827"
panel = "#17243a"
panel_hi = "#1d2e49"
grid = "#2a3c57"
axis = "#8fa6bd"
white = "#f4f7e8"
muted = "#b9c9cf"
ink = "#6b2635"

# Framed plotting area and title strip
result.rect(3, 3, 122, 58, "#0a101c")
result.rect(4, 4, 120, 56, panel)
result.rect(4, 4, 120, 8, panel_hi)
result.set(6, 6, "#ef4d5f")
result.set(8, 6, "#ffd34e")
result.set(10, 6, "#8fd14f")
result.text(14, 4, "FRUIT COUNT", white, font="5x7")

# Plot grid: 0, 5, 10, 14 levels
for y in (17, 27, 39, 51):
    for x in range(8, 121, 2):
        result.set(x, y, grid)
result.line(8, 14, 8, 51, axis)
result.line(8, 51, 120, 51, axis)
# Tiny scale ticks
for y in (17, 27, 39, 51):
    result.line(7, y, 9, y, muted)

# Data bars: apple 10, banana 5, orange 7, lemon 14, grape 2
bars = [
    (14, 10, 25, "#e7444f", "#ff6970", "#a92d43"),
    (36, 5, 13, "#f2c230", "#ffe064", "#b88722"),
    (58, 7, 18, "#f07a2b", "#ffad42", "#b84b25"),
    (80, 14, 35, "#e5d64a", "#fff078", "#a99f32"),
    (102, 2, 5, "#8b57c8", "#b879ef", "#5d3594"),
]
for x, value, height, base, hi, shade in bars:
    top = 51 - height
    # Dark one-pixel cast shadow and chunky outlined bar
    result.rect(x + 2, top + 2, 12, height, "#0b1220")
    result.rect(x, top, 12, height, shade)
    result.rect(x + 1, top, 9, height - 1, base)
    result.line(x + 2, top + 1, x + 2, 49, hi)
    # bright cap
    result.line(x + 1, top, x + 9, top, hi)
    label = str(value)
    tx = x + (12 - (5 * len(label) + max(0, len(label) - 1))) // 2
    result.text(tx, max(13, top - 8), label, white, font="5x7")

# Category icons under baseline, centered beneath each bar.
def apple(cx, y):
    result.rect(cx - 3, y + 2, 7, 5, "#e7444f")
    result.rect(cx - 4, y + 3, 9, 3, "#e7444f")
    result.set(cx - 3, y + 6, "#a92d43")
    result.set(cx + 3, y + 6, "#a92d43")
    result.rect(cx, y, 1, 2, "#6f4828")
    result.rect(cx + 1, y, 3, 1, "#75bd42")
    result.set(cx - 3, y + 3, "#ff8b82")

def banana(cx, y):
    result.set(cx - 4, y + 1, "#8b6420")
    result.line(cx - 3, y + 2, cx, y + 5, "#ffd84a")
    result.line(cx, y + 5, cx + 4, y + 4, "#ffd84a")
    result.line(cx - 2, y + 2, cx + 1, y + 4, "#fff078")
    result.set(cx + 5, y + 3, "#8b6420")

def orange(cx, y):
    result.rect(cx - 3, y + 2, 7, 5, "#f07a2b")
    result.rect(cx - 4, y + 3, 9, 3, "#f07a2b")
    result.set(cx - 3, y + 2, "#ffad42")
    result.set(cx + 3, y + 6, "#b84b25")
    result.rect(cx, y, 1, 2, "#4e9d43")
    result.line(cx + 1, y, cx + 3, y, "#75bd42")

def lemon(cx, y):
    result.rect(cx - 3, y + 2, 7, 5, "#eadb43")
    result.rect(cx - 4, y + 3, 9, 3, "#eadb43")
    result.set(cx - 5, y + 4, "#fff078")
    result.set(cx + 5, y + 4, "#a99f32")
    result.line(cx - 2, y + 2, cx + 2, y + 2, "#fff078")

def grapes(cx, y):
    purple = "#8b57c8"
    light = "#b879ef"
    result.set(cx, y, "#75bd42")
    result.line(cx, y + 1, cx + 3, y, "#4e9d43")
    for dx, dy in [(-2,2),(1,2),(3,3),(-3,4),(0,4),(2,5),(-1,6)]:
        result.rect(cx + dx, y + dy, 2, 2, purple)
    result.set(cx - 2, y + 2, light)
    result.set(cx + 1, y + 2, light)

apple(19, 53)
banana(41, 53)
orange(63, 53)
lemon(85, 53)
grapes(107, 53)

# Corner accents keep the frame crisp.
for x, y in [(4,4),(123,4),(4,59),(123,59)]:
    result.set(x, y, "#415673")

view(result, scale=6, margin=0)
finish(result)
