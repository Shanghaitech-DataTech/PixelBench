from pixelbench_api import *

c = new_canvas(32, 32, background=None, name="forest-slime")

GREEN = c.color("#4a8f3c", "slime")
DARKG = c.color("#2f6626", "slime_dark")
LIGHT = c.color("#79c455", "slime_light")
MOSS = c.color("#5c7a2e", "moss")
BROWN = c.color("#8a5a33", "antler")
EYEGLOW = c.color("#ffe66d", "eye_glow")
EYECORE = c.color("#ff9d2e", "eye_core")
RED = c.color("#c8322b", "mushroom_red")
SPOT = c.color("#f2e6d0", "mushroom_spot")
STEM = c.color("#e8dcc0", "mushroom_stem")

# body: rounded blob, front-facing, rows 12..29
body = [
 (10,14,12,2),(9,16,14,2),(8,18,16,4),(8,22,16,2),
 (9,24,14,2),(10,26,12,2),(12,28,8,1),
]
for x,y,w,h in body:
    c.rect(x,y,w,h,GREEN)
# highlight top-left
c.rect(10,15,3,2,LIGHT)
c.rect(11,17,2,1,LIGHT)
# darker bottom-right shading
c.rect(20,20,4,4,DARKG)
c.rect(18,24,6,4,DARKG)
c.rect(14,26,8,2,DARKG)
c.rect(10,25,3,2,DARKG)
c.rect(9,17,1,4,DARKG)
c.rect(8,22,2,4,DARKG)

# moss patches on top of head
c.set(13,13,MOSS); c.set(14,13,MOSS); c.set(18,13,MOSS)
c.set(12,14,MOSS); c.set(19,14,MOSS); c.set(16,12,MOSS)
c.set(15,13,MOSS); c.set(17,13,MOSS)
c.set(11,16,MOSS); c.set(20,17,MOSS)

# tiny antlers
# left
c.line(12,13,10,9,BROWN)
c.line(10,9,8,7,BROWN)
c.line(10,9,8,10,BROWN)
c.line(11,11,9,11,BROWN)
# right
c.line(20,13,22,9,BROWN)
c.line(22,9,24,7,BROWN)
c.line(22,9,24,10,BROWN)
c.line(21,11,23,11,BROWN)

# glowing eyes
c.rect(12,19,3,3,EYEGLOW)
c.rect(18,19,3,3,EYEGLOW)
c.set(13,20,EYECORE); c.set(19,20,EYECORE)
# small mouth
c.rect(15,24,3,1,DARKG)

# red mushroom on back (right side)
c.rect(22,16,5,3,RED)   # cap
c.set(21,17,RED); c.set(27,17,RED)
c.set(23,16,SPOT); c.set(26,17,SPOT)
c.rect(23,19,3,2,STEM)

print(c.stats_text())
save("forest-slime-monster", c)
finish(c)
