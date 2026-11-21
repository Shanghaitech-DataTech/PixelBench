from pixelbench_api import *

# Cozy tavern interior, 64x64, built from a restrained warm pixel palette.
c = new_canvas(64, 64, background="#120e12", name="tavern-interior")

# Palette
ink = "#171016"
deep = "#24151a"
wall = "#3a2525"
wall2 = "#4b3029"
beam = "#2b1718"
wood_dark = "#3a1d18"
wood = "#633522"
wood_mid = "#844b2a"
wood_light = "#aa6937"
edge = "#120c10"
amber = "#d88a35"
gold = "#f1bd55"
light = "#ffe18a"
cream = "#fff0ad"
red = "#8f3030"
red_hi = "#c75237"
green = "#38513a"
green_hi = "#64804b"
blue = "#334957"
blue_hi = "#66808a"
glass = "#b4b89a"
smoke = "#75605a88"
metal = "#827773"

# Back wall, uneven plaster blocks and warm lamp glow zones.
c.rect(2, 2, 60, 43, wall)
c.rect(3, 3, 58, 42, wall2)
c.dither(4, 4, 56, 39, [wall, wall2], pattern="bayer4")
# muted masonry strokes
for x,y,w in [(5,9,10),(19,7,8),(34,10,10),(48,7,9),(7,25,8),(25,22,9),(44,25,12),(5,38,12),(22,35,8),(47,37,10)]:
    c.rect(x,y,w,1,wall)

# Heavy timber frame and ceiling.
c.rect(0,0,64,4,edge)
c.rect(0,4,64,3,beam)
c.rect(1,6,3,41,edge)
c.rect(60,6,3,41,edge)
c.rect(3,29,58,3,edge)
c.rect(4,29,56,1,wood_mid)
# ceiling rafters
c.poly([(5,6),(8,6),(22,29),(18,29)], beam)
c.poly([(59,6),(56,6),(43,29),(47,29)], beam)
c.rect(30,6,4,23,beam)
c.rect(31,6,1,23,wood_mid)

# Shelves behind bar.
for y in (17,28,39):
    c.rect(7,y,49,2,edge)
    c.rect(8,y,47,1,wood_light)
c.rect(7,16,2,24,wood_dark)
c.rect(54,16,2,24,wood_dark)

# Bottles helper with dark outline, neck, colored body and highlight.
def bottle(x, base, col, hi, h=8, wide=4):
    c.rect(x+1, base-h, wide-2, 2, edge)
    c.rect(x, base-h+2, wide, h-2, edge)
    c.rect(x+1, base-h+3, wide-2, h-4, col)
    c.set(x+1, base-h+3, hi)
    c.rect(x+1, base-2, wide-2, 1, hi)

# upper shelf bottles
bottle(10,17,green,green_hi,8,4)
bottle(16,17,red,red_hi,6,4)
bottle(23,17,blue,blue_hi,9,4)
bottle(38,17,red,amber,7,4)
bottle(45,17,green,green_hi,9,4)
bottle(50,17,blue,blue_hi,6,4)
# middle shelf bottles and squat decanters
bottle(10,28,red,red_hi,7,4)
bottle(16,28,green,green_hi,9,4)
bottle(22,28,blue,blue_hi,6,4)
bottle(35,28,green,green_hi,7,4)
bottle(41,28,red,red_hi,9,4)
bottle(49,28,blue,blue_hi,7,4)
# labels
for x,y in [(11,14),(24,14),(17,25),(36,25),(42,25),(50,25)]: c.set(x,y,gold)

# Hanging lamps: cords, dark caps, glowing stepped shades.
for cx in (15,48):
    c.rect(cx,3,1,7,edge)
    c.rect(cx-2,9,5,2,edge)
    c.rect(cx-4,11,9,2,amber)
    c.rect(cx-3,10,7,2,gold)
    c.rect(cx-2,11,5,3,light)
    c.rect(cx-1,12,3,2,cream)
    c.rect(cx-4,14,9,1,edge)
# tiny glow pixels
for x,y in [(10,12),(20,12),(43,12),(53,12),(12,16),(51,16)]: c.set(x,y,amber)

# Lower shelf details: mugs, glasses, small keg.
for x in (11,16,22):
    c.rect(x,34,3,5,edge)
    c.rect(x+1,34,2,4,metal)
    c.set(x+1,34,glass)
    c.set(x+3,36,metal)
c.rect(37,33,14,6,edge)
c.rect(38,34,12,4,wood_mid)
c.line(38,35,49,35,wood_light)
c.rect(40,33,1,6,metal); c.rect(47,33,1,6,metal)
c.set(50,36,gold)

