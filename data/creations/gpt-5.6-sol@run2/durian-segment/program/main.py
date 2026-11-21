output = input_canvas.copy(name="output")

# Remove the broad lower-left flesh lobe.  A dark rind bed follows the old
# stepped silhouette, while the inset cream area reads as exposed inner pith.
output.poly([
    (5, 38), (8, 35), (11, 35), (11, 32), (14, 32), (14, 30),
    (18, 30), (20, 34), (21, 34), (21, 39), (24, 39), (24, 42),
    (28, 42), (28, 45), (33, 45), (33, 48), (29, 48), (29, 51),
    (24, 51), (24, 53), (10, 53), (10, 51), (7, 51), (7, 49),
    (5, 49)
], "c4")

# Pale fibrous inside of the now-empty rind pocket.
output.poly([
    (7, 38), (10, 35), (13, 35), (13, 33), (17, 31), (19, 34),
    (19, 39), (22, 39), (22, 42), (26, 42), (26, 45), (30, 46),
    (28, 48), (23, 48), (23, 50), (11, 50), (11, 49), (8, 49),
    (8, 46), (6, 46), (6, 40)
], "c5")

# Blocky rind folds and shadows, reusing the original palette.
output.rect(7, 39, 3, 7, "c3")
output.rect(8, 37, 4, 3, "c3")
output.rect(10, 35, 4, 2, "c3")
output.rect(10, 43, 2, 5, "c2")
output.rect(12, 47, 10, 2, "c3")
output.rect(17, 32, 2, 4, "c3")
output.rect(18, 36, 2, 6, "c3")
output.rect(20, 40, 3, 3, "c3")
output.rect(22, 43, 4, 3, "c3")
output.rect(26, 46, 4, 2, "c2")
output.rect(12, 38, 4, 2, "c5")
output.rect(14, 41, 5, 4, "c5")
output.rect(19, 45, 3, 2, "c5")
output.set(9, 47, "c2")
output.set(16, 34, "c2")
output.set(24, 47, "c2")

# Preserve the source silhouette exactly: the replacement is confined to
# pixels that were inside the removed flesh segment.
for y in range(30, 54):
    for x in range(4, 34):
        source_pixel = input_canvas.get(x, y)
        if source_pixel in (1, 2):  # white background or black contour
            output.set(x, y, source_pixel)

view(output, scale=8, margin=0, edges="none")
finish(output)
