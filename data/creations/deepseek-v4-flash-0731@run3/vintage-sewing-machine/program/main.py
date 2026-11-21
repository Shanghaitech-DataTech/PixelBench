from pixelbench_api import *

c = new_canvas(48, 48, name="sewing-machine")

BLACK  = c.color("#141416")
BODY   = c.color("#232329")
DARK   = c.color("#17171c")
MID    = c.color("#35353e")
LIGHT  = c.color("#5a5a64")
METAL  = c.color("#8d8d99")
SILVER = c.color("#c6c6d0")
PALE   = c.color("#eaeaf2")
GOLD   = c.color("#dfa43a")
GOLD_D = c.color("#a8731e")
RED    = c.color("#d62b2b")
RED_D  = c.color("#981b1b")
RED_L  = c.color("#ef5555")

# ---------------- BED / BASE ----------------
c.rect(2, 39, 43, 4, BODY)            # base body x=2..44, y=39..42
c.line(2, 39, 44, 39, MID)            # bed top surface
c.line(2, 41, 44, 41, GOLD)           # gold pinstripe
c.rect(2, 43, 43, 2, DARK)            # lower panel y=43..44
c.line(2, 44, 44, 44, BLACK)          # base bottom edge
c.rect(16, 39, 11, 1, SILVER)         # needle plate strip x=16..26
c.line(18, 39, 24, 39, METAL)         # plate slot

# ---------------- RED FABRIC ----------------
c.rect(4, 36, 23, 3, RED)             # fabric bulk on the bed x=4..26, y=36..38
c.line(4, 36, 26, 36, RED_L)          # lit crest
c.line(4, 38, 26, 38, RED_D)          # shadow against bed
c.rect(4, 39, 12, 2, RED)             # drape over the bed front x=4..15, y=39..40
c.line(4, 40, 15, 40, RED_D)
c.line(7, 38, 7, 40, RED_D)           # folds
c.line(11, 38, 11, 40, RED_D)
c.line(15, 38, 15, 40, RED_D)

# ---------------- MACHINE BODY ----------------
c.rect(5, 5, 35, 8, BODY)             # arm x=5..39, y=5..12
c.circle(36, 12, 6, BODY)              # shoulder x=30..42, y=6..18
c.rect(29, 10, 9, 29, BODY)           # pillar x=29..37, y=10..38
c.rect(5, 5, 11, 20, BODY)            # head x=5..15, y=5..24
c.line(5, 6, 5, 22, LIGHT)            # head left edge light
c.line(5, 5, 28, 5, MID)              # arm top edge
c.line(6, 12, 29, 12, DARK)           # under-arm shade
c.line(29, 12, 29, 38, DARK)          # pillar left edge shade

# face plate + dial + tension disc
c.rect(5, 8, 3, 12, MID)
c.circle(7, 14, 2, GOLD)
c.set(7, 14, GOLD_D)
c.circle(7, 20, 1, SILVER)             # tension disc
c.set(6, 20, METAL)
c.rect(7, 6, 2, 6, LIGHT)

# gold arm decals
c.line(8, 7, 30, 7, GOLD)
c.line(12, 9, 26, 9, GOLD)

# spool on the arm top
c.rect(10, 4, 4, 2, PALE)
c.line(10, 4, 10, 5, GOLD)
c.line(13, 4, 13, 5, GOLD)

# bobbin winder near the wheel
c.rect(30, 4, 4, 2, MID)
c.line(30, 4, 33, 4, LIGHT)
c.set(34, 4, SILVER)
c.set(34, 5, SILVER)

# thread from spool down the head front to the needle
c.line(13, 6, 11, 22, PALE)

# ---------------- SEWING MECHANISMS ----------------
c.rect(11, 26, 2, 10, SILVER)         # presser bar
c.rect(5, 35, 8, 2, SILVER)           # presser foot
c.line(5, 35, 12, 35, PALE)
c.line(5, 36, 12, 36, METAL)
c.rect(8, 25, 3, 10, METAL)           # needle bar
c.line(8, 25, 8, 34, SILVER)
c.set(9, 35, SILVER)
c.set(9, 36, SILVER)
c.set(9, 37, SILVER)                    # needle tip into the fabric

# ---------------- HANDWHEEL ----------------
c.circle(40, 13, 6, LIGHT)             # outer rim
c.circle(40, 13, 5, MID)               # disc
c.circle(40, 13, 4, DARK)              # recessed face
c.circle(40, 13, 4, LIGHT, fill=False) # groove ring
c.circle(40, 13, 1, METAL)             # hub
c.set(40, 13, SILVER)
c.set(42, 13, BLACK)                   # hub nut
c.set(40, 11, BLACK)                   # spoke holes
c.set(40, 15, BLACK)
c.set(38, 13, BLACK)
c.set(43, 8, PALE)                      # rim spark
c.set(44, 8, PALE)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 47, 47), indices=True))

finish(c)
