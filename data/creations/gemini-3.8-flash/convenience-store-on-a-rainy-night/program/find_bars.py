import main
c = main.draw_scene()
for x in [31, 32, 33, 34, 35, 36]:
    for y in range(23, 48):
        name = c.color_name(c.get(x, y))
        if '1d4ed8' in name or 'dc2626' in name:
            print(f"x={x}, y={y}: {name}")
