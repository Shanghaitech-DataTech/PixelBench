from pixelbench_api import new_canvas, finish, view

W, H = 128, 64
c = new_canvas(W, H, background="#101725", name="fruit_chart")

# Palette
panel = "#172235"
panel_hi = "#1d2b42"
axis = "#71839b"
grid = "#2c3b50"
text = "#eaf2f8"
muted = "#9cafc1"
shadow = "#0a0f19"

# Framed chart panel and heading
c.rect(3, 2, 122, 60, panel)
c.rect(3, 2, 122, 1, panel_hi)
c.rect(3, 61, 122, 1, shadow)
c.text(8, 6, "FRUIT COUNT", text, font="5x7")
c.rect(82, 7, 35, 1, grid)
c.set(119, 7, muted)

# Plot grid: 14, 7 and baseline
for y in (21, 35):
    for x in range(11, 120, 3):
        c.set(x, y, grid)
c.line(10, 20, 10, 50, axis)
c.line(10, 50, 120, 50, axis)
c.set(9, 21, axis)
c.set(9, 35, axis)

# Bar definitions: x, value, main, light, dark
bars = [
    (18, 10, "#df3e4f", "#ff6673", "#9d2737"),
    (39, 5,  "#f1c735", "#ffe26a", "#b28a18"),
    (60, 7,  "#f28a2e", "#ffb04c", "#b95420"),
    (81, 14, "#f5dc4e", "#fff27a", "#baa52b"),
    (102, 2, "#8f5ac8", "#ba7ee8", "#61378d"),
]

for x, value, main, light, dark in bars:
    height = value * 2
    top = 49 - height
    # One-pixel dark offset and crisp three-tone bar.
    c.rect(x + 1, top + 1, 11, height, shadow)
    c.rect(x, top, 11, height, main)
    c.rect(x, top, 2, height, light)
    c.rect(x + 9, top, 2, height, dark)
    c.rect(x + 2, top, 7, 1, light)
    label = str(value)
    label_x = x + (2 if value >= 10 else 3)
    c.text(label_x, top - 8, label, text, font="5x7")

# Fruit sprites replace category names. Each is centered under its bar.
# Apple
c.set(22, 53, "#6e4625"); c.set(23, 52, "#6e4625")
c.set(24, 52, "#63b84f"); c.set(25, 52, "#63b84f")
c.rect(20, 54, 7, 6, "#dc3546")
c.set(19, 55, "#dc3546"); c.set(27, 55, "#a92335")
c.set(20, 60, None); c.set(26, 60, None)
c.set(21, 54, "#ff6975"); c.set(21, 55, "#ff6975")

# Banana
banana = "#f4cf39"; banana_hi = "#ffe56a"; banana_dark = "#b48918"
c.set(41, 54, banana_dark); c.set(42, 55, banana); c.set(43, 56, banana)
c.set(44, 57, banana); c.set(45, 57, banana); c.set(46, 57, banana)
c.set(47, 56, banana); c.set(48, 55, banana_dark)
c.set(43, 55, banana_hi); c.set(44, 56, banana_hi); c.set(45, 56, banana_hi)
c.set(46, 56, banana_hi); c.set(47, 55, banana_hi)
c.set(42, 56, banana_dark); c.set(43, 57, banana_dark); c.set(44, 58, banana_dark)
c.set(45, 58, banana_dark); c.set(46, 58, banana_dark); c.set(47, 57, banana_dark)

# Orange
c.set(64, 53, "#5bb24a"); c.set(65, 52, "#5bb24a"); c.set(66, 53, "#5bb24a")
c.rect(62, 54, 7, 7, "#ef8129")
c.set(61, 56, "#ef8129"); c.set(69, 56, "#b95520")
c.set(62, 54, None); c.set(68, 54, None); c.set(62, 60, None); c.set(68, 60, None)
c.set(63, 55, "#ffb24b"); c.set(63, 56, "#ffb24b")

# Lemon
lemon = "#f5df48"; lemon_hi = "#fff47b"; lemon_dark = "#b9a52d"
c.set(83, 57, lemon_dark); c.set(84, 55, lemon); c.set(85, 54, lemon)
c.set(86, 54, lemon); c.set(87, 54, lemon); c.set(88, 55, lemon)
c.set(89, 56, lemon); c.set(90, 57, lemon_dark); c.set(89, 58, lemon)
c.set(88, 59, lemon); c.set(87, 60, lemon); c.set(86, 60, lemon)
c.set(85, 59, lemon_dark); c.set(84, 58, lemon_dark)
c.set(85, 55, lemon_hi); c.set(86, 55, lemon_hi); c.set(87, 55, lemon_hi)
c.set(88, 56, lemon_hi)

# Grape cluster with leaf and stem
c.set(106, 52, "#6d4328"); c.set(106, 53, "#6d4328")
c.set(107, 52, "#59ad4b"); c.set(108, 52, "#59ad4b"); c.set(108, 53, "#367f3e")
grape = "#8e57c6"; grape_hi = "#bd80e7"; grape_dark = "#603689"
for gx, gy in [(104,54),(106,54),(108,54),(103,56),(105,56),(107,56),(109,56),(104,58),(106,58),(108,58),(105,60),(107,60)]:
    c.rect(gx, gy, 2, 2, grape)
    c.set(gx, gy, grape_hi)
    c.set(gx+1, gy+1, grape_dark)

# Tiny corner fasteners for a finished dashboard-like frame.
for x, y in [(6,5),(121,5),(6,58),(121,58)]:
    c.set(x, y, "#34465c")

view(c, scale=6, margin=0)
finish(c)
