# Detailed coordinate analysis
for r in range(13, 19):
    pixels = []
    for y in range(16):
        for x in range(16):
            dc = (15.5 - x) + (15.5 - y)
            if dc == r:
                pixels.append((x, y))
    print(f"Radius {r}: count={len(pixels)}, pixels={pixels}")
