# Golden rice terraces during harvest, 64x64 pixel art.
from pixelbench_api import *

c = new_canvas(64, 64, background="#182c2a", name="rice_terraces")

# Compact harvest palette.
sky = "#b8c9a4"
haze = "#8da17f"
far_mtn = "#526c58"
mid_mtn = "#385445"
dark = "#182c2a"
ridge = "#263d32"
shadow = "#45543b"
olive = "#6f7040"
old_gold = "#9a8040"
gold = "#c49a3a"
bright = "#e1ba50"
straw = "#f0d06b"
cream = "#f7df8a"
water = "#718d78"
roof = "#6f3d2b"
roof_lit = "#a65a32"
wall = "#d6b56b"
skin = "#b96d3d"
cloth = "#315062"
white = "#e8dfbf"

# Hazy mountain bowl and distant slopes.
c.rect(0, 0, 64, 13, sky)
c.poly([(0,7),(8,3),(17,8),(25,4),(35,9),(44,3),(54,7),(64,4),(64,17),(0,17)], haze)
c.poly([(0,11),(8,7),(16,10),(23,6),(32,12),(40,8),(49,12),(57,7),(64,10),(64,20),(0,20)], far_mtn)
c.poly([(0,15),(9,11),(18,15),(28,10),(37,16),(46,11),(56,15),(64,12),(64,23),(0,23)], mid_mtn)
# Distant ridge highlights.
c.line(0,14,8,10,water).line(9,10,17,14,water)
c.line(28,9,37,15,water).line(46,10,56,14,water)

# Tiny village nestled at the high terrace edge.
def house(x,y,w=5):
    c.rect(x+1,y+2,w-2,3,wall)
    c.poly([(x,y+2),(x+w//2,y),(x+w,y+2)],roof)
    c.set(x+w//2,y+1,roof_lit)
    c.set(x+2,y+3,dark)

house(5,13,6); house(14,15,5); house(48,14,6); house(56,16,5)
c.rect(0,19,64,3,ridge)
c.line(0,18,12,17,old_gold).line(12,17,25,19,old_gold)
c.line(39,19,51,17,old_gold).line(51,17,63,19,old_gold)

# Upper terraces: nested contour shelves.
c.path("M0 21 C10 18 18 20 27 22 C38 25 51 20 64 21 L64 28 C51 27 42 31 29 27 C18 24 9 27 0 28 Z", old_gold)
c.path("M0 22 C11 19 18 21 28 23 C40 26 51 22 64 22 L64 25 C51 24 42 28 29 25 C18 22 10 25 0 26 Z", gold)
c.path("M0 28 C13 25 21 27 31 29 C43 32 53 27 64 28 L64 36 C53 34 44 38 31 34 C21 31 12 34 0 35 Z", olive)
c.path("M0 29 C12 26 21 28 31 30 C44 34 53 29 64 29 L64 33 C52 31 44 36 31 32 C20 29 12 32 0 33 Z", bright)
# Dark retaining edges.
c.path("M0 27 C12 24 21 26 31 28 C44 32 53 27 64 27", ridge, fill=False)
c.path("M0 35 C12 32 20 29 31 33 C44 37 52 33 64 35", dark, fill=False)

# Middle terraces, increasingly close and broad.
c.path("M0 36 C11 33 20 35 29 38 C40 42 51 36 64 37 L64 46 C52 43 42 49 29 44 C18 40 10 44 0 44 Z", old_gold)
c.path("M0 37 C10 34 19 36 29 39 C41 44 51 38 64 38 L64 42 C52 40 42 46 29 42 C18 38 10 42 0 42 Z", gold)
c.path("M0 45 C10 42 19 43 28 47 C40 52 51 45 64 46 L64 55 C52 52 41 59 27 54 C17 49 9 53 0 52 Z", shadow)
c.path("M0 46 C10 43 19 44 28 48 C41 54 51 47 64 47 L64 51 C52 49 41 56 28 51 C17 47 9 50 0 50 Z", bright)
c.path("M0 52 C9 49 17 51 27 55 C40 61 51 54 64 55 L64 64 L0 64 Z", old_gold)
c.path("M0 54 C9 51 17 53 27 57 C40 63 52 56 64 57 L64 63 C52 61 41 66 27 60 C17 56 9 55 0 58 Z", gold)
# Strong foreground terrace rims.
c.path("M0 44 C10 41 19 42 29 46 C41 51 51 44 64 45", dark, fill=False)
c.path("M0 52 C9 49 18 50 28 54 C41 60 51 53 64 54", ridge, fill=False)
c.path("M0 59 C10 55 17 56 27 61 C39 66 52 58 64 60", dark, fill=False)

# Harvested rice rows and glints, following each contour.
for x,y in [(3,23),(8,22),(14,22),(20,23),(35,25),(41,26),(48,24),(55,23),(60,23),
            (3,30),(9,29),(15,29),(22,30),(36,33),(42,34),(49,32),(56,31),(61,31),
            (3,39),(9,38),(15,38),(21,39),(35,43),(42,44),(49,42),(56,40),(61,40),
            (3,48),(9,47),(16,47),(22,49),(35,52),(42,53),(49,51),(56,49),(61,49),
            (4,56),(11,54),(18,56),(34,60),(42,60),(50,58),(58,57)]:
    c.line(x,y,x+2,y,straw)
    c.set(x+1,y-1,cream)

# Small water pockets add cool depth contrast.
c.line(0,32,5,31,water).line(57,34,63,33,water)
c.line(0,50,5,49,water).line(58,53,63,52,water)

# Two farmers on narrow ridges: hats, bodies, tools, shadows.
def farmer(x,y,flip=False):
    # long cast shadow on the paddy below
    c.line(x+1,y+4,x+(4 if not flip else -3),y+6,shadow)
    # legs and torso
    c.set(x,y+3,dark); c.set(x+2,y+3,dark)
    c.rect(x,y,3,3,cloth)
    c.set(x+1,y-1,skin)
    # broad conical hat
    c.line(x-1,y-2,x+3,y-2,straw)
    c.line(x,y-3,x+2,y-3,cream)
    # arm and carrying/tool pole
    if not flip:
        c.line(x+2,y+1,x+4,y+2,skin)
        c.line(x+4,y-1,x+4,y+5,dark)
    else:
        c.line(x,y+1,x-2,y+2,skin)
        c.line(x-2,y-1,x-2,y+5,dark)

farmer(18,36,False)
farmer(45,48,True)

# Foreground corner foliage frames the scene and reinforces depth.
c.poly([(0,64),(0,57),(2,58),(3,54),(5,59),(7,56),(8,64)], dark)
c.poly([(64,64),(64,56),(62,59),(60,55),(59,61),(56,58),(56,64)], dark)
c.set(3,57,water).set(61,58,water)

view(c, scale=8, margin=0)
finish(c)
