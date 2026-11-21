import main

c, pal = main.draw_portrait.build_portrait()
for y in range(0, 15):
    print(f"y={y:2d}, x=31: {c.color_name(c.get(31, y))}")