# Back barrels at sides.
def barrel(x,y,w=10,h=14):
    c.rect(x+2,y,w-4,h,edge)
    c.rect(x+1,y+2,w-2,h-4,edge)
    c.rect(x,y+4,w,h-8,edge)
    c.rect(x+2,y+1,w-4,h-2,wood)
    c.rect(x+1,y+4,w-2,h-8,wood_mid)
    c.rect(x+2,y+5,w-4,h-10,wood_light)
    c.rect(x,y+4,w,2,metal)
    c.rect(x,y+h-6,w,2,metal)
    c.line(x+w//2,y+2,x+w//2,y+h-3,wood_dark)
barrel(3,36,10,14)
barrel(51,35,10,15)

# Main counter, dark outlined, thick top and paneled front.
c.rect(5,42,54,4,edge)
c.rect(7,41,50,2,wood_light)
c.rect(6,43,52,2,wood_mid)
c.rect(8,46,48,15,edge)
c.rect(9,46,46,14,wood)
c.rect(10,47,44,3,wood_mid)
# panel recesses
for x in (11,25,39):
    c.rect(x,51,12,8,wood_dark)
    c.rect(x+1,52,10,6,wood_mid)
    c.rect(x+2,53,8,4,wood)
    c.line(x+2,53,x+9,53,wood_light)
c.rect(7,60,50,3,edge)
c.rect(9,60,46,1,wood_light)

# Countertop glasses, tankard, bottle.
# glasses
for x in (29,34):
    c.rect(x,37,4,5,edge)
    c.rect(x+1,38,2,3,glass)
    c.set(x+2,38,cream)
# tankard
c.rect(19,37,6,5,edge); c.rect(20,38,4,4,gold); c.rect(24,38,3,3,edge); c.set(25,39,amber)
# bottle foreground
bottle(42,42,green,green_hi,10,5)
c.rect(43,38,3,2,gold)

# Foreground floor.
c.rect(0,45,64,19,deep)
# redraw counter over floor (floor should only show around, restore from saved conceptual area)
c.rect(8,46,48,15,edge); c.rect(9,46,46,14,wood)
c.rect(10,47,44,3,wood_mid)
for x in (11,25,39):
    c.rect(x,51,12,8,wood_dark); c.rect(x+1,52,10,6,wood_mid)
    c.rect(x+2,53,8,4,wood); c.line(x+2,53,x+9,53,wood_light)
c.rect(7,60,50,3,edge); c.rect(9,60,46,1,wood_light)
# floorboards outside bar
for x in (3,60): c.line(x,48,x,63,wood_dark)
c.line(0,56,7,56,wood_dark); c.line(56,55,63,55,wood_dark)

# Stools in front, strong silhouettes.
def stool(cx, seat_y):
    c.rect(cx-6,seat_y-1,13,4,edge)
    c.rect(cx-5,seat_y,11,2,wood_mid)
    c.rect(cx-4,seat_y,9,1,wood_light)
    c.rect(cx-4,seat_y+3,3,9,edge)
    c.rect(cx+2,seat_y+3,3,9,edge)
    c.rect(cx-3,seat_y+4,1,7,wood_mid)
    c.rect(cx+3,seat_y+4,1,7,wood_mid)
    c.rect(cx-3,seat_y+8,7,2,edge)
    c.rect(cx-2,seat_y+8,5,1,wood_light)
stool(15,52)
stool(49,52)

# Restore countertop and its objects at visual front edge.
c.rect(5,42,54,4,edge); c.rect(7,41,50,2,wood_light); c.rect(6,43,52,2,wood_mid)
for x in (29,34):
    c.rect(x,37,4,5,edge); c.rect(x+1,38,2,3,glass); c.set(x+2,38,cream)
c.rect(19,37,6,5,edge); c.rect(20,38,4,4,gold); c.rect(24,38,3,3,edge); c.set(25,39,amber)
bottle(42,42,green,green_hi,10,5); c.rect(43,38,3,2,gold)

# Smoky atmosphere as sparse translucent curling clusters.
c.path("M3 34 C8 31 8 27 5 25 C2 23 4 20 8 19", smoke, fill=False)
c.path("M57 33 C52 30 54 27 58 25 C61 23 60 20 56 19", smoke, fill=False)
c.path("M27 34 C24 31 27 29 30 28 C34 27 35 24 32 22", smoke, fill=False)

# A few crisp specular pixels and nail heads.
for x,y in [(8,43),(15,43),(50,43),(56,43),(12,48),(26,48),(40,48),(53,48)]: c.set(x,y,gold)
for x,y in [(10,18),(55,18),(8,30),(56,30),(9,61),(54,61)]: c.set(x,y,metal)

view(c, scale=8, margin=0)
finish(c)
