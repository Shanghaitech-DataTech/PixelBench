from pixelbench_api import new_canvas, finish

c = new_canvas(48, 48)

BLK  = "#17191f"
MID  = "#2c313c"
LGT  = "#4d5464"
CHR  = "#d9dee8"
CHRD = "#96a0b2"
GD   = "#8a6a1d"
RED  = "#b5442e"
RDD  = "#7c2418"
RL   = "#e06a4e"
THR  = "#eadfc4"

# ---------- bed ----------
c.rect(2, 36, 44, 6, BLK)            # bed body x2..45 y36..41
c.rect(2, 36, 44, 1, LGT)           # top edge highlight
# band under the top edge
c.rect(4, 37, 40, 1, MID)
# ornamental feet
c.rect(5, 41, 5, 2, BLK)
c.rect(4, 42, 8, 1, BLK)
c.rect(35, 41, 5, 2, BLK)
c.rect(34, 42, 8, 1, BLK)

# ---------- red fabric on the bed (under the needle/presser) ----------
c.rect(34, 35, 8, 1, RL)            # ruffled top edge of fabric
c.rect(32, 36, 10, 1, RED)
c.rect(31, 37, 11, 1, RED)
c.rect(30, 38, 12, 1, RDD)
c.rect(31, 39, 11, 1, RED)
c.rect(32, 40, 10, 1, RED)
c.rect(33, 41, 9, 1, RDD)
c.rect(35, 40, 4, 1, RL)             # fold highlight
c.set(33, 36, RL); c.set(33, 37, RL)
c.set(38, 36, RL); c.set(38, 37, RL)
c.set(35, 39, RDD); c.set(36, 39, RDD)
# cream stitch dashes on the fabric
for sx in (30, 31, 35, 36, 40, 41):
    c.set(sx, 38, THR)
for sx in (33, 34, 38, 39):
    c.set(sx, 40, THR)
c.set(32, 39, THR); c.set(33, 39, THR)

# ---------- body: pillar (left) ----------
c.rect(6, 11, 8, 24, BLK)            # pillar x6..13 y11..34
c.circle(9, 11, 3, BLK)              # rounded pillar top
c.rect(6, 12, 1, 9, LGT)             # left highlight
c.set(7, 13, LGT); c.set(7, 15, LGT)
c.set(8, 12, LGT)
c.rect(7, 30, 6, 1, GD)              # gold band near pillar base

# ---------- arm across the top ----------
c.rect(11, 8, 23, 5, MID)            # x11..33 y8..12
c.rect(11, 8, 23, 1, LGT)            # arm top highlight
c.rect(12, 11, 21, 1, GD)            # gold trim line

# ---------- head (right end, front face) ----------
c.rect(31, 11, 9, 21, BLK)           # x31..39 y11..31
c.rect(31, 11, 9, 1, LGT)            # head top
c.rect(33, 13, 3, 2, CHR)            # face plate
c.rect(30, 14, 3, 4, CHRD)           # tension assembly on head front
c.set(31, 15, CHR)
c.rect(38, 13, 1, 6, GD)             # gold door line

# ---------- needle bar & presser foot ----------
c.rect(35, 15, 2, 15, CHR)           # needle bar
c.rect(34, 24, 3, 2, CHR)            # needle clamp
c.rect(33, 24, 2, 8, CHRD)           # presser bar
c.rect(31, 32, 6, 2, CHRD)           # presser foot
c.rect(31, 32, 6, 1, CHR)
c.rect(36, 30, 1, 5, CHR)            # needle
c.set(36, 35, CHR)

# ---------- handwheel (right side) ----------
c.rect(39, 21, 3, 5, BLK)            # axle block connecting head to wheel
c.circle(43, 23, 3, MID)             # wheel disc x40..46 y20..26
c.circle(43, 23, 3, CHRD, fill=False) # rim
c.circle(43, 23, 2, BLK)             # inner recess
c.circle(43, 23, 1, CHR)             # chrome hub
c.rect(41, 20, 5, 1, CHRD)           # rim top
c.rect(41, 26, 5, 1, CHRD)           # rim bottom

# ---------- spool on top of arm ----------
c.rect(24, 3, 8, 2, GD)              # top cap
c.rect(25, 5, 6, 3, THR)             # wound thread
c.rect(24, 8, 8, 2, GD)              # bottom cap
c.set(27, 2, CHR); c.set(28, 2, CHR)  # spool pin
# thread line down from spool to the head
c.set(28, 10, THR); c.set(29, 11, THR)
c.set(29, 12, THR); c.set(30, 13, THR); c.set(30, 14, THR)

print(c.stats_text())
print(c.matrix_text())
finish(c)
