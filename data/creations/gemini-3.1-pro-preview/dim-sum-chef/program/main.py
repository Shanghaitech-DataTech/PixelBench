from pixelbench_api import *

skin = "#FAD6B1"
skin_sh = "#E0B084"
white = "#FFFFFF"
grey = "#D0D0D0"
apron_c = "#5A7B9C"
pants = "#333333"
shoes = "#111111"
bamboo = "#E8C382"
bamboo_sh = "#B88A44"
bamboo_dk = "#5C3A21"
bamboo_band = "#F4D8A2"
bun = "#FFFDD0"
bun_sh = "#E6D5B8"
outline_c = "#2A2A2A"
red = "#D03030"
flour = "#F8F8F8"
blush = "#F0A0A0"

# Legs
c_legs = new_canvas(32, 32)
c_legs.rect(12, 28, 8, 4, pants)
c_legs.outline(outline_c)

# Shoes
c_shoes = new_canvas(32, 32)
c_shoes.rect(10, 30, 4, 2, shoes)
c_shoes.rect(18, 30, 4, 2, shoes)
c_shoes.outline(outline_c)

# Body (Shirt & Neck)
c_body = new_canvas(32, 32)
c_body.rect(9, 14, 14, 11, white) # shirt
c_body.rect(14, 14, 4, 2, skin_sh) # neck
c_body.rect(6, 15, 4, 6, white) # L sleeve
c_body.rect(22, 15, 4, 6, white) # R sleeve
c_body.outline(outline_c)

# Apron
c_apron = new_canvas(32, 32)
c_apron.rect(10, 19, 12, 10, apron_c)
flour_pts = [(11, 25), (12, 27), (14, 26), (15, 28), (17, 25), (18, 27), (19, 26), (13, 28), (16, 27), (20, 25)]
for x, y in flour_pts:
    c_apron.set(x, y, flour)
c_apron.outline(outline_c)

# Neckerchief
c_neck = new_canvas(32, 32)
c_neck.rect(13, 15, 6, 2, red)
c_neck.rect(14, 17, 2, 2, red)
c_neck.outline(outline_c)

# Head
c_head = new_canvas(32, 32)
c_head.rect(12, 8, 8, 6, skin)
c_head.rect(10, 9, 2, 3, skin) # ears
c_head.rect(20, 9, 2, 3, skin)
# face
c_head.set(13, 10, outline_c)
c_head.set(18, 10, outline_c)
c_head.rect(15, 11, 2, 1, skin_sh)
c_head.line(14, 13, 17, 13, outline_c)
c_head.set(14, 12, outline_c)
c_head.set(17, 12, outline_c)
c_head.set(12, 11, blush)
c_head.set(13, 11, blush)
c_head.set(18, 11, blush)
c_head.set(19, 11, blush)
# hat
c_head.rect(11, 3, 10, 5, white)
c_head.circle(11, 3, 2, white)
c_head.circle(15, 2, 3, white)
c_head.circle(20, 3, 2, white)
c_head.line(11, 7, 20, 7, grey)
c_head.outline(outline_c)

# Steamer Back
c_steamer_back = new_canvas(32, 32)
c_steamer_back.ellipse(15, 18, 7, 2, bamboo)
c_steamer_back.ellipse(15, 18, 6, 1, bamboo_dk)
c_steamer_back.outline(outline_c)

# Buns
c_buns = new_canvas(32, 32)
c_buns.circle(12, 17, 2, bun)
c_buns.circle(16, 16, 2, bun)
c_buns.circle(20, 17, 2, bun)
# shading
for bx, by in [(11, 18), (12, 18), (13, 18), (15, 17), (16, 17), (17, 17), (19, 18), (20, 18), (21, 18)]:
    c_buns.set(bx, by, bun_sh)
c_buns.set(12, 15, red)
c_buns.set(16, 14, red)
c_buns.set(20, 15, red)
c_buns.outline(outline_c)

# Steamer Front
c_steamer_front = new_canvas(32, 32)
c_steamer_front.rect(8, 18, 15, 5, bamboo)
c_steamer_front.ellipse(15, 22, 7, 2, bamboo)
c_steamer_front.line(8, 19, 22, 19, bamboo_band)
c_steamer_front.line(8, 22, 22, 22, bamboo_band)
for x in range(9, 23, 3):
    c_steamer_front.line(x, 19, x, 23, bamboo_sh)
c_steamer_front.ellipse(15, 18, 7, 2, bamboo)
c_steamer_front.ellipse(15, 18, 6, 1, "transparent")
c_steamer_front.clear(0, 0, 32, 18)
c_steamer_front.outline(outline_c)

# Hands
c_hands = new_canvas(32, 32)
c_hands.rect(5, 19, 4, 3, skin)
c_hands.rect(23, 19, 4, 3, skin)
c_hands.line(6, 19, 8, 19, skin_sh)
c_hands.line(6, 21, 8, 21, skin_sh)
c_hands.line(23, 19, 25, 19, skin_sh)
c_hands.line(23, 21, 25, 21, skin_sh)
c_hands.outline(outline_c)

out = flatten([c_legs, c_shoes, c_body, c_apron, c_neck, c_head, c_steamer_back, c_buns, c_steamer_front, c_hands])
finish(out)
