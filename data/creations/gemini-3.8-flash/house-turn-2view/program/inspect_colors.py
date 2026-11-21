# Detailed color usage
import collections
pixels = [input_canvas.get(x, y) for y in range(157) for x in range(112)]
counts = collections.Counter(pixels)
palette = input_canvas.palette()
for idx, count in counts.most_common():
    entry = palette[idx]
    print(f"Index {idx} ({entry['name']}): RGBA {entry['rgba']} - count {count}")
