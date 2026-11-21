# Cozy 64x64 tavern interior in a restrained nighttime palette.
result = new_canvas(64, 64, background="#17131a", name="tavern-interior")

# Palette
ink = "#17131a"
deep = "#211820"
wall = "#3a2524"
wall2 = "#49302a"
beam = "#2a1c1c"
wood_dark = "#38201b"
wood = "#653925"
wood_mid = "#85502e"
wood_light = "#ad713d"
edge = "#261719"
metal = "#69584e"
smoke = "#6b5650"
cream = "#f1cc72"
glow = "#d9963d"
hot = "#ffe69a"
red = "#8f3f35"
green = "#496044"
teal = "#376064"
blue = "#41506a"
glass = "#9bb0a2"

# Back wall: uneven wood panels and shadowed ceiling.
result.rect(0, 0, 64, 64, wall)
result.rect(0, 0, 64, 8, deep)
result.rect(0, 8, 64, 3, beam)
result.rect(3, 11, 2, 31, wall2)
result.rect(18, 11, 2, 31, beam)
result.rect(34, 11, 2, 31, beam)
result.rect(51, 11, 2, 31, beam)
for x, y, w in [(6,15,10),(22,13,10),(38,16,11),(54,14,8),(6,31,10),(22,34,10),(38,30,11),(54,33,8)]:
    result.line(x, y, x+w, y, "#513029")
# Nail and grain pixels.
for x, y in [(4,18),(4,36),(19,23),(19,39),(35,19),(35,35),(52,21),(52,38),(12,25),(28,28),(44,24),(59,29)]:
    result.set(x,y,"#21181b")

# Heavy shelf behind bar.
result.rect(6, 18, 52, 3, edge)
result.rect(7, 17, 50, 2, wood_mid)
result.rect(9, 20, 2, 14, wood_dark)
result.rect(54, 20, 2, 14, wood_dark)
result.rect(7, 32, 50, 3, edge)
result.rect(8, 32, 48, 1, wood_light)

# Bottles: outlined silhouettes with tiny colored highlights.
def bottle(x, base, h, color, width=4):
    neck_x = x + (width-2)//2
    result.rect(neck_x, base-h, 2, 3, edge)
    result.rect(neck_x, base-h+1, 1, 1, color)
    result.rect(x, base-h+3, width, h-3, edge)
    result.rect(x+1, base-h+4, max(1,width-2), h-5, color)
    result.set(x+1, base-h+4, "#c1a76d")

bottle(11,32,10,green,4)
bottle(16,32,8,red,4)
bottle(22,32,12,teal,4)
bottle(28,32,9,"#b06b32",3)
bottle(33,32,11,blue,4)
bottle(39,32,8,"#6d783f",4)
bottle(45,32,12,red,4)
bottle(50,32,9,teal,3)
# Shelf brackets.
result.poly([(8,35),(13,35),(8,40)], edge)
result.poly([(56,35),(51,35),(56,40)], edge)

# Ceiling cords and hanging lamps.
for x, length in [(15,8),(45,10)]:
    result.rect(x, 0, 2, length, edge)
# Pixel halos behind shades.
result.rect(10,7,12,1,"#67452d")
result.rect(8,8,16,3,"#79502c")
result.rect(39,9,14,1,"#67452d")
result.rect(37,10,18,3,"#79502c")
# Shades with dark stepped outlines.
result.poly([(11,7),(20,7),(24,13),(7,13)], edge)
result.poly([(12,8),(19,8),(22,12),(9,12)], glow)
result.rect(10,12,11,2,cream)
result.rect(13,13,5,2,hot)
result.poly([(40,9),(49,9),(54,15),(36,15)], edge)
result.poly([(41,10),(48,10),(51,14),(39,14)], glow)
result.rect(39,14,12,2,cream)
result.rect(42,15,6,2,hot)

# Warm pools of light on the wall, pixel-dithered at edges.
for x,y in [(8,16),(10,18),(22,16),(25,18),(37,18),(52,18),(39,20),(50,21),(12,29),(25,30),(42,29)]:
    result.set(x,y,"#6c4530")

