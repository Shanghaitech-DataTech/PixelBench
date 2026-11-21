c = input_canvas

# Print hex colours for the top portion (y=4..30) to understand the ice cream
for y in range(4, 32):
    row = []
    for x in range(10, 48):
        idx = c.get(x, y)
        p = c.palette()
        rgba = p[idx]["rgba"]
        if rgba[0] > 245 and rgba[1] > 245 and rgba[2] > 245:
            row.append("......")
        else:
            row.append(f"{rgba[0]:02x}{rgba[1]:02x}{rgba[2]:02x}")
    print(f"{y:2d} " + " ".join(row))
