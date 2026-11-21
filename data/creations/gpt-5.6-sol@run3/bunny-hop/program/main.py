# Bunny-hop: preserve the supplied frame, then draw a matching airborne pose.
W, H = 40, 32
f1 = new_canvas(W, H, name="bunny_rest")
f1.blit(input_canvas, 2, 4)

f2 = new_canvas(W, H, name="bunny_hop")
# Existing input palette: 1 outline, 2 light gray, 3 mid gray, 4 white,
# 5 pale ear, 6 deep ear, 7 gold.
out, light, mid, white, ear, ear_dark, gold = 1, 2, 3, 4, 5, 6, 7

# Airborne silhouette: tail, swept ears, long body, head, and extended limbs.
f2.poly([(3,14),(5,12),(8,12),(10,14),(10,18),(8,20),(5,19),(3,17)], out)
f2.poly([(22,12),(18,10),(14,7),(10,5),(9,3),(11,2),(15,4),(20,7),(25,10)], out)
f2.poly([(25,11),(21,8),(18,4),(18,1),(20,0),(22,3),(23,7),(28,11)], out)
f2.poly([(7,14),(11,11),(18,10),(25,12),(30,16),(29,21),(24,24),(15,25),(8,22),(6,18)], out)
f2.poly([(24,10),(28,8),(33,9),(36,12),(36,17),(33,20),(28,20),(24,17)], out)
# Hind legs trail backward/downward.
f2.poly([(16,21),(15,25),(12,28),(5,29),(2,27),(3,25),(10,24),(12,20)], out)
f2.poly([(21,22),(20,26),(17,29),(11,30),(8,28),(10,26),(16,24),(17,21)], out)
# Forelegs reach forward to sell the leap.
f2.poly([(29,17),(33,18),(36,21),(39,21),(39,24),(35,25),(31,22),(27,21)], out)
f2.poly([(28,19),(31,22),(34,25),(38,26),(38,29),(34,29),(30,26),(25,23)], out)

# White interior masses, leaving the charcoal silhouette as a crisp outline.
f2.poly([(5,14),(7,13),(9,14),(9,17),(7,19),(5,18),(4,16)], light)
f2.poly([(9,15),(12,12),(18,11),(24,13),(28,16),(28,20),(23,23),(16,24),(10,21),(8,18)], white)
f2.poly([(25,11),(28,9),(32,10),(35,12),(35,16),(32,19),(28,19),(25,16)], white)
# Swept ear interiors.
f2.poly([(21,11),(17,9),(13,6),(11,4),(12,4),(16,6),(20,9),(24,11)], white)
f2.poly([(19,2),(20,2),(21,5),(22,9),(25,11),(23,12),(21,8),(19,5)], white)
f2.poly([(17,9),(14,7),(12,5),(13,5),(16,7),(20,10)], ear)
f2.poly([(19,3),(20,4),(21,8),(23,10),(22,10),(20,7)], ear_dark)

# Trailing hind feet and reaching forepaws.
f2.poly([(14,22),(13,25),(11,27),(5,28),(3,27),(4,26),(10,25),(11,22)], white)
f2.poly([(19,23),(18,26),(16,28),(11,29),(9,28),(11,27),(16,25),(17,22)], light)
f2.poly([(29,19),(32,19),(35,22),(38,22),(38,23),(35,24),(31,21),(27,20)], white)
f2.poly([(27,21),(30,23),(33,26),(37,27),(37,28),(34,28),(30,25),(25,23)], white)

# Gray modeling follows the original sprite's lower/right-side shading.
f2.poly([(9,18),(12,20),(17,21),(23,20),(28,18),(28,21),(23,24),(16,24),(10,21)], light)
f2.poly([(18,22),(23,21),(27,19),(28,21),(24,23),(20,24)], mid)
f2.poly([(25,16),(28,17),(29,19),(27,20),(24,18)], light)
f2.rect(32,17,2,2,light)
f2.set(33,18,mid)
f2.rect(12,24,3,2,mid)
f2.rect(5,27,5,1,light)

# Face and small identifying details.
f2.rect(31,11,2,2,out)
f2.set(31,11,light)
f2.set(35,15,gold)
f2.set(35,16,gold)
f2.set(34,17,mid)
f2.set(27,10,light)
f2.set(24,12,mid)

# A few stepped outline pixels sharpen joints and paws.
f2.set(8,22,out)
f2.set(15,25,out)
f2.set(24,24,out)
f2.set(31,22,out)
f2.set(38,25,out)

view(f1, scale=12, margin=1, edges="all")
view(f2, scale=12, margin=1, edges="all")
finish([f1, f2])
