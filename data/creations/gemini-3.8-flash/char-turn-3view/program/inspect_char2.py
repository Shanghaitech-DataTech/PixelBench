palette = input_canvas.palette()
pal_dict = {p['index']: p['rgba'] for p in palette}
for p in palette:
    print(f"Index {p['index']}: name={p['name']}, rgba={p['rgba']}")

# Let's inspect rows from top to bottom
for y in range(0, 119, 5):
    row = [input_canvas.get(x, y) for x in range(66)]
    # find min and max non-zero x
    non_zeros = [x for x in range(66) if row[x] != 0]
    if non_zeros:
        print(f"y={y:3d}: x in [{min(non_zeros):2d}, {max(non_zeros):2d}], width={max(non_zeros)-min(non_zeros)+1}")
    else:
        print(f"y={y:3d}: empty")
