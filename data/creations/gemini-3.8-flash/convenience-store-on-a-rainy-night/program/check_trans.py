import main
c = main.draw_scene()
transparent_pts = []
for y in range(64):
    for x in range(64):
        idx = c.get(x, y)
        pal = c.palette()
        # check alpha of idx
        if pal[idx]['rgba'][3] == 0:
            transparent_pts.append((x, y))
print(f"Transparent count: {len(transparent_pts)}, samples: {transparent_pts[:10]}")
