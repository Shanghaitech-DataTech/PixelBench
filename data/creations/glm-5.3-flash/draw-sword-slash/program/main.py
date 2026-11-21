W, H = 76, 84
OX, OY = 7, 6

# ---------- Frame 1: original picture content ----------
f1 = new_canvas(W, H, background=None, name="f1")
f1.blit(input_canvas, OX, OY)

# ---------- Frame 2: completed drawn-sword slash ----------
f2 = new_canvas(W, H, background=None, name="f2")
f2.blit(input_canvas, OX, OY)

# Colours
BLACK = f2.color("#000000", name="slash_black")
BLADE_HI = f2.color("#eedddd", name="blade_hi")
BLADE_MID = f2.color("#b2aeb1", name="blade_mid")
BLADE_LO = f2.color("#6e6a72", name="blade_lo")

# --- 1. Turn the old motion streak into a black slash trail ---
DARK = {1, 2, 5, 6, 7, 10}
for y in range(43, 53):
    for x in range(0, 26):
        if f2.get(x, y) in DARK:
            f2.set(x, y, BLACK)
for (x, y) in [(26, 44), (26, 45)]:
    if f2.get(x, y) in DARK:
        f2.set(x, y, BLACK)

# --- 2. Bridge the trail toward the sword hand ---
f2.line(32, 49, 40, 47, BLACK)
f2.line(32, 50, 40, 48, BLACK)
f2.line(32, 51, 40, 49, BLACK)

# --- 3. Remove the old short blade ---
for y in range(45, 49):
    for x in range(48, 56):
        if (x, y) == (55, 45):
            continue
        f2.set(x, y, None)

# --- 4. Draw the fully extended blade sweeping to the upper right ---
f2.line(48, 46, 70, 39, BLADE_MID)
f2.line(48, 47, 72, 40, BLADE_HI)
f2.line(48, 48, 70, 41, BLADE_LO)
f2.set(71, 40, BLADE_MID)
f2.set(72, 40, BLADE_MID)

print("F1:", f1.stats_text())
print("F2:", f2.stats_text())

finish([f1, f2])
