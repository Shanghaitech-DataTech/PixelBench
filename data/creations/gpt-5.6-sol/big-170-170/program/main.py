# Remove the central character, reconstruct the vending machine and foreground,
# then shift the scene into a wet thunderstorm.
out = input_canvas.copy(name='output')

# Registered edit palette.
navy = out.color('#11183b', 'machine_shadow')
deep = out.color('#171447', 'machine_deep')
edge = out.color('#25205b', 'machine_edge')
face = out.color('#d9cad1', 'machine_face')
face_hi = out.color('#f0ded9', 'machine_face_hi')
face_sh = out.color('#9e91a2', 'machine_face_shadow')
slot = out.color('#4d304b', 'slot_dark')
red = out.color('#a43d32', 'product_red')
orange = out.color('#ca6845', 'product_orange')
blue = out.color('#6166cf', 'product_blue')
green = out.color('#4f9c75', 'product_green')
pink = out.color('#c1759e', 'product_pink')
black = out.color('#08151d', 'bike_black')
rubber = out.color('#132631', 'rubber')
metal = out.color('#526b70', 'wet_metal')
metal_hi = out.color('#9bb0aa', 'metal_highlight')
redbike = out.color('#6f2934', 'bike_red')
redhi = out.color('#a84d4b', 'bike_red_hi')
road = out.color('#382f38', 'wet_road')
road_dark = out.color('#202b32', 'road_dark')
water = out.color('#4aaac9aa', 'rain_translucent')
water_hi = out.color('#9fe5edbb', 'rain_highlight')
lightning = out.color('#e9f7e8', 'lightning_core')
glow = out.color('#9fc9d788', 'lightning_glow')

# Reconstruct vending machine front where the figure stood.
# Outer cabinet front and left recessed side, covering the full figure silhouette.
out.poly([(75,64),(82,58),(84,60),(84,116),(75,121)], deep)
out.line(76,66,76,117,navy)
out.line(79,63,79,118,edge)
out.rect(80, 57, 37, 60, edge)
out.rect(82, 58, 34, 57, face_sh)
out.rect(84, 59, 31, 54, face)
out.rect(86, 60, 28, 51, face_hi)
out.rect(81, 61, 3, 52, deep)
out.rect(84, 60, 2, 51, '#b28f95')
# Top display header and compartment grid.
out.rect(87, 61, 26, 7, '#f6d6c7')
out.rect(88, 62, 8, 5, '#c97b58')
out.rect(98, 62, 6, 5, green)
out.rect(106, 62, 6, 5, '#6f9a55')
for y in (69, 79, 89):
    out.rect(87, y, 26, 9, '#e7d0cf')
    out.line(87, y, 112, y, '#8f7489')
    out.line(87, y+8, 112, y+8, '#b2919a')
for x in (96, 105):
    out.line(x, 69, x, 97, '#ab8794')
# Product packs, deliberately irregular for pixel detail.
products = [
    (89,71,red),(92,71,orange),(98,71,green),(101,72,blue),(107,70,pink),(109,72,blue),
    (88,81,orange),(91,82,red),(98,81,blue),(101,81,green),(107,81,pink),(109,83,blue),
    (88,91,green),(91,91,orange),(98,90,red),(101,92,pink),(107,90,blue),(110,92,pink)]
for x,y,col in products:
    out.rect(x,y,3,5,col)
    out.set(x+1,y,col)
    out.set(x+2,y+4,face_hi)
# Lower controls and retrieval hatch.
out.rect(87, 99, 26, 12, '#d7c2c5')
out.rect(89, 101, 14, 4, slot)
out.rect(90, 102, 11, 2, '#281d2d')
out.rect(105, 100, 7, 8, '#69404c')
out.rect(106, 101, 5, 3, red)
out.set(109,106,'#f0a37e')
out.rect(85, 112, 30, 5, deep)

# Restore the cabinet's dark lower panel behind the motorcycle.
out.poly([(80,114),(116,114),(116,146),(79,146)], deep)
out.line(82,116,82,143,edge)
out.rect(108,119,6,4,'#30415b')
out.set(110,120,'#71888a')
out.set(111,119,'#71888a')

# Reconstruct motorcycle sections hidden by the figure.
# Rear/top tank and saddle.
out.poly([(54,117),(60,113),(69,114),(76,119),(72,124),(61,126),(55,122)], black)
out.poly([(55,116),(63,114),(72,116),(76,119),(69,122),(60,122)], redbike)
out.line(58,116,70,117,redhi)
out.line(61,123,75,121,'#321f2a')
# Main frame and engine block.
out.poly([(61,124),(77,116),(96,116),(103,124),(91,131),(77,139),(66,136)], black)
out.line(69,131,92,118,metal)
out.line(75,137,99,123,'#6b7778')
out.line(80,125,103,128,metal_hi)
out.poly([(88,124),(101,124),(107,132),(99,139),(89,135)], '#6d6764')
out.rect(93,127,10,7,'#a38d79')
out.line(94,128,101,133,'#d0b19a')
out.line(68,126,87,139,deep)
# Front fork and wheel attachment.
out.line(94,118,109,139,metal)
out.line(97,117,112,139,'#70858a')
out.circle(101,147,14,rubber,fill=False)
out.circle(101,147,10,'#243b43',fill=False)
out.circle(101,147,3,metal)
for x,y in [(101,137),(108,140),(111,147),(107,154),(101,157),(94,154),(91,147),(94,140)]:
    out.line(101,147,x,y,'#60777b')
