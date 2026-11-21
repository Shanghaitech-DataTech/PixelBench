from pixelbench_api import *

c = new_canvas(32, 32, name="sheep")

W = "#F2EEE4"   # fluff white
WS = "#DDD5C6"  # fluff shade
P = "#EFC9CC"   # pale pink ear
PS = "#E0AEB4"  # ear shade
F = "#8A6F5C"   # face brown-grey
FS = "#6E5748"  # face shade
E = "#3A3230"   # eye
L = "#4A3F38"   # legs
LS = "#3A322C"  # leg shade
H = "#C9BFAE"   # hoof highlight

# Body fluff (rounded blob) rows y=8..21
fluff = [
 (6,12,4,3),(5,14,6,4),(5,17,7,3),(6,19,7,2),
 (9,9,12,3),(8,11,15,3),(8,13,16,4),(8,17,15,3),(9,19,13,2),
 (19,10,6,3),(20,12,7,4),(20,15,7,3),(19,17,6,3),(18,19,6,2),
 (14,8,6,2),
]
for x,y,w,h in fluff:
    c.rect(x,y,w,h,W)
# fluff shading bottom
c.rect(9,20,12,1,WS)
c.rect(18,19,6,1,WS)
c.rect(6,20,3,1,WS)
# small fluff bumps on top edge
c.set(10,8,W); c.set(15,7,W); c.set(16,7,W); c.set(20,9,W); c.set(24,12,W)
c.set(7,11,W); c.set(23,10,W); c.set(25,14,W); c.set(8,20,WS); c.set(21,19,WS)

# Head (facing left), x=2..9, y=10..17
c.rect(2,10,7,6,F)
c.rect(2,11,1,4,F)
c.rect(3,16,4,1,FS)
c.rect(2,15,1,1,FS)
# top of head fluff cap
c.rect(2,9,6,2,W)
c.set(3,8,W); c.set(5,8,W); c.set(7,9,W)
# eye
c.set(4,12,E)
# ear pale pink
c.rect(2,12,1,2,P)
c.set(1,13,P)
c.set(2,13,PS)
# muzzle
c.rect(2,14,3,1,FS)
c.set(2,14,"#5A463A")

# Legs y=21..26
c.rect(9,21,2,5,L)
c.rect(10,21,1,4,LS)
c.rect(19,21,2,5,L)
c.rect(20,21,1,4,LS)
# hooves
c.rect(9,26,2,1,LS)
c.rect(19,26,2,1,LS)
c.set(9,26,H)

# tail fluff
c.rect(25,15,2,3,W)
c.set(26,17,WS)

print(c.stats_text())
save("farm-sheep", c)
finish(c)
