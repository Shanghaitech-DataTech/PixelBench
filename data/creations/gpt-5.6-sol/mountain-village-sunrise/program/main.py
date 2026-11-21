from pixelbench_api import *
import random

W = H = 128
c = new_canvas(W, H, background="#f6ad62", name="mountain_village_sunrise")

# Compact sunrise palette.
sky_top = "#667596"
sky_mid = "#c98178"
sky_low = "#f6ad62"
sun = "#ffe39a"
sun_core = "#fff2bd"
cloud = "#e89a78"
cloud_light = "#f7bd82"
far_mtn = "#74758a"
far_light = "#9a8190"
mid_mtn = "#4f6275"
mid_light = "#687689"
near_mtn = "#344e59"
near_light = "#47636a"
ground_far = "#465a50"
ground = "#2f493f"
ground_dark = "#233a35"
grass_light = "#61735a"
pine_dark = "#172f2f"
pine_mid = "#24433a"
pine_light = "#3b5944"
wood_dark = "#402f2b"
wood = "#704636"
wood_light = "#9a6040"
wood_sun = "#bd7548"
roof_dark = "#322c31"
roof = "#554047"
roof_light = "#795457"
snow = "#d5c5b5"
window = "#ffd575"
window_hot = "#fff0a4"
stone_dark = "#59605a"
stone = "#858276"
stone_light = "#b0a28b"
smoke_dark = "#867b7c"
smoke = "#b49b91"

# Sky bands and blocky dawn haze.
c.rect(0, 0, 128, 18, sky_top)
c.rect(0, 18, 128, 16, sky_mid)
c.rect(0, 34, 128, 29, sky_low)
c.dither(0, 14, 128, 10, [sky_top, sky_mid], pattern="bayer4")
c.dither(0, 29, 128, 10, [sky_mid, sky_low], pattern="bayer4")
# Slim horizontal cloud fragments.
c.rect(8, 25, 22, 2, cloud)
c.rect(14, 23, 11, 2, cloud)
c.rect(96, 30, 24, 2, cloud_light)
c.rect(103, 28, 10, 2, cloud_light)
c.rect(34, 39, 13, 1, cloud_light)

# Sun: clear central focal point, partially tucked behind the ridges.
c.circle(65, 38, 12, sun)
c.circle(65, 38, 8, sun_core)
c.rect(55, 42, 21, 9, sun)

# Distant mountain silhouettes, snow caps, and atmospheric cuts.
c.poly([(0,55),(11,45),(20,51),(31,35),(40,46),(51,38),(62,53),(74,39),(83,47),(94,32),(108,46),(118,39),(127,49),(127,72),(0,72)], far_mtn)
c.poly([(20,51),(31,35),(40,46),(35,43),(31,47),(28,42)], snow)
c.poly([(83,47),(94,32),(108,46),(100,42),(95,45),(91,40)], snow)
c.poly([(0,62),(15,53),(28,60),(43,45),(57,59),(70,48),(82,59),(99,45),(112,56),(127,50),(127,79),(0,79)], mid_mtn)
c.poly([(33,54),(43,45),(57,59),(45,52),(41,55)], mid_light)
c.poly([(88,54),(99,45),(112,56),(101,51),(97,54)], mid_light)
# Near ridge opens a valley in the center.
c.poly([(0,63),(18,54),(35,66),(49,60),(57,68),(57,79),(0,83)], near_mtn)
c.poly([(71,70),(82,59),(95,64),(111,54),(127,62),(127,84),(70,81)], near_mtn)
c.poly([(0,73),(18,66),(37,74),(53,69),(64,76),(78,68),(96,73),(112,65),(127,72),(127,96),(0,96)], ground_far)

# Tiny distant village marks for scale.
for x, y in [(6,69),(25,70),(101,69),(116,68),(41,72),(87,71)]:
    c.rect(x, y, 6, 4, "#6f5546")
    c.poly([(x-1,y),(x+3,y-3),(x+7,y)], roof_dark)
    c.set(x+2, y+1, window)

# Ground plane.
c.poly([(0,80),(31,77),(53,80),(65,77),(82,80),(101,76),(127,81),(127,127),(0,127)], ground)
c.dither(0, 93, 128, 35, [ground, ground_dark], pattern="checker")

# Stone path, widening toward the viewer.
c.poly([(61,83),(71,83),(79,101),(100,127),(28,127),(52,101)], stone_dark)
c.poly([(63,84),(69,84),(75,100),(89,127),(40,127),(56,100)], stone)
# Path stones: irregular slab highlights and dark joints.
stones = [
    (61,88,5,2),(57,94,7,3),(66,95,6,2),(53,101,9,3),(65,102,11,3),
    (48,109,12,4),(63,110,13,3),(76,113,8,3),(40,119,15,4),(60,119,16,4),
    (79,121,10,4),(49,126,13,2),(70,126,14,2)
]
for x,y,w,h in stones:
    c.rect(x,y,w,h,stone_light)
    c.line(x, min(127, y+h), x+w-1, min(127, y+h), stone_dark)