# Seat/front fairing and cable details.
out.poly([(72,118),(82,114),(98,113),(101,117),(91,121),(77,124)], black)
out.line(80,117,96,114,'#55707a')
out.line(75,121,92,119,'#aa3b3f')
out.line(94,113,102,109,metal)
out.line(101,109,105,113,black)
out.line(101,111,108,110,metal_hi)

# Wet roadway over the bottom strip, preserving silhouettes while adding reflections.
out.rect(0, 151, 170, 19, road)
# Broad irregular asphalt bands avoid a regular texture while retaining pooled darkness.
out.poly([(0,151),(34,152),(55,155),(83,153),(112,156),(141,152),(169,154),(169,161),(0,160)], road_dark)
out.line(0,152,25,152,'#4b3a42')
out.line(122,154,160,154,'#4b3a42')
# Repaint wheel portions over the road.
out.circle(56,148,14,rubber,fill=False)
out.circle(56,148,10,'#263c43',fill=False)
out.circle(56,148,3,metal)
out.circle(101,147,14,rubber,fill=False)
out.circle(101,147,10,'#263c43',fill=False)
out.circle(101,147,3,metal)
for cx,cy in [(56,148),(101,147)]:
    for x,y in [(cx,cy-10),(cx+7,cy-7),(cx+10,cy),(cx+7,cy+7),(cx,cy+10),(cx-7,cy+7),(cx-10,cy),(cx-7,cy-7)]:
        out.line(cx,cy,x,y,'#566e73')
# Frame passing between the wheels.
out.line(57,138,78,142,black)
out.line(62,134,91,146,metal)
out.line(69,137,96,151,black)
# Puddles and reflected machine/neon colors.
out.rect(0,162,170,8,'#173d4b')
out.dither(0,160,170,10,['#1d5365','#314456'],pattern='checker')
out.poly([(5,164),(26,163),(40,165),(34,168),(8,168)],'#2e849a')
out.poly([(132,163),(156,162),(168,165),(160,168),(136,167)],'#2b8ca8')
out.rect(82,160,4,8,'#443981')
out.rect(87,162,2,6,'#725eaa')
out.rect(105,159,3,9,'#5e577c')
out.line(38,158,66,158,'#7895a0')
out.line(42,159,59,159,'#b1c8c8')
out.line(92,156,113,156,'#4e7985')

# Lightning in the open sky, behind the rain but visibly illuminating clouds.
out.line(146,10,140,20,glow)
out.line(140,20,144,20,glow)
out.line(144,20,135,33,glow)
out.line(135,33,140,32,glow)
out.line(140,32,130,49,glow)
out.line(145,10,139,20,lightning)
out.line(139,20,142,20,lightning)
out.line(142,20,133,33,lightning)
out.line(133,33,137,32,lightning)
out.line(137,32,128,49,lightning)
out.set(145,9,lightning)

# Semi-transparent wind-driven rain across the scene.
rain = [(8,8,12,15),(25,2,28,9),(43,14,47,22),(60,5,64,13),(78,18,82,27),
        (96,3,100,11),(116,15,120,24),(132,2,136,10),(154,20,158,29),(164,3,168,12),
        (2,34,6,42),(20,27,24,36),(37,39,41,47),(55,29,59,38),(70,45,74,54),
        (90,31,94,40),(108,43,112,52),(124,34,128,43),(148,43,152,52),(163,36,167,45),
        (10,61,14,70),(29,53,33,62),(47,66,51,75),(64,58,68,67),(83,69,87,78),
        (101,57,105,66),(121,72,125,81),(139,60,143,69),(158,75,162,84),
        (4,90,8,99),(23,81,27,90),(41,94,45,103),(59,85,63,94),(76,99,80,108),
        (96,87,100,96),(115,101,119,110),(135,89,139,98),(153,105,157,114),(166,91,169,98),
        (14,119,18,128),(34,110,38,119),(51,126,55,135),(72,113,76,122),(91,132,95,141),
        (111,118,115,127),(130,136,134,145),(149,121,153,130),(164,139,168,148)]
for x0,y0,x1,y1 in rain:
    out.line(x0,y0,x1,y1,water)
    out.set(x1,y1,water_hi)
# Clinging droplets on machine, bike and ground.
for x,y in [(84,62),(113,67),(87,79),(115,91),(82,107),(113,121),(92,116),(103,128),
            (55,120),(65,135),(88,141),(105,147),(18,154),(30,160),(48,157),(75,163),
            (117,158),(143,155),(158,164)]:
    out.set(x,y,water_hi)
    out.set(x,y+1,water)
# Small splash crowns and runoff.
for x,y in [(18,150),(43,154),(121,151),(148,158)]:
    out.line(x-2,y,x,y-2,water)
    out.line(x,y-2,x+2,y,water)
    out.set(x,y,water_hi)

view(out, scale=3, margin=0)
finish(out)
