# Vintage mechanical sewing machine, 48x48, slightly angled side view.
# Components: base, body (arm/column/head), handwheel, needle bar,
# presser foot, spool, and red fabric draped over the base.

c = new_canvas(48, 48, background=None, name="vintage_sewing_machine")

OUT   = '#14141c'   # outline
BLK   = '#22222c'   # body black japan
BLK2  = '#32323e'   # body mid
BLK3  = '#4c4c5e'   # body highlight
GOLD  = '#c9961f'   # gold decals
GOLDL = '#f2d268'
MET   = '#aab0bb'   # steel
METD  = '#686e7a'
METL  = '#e6eaf2'
RED   = '#b82334'   # fabric
REDD  = '#7c1424'
REDL  = '#e8505c'
SHD   = '#10101a55' # soft ground shadow

# ---- ground shadow ----
c.ellipse(24, 45, 17, 1, SHD)

# ---- base (parallelogram top = angled view) ----
c.poly([(5, 37), (7, 35), (42, 35), (44, 37), (44, 41), (42, 42), (6, 42), (5, 41)], OUT)
c.poly([(7, 36), (41, 36), (43, 38), (6, 38)], BLK2)          # top surface
c.rect(6, 39, 37, 2, BLK)                                     # front face
c.line(8, 40, 40, 40, GOLD)                                   # gold pinstripe
# metal slide plates on the bed, right of the fabric
c.rect(22, 36, 4, 2, METD)
c.line(22, 36, 25, 36, MET)
# feet
c.rect(7, 42, 3, 2, OUT);  c.set(8, 42, BLK2)
c.rect(38, 42, 3, 2, OUT); c.set(39, 42, BLK2)

# ---- red fabric: flat piece on bed + drape over the front edge ----
c.poly([(8, 36), (20, 36), (21, 38), (8, 38)], RED)
c.line(9, 36, 19, 36, REDL)                                   # top light
c.set(9, 37, REDD); c.set(11, 37, REDD); c.set(17, 37, REDD)  # stitches
c.poly([(8, 38), (15, 38), (14, 44), (12, 46), (10, 45), (8, 42)], RED)  # drape
c.line(11, 39, 11, 43, REDD)                                  # fold shade
c.line(10, 39, 10, 43, REDL)                                  # fold light

# ---- machine body silhouette + inner fill ----
c.poly([(11, 16), (13, 12), (35, 12), (38, 13), (41, 16), (41, 35),
        (32, 35), (32, 24), (19, 24), (18, 31), (14, 32), (11, 29),
        (10, 25), (10, 18)], OUT)
c.poly([(12, 16), (14, 13), (34, 13), (37, 14), (40, 17), (40, 34),
        (33, 34), (33, 23), (20, 23), (19, 30), (15, 31), (12, 28),
        (11, 25), (11, 18)], BLK)

# shading
c.line(15, 14, 33, 14, BLK3)        # arm top light
c.set(13, 15, BLK3)                 # head crown light
c.line(21, 23, 32, 23, OUT)         # arm underside shade

# face plate + tension discs on the head
c.rect(11, 17, 2, 10, BLK2)
c.circle(11, 20, 1, METD)
c.set(11, 20, METL)

# gold decals
c.line(16, 18, 33, 18, GOLD)                      # arm pinstripe
c.set(15, 20, GOLDL); c.set(14, 21, GOLD); c.set(16, 21, GOLD); c.set(15, 22, GOLD)  # head rosette
c.set(36, 19, GOLD); c.set(37, 20, GOLDL); c.set(36, 21, GOLD)  # column rosette
c.line(35, 23, 35, 26, GOLD)                      # column flourish

# take-up lever
c.line(17, 15, 19, 17, MET)
c.set(19, 18, METL)

# stitch knob on column
c.circle(37, 29, 1, METD)
c.set(37, 29, METL)

# ---- handwheel (right of column): solid japanned disc ----
c.circle(42, 19, 4, OUT)
c.circle(42, 19, 3, BLK)
c.circle(42, 19, 2, BLK2)                # spoked inset shading
c.set(40, 16, MET); c.set(39, 18, MET)   # rim glint
c.circle(42, 19, 1, METD)                # hub
c.set(42, 19, METL)

# ---- spool pin + red thread spool on arm ----
c.line(30, 7, 30, 12, METD)
c.rect(29, 9, 3, 3, RED)
c.line(29, 11, 31, 11, REDD)
c.set(29, 9, REDL)
# thread running down the arm face to the take-up lever
c.line(29, 10, 20, 14, REDL)

# ---- needle bar + presser foot ----
c.rect(15, 31, 2, 5, METD)          # presser bar
c.rect(12, 30, 2, 6, METD)          # needle bar
c.line(12, 30, 12, 35, MET)         # bar face
c.set(15, 31, MET)
c.rect(13, 35, 2, 1, METD)          # foot ankle
c.rect(11, 36, 5, 1, MET)           # presser foot sole
c.set(11, 36, METL)
c.line(13, 36, 13, 38, METL)        # needle into fabric

print(c.stats_text())
view(c)
finish(c)
