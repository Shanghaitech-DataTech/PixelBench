# 32x32 chainmail armor sprite
result = new_canvas(32, 32, background=None, name="chainmail-armor")

outline = "#171a22"
deep = "#252b36"
shadow = "#39424f"
steel = "#596675"
light = "#82909c"
glint = "#b3bec5"
black = "#0d1016"

# Dark, compact shirt silhouette.
result.poly([
    (9, 3), (13, 2), (14, 4), (18, 4), (19, 2), (23, 3),
    (29, 8), (30, 11), (27, 15), (25, 14), (25, 27),
    (23, 29), (9, 29), (7, 27), (7, 14), (5, 15), (2, 11),
    (3, 8)
], outline)

# Steel body and sleeves, leaving a one-pixel dark rim.
result.poly([
    (9, 5), (12, 4), (14, 6), (18, 6), (20, 4), (23, 5),
    (27, 8), (28, 11), (26, 13), (24, 12), (23, 10),
    (24, 27), (22, 28), (10, 28), (8, 27), (8, 10),
    (7, 13), (5, 13), (4, 11), (5, 8)
], shadow)

# Sleeve planes and reinforced edges.
result.poly([(5,8),(9,5),(10,8),(8,10),(7,13),(5,13),(4,11)], steel)
result.poly([(23,5),(27,8),(28,11),(26,13),(24,12),(22,8)], steel)
result.line(4, 11, 7, 14, deep)
result.line(28, 11, 25, 14, deep)
result.set(5,9,light).set(6,8,light).set(26,9,light).set(25,8,light)

# Dark collar with a cold metal rim.
result.poly([(12,3),(14,5),(18,5),(20,3),(20,6),(18,8),(14,8),(12,6)], deep)
result.poly([(13,3),(14,5),(18,5),(19,3),(19,6),(17,7),(15,7),(13,6)], black)
result.set(13,4,light).line(14,6,18,6,steel).set(19,4,light)

# Subtle side shadow and hem reinforcement.
result.rect(8, 12, 2, 15, deep)
result.rect(22, 12, 2, 15, deep)
result.line(9, 27, 23, 27, deep)
result.set(10,28,steel).set(12,28,light).set(14,28,steel)
result.set(17,28,light).set(19,28,steel).set(21,28,light)

# Interlocking mail: staggered small rings, clipped to the torso interior.
def ring(cx, cy, bright=False):
    # 3x3 angular ring with a dark hollow and directional steel light.
    result.set(cx, cy-1, light if bright else steel)
    result.set(cx-1, cy, steel)
    result.set(cx+1, cy, deep)
    result.set(cx, cy+1, outline)
    result.set(cx, cy, shadow)
    result.set(cx-1, cy-1, glint if bright else light)
    result.set(cx+1, cy+1, black)

rows = [
    (9, [11,14,17,20]),
    (12, [10,13,16,19,22]),
    (15, [11,14,17,20]),
    (18, [10,13,16,19,22]),
    (21, [11,14,17,20]),
    (24, [10,13,16,19,22]),
]
for y, xs in rows:
    for x in xs:
        ring(x, y, bright=((x + y) % 6 == 2))

# A few sleeve links continue the pattern around the arms.
for x, y in [(6,10),(7,12),(25,10),(25,12)]:
    ring(x, y, bright=(y == 10))

# Crisp seams, specular flecks, and separated bottom links.
result.set(9,7,glint).set(22,6,light)
result.set(11,17,glint).set(17,14,glint).set(20,20,glint)
result.set(13,23,glint).set(19,26,glint)
result.set(8,26,outline).set(24,26,outline)
result.set(11,29,outline).set(15,29,outline).set(19,29,outline).set(23,29,outline)

view(result, scale=16, margin=0)
finish(result)
