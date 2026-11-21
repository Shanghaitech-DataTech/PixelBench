from pixelbench_api import *

# Frame 1 = original content on a shared, slightly larger canvas
f1 = new_canvas(56, 63, name='f1')
f1.blit(input_canvas, 0, 0)

# Frame 2 = paladin's heavy downward attack
f2 = new_canvas(56, 63, name='f2')
# copy the whole original over as the base, then remove the raised weapon/arm
f2.blit(input_canvas, 0, 0)

dark   = f2.color('#101010')
silver = f2.color('#a8a098')
silver2= f2.color('#a9a5ab')
silver3= f2.color('#dccaca')
cream  = f2.color('#ffffd5')
gold   = f2.color('#ffcc43')
dgold  = f2.color('#d1b563')
white  = f2.color('#ffffff')
footc  = f2.color('#462125')
cloth  = f2.color('#3f0016')
deep   = f2.color('#2c2623')
sha    = f2.color('#17003599')

# --- remove the raised right arm + old raised sword (right-upper region) ---
f2.clear(20, 2, 22, 34)

# --- right arm swinging down-forward to swing the blade down ---
# shoulder + upper arm
f2.rect(15, 18, 4, 4, deep)
f2.rect(16, 19, 2, 2, silver)
f2.line(15, 21, 20, 24, silver)
f2.line(16, 21, 21, 24, silver)
f2.line(17, 22, 22, 25, silver)
f2.line(15, 23, 20, 26, silver)
f2.line(16, 24, 21, 27, silver)
# forearm driving down
f2.line(20, 25, 25, 31, silver)
f2.line(21, 26, 26, 32, silver)
f2.line(22, 27, 27, 32, silver2)
# hand / gauntlet
f2.rect(23, 30, 6, 4, silver)
f2.rect(24, 31, 4, 3, cream)
f2.rect(24, 34, 2, 2, silver)

# --- heavy sword pointing down to the ground in front, just driven down ---
# grip
f2.line(24, 32, 25, 36, dgold)
f2.line(25, 32, 26, 36, dgold)
# crossguard (perpendicular)
f2.line(18, 36, 31, 36, dgold)
f2.line(19, 37, 30, 37, gold)
# broad blade vertical, tip near ground
f2.line(25, 38, 25, 56, cream)     # bright cutting edge
f2.line(26, 37, 26, 57, dgold)
f2.line(27, 38, 27, 57, silver)
f2.line(28, 39, 28, 55, dgold)
f2.line(24, 39, 24, 54, silver2)

# --- white motion trail streaming out behind the swinging blade ---
# broad arcing sweep on the back side (upper-right) streaming toward the blade
for n, (a) in enumerate([(39,2),(40,6),(39,10),(37,14),(34,18),(30,22)]):
    pass
f2.line(39, 1, 26, 13, white)
f2.line(40, 3, 27, 16, white)
f2.line(41, 6, 28, 19, white)
f2.line(39, 9, 27, 21, white)
f2.line(37, 12, 26, 23, white)
f2.line(35, 15, 25, 25, white)
f2.line(32, 18, 24, 27, white)
f2.line(30, 21, 24, 29, white)
f2.line(28, 24, 24, 31, white)
# a few bright specks along the arc
for (px,py) in [(44,3),(43,8),(42,12),(40,16),(30,18),(38,20)]:
    f2.set(px,py,white)

# --- footing: the left (front) foot steps forward, weight into the blow ---
f2.clear(0, 46, 22, 15)      # remove old feet/legs
# rear leg (keeps posture)
f2.line(6, 45, 4, 54, silver2)
f2.line(7, 46, 5, 55, deep)
f2.rect(1, 54, 7, 3, footc)
# front leg extended forward (steps forward, lower, toward viewer)
f2.line(11, 44, 14, 51, silver)
f2.line(12, 45, 15, 52, deep)
f2.line(15, 51, 16, 56, deep)
f2.rect(9, 53, 10, 4, footc)
f2.rect(13, 57, 7, 2, footc)   # toe planted forward
f2.rect(10, 54, 3, 2, silver)  # boot armor highlight
# ground shadow stretched under the forward stance
f2.clear(0, 59, 34, 4)
f2.ellipse(16, 59, 16, 3, sha)

finish([f1, f2])
print("f2 upper:")
print(f2.matrix_text(region=(0,0,44,34)))
print("f2 lower:")
print(f2.matrix_text(region=(0,34,40,61)))
