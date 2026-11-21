out = input_canvas.copy(name='output')

E = '#5e363e'   # chocolate dark body
R = '#95524c'   # chocolate mid/light
V = '#bd5333'   # chocolate warm highlight
D = '#533444'   # dark outline

def drip(x, w, y0, y1, hl=True):
    for y in range(y0, y1 + 1):
        for i in range(w):
            out.set(x + i, y, E)
    # rounded tip
    out.set(x, y1 + 1, E)
    if w > 1:
        out.set(x + w - 1, y1 + 1, E)
    if w > 2:
        out.set(x + 1, y1 + 2, E)
        out.set(x + w - 2, y1 + 2, E)
        out.set(x + 1, y1 + 1, E)
        out.set(x + w - 2, y1 + 1, E)
    if hl:
        for y in range(y0, y1 + 1):
            out.set(x, y, R)

# melt bulges along the bottom edge of the scoop (scoop bottom ~row 31-32)
for (x0, x1, dy) in [(23, 26, 2), (30, 32, 1), (36, 39, 3), (42, 43, 1)]:
    for x in range(x0, x1 + 1):
        for y in range(31, 31 + dy + 1):
            if out.get(x, y) == 1 or True:
                pass
    for x in range(x0, x1 + 1):
        for y in range(32, 32 + dy):
            out.set(x, y, E)
    out.set(x0, 31 + dy, E)
    out.set(x1, 31 + dy, E)

# drips running down the cone
drip(33, 4, 33, 47)          # wide drip, left of centre
drip(39, 3, 33, 55)          # long thin drip
drip(43, 2, 33, 42)          # short drip near right edge

# detached droplet below the longest drip
out.set(40, 58, E); out.set(41, 58, E)
out.set(40, 59, E); out.set(41, 59, E)
out.set(40, 57, R)

finish(out)
print(out.matrix_text(region=(16, 28, 48, 60)))
