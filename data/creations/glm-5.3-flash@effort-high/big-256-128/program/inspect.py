c = input_canvas
# Downsample: 4x4 blocks -> 64x32 grid, print dominant color index per block
import numpy as np
w, h, rgba = c.to_rgba()
arr = np.array(rgba, dtype=np.uint8).reshape(h, w, 4)
bs = 4
gh, gw = h // bs, w // bs
grid = np.zeros((gh, gw), dtype=int)
for gy in range(gh):
    for gx in range(gw):
        block = arr[gy*bs:(gy+1)*bs, gx*bs:(gx+1)*bs]
        # dominant color (count exact tuples)
        flat = block.reshape(-1, 4)
        vals, counts = np.unique(flat, axis=0, return_counts=True)
        grid[gy, gx] = int(np.argmax(counts))  # position of most common
# map unique colors to letters
uniq = {}
chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = np.empty((gh, gw), dtype='<U1')
legend = {}
for gy in range(gh):
    for gx in range(gw):
        t = tuple(arr[gy*bs, gx*bs])
        if t not in uniq:
            uniq[t] = chars[len(uniq) % len(chars)]
        letters[gy, gx] = uniq[t]
for t, ch in sorted(uniq.items(), key=lambda kv: kv[1]):
    print(ch, t)
print()
for gy in range(gh):
    print("".join(letters[gy]))
