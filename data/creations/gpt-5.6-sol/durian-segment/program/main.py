# Remove the lowest flesh lobe while keeping the original silhouette and other lobes.
output = input_canvas.copy(name='output')

# Scanline bounds follow the orange seam above the bottom lobe and the rind edge below.
bounds = {
    36:(15,20), 37:(13,21), 38:(12,22), 39:(10,24), 40:(9,26),
    41:(8,28), 42:(7,31), 43:(6,36), 44:(5,38), 45:(5,37),
    46:(5,36), 47:(6,35), 48:(7,34), 49:(8,33), 50:(10,32),
    51:(12,31), 52:(16,29), 53:(20,28)
}

# Brown-orange rind revealed where the yellow flesh used to sit. Existing outline pixels
# and seam pixels are retained; the restrained highlights match the rind already visible.
for y, (x0, x1) in bounds.items():
    for x in range(x0, x1 + 1):
        old = output.get(x, y)
        if old in (6, 7, 8):
            if y >= 51 or x <= x0 + 1:
                colour = 5                 # dark rind edge
            elif ((x + 2*y) % 11) in (0, 1):
                colour = 3                 # deepest rind fleck
            elif ((2*x + y) % 9) in (0, 1, 2):
                colour = 9                 # golden inner-rind highlight
            else:
                colour = 4                 # main exposed rind
            output.set(x, y, colour)

# A few connected highlight facets give the exposed rind the same chunky pixel texture.
for x, y in [(11,42),(12,42),(13,42),(14,42),(15,42),
             (10,43),(11,43),(12,43),(19,44),(20,44),(21,44),
             (28,45),(29,45),(30,45),(26,46),(27,46),(28,46),
             (17,48),(18,48),(19,48),(20,48),(21,48)]:
    if output.get(x, y) not in (1, 2):
        output.set(x, y, 9)

view(output, scale=8, margin=0)
finish(output)
