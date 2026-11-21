c = input_canvas
W, H = 43, 61

# Which palette indices appear in which y-band, with counts
import collections
band_counts = collections.defaultdict(collections.Counter)
for y in range(H):
    for x in range(W):
        i = c.get(x, y)
        if i:
            band = 'head(0-7)' if y < 8 else ('cape(8-23)' if y < 24 else ('torso(24-43)' if y < 44 else 'legs(44-60)'))
            band_counts[band][i] += 1

for band, cnt in band_counts.items():
    print(f"=== {band} ===")
    for i, n in cnt.most_common():
        pal = c.palette()[i]
        print(f"  idx{i:2d} {pal['rgba']}  n={n}")
