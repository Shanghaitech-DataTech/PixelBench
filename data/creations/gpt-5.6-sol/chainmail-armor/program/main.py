# 32x32 chainmail armor sprite
result = new_canvas(32, 32, background=None, name="chainmail-armor")

outline = "#11171d"
deep = "#202a31"
shadow = "#303c44"
steel = "#485861"
mid = "#657780"
light = "#91a1a6"
glint = "#c3ced0"

# Dark, stepped hauberk silhouette with short sleeves.
result.poly([
    (8, 4), (12, 4), (13, 6), (18, 6), (19, 4), (23, 4),
    (29, 9), (29, 12), (26, 17), (24, 16), (24, 28),
    (21, 31), (17, 29), (15, 31), (10, 31), (7, 28),
    (7, 16), (5, 17), (2, 12), (2, 9)
], outline)

# Main metal fields, preserving a one-pixel dark border.
result.poly([(9,5),(12,5),(14,8),(17,8),(19,5),(22,5),(27,9),(27,12),
             (25,15),(23,13),(23,27),(20,29),(17,27),(15,29),(11,29),
             (8,27),(8,13),(6,15),(4,11),(4,9)], steel)
# Shadow masses beneath arms and down the sides.
result.poly([(4,11),(8,12),(8,17),(6,16)], shadow)
result.poly([(23,11),(27,11),(25,15),(23,14)], shadow)
result.rect(8,15,2,12,shadow)
result.rect(21,15,2,12,shadow)

# Open neck and its heavy linked collar.
result.rect(13,4,6,2,None)
result.poly([(12,5),(13,5),(14,7),(17,7),(18,5),(19,5),(18,8),(17,9),
             (14,9),(12,7)], outline)
result.line(13,6,14,8,light)
result.line(18,6,17,8,mid)
result.line(15,9,16,9,glint)

# Interlocking ring: dark lower loop, bright upper arc, and a hollow center.
def ring(cx, cy, bright=True):
    # 5x4 ring, deliberately asymmetric to imply an over-under weave.
    result.set(cx-2, cy, deep)
    result.set(cx+2, cy, deep)
    result.set(cx-1, cy+1, deep)
    result.set(cx,   cy+1, deep)
    result.set(cx+1, cy+1, deep)
    result.set(cx-1, cy-1, light if bright else mid)
    result.set(cx,   cy-1, glint if bright else light)
    result.set(cx+1, cy-1, mid)
    result.set(cx-2, cy-1, mid)
    result.set(cx+2, cy-1, shadow)
    result.set(cx, cy, shadow)

# Staggered rows across the torso. Side links disappear under the edge shadows.
for y, xs in [
    (11, [10,15,20]),
    (14, [12,17]),
    (17, [10,15,20]),
    (20, [12,17]),
    (23, [10,15,20]),
    (26, [12,17]),
]:
    for i, x in enumerate(xs):
        ring(x, y, bright=((x + y) % 3 != 0))

# Horizontal overlap pins visually connect neighboring loops.
for y in (11,17,23):
    result.set(12,y-1,mid); result.set(13,y-1,deep)
    result.set(17,y-1,mid); result.set(18,y-1,deep)
for y in (14,20,26):
    result.set(14,y-1,mid); result.set(15,y-1,deep)

# Smaller sleeve links following the angled arms.
for cx, cy in [(6,10),(7,13),(25,10),(24,13)]:
    result.set(cx-1,cy-1,light)
    result.set(cx,cy-1,mid)
    result.set(cx-1,cy,deep)
    result.set(cx,cy,shadow)

# Reinforced sleeve cuffs and bottom hem.
result.line(3,12,6,16,deep)
result.set(4,12,light); result.set(5,14,mid)
result.line(28,12,25,16,deep)
result.set(27,12,mid); result.set(26,14,light)
result.line(9,28,14,30,deep)
result.line(17,28,21,30,deep)
result.set(10,28,light); result.set(12,29,mid)
result.set(19,29,light); result.set(21,28,mid)

# A few hard specular pixels keep the metal crisp.
for x,y in [(9,7),(21,7),(10,10),(20,16),(11,22),(18,25)]:
    result.set(x,y,glint)

view(result, scale=16, margin=1, edges="all")
finish(result)
