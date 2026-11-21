from pixelbench_api import new_canvas, view, finish

# Muted, slightly cool stone palette: eight visible colours.
result = new_canvas(16, 16, background="#7b7f7e", name="minecraft_stone")

light = "#a4a7a3"
highlight = "#b8bab5"
mid_light = "#8d918f"
mid_dark = "#6c706f"
shadow = "#5b605f"
deep = "#454a49"
cool = "#737a7a"

# Broad blocky mineral patches.
result.rect(2, 1, 4, 2, mid_light)
result.set(3, 0, mid_light)
result.set(5, 3, mid_light)
result.rect(11, 0, 3, 2, mid_dark)
result.set(10, 1, mid_dark)
result.set(14, 2, mid_dark)

result.rect(0, 4, 3, 3, mid_dark)
result.set(3, 5, mid_dark)
result.set(15, 4, mid_dark)  # wraps into the left-edge patch
result.set(15, 5, mid_dark)
result.set(1, 7, shadow)

result.rect(5, 5, 3, 2, light)
result.set(4, 6, light)
result.set(6, 4, light)
result.set(7, 7, mid_light)
result.set(5, 7, highlight)

result.rect(11, 4, 4, 3, cool)
result.set(10, 5, cool)
result.set(12, 7, cool)
result.set(14, 7, mid_dark)

result.rect(1, 10, 4, 2, cool)
result.set(0, 11, cool)
result.set(3, 9, cool)
result.set(5, 10, mid_dark)
result.set(2, 12, mid_dark)

result.rect(8, 10, 3, 3, mid_light)
result.set(7, 11, mid_light)
result.set(9, 9, light)
result.set(10, 13, light)
result.set(11, 11, mid_light)

result.rect(13, 10, 3, 3, shadow)
result.set(12, 11, shadow)
result.set(14, 9, shadow)
result.set(0, 10, shadow)  # opposite-edge continuation

# Bottom/top wrapping mineral flecks.
result.rect(4, 14, 3, 2, mid_dark)
result.set(3, 15, mid_dark)
result.set(6, 0, mid_dark)
result.set(4, 0, mid_dark)
result.rect(11, 14, 3, 2, cool)
result.set(12, 13, cool)
result.set(11, 0, cool)
result.set(13, 0, cool)

# Small chips and highlights break up the larger patches.
for x, y in [(1, 1), (8, 2), (13, 3), (3, 7), (1, 8), (6, 9), (2, 14), (15, 14)]:
    result.set(x, y, light)
for x, y in [(0, 2), (7, 1), (15, 8), (4, 12), (7, 14), (14, 13)]:
    result.set(x, y, shadow)
result.set(2, 1, highlight)
result.set(6, 5, highlight)
result.set(1, 14, mid_light)

# Central stepped fissure with a short fork and a subtle shadow lip.
for x, y in [(9, 3), (9, 4), (8, 4), (8, 5), (8, 6), (9, 7), (9, 8),
             (10, 8), (10, 9), (11, 9), (11, 10)]:
    result.set(x, y, deep)
for x, y in [(8, 7), (7, 8), (6, 8), (6, 9)]:
    result.set(x, y, deep)
for x, y in [(10, 4), (9, 5), (9, 6), (10, 7), (11, 8), (12, 9), (12, 10)]:
    result.set(x, y, shadow)

view(result, scale=24, margin=0)
finish(result)
