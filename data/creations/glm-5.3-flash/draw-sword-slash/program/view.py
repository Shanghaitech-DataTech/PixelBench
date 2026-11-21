c = input_canvas
groups = {
    1: "O", 2: "O", 5: "O", 6: "O", 10: "O",
    3: "M", 4: "M",
    11: "S",
    12: "L", 13: "L", 14: "L",
    15: "X",
    7: "B", 9: "B", 8: "B",
}
print("FULL ORIGINAL (semantic):")
for y in range(0, 72):
    row = ""
    for x in range(62):
        v = c.get(x, y)
        row += groups.get(v, ".") if v else "."
    print(f"{y:2d} {row}")
