from main import draw_beach_scene
c = draw_beach_scene()
for y in range(60, 75):
    for x in range(60, 75):
        col = c.color_name(c.get(x, y))
        if "c01a1a" in col or "ef3838" in col or "ff7070" in col:
            print(f"Red at ({x}, {y})")
