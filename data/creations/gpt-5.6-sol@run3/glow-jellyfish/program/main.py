# 16x16 glowing jellyfish RPG enemy
result = new_canvas(16, 16, background=None, name="glow-jellyfish")

# Compact palette: deep-water outline plus translucent cyan glow.
colors = {
    "a": "#45eaff38",  # aura
    "o": "#071a3cff",  # dark outline
    "s": "#124c6fff",  # deep shell
    "b": "#238faaff",  # bell body
    "c": "#4bdce1e8",  # bright cyan
    "h": "#a8fff2f2",  # highlight
    "w": "#e5fff9ff",  # hot core
    "t": "#46c8d9c8",  # translucent tentacle
}

# Each character is exactly one source pixel; spaces stay transparent.
sprite = [
    "                ",
    "      aaa       ",
    "     aoooa      ",
    "    aosbboa     ",
    "   aobchbboa    ",
    "   aobhwcbosa   ",
    "  aaobccbbsoa   ",
    "   aobbbbbsoa   ",
    "    oososoos    ",
    "     t t t      ",
    "     t t t      ",
    "     t  tt      ",
    "    tt  t       ",
    "    t   tt      ",
    "        t       ",
    "                ",
]

for y, row in enumerate(sprite):
    for x, key in enumerate(row):
        if key != " ":
            result.set(x, y, colors[key])

# Pinprick eye-like glints make the enemy face readable at game scale.
result.set(6, 6, "#d9fff7ff")
result.set(10, 6, "#0a2948ff")

finish(result)
view(result, scale=24, margin=2, edges="all")
