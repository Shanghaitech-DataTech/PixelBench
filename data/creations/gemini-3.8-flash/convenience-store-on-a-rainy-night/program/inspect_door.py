import main
c = main.draw_scene()
for y in range(43, 52):
    row = [f"{c.color_name(c.get(x, y)):8s}" for x in range(36, 54)]
    print(f"y={y}: " + " ".join(row))
