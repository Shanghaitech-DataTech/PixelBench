from main import draw_beach_scene
c = draw_beach_scene()
for y in range(75, 83):
    row = "".join([c.color_name(c.get(x, y))[:3] for x in range(75, 115, 2)])
    print(f"y={y}: {row}")
