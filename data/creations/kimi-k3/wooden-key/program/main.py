# Wooden key — 16x16, 5 visible colours, detective-game item icon
key = new_canvas(16, 16, name="wooden-key")

OUT   = key.color("#2a1608", "outline")   # near-black brown outline
GRAIN = key.color("#5e3a1c", "grain")     # dark wood grain / shade
WOOD  = key.color("#96642e", "wood")      # mid wood
LIGHT = key.color("#c89452", "light")     # light wood
HI    = key.color("#f0d9a0", "highlight") # pale polished highlight

# --- silhouette (outline colour) ---
key.circle(3, 6, 3, OUT)        # bow ring, x0..6 y3..9
key.rect(4, 5, 11, 4, OUT)      # shaft x4..14, y5..8
key.rect(9, 9, 2, 3, OUT)       # tooth 1: x9..10, y9..11
key.rect(12, 9, 2, 2, OUT)      # tooth 2: x12..13, y9..10

# --- interiors ---
key.circle(3, 6, 2, LIGHT)      # ring band
key.circle(3, 6, 1, None)       # punch the bow hole (transparent)

# shaft interior: two rows, x5..13
key.rect(5, 6, 9, 1, LIGHT)     # upper row lit
key.rect(5, 7, 9, 1, WOOD)      # lower row mid tone

# polished glints on the shaft's lit row
key.set(5, 6, HI)
key.set(6, 6, HI)
key.set(7, 6, HI)

# wood-grain flecks in the shaded row
key.set(9, 7, GRAIN)
key.set(12, 7, GRAIN)

# ring shading: glint upper-left, grain lower-right
key.set(2, 4, HI)
key.set(2, 5, HI)
key.set(3, 8, GRAIN)
key.set(4, 8, GRAIN)

# teeth interiors (wood with dark tip/edge)
key.set(10, 9, WOOD)
key.set(10, 10, WOOD)
key.set(13, 9, WOOD)

view(key)
finish(key)
