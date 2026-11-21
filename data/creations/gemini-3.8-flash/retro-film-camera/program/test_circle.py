import math

cx, cy = 15.5, 19.0

for y in range(11, 28):
    row = ""
    for x in range(8, 24):
        d = math.hypot(x - cx, y - cy)
        if d <= 3.0:
            row += "A"
        elif d <= 4.6:
            row += "G"
        elif d <= 5.6:
            row += "S"
        elif d <= 6.6:
            row += "B"
        else:
            row += "."
    print(f"y={y:2d}: {row} (B_count: {row.count('B') + row.count('S') + row.count('G') + row.count('A')})")
