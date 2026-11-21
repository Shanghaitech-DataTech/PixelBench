inp = input_canvas
W, H = 58, 57


def band(src, y0, y1):
    t = src.copy()
    if y0 > 0:
        t.clear(0, 0, W, y0)
    if y1 < H - 1:
        t.clear(0, y1 + 1, W, H - (y1 + 1))
    return t


lower = band(inp, 44, 56)
print('lower stats:', lower.stats_text())
row43 = band(inp, 43, 43)
print('row43 stats:', row43.stats_text())
