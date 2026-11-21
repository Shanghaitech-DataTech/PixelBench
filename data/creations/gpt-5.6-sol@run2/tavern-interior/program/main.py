from pixelbench_api import *

# Cozy tavern interior, drawn directly at 64x64.
c = new_canvas(64, 64, background="#17131a", name="tavern-interior")

# Palette
ink = "#17131a"
deep = "#211821"
wall = "#3b2927"
wall2 = "#4a312b"
smoke = "#5a4034"
beam = "#2b1c1c"
wood_dark = "#3a211b"
wood = "#6b3b24"
wood_mid = "#87502b"
wood_light = "#b06c34"
edge_light = "#d18a43"
gold_dark = "#8a4d1f"
gold = "#d88a2d"
lamp = "#ffd66b"
lamp_hi = "#fff0a0"
red = "#8f382d"
red_hi = "#c55b38"
green = "#36513b"
green_hi = "#59825a"
blue = "#34505c"
blue_hi = "#5d8490"
glass = "#9fb3a0"
cream = "#d6b77a"

# Back wall, mottled masonry and smoky patches.
c.rect(2, 3, 60, 46, wall)
c.rect(3, 4, 58, 45, wall2)
c.rect(4, 5, 56, 43, wall)
# irregular brick/plaster marks
for x,y,w,h in [(5,7,8,2),(26,6,11,2),(49,8,8,2),(8,22,10,2),(29,20,8,2),(45,25,12,2),(5,34,9,2),(24,35,7,2),(50,37,8,2)]:
    c.rect(x,y,w,h,wall2)
for x,y,w in [(15,11,7),(38,12,8),(4,27,6),(21,25,10),(42,33,7),(13,40,8),(32,42,8)]:
    c.rect(x,y,w,1,smoke)
# brick seams
for x0,y0,x1,y1 in [(4,17,15,17),(26,16,34,16),(49,18,59,18),(7,31,18,31),(35,28,44,28)]:
    c.line(x0,y0,x1,y1,"#312322")

# Heavy timber framing.
c.rect(0,0,64,4,ink)
c.rect(2,3,4,46,beam)
c.rect(58,3,4,46,beam)
c.rect(0,46,64,4,ink)
c.rect(3,47,58,2,wood_dark)
c.rect(31,3,3,43,beam)
c.rect(5,4,53,2,wood_dark)
# pegs
for x,y in [(4,9),(4,29),(59,14),(59,36),(32,11),(32,31)]:
    c.set(x,y,wood_light)

# Shelf supports and shelves.
for y in (16,30):
    c.rect(7,y,50,3,ink)
    c.rect(8,y,48,1,wood_light)
    c.rect(9,y+1,46,1,wood)
for x in (9,28,53):
    c.rect(x,18,2,12,wood_dark)
    c.set(x+1,19,wood_light)

# Bottle helper.
def bottle(x,y,h,col,hi):
    c.rect(x+1,y,2,2,ink)
    c.rect(x,y+2,4,h-2,ink)
    c.rect(x+1,y+2,2,h-3,col)
    c.set(x+1,y+3,hi)
    c.set(x+2,y+h-2,deep)

def jug(x,y,col):
    c.rect(x+1,y,3,2,ink)
    c.rect(x,y+2,5,7,ink)
    c.rect(x+1,y+3,3,5,col)
    c.rect(x+5,y+3,2,4,ink)
    c.set(x+5,y+4,col)
    c.set(x+1,y+3,wood_light)

# Top shelf bottles.
bottle(9,8,8,green,green_hi)
bottle(15,10,6,red,red_hi)
bottle(21,7,9,blue,blue_hi)
bottle(27,11,5,gold_dark,gold)
bottle(36,8,8,red,red_hi)
bottle(42,10,6,green,green_hi)
bottle(48,7,9,blue,blue_hi)
jug(53,8,wood_mid)
# Lower shelf assortment.
jug(8,20,wood_mid)
bottle(15,21,9,blue,blue_hi)
bottle(21,23,7,green,green_hi)
bottle(26,20,10,red,red_hi)
bottle(35,22,8,gold_dark,gold)
bottle(41,20,10,green,green_hi)
bottle(47,23,7,red,red_hi)
jug(52,20,wood_mid)