# House helper with timber framing and lit windows.
def house(x, y, w, h, main=False):
    # shadow and wall
    c.rect(x+2, y+8, w-2, h-8, wood_dark)
    c.rect(x+3, y+9, w-4, h-10, wood if not main else wood_light)
    # roof with warm rim on the central building
    c.poly([(x,y+9),(x+w//2,y),(x+w+2,y+9)], roof_dark)
    c.poly([(x+2,y+8),(x+w//2,y+2),(x+w,y+8)], roof if not main else roof_light)
    c.line(x+2,y+8,x+w,y+8,roof_dark)
    if main:
        c.line(x+4,y+7,x+w//2,y+2,wood_sun)
        c.line(x+w//2,y+2,x+w-1,y+7,wood_sun)
    # timber beams
    c.rect(x+4,y+10,2,h-12,wood_dark)
    c.rect(x+w-6,y+10,2,h-12,wood_dark)
    c.rect(x+3,y+17,w-5,2,wood_dark)
    # windows
    wy = y+12
    c.rect(x+7,wy,5,6,wood_dark)
    c.rect(x+8,wy+1,3,4,window_hot if main else window)
    c.set(x+9,wy+1,sun_core)
    if w >= 25:
        c.rect(x+w-13,wy,5,6,wood_dark)
        c.rect(x+w-12,wy+1,3,4,window)
    # door and sill
    c.rect(x+w//2-3,y+h-9,7,8,wood_dark)
    c.set(x+w//2+2,y+h-5,window)
    c.rect(x+1,y+h-2,w,2,roof_dark)

# Three wooden houses, center is largest and brightest.
house(13, 70, 24, 22, False)
house(46, 58, 37, 31, True)
house(91, 69, 25, 23, False)

# Chimneys and rising pixel smoke.
c.rect(70,57,4,7,roof_dark)
c.rect(71,56,4,2,wood_dark)
c.rect(72,51,4,5,smoke_dark)
c.rect(74,47,5,5,smoke)
c.rect(77,43,5,4,smoke)
c.rect(80,40,4,3,cloud_light)
c.rect(100,67,3,6,roof_dark)
c.rect(101,63,3,4,smoke_dark)
c.rect(102,60,5,3,smoke)
c.rect(105,57,4,3,smoke)

# Pine helper: tiered, intentionally chunky silhouettes.
def pine(x, base, height, back=False):
    trunk = max(2, height//12)
    c.rect(x-trunk//2, base-height//5, trunk, height//5, wood_dark)
    col = pine_mid if back else pine_dark
    hi = near_light if back else pine_light
    top = base-height
    tiers = 5 if height > 27 else 4
    for i in range(tiers):
        yy = top + 3 + i*(height-7)//tiers
        half = 3 + i*(height//(tiers*2))
        c.poly([(x,yy-5),(x-half,yy+8),(x-2,yy+6),(x-half-2,yy+11),(x+half+2,yy+11),(x+2,yy+6)], col)
        c.line(x,yy-3,x-half+2,yy+7,hi)

# Back pines add scale; foreground pines frame the view.
for args in [(5,87,20),(41,82,17),(87,82,16),(122,88,21),(29,82,15)]:
    pine(*args, back=True)
pine(5,116,48)
pine(19,108,34)
pine(119,117,51)
pine(106,109,35)

# Grass tufts and warm edge accents around the path.
for x,y in [(3,121),(14,116),(23,125),(31,111),(38,101),(45,96),(87,99),(95,106),(108,123),(116,98),(8,99),(25,96)]:
    c.line(x,y,x-2,y-4,grass_light)
    c.line(x,y,x+2,y-5,grass_light)
    c.set(x,y-2,ground_far)

# A few foreground rocks stabilize the lower corners.
for x,y,w in [(4,123,9),(17,118,7),(104,122,10),(115,125,8),(28,116,5)]:
    c.rect(x,y,w,3,stone_dark)
    c.rect(x+1,y-1,max(2,w-3),2,stone)
    c.set(x+2,y-1,stone_light)

# Crisp isolated glints guiding the eye to the center.
c.set(43,91,grass_light)
c.set(86,91,grass_light)
c.set(62,91,sun)
c.set(69,91,sun)

view(c, scale=4, margin=0)
finish(c)
