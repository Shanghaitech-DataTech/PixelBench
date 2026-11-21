from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="pear")

DARK   = "#2e5d1f"   # outline, dark green
MAIN   = "#6bbf3a"   # body main green
LIGHT  = "#a8e25f"   # highlight
SHADE  = "#4c8f2a"   # shade green
STEM   = "#7a4a1f"   # stem brown
LEAF   = "#3e7a1a"   # leaf green
LEAFD  = "#25530f"   # leaf dark

# Pear body path (closed)
body = ("M 16 9 "
        "C 18 8, 20 10, 20 14 "
        "C 20 17, 24 18, 25 21 "
        "C 26 24, 25 28, 16 30 "
        "C 7 28, 6 24, 7 21 "
        "C 8 18, 12 17, 12 14 "
        "C 12 10, 14 8, 16 9 Z")

# Fill body with main green
c.path(body, MAIN, fill=True)

# Highlights and shading
c.ellipse(20, 15, 3, 5, LIGHT, fill=True)   # top-right highlight
c.ellipse(10, 24, 3, 4, SHADE, fill=True)   # bottom-left shading
c.ellipse(21, 20, 2, 3, LIGHT, fill=True)   # side glint
c.ellipse(12, 15, 2, 3, SHADE, fill=True)   # shoulder shade

# Outline of the fruit
c.path(body, DARK, fill=False)

# Stem
c.line(15, 7, 15, 2, STEM)
c.set(14, 2, STEM)
c.set(16, 7, STEM)

# Leaf
c.path("M 17 8 Q 23 2 27 5 Q 22 9 17 8 Z", LEAF, fill=True)
c.path("M 17 8 Q 23 2 27 5 Q 22 9 17 8 Z", LEAFD, fill=False)

print(c.stats_text())
finish(c)