# Back counter ledge and scattered glasses.
result.rect(0, 38, 64, 3, edge)
result.rect(0, 37, 64, 2, wood_light)
result.rect(0, 39, 64, 3, wood_mid)
# Mugs/glasses behind the main bar.
result.rect(13,33,5,1,glass)
result.rect(14,34,3,3,ink)
result.rect(15,34,2,2,"#70847c")
result.set(18,35,glass)
result.rect(37,34,4,1,glass)
result.rect(38,35,2,2,"#70847c")
result.set(41,36,glass)

# Main bar front, strong perspective and thick outline.
result.poly([(0,40),(63,40),(63,56),(6,56),(0,52)], edge)
result.poly([(1,43),(63,43),(63,53),(7,53),(1,50)], wood)
result.rect(0,40,64,4,edge)
result.rect(0,40,64,2,wood_light)
result.rect(1,42,62,1,"#c18145")
# Front panels.
for x in [8,25,42,58]:
    result.rect(x,44,2,10,wood_dark)
result.rect(6,53,58,3,edge)
result.line(10,47,23,47,"#8c5430")
result.line(28,50,40,50,"#4d2c21")
result.line(45,46,56,46,"#8c5430")

# Foreground floorboards.
result.rect(0,56,64,8,"#251a1d")
result.line(0,59,63,59,"#352321")
result.line(14,56,11,63,"#402720")
result.line(39,56,41,63,"#402720")
result.line(57,56,62,63,"#402720")

# Bar stools: stepped round seats and splayed legs.
def stool(cx, seat_y):
    result.rect(cx-5,seat_y,10,2,edge)
    result.rect(cx-4,seat_y-1,8,2,wood_mid)
    result.rect(cx-3,seat_y,6,1,wood_light)
    result.rect(cx-2,seat_y+2,4,2,edge)
    result.line(cx-2,seat_y+3,cx-5,63,edge)
    result.line(cx+1,seat_y+3,cx+5,63,edge)
    result.line(cx-3,seat_y+10,cx+3,seat_y+10,wood_mid)
stool(17,50)
stool(47,51)

# Barrel at right foreground: outlined staves and metal hoops.
result.rect(54,45,9,2,edge)
result.rect(52,47,12,13,edge)
result.rect(53,47,10,13,wood_mid)
result.rect(54,46,8,2,wood_light)
result.rect(53,50,10,2,metal)
result.rect(53,57,10,2,metal)
result.line(56,48,56,59,wood_dark)
result.line(60,48,60,59,wood_dark)
result.set(62,53,"#c18348")

# Small barrel tucked left.
result.rect(0,49,7,11,edge)
result.rect(0,50,6,9,wood)
result.rect(0,51,7,2,metal)
result.rect(0,57,7,2,metal)
result.line(3,50,3,59,wood_dark)

# Tankard on the bar and bright glass glints.
result.rect(27,35,6,2,edge)
result.rect(28,36,4,4,glass)
result.rect(29,37,3,3,"#546961")
result.rect(32,37,3,3,edge)
result.set(33,38,glass)
result.set(28,36,hot)
result.rect(6,37,4,1,"#b7c1a6")
result.set(7,36,hot)

# Smoky atmosphere: sparse, blocky wisps kept behind focal foreground details.
result.path("M2 25 C7 22 9 25 14 22 S23 22 27 19", smoke, fill=False)
result.path("M31 27 C36 24 38 27 43 24 S52 24 60 20", "#73574c", fill=False)
result.path("M3 29 C8 27 12 30 17 27", "#57413d", fill=False)

# A few crisp edge highlights unify the warm lighting.
for x,y in [(2,41),(20,41),(35,41),(51,41),(9,18),(31,18),(55,18),(15,51),(46,52),(55,47)]:
    result.set(x,y,"#d4934d")

view(result, scale=8, margin=0)
finish(result)
