from collections import Counter

# Find where the original foreground first becomes dense in each column.
for y in range(45, 71):
    counts = Counter(input_canvas.get(x, y) for x in range(250))
    print(y, counts.most_common(5))

output = input_canvas.copy(name="output")
# Noon sky gradient ends just above the foreground's first continuous rows.
sky_bands = [(0, 13, "#579fe0"), (14, 27, "#63afea"), (28, 41, "#74c1ef"), (42, 54, "#8bd2f3")]
for y0, y1, color in sky_bands:
    output.rect(0, y0, 250, y1 - y0 + 1, color)
# Remove the final two rows of the disc at its lower edge.
output.rect(103, 55, 43, 2, "#8bd2f3")
print(output.stats_text())
finish(output)
