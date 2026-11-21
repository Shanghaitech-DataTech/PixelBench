from pixelbench_api import new_canvas, finish

OUT = "#141414"
c = new_canvas(32, 32, name="retro_camera")

# ---------- silhouette (dark outline) ----------
c.rect(3, 9, 26, 17, OUT)   # body  x3..28 y9..25
c.rect(2, 9, 2, 3, OUT)     # strap lug left
c.rect(28, 9, 2, 3, OUT)    # strap lug right
c.rect(3, 10, 1, 1, "#56514c")   # lug fill
c.rect(28, 10, 1, 1, "#56514c")  # lug fill
c.rect(11, 5, 10, 4, OUT)   # viewfinder hump x11..20 y5..8
c.rect(13, 3, 6, 2, OUT)    # hot shoe  x13..18 y3..4
c.rect(23, 3, 2, 3, OUT)    # shutter button x23..24 y3..5
c.rect(5, 6, 4, 3, OUT)     # rewind knob x5..8 y6..8
c.rect(20, 7, 4, 2, OUT)    # film advance lever x20..23 y7..8
c.circle(16, 17, 8, OUT)     # lens barrel x8..24 y9..25

# ---------- base fills ----------
c.rect(4, 10, 24, 15, "#2e2925")   # body leather base
c.rect(4, 10, 24, 1, "#4a443e")    # top plate
c.rect(4, 24, 24, 1, "#1f1a16")    # bottom shade
c.rect(12, 6, 8, 2, "#4a443e")     # hump
c.rect(14, 4, 4, 1, "#33302c")      # hot shoe
c.rect(6, 7, 2, 1, "#56514c")       # knob
c.rect(23, 4, 2, 1, "#56514c")      # shutter
c.rect(21, 8, 2, 1, "#56514c")      # lever

# ---------- small details ----------
c.rect(14, 6, 4, 2, "#0d0d0d")      # viewfinder window
c.set(14, 6, "#4c4a56")
c.set(25, 10, "#d9403a")             # red LED
c.set(26, 10, "#8f2320")
c.set(23, 4, "#8d877f")              # shutter highlight
c.set(21, 8, "#8d877f")              # lever highlight
c.set(6, 7, "#8d877f")               # knob highlight

# ---------- leather stipple ----------
for y in range(11, 24, 2):
    c.set(7, y, "#1b1612")
    c.set(25, y, "#1b1612")
for y in range(12, 24, 2):
    c.set(5, y, "#1b1612")
    c.set(26, y, "#1b1612")
c.set(11, 24, "#1b1612")
c.set(21, 24, "#1b1612")
c.set(9, 13, "#1b1612")
c.set(23, 13, "#1b1612")
c.set(15, 22, "#1b1612")
c.set(20, 22, "#1b1612")
c.set(6, 15, "#1b1612")
c.set(26, 17, "#1b1612")
c.set(8, 19, "#1b1612")
c.set(24, 21, "#1b1612")
c.set(6, 21, "#1b1612")
c.set(9, 11, "#1b1612")
c.set(23, 11, "#1b1612")
c.line(4, 11, 4, 23, "#3a342e")      # left edge light
c.line(27, 11, 27, 23, "#26211d")    # right edge shade

# ---------- lens ----------
c.circle(16, 17, 8, OUT)             # outer barrel
c.circle(16, 17, 6, "#3a3a3a")
c.circle(16, 17, 5, "#6f6f6f")        # metal rim
c.circle(16, 17, 4, "#242424")        # inner bezel
c.circle(16, 17, 3, "#0d101a")        # glass
c.set(13, 13, "#9a9a9a")              # rim highlight
c.set(12, 14, "#9a9a9a")
c.set(12, 15, "#9a9a9a")
c.set(13, 16, "#6f6f6f")
c.set(20, 19, "#2a2a2a")              # rim shadow
c.set(19, 20, "#2a2a2a")
c.set(16, 14, "#c8dcff")              # glass reflections
c.set(15, 15, "#8fb0e8")
c.set(14, 16, "#8fb0e8")
c.set(17, 19, "#2c4a7a")

print(c.stats_text())
print(c.matrix_text())
finish(c)
