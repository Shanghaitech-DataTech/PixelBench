import numpy as np

w, h = input_canvas.stats()['size']
_, _, raw = input_canvas.to_rgba()
arr = np.frombuffer(raw, dtype=np.uint8).reshape(h, w, 4)

PALETTE = {
    'a': (255,255,255,255), 'b': (0,0,0,255), 'c': (166,85,55,255),
    'd': (224,140,55,255), 'e': (190,111,72,255), 'f': (251,244,201,255),
    'g': (255,200,48,255), 'h': (255,218,69,255), 'i': (239,157,14,255),
}
rev = {v: k for k, v in PALETTE.items()}
grid = np.empty((h, w), dtype='<U1')
for y in range(h):
    for x in range(w):
        grid[y, x] = rev.get(tuple(int(v) for v in arr[y, x]), '?')

# Crevice lines fitted through the two main 'd' streaks:
#  S3 through (32,25)-(41,33):  8x - 9y = 31
#  S4 through (20,33)-(33,48): 15x - 13y = -129
def region(x, y):
    if 8*x - 9*y > 31: return 'T'
    if 15*x - 13*y < -129: return 'B'
    return 'M'

counts = {'T':0,'M':0,'B':0}
print("    " + "".join(str(x % 10) for x in range(w)))
for y in range(h):
    row = []
    for x in range(w):
        ch = grid[y, x]
        if ch == 'b': row.append('#')
        elif ch in 'cde': row.append('R')
        elif ch in 'fghi':
            r = region(x, y); counts[r] += 1; row.append(r)
        else: row.append('.')
    print(f"{y:3d} " + "".join(row))
print(counts)
