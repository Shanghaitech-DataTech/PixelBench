# Let's inspect the top and bottom rows
from main import pixels, c
for y in range(5):
    row = ''.join('#' if (x, y) in pixels else '.' for x in range(32))
    print(f"y={y:2d}: {row}")
