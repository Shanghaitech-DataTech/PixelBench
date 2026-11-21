W, H, rgba = input_canvas.to_rgba()

def px(x, y):
    i = (y*W + x)*4
    return rgba[i], rgba[i+1], rgba[i+2], rgba[i+3]

# all pixels with R>=170 and G>=95 (bright warm glow family)
pts = set()
for y in range(H):
    for x in range(W):
        r, g, b, a = px(x, y)
        if r >= 170 and g >= 95:
            pts.add((x, y))
print("bright warm pixels:", len(pts))

# connected components (4-neighbour)
comps = []
seen = set()
for p in pts:
    if p in seen: continue
    stack = [p]; comp = []
    seen.add(p)
    while stack:
        cx, cy = stack.pop()
        comp.append((cx, cy))
        for nx, ny in ((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1)):
            if (nx, ny) in pts and (nx, ny) not in seen:
                seen.add((nx, ny)); stack.append((nx, ny))
    comps.append(comp)

comps.sort(key=len, reverse=True)
print("components:", len(comps))
for comp in comps[:25]:
    xs = [p[0] for p in comp]; ys = [p[1] for p in comp]
    print(f"  n={len(comp):5d} bbox=({min(xs)},{min(ys)})-({max(xs)},{max(ys)})")
