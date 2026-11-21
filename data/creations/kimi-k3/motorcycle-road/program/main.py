# --- 1. Separate the motorcycle from its white background ---
bike = input_canvas.copy(name="bike")
bike.fill_at(0, 0, None)   # erase the connected white background (rim whites are enclosed, they stay)

# --- 2. Build a country-road backdrop ---
bg = new_canvas(64, 64, "#00000000", name="bg")

# Sky: two-tone blue
bg.rect(0, 0, 64, 15, "#6ea6d9")
bg.rect(0, 15, 64, 12, "#a7cdec")

# Sun
bg.circle(52, 8, 4, "#ffd94a")

# Clouds
bg.ellipse(13, 8, 6, 2, "#ffffff")
bg.ellipse(17, 7, 4, 2, "#ffffff")
bg.ellipse(36, 14, 5, 2, "#ffffff")
bg.ellipse(40, 13, 3, 2, "#ffffff")

# Distant rolling hills
bg.ellipse(14, 33, 17, 6, "#4f8340")
bg.ellipse(49, 32, 19, 6, "#5b924a")

# Field between hills and road
bg.rect(0, 32, 64, 6, "#69a34c")
bg.dither(0, 32, 64, 6, ["#69a34c", "#619a46"], pattern="bayer4")

# Trees and a bush on the horizon
bg.rect(5, 28, 1, 4, "#6b4a2f")
bg.circle(5, 26, 3, "#3f7034")
bg.rect(59, 29, 1, 3, "#6b4a2f")
bg.circle(59, 27, 3, "#3f7034")
bg.circle(2, 31, 2, "#4f8340")

# Road (rows 38-56), asphalt with texture, edges and a dashed centre line
bg.rect(0, 38, 64, 19, "#82848a")
bg.dither(0, 40, 64, 14, ["#82848a", "#787a80"], pattern="bayer4")
bg.line(0, 38, 63, 38, "#5c5e63")
bg.line(0, 56, 63, 56, "#5c5e63")
for x in range(1, 64, 9):
    bg.rect(x, 49, 5, 2, "#dcdcd0")

# Shadow under the motorcycle, grounding it on the road
bg.ellipse(33, 46, 24, 2, "#4e5056")

# Foreground grass with tufts and flowers
bg.rect(0, 57, 64, 7, "#5c9440")
bg.dither(0, 58, 64, 6, ["#5c9440", "#548a3a"], pattern="bayer4")
for x in (4, 12, 21, 33, 45, 53, 60):
    bg.set(x, 56, "#4a7a34")
bg.set(13, 55, "#4a7a34")
bg.set(46, 55, "#4a7a34")
bg.set(9, 60, "#f2d24a")
bg.set(26, 61, "#ffffff")
bg.set(41, 59, "#f2d24a")
bg.set(56, 62, "#e8a0c0")

# --- 3. Composite bike onto the scene ---
result = flatten([bg, bike], name="output")

view(result)
finish(result)
