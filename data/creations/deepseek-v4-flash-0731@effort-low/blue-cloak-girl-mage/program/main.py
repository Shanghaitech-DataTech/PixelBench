from pixelbench_api import *

c = new_canvas(64, 64)

# ---- palette ----
SKIN=(245,200,158); SKIN_SH=(213,167,118)
HAIR=(226,186,98); HAIR_SH=(192,144,64)
CAPE=(26,44,94); CAPE_D=(15,26,62); CAPE_L=(50,78,152); CAPE_HI=(78,114,198)
HOOD_IN=(12,16,42)
EYE=(24,28,46); EYE_HI=(240,240,255)
BOOT=(238,238,240); BOOT_SH=(196,196,204); BOOT_D=(146,146,158)
WOOD=(124,74,34); WOOD_D=(86,52,26); WOOD_L=(158,104,62)
GOLD=(216,180,98)
AMBER=(255,199,66); AMB_B=(255,238,152); AMB_C=(255,252,238)

# ---- ground shadow ----
c.ellipse(32,61,15,2,(0,0,0,55))

# ---- staff ----
# pole
c.rect(46,16,3,43,WOOD)          # x46-48, y16-58
c.rect(46,16,1,43,WOOD_D)        # left shade
c.rect(48,16,1,43,WOOD_L)        # right light
# ferrule bands
c.rect(46,19,3,2,GOLD)
c.rect(46,44,3,2,GOLD)
# amber orb + glow
c.circle(47,9,6,AMB_B,fill=False)   # outer glow ring
c.circle(47,9,5,(255,199,66,90),fill=False)
c.circle(47,9,4,AMBER)              # orb
c.circle(47,9,2,AMB_B)
c.set(46,7,AMB_C)
c.set(48,9,AMB_C)
# handle seen top above orb
c.rect(46,14,3,2,WOOD)

# ---- hooded head ----
c.ellipse(32,13,10,10,CAPE)      # hood silhouette x22-42,y3-23
# face
c.rect(27,15,12,9,SKIN)          # x27-38, y15-23
c.rect(27,15,12,1,SKIN_SH)       # forehead shadow under rim
c.rect(27,23,12,1,SKIN_SH)       # jaw shadow
# bangs
c.rect(28,16,4,3,HAIR)
c.rect(33,16,4,3,HAIR)
c.rect(27,17,1,3,HAIR)           # side strands
c.rect(37,17,1,3,HAIR)
# eyes
c.rect(29,19,3,2,EYE)
c.rect(34,19,3,2,EYE)
c.set(30,19,EYE_HI)
c.set(35,19,EYE_HI)
# brow highlight
c.rect(29,18,3,1,HAIR_SH)
c.rect(34,18,3,1,HAIR_SH)
# mouth
c.set(32,23,(160,110,80))

# ---- cloak body ----
c.poly([(23,24),(41,24),(46,54),(18,54)],CAPE)
# hood rim overlap top (re-affirm over body)
c.ellipse(32,13,10,9,CAPE)
# shading bands
c.rect(23,25,5,28,CAPE_L)        # left light panel
c.rect(38,25,6,28,CAPE_D)        # right shade
c.rect(39,26,3,26,CAPE)          # reintroduce base
# hood highlight
c.ellipse(29,10,3,4,CAPE_HI,fill=False)
# belt
c.rect(21,41,23,3,GOLD)

# ---- gripping hand on staff ----
c.circle(47,40,3,SKIN)
c.rect(46,40,3,2,SKIN_SH)

# ---- boots ----
# left
c.rect(23,53,7,1,BOOT_D)
c.rect(23,54,7,5,BOOT)
c.rect(28,54,2,5,BOOT_SH)
c.rect(23,59,7,1,BOOT_D)
# right
c.rect(35,53,7,1,BOOT_D)
c.rect(35,54,7,5,BOOT)
c.rect(35,54,2,5,BOOT_SH)
c.rect(35,59,7,1,BOOT_D)

print(c.stats_text())
print(c.matrix_text(region=(16,50,53,63)))
finish(c)
