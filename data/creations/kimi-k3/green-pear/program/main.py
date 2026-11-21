
pear = new_canvas(32, 32, name="green_pear")

# Palette (6 colours + transparency)
OUT  = "#1e5b23"  # dark green outline
BODY = "#5cb050"  # main pear green
SHD  = "#3c8a3c"  # shadow green
HI   = "#c1ed7e"  # highlight
STEM = "#7b4a24"  # brown stem
LEAF = "#2f9e44"  # leaf green

# Silhouette in outline colour (two merged ellipses = pear)
pear.ellipse(16, 12, 6, 7, OUT)    # top bulb
pear.ellipse(16, 22, 10, 8, OUT)   # bottom bulb

# Body, 1px inside the outline
pear.ellipse(16, 12, 5, 6, BODY)
pear.ellipse(16, 22, 9, 7, BODY)

# Shading and highlights (kept inside the body)
pear.ellipse(19, 23, 4, 4, SHD)    # right-side shadow
pear.set(16, 22, SHD)              # soften the shadow edge
pear.set(17, 25, SHD)
pear.set(20, 18, SHD)              # shadow dabs near the waist
pear.set(21, 19, SHD)
pear.ellipse(12, 20, 2, 3, HI)     # left highlight on belly
pear.ellipse(13, 9, 2, 2, HI)      # small highlight near top

# Stem (2px thick, slight lean)
pear.rect(15, 3, 2, 4, STEM)
pear.set(17, 4, STEM)

# Leaf, attached to the stem, pointing right
pear.path("M16,4 Q21,0 26,2 Q22,7 16,6 Z", LEAF)
pear.line(17, 4, 22, 3, SHD)  # soft leaf vein

print(pear.stats_text())
view(pear)
finish(pear)
