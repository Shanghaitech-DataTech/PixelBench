# Melting ice cream: chocolate scoop melts and drips down the cone.
out = input_canvas.copy(name='output')

CHOC_DARK = '#5e363e'   # scoop body dark chocolate (matches scoop bottom edge)
CHOC_MID  = '#95524c'   # scoop lighter midtone, used as melt highlight

def drip(x0, w, y0, y1, highlight=False):
    """Vertical melt drip, width w, rounded tip, from y0 to y1 inclusive."""
    for y in range(y0, y1 + 1):
        rem = y1 - y
        if rem == 0:
            # tip: narrow to a point
            out.set(x0 + (1 if w >= 3 else 0), y, CHOC_DARK)
        elif rem == 1 and w >= 3:
            out.set(x0, y, CHOC_DARK)
            out.set(x0 + 1, y, CHOC_DARK)
        else:
            for i in range(w):
                col = CHOC_MID if (highlight and i == 1 and rem > 2) else CHOC_DARK
                out.set(x0 + i, y, col)

# --- Melt layer along the top of the cone (cone top edge is y=33, x19-42) ---
for x in range(19, 43):
    out.set(x, 33, CHOC_DARK)
# a few lighter chocolate pixels inside the melt layer for texture
for x in (22, 27, 33, 39):
    out.set(x, 33, CHOC_MID)
# irregular sag: melt bulges one row lower in spots
for x in (23, 28, 36):
    out.set(x, 34, CHOC_DARK)

# --- Drips running down the cone (cone tapers: keep each drip on the cone) ---
drip(21, 2, 34, 40)              # short drip, left
drip(25, 2, 34, 46)              # medium drip
drip(29, 3, 34, 50, highlight=True)  # longest, thickest drip with highlight
drip(34, 2, 34, 43)              # medium-short drip
drip(37, 2, 34, 38)              # short drip, right

# --- Drips running off the sides of the scoop ---
drip(17, 2, 30, 34)              # off the lower-left edge of the scoop
drip(43, 2, 30, 33)              # off the lower-right edge of the scoop

print(out.stats_text())
view(out, scale=8)
finish(out)
