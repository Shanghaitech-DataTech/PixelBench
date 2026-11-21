from pixelbench_api import *

c = new_canvas(64, 64, background=None, name="dining")

# ===== Palette =====
dark      = '#241610'   # dark outline
table     = '#b8773f'
table_d   = '#9a5f2f'
table_l   = '#c98d52'
chair_w   = '#8a5a28'
chair_wd  = '#633d1a'
cushion   = '#d05a52'
cush_l    = '#e88078'
cush_d    = '#b0423c'
bowl      = '#ece4d4'
bowl_in   = '#c4b89c'
apple     = '#e22d2c'
apple_d   = '#a81f1f'
apple_l   = '#f05c56'
banana    = '#f2d53c'
banana_d  = '#d0a02a'
orange    = '#f08a28'
orange_l  = '#f8a850'
grape     = '#7a4e8a'
grape_l   = '#9a6aaa'
leaf      = '#3e8a3e'
stem      = '#5a3a1a'
floor     = '#e4d2ae'
floor_d   = '#cdba92'
rug       = '#b06a42'
rug_d     = '#96562e'
rug_pat   = '#d18a5a'
shadow    = '#2e1e10'
plate     = '#f2ecda'
steam     = '#d8c8a8'
house     = '#c89460'   # warm wall behind top

# ===== Warm wall / floor split (front-view feel): wall at top, floor below =====
# Actually full top-down is cleaner. Use a warm floor throughout with a rug.
c.rect(0, 0, 64, 64, floor, fill=True)
for yy in range(5, 64, 9):
    c.rect(0, yy, 64, 1, floor_d, fill=True)

# ===== Rug (large rounded rect) =====
c.rect(4, 6, 56, 52, rug, fill=True)
c.rect(6, 8, 52, 48, rug_d, fill=True)
c.rect(8, 10, 48, 44, rug_pat, fill=True)
c.rect(10, 12, 44, 40, rug_d, fill=True)

# ===== Table (rounded rectangle 38 x 26, centered x so table 13-51) =====
tw, th = 38, 26
tx, ty = 13, 19
# soft drop shadow offset 2px down-right
c.rect(tx+2, ty+2, tw, th, shadow, fill=True)
c.rect(tx, ty, tw, th, dark, fill=True)
c.rect(tx+2, ty+2, tw-4, th-4, table, fill=True)
# wood grain vertical lines
for gx in (17, 23, 29, 35, 41, 47):
    c.rect(gx, ty+3, 1, th-6, table_d, fill=False)
# top-left highlight
c.rect(tx+3, ty+3, tw-6, 2, table_l, fill=True)
c.rect(tx+3, ty+3, 2, th-6, table_l, fill=True)

# ===== Place settings: 2 plates on ends + napkins? Keep center clear for bowl =====
# Red runners/placemats at four edges of table
# top mat
c.rect(24, 22, 16, 3, '#c06040', fill=True)
c.rect(24, 22, 16, 1, '#d87a55', fill=True)
# bottom mat
c.rect(24, 39, 16, 3, '#c06040', fill=True)
c.rect(24, 41, 16, 1, '#d87a55', fill=True)
# left mat
c.rect(14, 27, 3, 10, '#c06040', fill=True)
c.rect(14, 27, 1, 10, '#d87a55', fill=True)
# right mat
c.rect(47, 27, 3, 10, '#c06040', fill=True)
c.rect(49, 27, 1, 10, '#d87a55', fill=True)

# small plates on mats
c.circle(32, 24, 3, plate, fill=True)
c.circle(32, 40, 3, plate, fill=True)
c.circle(19, 32, 3, plate, fill=True)
c.circle(45, 32, 3, plate, fill=True)
for pcx, pcy in ((32,24),(32,40),(19,32),(45,32)):
    c.circle(pcx, pcy, 2, '#d8d0b8', fill=False)

# ===== Fruit bowl at center =====
bcx, bcy = 32, 32
c.circle(bcx, bcy+1, 8, shadow, fill=True)
c.circle(bcx, bcy, 8, bowl, fill=True)
c.circle(bcx, bcy, 7, bowl_in, fill=False)
# leaf
c.ellipse(bcx-1, bcy-7, 3, 2, leaf, fill=True)
# banana
c.ellipse(bcx+5, bcy-3, 4, 2, banana, fill=True)
c.ellipse(bcx+5, bcy-3, 4, 2, banana_d, fill=False)
# apple
c.circle(bcx-3, bcy-2, 3, apple, fill=True)
c.circle(bcx-4, bcy-1, 2, apple_l, fill=True)
c.rect(bcx-4, bcy-3, 1, 2, stem, fill=True)
# orange
c.circle(bcx+1, bcy+3, 3, orange, fill=True)
c.circle(bcx, bcy+2, 1, orange_l, fill=True)
# grapes
c.circle(bcx-3, bcy+4, 2, grape, fill=True)
c.circle(bcx-1, bcy+5, 2, grape, fill=True)
c.rect(bcx-5, bcy+4, 1, 1, grape_l, fill=True)
# bowl rim thick dark edge at bottom
c.circle(bcx, bcy, 8, bowl, fill=False)

# ===== Chairs: four around the table with clear gap =====
# Chair seat width 14, back plank behind.
# TOP chair (facing down toward table) - back at top
c.rect(25, 9, 14, 3, dark, fill=True)
c.rect(26, 10, 12, 2, chair_w, fill=True)       # back top bar
c.rect(24, 12, 16, 2, dark, fill=True)
c.rect(25, 13, 14, 1, chair_w, fill=True)       # back slat
c.rect(25, 15, 14, 2, dark, fill=True)         # back bottom / seat base start
c.rect(24, 17, 15, 1, dark, fill=True)

# Top chair seat
c.rect(24, 13, 16, 4, dark, fill=True)
c.rect(25, 14, 14, 3, cushion, fill=True)
c.rect(25, 14, 14, 1, cush_l, fill=True)

# BOTTOM chair (facing up)
c.rect(24, 51, 16, 4, dark, fill=True)
c.rect(25, 51, 14, 3, cushion, fill=True)
c.rect(25, 51, 14, 1, cush_l, fill=True)
c.rect(25, 55, 14, 1, chair_w, fill=True)
c.rect(24, 56, 16, 2, dark, fill=True)
c.rect(26, 54, 12, 2, chair_w, fill=True)
c.rect(25, 58, 14, 2, dark, fill=True)

# LEFT chair (facing right)
c.rect(4, 24, 3, 16, dark, fill=True)
c.rect(5, 25, 2, 14, chair_w, fill=True)
c.rect(7, 26, 2, 12, dark, fill=True)
c.rect(9, 24, 3, 16, dark, fill=True)
c.rect(10, 25, 2, 14, cushion, fill=True)
c.rect(10, 25, 1, 14, cush_l, fill=True)
# LEFT back planks
c.rect(2, 25, 2, 14, dark, fill=True)
c.rect(2, 26, 1, 12, chair_wd, fill=True)

# RIGHT chair (facing left)
c.rect(57, 24, 3, 16, dark, fill=True)
c.rect(58, 25, 2, 14, chair_w, fill=True)
c.rect(56, 26, 2, 12, dark, fill=True)
c.rect(52, 24, 3, 16, dark, fill=True)
c.rect(53, 25, 2, 14, cushion, fill=True)
c.rect(53, 25, 1, 14, cush_l, fill=True)
c.rect(61, 25, 2, 14, dark, fill=True)
c.rect(62, 26, 1, 12, chair_wd, fill=True)

finish(c)
