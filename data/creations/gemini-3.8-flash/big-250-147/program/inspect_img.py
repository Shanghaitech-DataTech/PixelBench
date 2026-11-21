import numpy as np

stats = input_canvas.stats()
w, h = stats['size']
print(f"Canvas size: {w}x{h}")

palette = input_canvas.palette()
print(f"Palette size: {len(palette)}")

color_counts = {}
for y in range(h):
    for x in range(w):
        idx = input_canvas.get(x, y)
        color_counts[idx] = color_counts.get(idx, 0) + 1

sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
print("Top 30 colors:")
pal_dict = {p['index']: p for p in palette}
for idx, count in sorted_colors[:30]:
    entry = pal_dict[idx]
    print(f"Idx {idx}: {entry['rgba']} ({entry.get('name')}) - {count} pixels")

# Let's inspect where the sun/moon is located
# Sun is bright white/cream: let's find the color of the sun
print("\nBrightest colors (high R, G, B):")
for idx, entry in pal_dict.items():
    r, g, b, a = entry['rgba']
    if r > 200 and g > 200 and b > 180:
        print(f"Sun candidate Idx {idx}: {entry['rgba']} - {color_counts.get(idx, 0)} pixels")
