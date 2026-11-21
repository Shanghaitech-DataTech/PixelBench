# Public transportation icon set, 64x64 pixel art
result = new_canvas(64, 64, background="#0b1626", name="public-transportation-icon-set")

# Palette
bg = "#0b1626"
frame_shadow = "#17263a"
frame = "#2b3e55"
panel = "#122238"
panel_hi = "#1b3048"
ink = "#07111e"
cream = "#f3e6c8"
yellow = "#f4bf3a"
yellow_hi = "#ffd75a"
cyan = "#43c5cf"
cyan_hi = "#82e1dc"
coral = "#ef6f61"
coral_hi = "#ff9b78"
green = "#69c774"
green_hi = "#a3df7e"

# Four matching recessed sign frames.
for x, y in [(2, 2), (34, 2), (2, 34), (34, 34)]:
    result.rect(x + 2, y + 2, 28, 28, frame_shadow)
    result.rect(x, y, 28, 28, frame)
    result.rect(x + 2, y + 2, 24, 24, panel)
    result.line(x + 3, y + 3, x + 24, y + 3, panel_hi)
    result.line(x + 3, y + 3, x + 3, y + 24, panel_hi)
    # Corner rivets unify the sign system.
    result.set(x + 2, y + 2, cream)
    result.set(x + 25, y + 25, ink)

# BUS, upper-left: blocky side/front hybrid silhouette.
# destination cap and body outline
result.rect(8, 7, 16, 3, ink)
result.rect(6, 10, 20, 14, ink)
result.rect(8, 7, 14, 2, yellow_hi)
result.rect(8, 10, 16, 12, yellow)
# windows
result.rect(9, 11, 5, 5, cyan_hi)
result.rect(16, 11, 5, 5, cyan_hi)
result.set(9, 11, cream)
result.set(16, 11, cream)
# center divider and lower face
result.rect(14, 11, 2, 6, ink)
result.rect(8, 17, 16, 2, yellow_hi)
result.rect(10, 20, 3, 2, cream)
result.rect(19, 20, 3, 2, cream)
# side mirrors
result.rect(4, 12, 2, 5, ink)
result.set(4, 12, yellow_hi)
result.rect(26, 12, 2, 5, ink)
result.set(27, 12, yellow_hi)
# wheels and roadway cue
result.rect(9, 23, 5, 3, ink)
result.rect(19, 23, 5, 3, ink)
result.rect(10, 23, 3, 2, frame)
result.rect(20, 23, 3, 2, frame)
result.rect(7, 27, 18, 1, frame)

# SUBWAY, upper-right: front-facing car and twin rails.
# outer car shell
result.rect(41, 7, 16, 2, ink)
result.rect(39, 9, 20, 15, ink)
result.rect(41, 7, 14, 2, cyan_hi)
result.rect(41, 9, 16, 13, cyan)
# roof sign
result.rect(46, 8, 6, 2, cream)
result.rect(47, 8, 4, 1, coral)
# windshield pair
result.rect(42, 11, 6, 6, cyan_hi)
result.rect(50, 11, 6, 6, cyan_hi)
result.set(42, 11, cream)
result.set(50, 11, cream)
result.rect(48, 11, 2, 7, ink)
# lower front and lights
result.rect(41, 18, 16, 4, cyan_hi)
result.rect(43, 19, 3, 2, yellow_hi)
result.rect(52, 19, 3, 2, yellow_hi)
result.rect(47, 20, 4, 2, frame)
# coupler, wheels, angled rails
result.rect(47, 22, 4, 3, ink)
result.rect(41, 23, 4, 2, ink)
result.rect(54, 23, 4, 2, ink)
result.line(44, 25, 41, 28, cream)
result.line(54, 25, 57, 28, cream)
result.rect(47, 26, 4, 1, frame)

# BICYCLE, lower-left: concentric pixel wheels and a compact diamond frame.
for cx in (10, 24):
    result.circle(cx, 52, 6, coral_hi)
    result.circle(cx, 52, 4, panel)
    result.rect(cx - 1, 51, 3, 3, cream)
    result.set(cx, 52, ink)
# Frame triangle, chain stay, and front fork.
result.line(10, 52, 15, 46, coral)
result.line(10, 52, 18, 52, coral)
result.line(15, 46, 18, 52, coral)
result.line(15, 46, 22, 46, coral)
result.line(18, 52, 22, 45, coral)
result.line(18, 52, 24, 52, coral)
result.line(22, 45, 24, 52, coral)
# Parallel highlights give the one-pixel diagonals the set's chunky weight.
result.line(11, 52, 16, 47, coral_hi)
result.line(16, 47, 19, 52, coral_hi)
result.rect(17, 51, 3, 3, yellow_hi)
result.set(18, 52, ink)
# Seat, stem, and handlebar.
result.rect(11, 43, 6, 2, ink)
result.rect(13, 45, 3, 2, coral)
result.line(22, 46, 21, 42, coral_hi)
result.rect(20, 41, 2, 3, coral_hi)
result.rect(20, 40, 6, 2, cream)

# PEDESTRIAN, lower-right: forward walking pose.
# head with highlight
result.rect(46, 39, 6, 2, green_hi)
result.rect(44, 41, 10, 5, green)
result.rect(46, 46, 6, 2, green)
result.set(46, 40, cream)
result.rect(46, 41, 6, 5, green_hi)
# torso, backpack edge, and arms
result.rect(45, 48, 8, 8, green)
result.rect(47, 47, 5, 9, green_hi)
result.rect(43, 49, 3, 6, green)
result.line(44, 54, 40, 58, green)
result.rect(39, 57, 3, 2, green_hi)
result.rect(53, 49, 3, 5, green)
result.line(55, 53, 58, 56, green)
result.rect(57, 55, 2, 3, green_hi)
# walking legs and shoes
result.line(48, 55, 45, 60, green_hi)
result.rect(43, 59, 5, 2, green_hi)
result.line(51, 55, 55, 60, green)
result.rect(54, 59, 6, 2, green)
result.rect(42, 61, 6, 1, ink)
result.rect(54, 61, 6, 1, ink)

# Tiny mode markers at each panel's upper-right tie the set together.
for x, y, col in [(27, 5, yellow_hi), (59, 5, cyan_hi), (27, 37, coral_hi), (59, 37, green_hi)]:
    result.set(x, y, col)

view(result, scale=8, margin=0)
finish(result)
