from pixelbench_api import new_canvas, finish, view

# 64x64 battery status sprite sheet: four equal vertical batteries in one row.
c = new_canvas(64, 64, background="#0c121c", name="battery-status-set")

# Palette
bg2 = "#111b28"
panel = "#162334"
panel_hi = "#1d2d40"
divider = "#26384b"
shadow = "#06090e"
outline_dark = "#526579"
outline = "#b9c8d5"
outline_hi = "#e7f1f5"
empty = "#253547"
green_dark = "#168b54"
green = "#35d07f"
green_hi = "#8df0b7"
yellow_dark = "#a87817"
yellow = "#f3bf3f"
yellow_hi = "#ffe486"
red_dark = "#9e3540"
red = "#ef5563"
red_hi = "#ff9a9f"
cyan_dark = "#167d9f"
cyan = "#28c7e8"
cyan_hi = "#9af2ff"
white = "#f8ffff"

# Four compact status bays, with subtle top/bottom rails.
for x in (0, 16, 32, 48):
    c.rect(x + 1, 6, 14, 51, bg2)
    c.rect(x + 2, 8, 12, 47, panel)
    c.rect(x + 3, 9, 10, 1, panel_hi)
    c.set(x + 2, 54, "#0a1018")
for x in (15, 31, 47):
    c.rect(x, 10, 1, 44, divider)
    c.set(x, 9, panel_hi)
    c.set(x, 54, shadow)

xs = [2, 18, 34, 50]

# Identical battery housings. Outer size is 12x32 including the terminal.
for x in xs:
    # Drop shadow
    c.rect(x + 2, 17, 11, 31, shadow)
    c.rect(x + 5, 13, 5, 4, shadow)
    # Positive terminal
    c.rect(x + 4, 12, 5, 2, outline_dark)
    c.rect(x + 3, 14, 7, 3, outline_dark)
    c.rect(x + 4, 13, 5, 3, outline)
    c.rect(x + 5, 13, 3, 1, outline_hi)
    # Main shell: dark outer edge, pale inner edge, recessed cavity
    c.rect(x, 16, 12, 32, outline_dark)
    c.rect(x + 1, 17, 10, 30, outline)
    c.rect(x + 2, 18, 8, 28, outline_hi)
    c.rect(x + 3, 19, 6, 26, empty)
    # Tiny shell corner cuts for crisp pixel construction
    c.set(x, 16, panel)
    c.set(x + 11, 16, panel)
    c.set(x, 47, panel)
    c.set(x + 11, 47, panel)
    # Cavity guide ticks
    c.set(x + 3, 25, "#33475b")
    c.set(x + 8, 25, "#33475b")
    c.set(x + 3, 32, "#33475b")
    c.set(x + 8, 32, "#33475b")
    c.set(x + 3, 39, "#33475b")
    c.set(x + 8, 39, "#33475b")

# 100%: full green core (26-pixel cavity).
x = xs[0]
c.rect(x + 3, 19, 6, 26, green_dark)
c.rect(x + 4, 19, 4, 25, green)
c.rect(x + 4, 19, 3, 2, green_hi)
c.set(x + 8, 44, "#0d673d")

# 60%: 16 of 26 pixels, amber to distinguish mid charge.
x = xs[1]
c.rect(x + 3, 29, 6, 16, yellow_dark)
c.rect(x + 4, 29, 4, 15, yellow)
c.rect(x + 4, 29, 3, 2, yellow_hi)
c.set(x + 8, 44, "#80580f")

# 20%: 5 of 26 pixels, warning red.
x = xs[2]
c.rect(x + 3, 40, 6, 5, red_dark)
c.rect(x + 4, 40, 4, 4, red)
c.rect(x + 4, 40, 3, 1, red_hi)
c.set(x + 8, 44, "#6e2029")

# Active charging: cyan energy fill plus a white pixel lightning glyph.
x = xs[3]
c.rect(x + 3, 27, 6, 18, cyan_dark)
c.rect(x + 4, 27, 4, 17, cyan)
c.rect(x + 4, 27, 3, 2, cyan_hi)
c.set(x + 8, 44, "#0b607c")
# Lightning bolt extends across empty and filled portions for immediate recognition.
c.poly([(x + 7, 20), (x + 3, 31), (x + 6, 31), (x + 4, 40),
        (x + 9, 28), (x + 6, 28), (x + 9, 20)], shadow)
c.poly([(x + 6, 20), (x + 3, 30), (x + 6, 30), (x + 4, 39),
        (x + 9, 27), (x + 6, 27), (x + 8, 20)], white)
c.set(x + 7, 21, cyan_hi)

# Minimal status marks beneath each bay: full, mid, low, live pulse.
c.rect(4, 51, 8, 2, green_dark)
c.rect(4, 51, 8, 1, green)
c.rect(20, 51, 5, 2, yellow_dark)
c.rect(20, 51, 5, 1, yellow)
c.rect(36, 51, 2, 2, red)
c.set(52, 52, cyan_dark)
c.rect(53, 51, 2, 2, cyan)
c.rect(55, 50, 2, 2, cyan_hi)
c.rect(57, 51, 2, 2, cyan)
c.set(59, 52, cyan_dark)

view(c, scale=8, margin=0)
finish(c)
