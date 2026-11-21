out = input_canvas.copy(name='output')

W = '#ffffffff'        # background white
OUT = '#2e1f12ff'      # existing outline colour
SKIN = '#f2c49bff'     # existing hand skin
GOLD = '#c9a227ff'     # existing gold
GEM = '#3fa9cf'
GEM_L = '#a5e8f7'
GEM_D = '#1f6e8c'
WOOD_L = '#a9743f'
WOOD_D = '#6e4a26'


def erase(x0, y0, x1, y1):
    out.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, W)


# --- 1. remove the sword ---
erase(42, 41, 44, 55)   # steel blade down to its tip
erase(40, 39, 46, 40)   # gold crossguard plus its outline pixels
erase(40, 38, 44, 38)   # visible grip row between fist and guard
erase(42, 34, 43, 34)   # grip top just above the fist

# --- 2. staff shaft (vertical, through the same hand position) ---
for y in range(20, 58):
    out.set(42, y, WOOD_L)
    out.set(43, y, WOOD_D)

# fist bottom outline kept on both sides of the emerging shaft
out.set(40, 38, OUT)
out.set(41, 38, OUT)
out.set(44, 38, OUT)

# --- 3. redraw the fist over the shaft so it reads as gripping ---
for y in range(35, 38):
    for x in range(40, 44):
        out.set(x, y, SKIN)

# --- 4. orb topper ---
out.set(42, 14, GEM_D)
out.set(43, 14, GEM_D)
for x, c in zip(range(41, 45), [GEM_L, GEM, GEM, GEM_D]):
    out.set(x, 15, c)
    out.set(x, 16, c)
out.set(41, 17, GEM)
out.set(42, 17, GEM)
out.set(43, 17, GEM_D)
out.set(44, 17, GEM_D)
out.set(42, 18, GEM_D)
out.set(43, 18, GEM_D)

# gold collar between orb and shaft
for x in range(41, 45):
    out.set(x, 19, GOLD)

print(out.stats_text())
print(out.matrix_text(region=(34, 10, 50, 60), indices=True))
finish(out)
