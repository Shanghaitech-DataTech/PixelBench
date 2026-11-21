from pixelbench_api import new_canvas, view, finish

# 32x32 chainmail hauberk on transparency.
c = new_canvas(32, 32, background=None, name="chainmail-armor")

outline = "#171a20"
deep = "#252b33"
shadow = "#39434d"
steel = "#667581"
light = "#9aabb3"
glint = "#c8d3d5"

# Strong, stepped silhouette: broad shoulders, short sleeves, tapered body.
c.poly([
    (11, 3), (21, 3), (23, 5), (27, 6), (27, 8), (30, 10),
    (29, 16), (26, 16), (25, 14), (25, 27),
    (23, 27), (22, 29), (19, 28), (16, 30), (13, 28),
    (10, 29), (9, 27), (7, 27), (7, 14), (6, 16),
    (3, 16), (2, 10), (5, 8), (5, 6), (9, 5)
], outline)

# Mail field, leaving a one-pixel dark rim.
c.poly([
    (11, 5), (21, 5), (22, 6), (25, 7), (25, 9), (28, 11),
    (27, 14), (25, 14), (23, 11), (23, 26),
    (21, 26), (20, 27), (19, 26), (16, 28), (13, 26),
    (11, 27), (10, 26), (9, 26), (9, 11), (7, 14),
    (5, 14), (4, 11), (7, 9), (7, 7), (10, 6)
], shadow)

# Sleeve planes and lower-body depth.
c.poly([(4,10),(7,8),(9,9),(9,15),(7,13),(6,15),(5,14)], deep)
c.poly([(23,9),(25,8),(28,11),(27,14),(25,13),(23,15)], deep)
c.rect(10, 23, 13, 3, deep)
c.set(11,26, deep); c.set(14,26, deep); c.set(18,26, deep); c.set(21,26, deep)

# Raised collar and transparent neck opening.
c.poly([(10,5),(12,3),(20,3),(22,5),(21,8),(19,9),(13,9),(11,8)], deep)
c.poly([(12,4),(14,3),(18,3),(20,4),(19,7),(18,8),(14,8),(13,7)], outline)
c.poly([(14,4),(18,4),(18,6),(17,7),(15,7),(14,6)], None)
c.set(13,4, steel); c.set(19,4, steel)

# Shoulder catches and edge highlights.
c.line(8,7,10,6,steel); c.set(7,8, light)
c.line(22,6,24,8,steel); c.set(25,9, light)
c.set(4,11, steel); c.set(27,11, steel)
c.set(8,16, steel); c.set(23,16, steel)

# Interlocking ring rows. Dark centres keep every link individually legible.
def ring(x, y, bright=False):
    hi = glint if bright else light
    c.set(x, y, hi)
    c.set(x + 1, y, steel)
    c.set(x - 1, y + 1, steel)
    c.set(x, y + 1, deep)
    c.set(x + 1, y + 1, outline)
    c.set(x + 2, y + 1, steel)
    c.set(x - 1, y + 2, deep)
    c.set(x, y + 2, outline)
    c.set(x + 1, y + 2, deep)
    c.set(x + 2, y + 2, outline)
    c.set(x, y + 3, deep)
    c.set(x + 1, y + 3, deep)

# Widely spaced, offset rows suggest links passing over and under each other.
for x, y, bright in [
    (11,9,True),(16,9,False),(21,9,True),
    (9,13,False),(14,13,True),(19,13,False),
    (11,17,True),(16,17,False),(21,17,True),
    (9,21,False),(14,21,False),(19,21,True),
    (12,24,False),(17,24,False)
]:
    ring(x, y, bright)

# Small sleeve rings, oriented to follow the shoulders.
c.set(6,10,light); c.set(5,11,deep); c.set(7,11,outline); c.set(6,12,outline)
c.set(25,10,light); c.set(24,11,deep); c.set(26,11,outline); c.set(25,12,outline)

# Restore a crisp stepped hem and a few metallic pinpricks.
c.set(9,26, outline); c.set(12,27, outline); c.set(15,27, outline)
c.set(17,27, outline); c.set(20,27, outline); c.set(22,26, outline)
c.set(12,10, glint); c.set(20,13, glint); c.set(16,19, glint)

view(c, scale=14, margin=1, edges="all")
finish(c)
