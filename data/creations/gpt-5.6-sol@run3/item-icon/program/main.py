from pixelbench_api import *

# Ancient golden compass inventory icon, 32x32, transparent background.
c = new_canvas(32, 32, background=None, name="ancient_golden_compass")

OUT = "#17131c"
EDGE = "#2b1b20"
DEEP = "#51301e"
BRONZE = "#865126"
GOLD_D = "#b8752d"
GOLD = "#d99a3b"
GOLD_L = "#f2c55c"
GLINT = "#ffe58a"
BLUE_D = "#123c65"
BLUE = "#176a9e"
CYAN = "#28a9cf"
ICE = "#76d9e5"
WHITE = "#bff5ee"

# Heavy cardinal-point silhouette and small diagonal lugs.
c.poly([(11,9),(13,6),(13,3),(15,0),(16,0),(18,3),(18,6),(20,9)], OUT)
c.poly([(11,23),(13,26),(13,29),(15,31),(16,31),(18,29),(18,26),(20,23)], OUT)
c.poly([(9,11),(6,13),(3,13),(0,15),(0,16),(3,18),(6,18),(9,20)], OUT)
c.poly([(23,11),(26,13),(29,13),(31,15),(31,16),(29,18),(26,18),(23,20)], OUT)
for pts in [
    [(8,8),(7,5),(10,7),(11,9)], [(23,8),(24,5),(21,7),(20,9)],
    [(8,23),(7,26),(10,24),(11,22)], [(23,23),(24,26),(21,24),(20,22)]
]:
    c.poly(pts, OUT)

# Inlaid gold on the four main points.
c.poly([(13,9),(15,6),(15,2),(16,1),(17,4),(17,7),(19,10)], GOLD_D)
c.poly([(13,23),(15,26),(15,29),(16,30),(17,27),(17,25),(19,22)], BRONZE)
c.poly([(9,13),(6,15),(2,15),(1,16),(4,17),(7,17),(10,19)], GOLD_D)
c.poly([(23,13),(26,15),(30,15),(31,16),(27,17),(25,17),(22,19)], BRONZE)
c.set(15,2,GOLD_L).set(16,2,GOLD).set(2,15,GOLD_L).set(29,15,GOLD)

# Stepped circular case. Rings are centered between pixels for true symmetry.
for y in range(32):
    for x in range(32):
        dx, dy = x - 15.5, y - 15.5
        d2 = dx*dx + dy*dy
        if d2 <= 13.2*13.2:
            c.set(x, y, OUT)
        if d2 <= 11.35*11.35:
            # Warm directional shading: light upper-left, aged bronze lower-right.
            if x + y <= 24:
                col = GOLD_L
            elif x + y >= 39:
                col = BRONZE
            else:
                col = GOLD
            c.set(x, y, col)
        if d2 <= 8.8*8.8:
            c.set(x, y, EDGE)
        if d2 <= 7.65*7.65:
            c.set(x, y, DEEP)

# Ring bevel glints and old dark notches.
c.line(8,8,12,6,GLINT).line(6,12,7,9,GOLD_L)
c.line(20,25,24,21,DEEP).line(25,18,25,21,EDGE)
c.set(5,14,GLINT).set(5,15,GOLD_L).set(6,10,GLINT)
c.set(10,6,GLINT).set(21,7,GOLD).set(24,10,GOLD_D)
c.set(26,15,DEEP).set(25,16,BRONZE).set(23,23,EDGE)
c.set(7,20,GOLD_D).set(9,23,BRONZE).set(15,26,EDGE)
# Tiny engraved ticks around the inner rim.
for x,y in [(15,5),(16,5),(26,15),(26,16),(15,26),(16,26),(5,15),(5,16),
            (8,9),(23,8),(23,23),(8,22)]:
    c.set(x,y,EDGE)

# Eight-point compass rose beneath the crystal, with a dark keyline.
rose = [(15,7),(18,12),(23,9),(20,14),(25,15),(20,18),
        (23,23),(18,20),(16,25),(13,20),(9,23),(11,18),
        (7,16),(11,13),(9,9),(14,12)]
c.poly(rose, OUT)
# Gold/bronze directional needles.
c.poly([(15,8),(16,15),(12,13)], GOLD_L)
c.poly([(16,15),(24,15),(19,18)], GOLD)
c.poly([(16,16),(16,24),(13,19)], BRONZE)
c.poly([(15,16),(8,16),(12,13)], GOLD_D)
# Smaller diagonal rose facets.
c.poly([(14,14),(10,10),(15,13)], GOLD)
c.poly([(17,14),(22,10),(18,15)], GOLD_D)
c.poly([(18,17),(22,22),(17,19)], BRONZE)
c.poly([(14,18),(10,22),(13,17)], GOLD_D)

# Blue crystal: thick dark mount and angular top-down gem.
c.poly([(13,10),(18,10),(21,13),(21,18),(18,21),(13,21),(10,18),(10,13)], OUT)
c.poly([(14,11),(18,11),(20,14),(20,18),(17,20),(13,20),(11,17),(11,14)], BLUE_D)
# Faceted crystal faces.
c.poly([(14,11),(18,11),(16,15),(11,14)], CYAN)
c.poly([(18,11),(20,14),(16,15)], ICE)
c.poly([(20,14),(20,18),(16,16),(16,15)], BLUE)
c.poly([(20,18),(17,20),(16,16)], BLUE_D)
c.poly([(17,20),(13,20),(16,16)], BLUE)
c.poly([(13,20),(11,17),(16,16)], "#18547f")
c.poly([(11,17),(11,14),(16,15),(16,16)], "#208db5")
# Bright crystalline core and single hard specular pixel.
c.poly([(16,13),(18,15),(16,18),(14,16)], CYAN)
c.set(15,13,WHITE).set(14,14,ICE).set(17,14,ICE).set(15,15,"#4fc9dc")

# A few age chips on the case, kept away from the crystal focal point.
c.set(12,5,OUT).set(20,6,EDGE).set(25,13,OUT)
c.set(24,20,OUT).set(11,25,EDGE).set(6,18,EDGE)

result = c
view(result, scale=16, margin=0)
finish(result)
