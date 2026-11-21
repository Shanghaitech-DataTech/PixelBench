# Analyze input image in detail
palette = input_canvas.palette()
print(f"Palette length: {len(palette)}")
for p in palette:
    print(p)

# Check colors used and bounding box
stats = input_canvas.stats()
print("Stats:", stats)

# Let's inspect symmetry of the front view
w, h = input_canvas.stats()['size']
print(f"Size: {w}x{h}")
