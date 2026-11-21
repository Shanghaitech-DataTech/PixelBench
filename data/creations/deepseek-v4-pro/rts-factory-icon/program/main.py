c = new_canvas(32, 32, name="factory")

# ---------- palette ----------
OUT       = c.color('#191420', 'outline')
BRICK     = c.color('#b4502f', 'brick')
BRICK_LT  = c.color('#c9673f', 'brick_light')
BRICK_DK  = c.color('#8f3a24', 'brick_dark')
MORTAR    = c.color('#7c2f1e', 'mortar')
ROOF      = c.color('#4a4452', 'roof')
ROOF_LT   = c.color('#6b6476', 'roof_light')
ROOF_DK   = c.color('#33303c', 'roof_dark')
CAP       = c.color('#3a3542', 'cap')
VENT      = c.color('#241e2c', 'vent')
DOOR      = c.color('#2e2118', 'door')
DOOR_LT   = c.color('#4a3525', 'door_light')
SMOKE     = c.color('#cfc8d8', 'smoke')
SMOKE_DK  = c.color('#9a91ab', 'smoke_shadow')

# ---------- silhouette (dark outline) ----------
c.rect(5, 5, 9, 5, OUT)    # chimney cap outline   x5..13  y5..9
c.rect(7, 9, 6, 4, OUT)    # chimney shaft outline x7..12  y9..12
c.rect(3, 11, 26, 6, OUT)  # roof outline          x3..28  y11..16
c.rect(5, 15, 22, 15, OUT) # wall outline          x5..26  y15..29

# ---------- inner fill ----------
# chimney cap
c.rect(6, 6, 7, 3, CAP)        # x6..12 y6..8
c.line(6, 6, 12, 6, ROOF_LT)   # cap top highlight
c.line(12, 7, 12, 8, OUT)      # cap right shade

# chimney shaft
c.rect(8, 8, 4, 4, BRICK)      # x8..11 y8..11
c.line(8, 8, 8, 11, BRICK_LT)  # left light
c.line(11, 8, 11, 11, BRICK_DK)# right shade

# roof
c.rect(4, 12, 24, 4, ROOF)     # x4..27 y12..15
c.line(4, 12, 27, 12, ROOF_LT) # top highlight
c.line(4, 15, 27, 15, ROOF_DK) # bottom shade

# wall
c.rect(6, 17, 20, 12, BRICK)   # x6..25 y17..28
c.line(6, 17, 25, 17, BRICK_LT)  # top highlight
c.line(6, 18, 6, 27, BRICK_LT)   # left light
c.line(25, 18, 25, 27, BRICK_DK) # right shade
c.line(6, 28, 25, 28, BRICK_DK)  # bottom shade

# mortar lines
c.line(6, 20, 25, 20, MORTAR)
c.line(6, 24, 25, 24, MORTAR)

# vertical brick joints (staggered)
for x in (12, 18):
    c.line(x, 18, x, 19, MORTAR)   # row 1
for x in (9, 15, 21):
    c.line(x, 21, x, 23, MORTAR)   # row 2
for x in (12, 18):
    c.line(x, 25, x, 27, MORTAR)   # row 3

# vents
c.rect(9, 18, 6, 2, VENT)    # x9..14 y18..19
c.rect(17, 18, 6, 2, VENT)   # x17..22 y18..19

# door
c.rect(13, 23, 6, 6, DOOR)   # x13..18 y23..28
c.line(13, 23, 18, 23, OUT)  # top edge
c.line(14, 24, 14, 27, DOOR_LT)  # inner highlight

# smoke puffs above chimney
c.rect(8, 3, 4, 3, SMOKE)    # lower puff x8..11 y3..5
c.rect(10, 1, 3, 2, SMOKE)   # upper puff x10..12 y1..2
c.line(8, 5, 11, 5, SMOKE_DK)
c.line(10, 2, 12, 2, SMOKE_DK)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 31, 31), indices=True))

finish(c)