# Hanging lamps and chains.
def hanging_lamp(cx, chain_top, shade_y):
    c.rect(cx,chain_top,1,shade_y-chain_top,ink)
    c.set(cx-1,chain_top+2,wood_light)
    c.rect(cx-2,shade_y-1,5,2,ink)
    c.rect(cx-4,shade_y+1,9,2,ink)
    c.rect(cx-3,shade_y+1,7,2,gold)
    c.rect(cx-2,shade_y+3,5,4,ink)
    c.rect(cx-1,shade_y+3,3,3,lamp)
    c.set(cx,shade_y+3,lamp_hi)
    c.line(cx-3,shade_y+7,cx+3,shade_y+7,gold_dark)

hanging_lamp(18,3,8)
hanging_lamp(46,3,9)
# warm glow pixels
for x,y in [(13,13),(14,14),(22,13),(23,14),(41,14),(40,15),(51,14),(50,16)]:
    c.set(x,y,gold_dark)

# Bar back clutter: glasses and mugs.
def glass_item(x,y):
    c.rect(x,y,4,1,glass)
    c.set(x,y+1,glass); c.set(x+3,y+1,glass)
    c.rect(x+1,y+2,2,2,blue)
    c.rect(x,y+4,4,1,ink)

def mug(x,y):
    c.rect(x,y,5,5,ink)
    c.rect(x+1,y+1,3,3,cream)
    c.rect(x+5,y+1,2,3,ink)
    c.set(x+5,y+2,cream)

glass_item(11,34)
glass_item(19,33)
mug(43,34)
mug(51,33)

# Main bar silhouette and wooden face.
c.rect(3,39,58,4,ink)
c.rect(1,41,62,4,ink)
c.rect(2,41,60,2,wood_light)
c.rect(3,43,58,3,wood_mid)
c.rect(5,46,54,13,ink)
c.rect(7,46,50,11,wood)
# paneling
for x in (8,20,32,44,55):
    c.rect(x,47,2,10,wood_dark)
    c.set(x+1,48,wood_light)
c.rect(7,47,50,2,wood_mid)
c.rect(7,55,50,2,wood_dark)
# panel inset highlights
for x in (11,23,35,47):
    c.rect(x,50,7,1,wood_light)
    c.rect(x,51,1,3,wood_mid)
# countertop shine and dark edge
c.rect(2,40,60,2,wood_light)
c.rect(4,40,18,1,edge_light)
c.rect(28,40,13,1,edge_light)
c.rect(49,40,9,1,edge_light)
c.rect(1,44,62,2,ink)

# Items resting on counter.
mug(9,35)
c.rect(26,35,2,5,ink); c.rect(27,36,2,4,glass); c.set(28,37,lamp_hi)
c.rect(34,37,6,3,ink); c.rect(35,36,4,1,cream); c.rect(35,38,4,1,gold)

# Barrels in foreground corners.
def barrel(x,y):
    c.rect(x+2,y,8,1,ink)
    c.rect(x,y+2,12,10,ink)
    c.rect(x+1,y+1,10,12,ink)
    c.rect(x+2,y+1,8,12,wood_mid)
    c.rect(x+1,y+3,10,2,wood_dark)
    c.rect(x+1,y+9,10,2,wood_dark)
    c.rect(x+3,y+2,1,10,wood_light)
    c.rect(x+8,y+2,1,10,wood)
    c.set(x+5,y+6,ink); c.set(x+6,y+6,gold_dark)

barrel(-2,49)
barrel(54,49)

# Stools in front of the bar.
def stool(x,y):
    c.rect(x,y,11,2,ink)
    c.rect(x+1,y-1,9,2,wood_mid)
    c.rect(x+2,y,7,1,wood_light)
    c.rect(x+2,y+2,2,9,ink)
    c.rect(x+7,y+2,2,9,ink)
    c.rect(x+3,y+2,1,8,wood_mid)
    c.rect(x+7,y+2,1,8,wood)
    c.rect(x+3,y+7,5,2,ink)
    c.rect(x+4,y+7,3,1,wood_light)

stool(13,51)
stool(39,51)

# Floor strip and scattered warm reflections.
c.rect(0,61,64,3,ink)
c.rect(9,59,45,2,deep)
for x in (10,28,33,51):
    c.rect(x,60,5,1,wood_dark)
for x,y in [(25,58),(30,59),(35,58),(37,60)]:
    c.set(x,y,gold_dark)

# Smoke curls in open wall areas, sparse and muted.
c.line(24,31,22,29,smoke); c.line(22,29,23,27,smoke)
c.line(38,19,36,17,smoke); c.set(35,17,smoke)
c.line(57,31,55,29,smoke)

# A few crisp outline accents and nail heads.
for x,y in [(6,42),(17,42),(24,42),(45,42),(58,42),(12,48),(30,48),(52,48)]:
    c.set(x,y,lamp)

view(c, scale=8, margin=0)
finish(c)
