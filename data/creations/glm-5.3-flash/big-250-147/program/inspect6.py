w, h, rgba = input_canvas.to_rgba()

def px(x, y):
    i = (y*w + x)*4
    return (rgba[i], rgba[i+1], rgba[i+2], rgba[i+3])

# 1) detect "bright/glow" pixels: G >= 118 (sky max G is 114)
pts = []
for y in range(h):
    for x in range(w):
        r, g, b, a = px(x, y)
        if g >= 118 and r >= 176:
            pts.append((x, y))
xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
print("glow-ish pixels:", len(pts), "bbox", (min(xs), min(ys), max(xs), max(ys)) if pts else None)

# per-row extent of glow
rows = {}
for x, y in pts:
    rows.setdefault(y, []).append(x)
for y in sorted(rows):
    r = rows[y]
    print(y, min(r), max(r), len(r))
