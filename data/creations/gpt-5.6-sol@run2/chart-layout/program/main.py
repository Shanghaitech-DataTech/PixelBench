from pixelbench_api import *

# 128x64 pixel-art fruit bar chart
result = new_canvas(128, 64, background="#10182b", name="fruit_chart")

# Palette
bg = "#10182b"
panel = "#17233c"
panel2 = "#1d2c49"
grid = "#33415f"
axis = "#8fa6bd"
ink = "#dce8df"
shadow = "#090e1a"

# Chart panel and pixel frame
result.rect(1, 1, 126, 62, "#0a1020")
result.rect(2, 2, 124, 60, panel)
result.rect(4, 10, 120, 42, panel2)
result.line(4, 9, 123, 9, "#40506d")
result.line(123, 10, 123, 51, "#0b1324")

# Header: tiny fruit accent and title
result.set(6, 4, "#63a84f").set(7, 3, "#79c45d")
result.set(7, 5, "#e94b49").set(8, 5, "#ff6a58")
result.text(11, 2, "FRUIT DATA", ink, font="5x7")
result.text(105, 2, "0-14", "#8fa6bd", font="5x7")

# Plot guides: values 0, 5, 10, 14 on a 2px/unit scale, baseline y=48
for y in (38, 28, 20):
    for x in range(18, 121, 4):
        result.rect(x, y, 2, 1, grid)
result.line(17, 20, 17, 48, axis)
result.line(17, 48, 121, 48, axis)
result.set(16, 20, axis).set(16, 28, axis).set(16, 38, axis)
result.text(3, 18, "14", "#7f96af", font="5x7")
result.text(8, 45, "0", "#7f96af", font="5x7")

# Bars: (x, value, main, light, dark)
bars = [
    (24, 10, "#e84d4f", "#ff7470", "#a52e3d"),
    (44, 5,  "#f3c94c", "#ffe47a", "#b7862d"),
    (64, 7,  "#f18435", "#ffad4f", "#b94d29"),
    (84, 14, "#f5e45f", "#fff58a", "#b8a63a"),
    (104, 2, "#8b59bd", "#bb7be0", "#573581"),
]
for x, value, main, light, dark in bars:
    h = value * 2
    y = 48 - h
    # one-pixel cast shadow and outlined body
    result.rect(x + 2, y + 2, 10, h, shadow)
    result.rect(x, y, 10, h, dark)
    if h > 2:
        result.rect(x + 1, y + 1, 8, h - 1, main)
        result.rect(x + 1, y + 1, 2, h - 2, light)
    # value above each bar
    label = str(value)
    tx = x + (10 - (len(label) * 6 - 1)) // 2
    result.text(tx, y - 8, label, ink, font="5x7")

# Apple icon under bar 1
result.set(28, 52, "#72422b").set(29, 51, "#72422b")
result.set(30, 52, "#62ad4d").set(31, 52, "#62ad4d").set(30, 53, "#62ad4d")
result.rect(25, 54, 8, 6, "#a52e3d")
result.rect(24, 55, 10, 4, "#e84d4f")
result.rect(26, 54, 3, 2, "#ff7470")
result.set(26, 60, "#a52e3d").set(31, 60, "#a52e3d")

# Banana icon under bar 2
banana = "#f3c94c"
banana_hi = "#ffe47a"
banana_dark = "#9f7429"
result.set(45, 53, banana_dark).set(46, 53, banana)
result.set(46, 54, banana).set(47, 55, banana_hi)
result.set(48, 56, banana_hi).set(49, 57, banana_hi)
result.rect(50, 58, 5, 2, banana)
result.set(54, 57, banana).set(55, 56, banana_dark)
result.set(47, 56, banana_dark).set(48, 57, banana_dark).set(49, 58, banana_dark)

# Orange icon under bar 3
result.set(68, 52, "#5c9f48").set(69, 52, "#70bd56").set(67, 53, "#6a9b3f")
result.rect(65, 54, 8, 6, "#c95727")
result.rect(64, 55, 10, 4, "#f18435")
result.rect(66, 54, 3, 2, "#ffad4f")
result.set(66, 60, "#c95727").set(71, 60, "#c95727")

# Lemon icon under bar 4 (pointed oval)
result.set(84, 56, "#b8a63a").set(94, 56, "#b8a63a")
result.rect(85, 54, 8, 6, "#d3bf3f")
result.rect(83, 56, 12, 2, "#f5e45f")
result.rect(86, 54, 5, 2, "#fff58a")
result.rect(86, 58, 6, 2, "#f5e45f")

# Grape cluster under bar 5
result.set(108, 52, "#6aae4e").set(109, 51, "#6aae4e").set(110, 52, "#477f3c")
for x, y, c in [
    (106,54,"#bb7be0"),(109,54,"#8b59bd"),(112,54,"#bb7be0"),
    (107,56,"#8b59bd"),(110,56,"#bb7be0"),(113,56,"#75459f"),
    (108,58,"#75459f"),(111,58,"#8b59bd"),(109,60,"#573581"),(112,60,"#75459f")]:
    result.rect(x, y, 3, 3, c)

# Baseline end caps and corner glints
result.set(16, 48, "#c3d2d6").set(121, 48, "#c3d2d6")
result.set(2, 2, "#53627a").set(125, 61, "#070b15")

view(result, scale=6, margin=0)
finish(result)
