from pixelbench_api import new_canvas, finish

W, H = 64, 64
c = new_canvas(W, H)

outline = "#212529"
green = "#2ecc71"
amber = "#f5a623"
red = "#e74c3c"
bolt = "#ffd60a"

c.color(outline)
c.color(green)
c.color(amber)
c.color(red)
c.color(bolt)


def draw_battery(ix, frac, color, bolt_on=False):
    # positive terminal nub
    c.rect(ix + 4, 18, 6, 4, outline)
    # identical body outline (14x24)
    c.rect(ix, 22, 14, 24, outline, fill=False)
    # interior fill from the bottom (interior is 12 wide x 22 tall)
    rows = int(round(22 * frac))
    if rows > 0:
        y0 = 23 + (22 - rows)
        c.rect(ix + 1, y0, 12, rows, color)
    if bolt_on:
        # lightning bolt, 13 rows centred inside the body
        bolt_rows = [
            (4, 9), (3, 9), (3, 9), (2, 8), (2, 8),
            (1, 7), (1, 7), (1, 6), (2, 6), (2, 5),
            (3, 5), (3, 4), (4, 4),
        ]
        by = 27
        for k, (a, b) in enumerate(bolt_rows):
            c.rect(ix + 1 + a, by + k, b - a + 1, 1, bolt)


draw_battery(2, 1.00, green)      # 100%
draw_battery(18, 0.60, amber)     # 60%
draw_battery(34, 0.20, red)       # 20%
draw_battery(50, 0.42, green, bolt_on=True)  # charging

print(c.stats_text())
print(c.matrix_text(region=(2, 18, 63, 45)))
finish(c)
