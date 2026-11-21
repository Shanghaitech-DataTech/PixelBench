chars = {0: ".", 1: ".", 2: "#", 3: "g", 4: "@", 5: "d", 6: "~", 7: "l", 8: "o", 9: ",", 10: "`"}
for y in range(64):
    print(f"{y:2d} " + "".join(chars[input_canvas.get(x, y)] for x in range(64)))
