from pixelbench_api import *

W = H = 16
c = new_canvas(W, H, name="glow_jellyfish")

# ---------------------------------------------------------------- palette
PAL = {
    'o': '#0a1622',   # dark navy outline
    'h': '#e8fdff',   # pale glow highlight
    'c': '#6fe3ff',   # bright cyan glow
    'g': '#2f9dc9',   # mid cyan (bell body / dimmer glow)
    'b': '#12506e',   # deep translucent interior
}

# ---------------------------------------------------------------- pixel map
SPEC = {
    2:  {7: 'o', 8: 'o'},
    3:  {6: 'o', 7: 'h', 8: 'h', 9: 'o'},
    4:  {5: 'o', 6: 'h', 7: 'h', 8: 'c', 9: 'c', 10: 'o'},
    5:  {4: 'o', 5: 'h', 6: 'c', 7: 'c', 8: 'c', 9: 'c', 10: 'g', 11: 'o'},
    6:  {4: 'o', 5: 'c', 6: 'c', 7: 'c', 8: 'g', 9: 'g', 10: 'g', 11: 'o'},
    7:  {4: 'o', 5: 'c', 6: 'g', 7: 'b', 8: 'b', 9: 'g', 10: 'g', 11: 'o'},
    8:  {4: 'o', 5: 'o', 6: 'c', 7: 'o', 8: 'o', 9: 'c', 10: 'o', 11: 'o'},
    9:  {6: 'c', 9: 'c'},
    10: {6: 'c', 9: 'c'},
    11: {5: 'g', 10: 'g'},
    12: {5: 'c', 10: 'c'},
}

for y, row in SPEC.items():
    for x, ch in row.items():
        assert 0 <= x < W and 0 <= y < H, (x, y)
        c.set(x, y, PAL[ch])

# ---------------------------------------------------------------- report
print(c.stats_text())
print()
print(c.matrix_text())
print()
print("palette:", [p["rgba"] for p in c.palette()])

save("glow_jellyfish", c, indexed=True)
finish(c)
