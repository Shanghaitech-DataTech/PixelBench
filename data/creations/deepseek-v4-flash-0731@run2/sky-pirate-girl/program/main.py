from pixelbench_api import *

W = H = 64

SKY   = "#BFE3F7"
SKY_T = "#D9F0FC"
SKY_B = "#A4D3EC"
CLOUD = "#FFFFFF"
WIND  = "#AAD9F0"
HAIR_B = "#A97438"
HAIR_H = "#DFA961"
HAIR_S = "#7A4E22"
SKIN  = "#F7D3AC"
SKIN_S = "#E3B183"
SKIN_H = "#FDE9D2"
EYE_W = "#FFFFFF"
EYE_I = "#5B8CBF"
EYE_P = "#1F3348"
LASH = "#241510"
BROW = "#4A2D12"
LIP  = "#B3473A"
BLUSH = "#E8927D"
GOG_F = "#9AA3AD"
GOG_D = "#5E6A75"
GOG_L = "#96D8EE"
GOG_G = "#3A2A1A"
SHIRT = "#F2EEE4"
SHIRT_S = "#CFC6B2"
SCARF = "#D63B28"
SCARF_S = "#9E2417"
SCARF_H = "#F2765A"
COAT = "#1F3B63"
COAT_S = "#122441"
COAT_H = "#3B5F8F"
GOLD = "#D9B44A"
DARK = "#151B27"

bg = new_canvas(W, H, name="bg")
bg.rect(0, 0, 64, 18, SKY_T)
bg.rect(0, 18, 64, 26, SKY)
bg.rect(0, 44, 64, 20, SKY_B)
bg.circle(50, 10, 4, CLOUD)
bg.circle(45, 12, 3, CLOUD)
bg.ellipse(48, 13, 7, 2, CLOUD)
bg.ellipse(8, 20, 6, 2, CLOUD)
bg.ellipse(58, 30, 5, 2, CLOUD)
bg.ellipse(12, 54, 8, 2, CLOUD)
bg.line(0, 6, 30, 6, WIND)
bg.line(6, 22, 50, 22, WIND)
bg.line(0, 36, 28, 36, WIND)
bg.line(34, 48, 63, 48, WIND)
bg.line(0, 60, 26, 60, WIND)

ch = new_canvas(W, H, name="char")

# hair back mass
ch.ellipse(30, 21, 15, 14, HAIR_B)
ch.poly([(22, 6), (24, 2), (27, 6), (26, 8)], HAIR_B)
ch.poly([(27, 6), (30, 1), (33, 5), (31, 7)], HAIR_B)
ch.poly([(33, 7), (37, 3), (39, 8), (36, 9)], HAIR_B)
ch.poly([(39, 9), (43, 8), (44, 12), (40, 11)], HAIR_B)
ch.poly([(20, 9), (18, 6), (15, 8), (17, 11)], HAIR_B)

# neck + face
ch.rect(27, 32, 10, 8, SKIN_S)
ch.ellipse(30, 24, 10, 11, SKIN)

# hair sides
ch.poly([(18, 16), (14, 15), (13, 19), (15, 24), (18, 27), (21, 28), (21, 23), (20, 19)], HAIR_B)
ch.poly([(40, 15), (43, 14), (44, 18), (43, 24), (40, 28), (37, 30), (36, 27), (38, 22), (39, 18)], HAIR_B)

# wind tail
ch.poly([(15, 19), (10, 18), (6, 19), (3, 21), (2, 24), (4, 26), (7, 24), (11, 24), (14, 25)], HAIR_B)
ch.poly([(15, 26), (11, 24), (7, 25), (4, 27), (3, 30), (6, 29), (9, 28), (13, 29), (15, 30)], HAIR_B)
ch.line(12, 20, 5, 22, HAIR_H)
ch.line(11, 25, 6, 27, HAIR_H)

# hair top shine
ch.line(25, 8, 32, 9, HAIR_H)
ch.line(22, 9, 20, 12, HAIR_H)

# fringe
ch.poly([(22, 14), (23, 10), (26, 11), (26, 15), (24, 17), (22, 16)], HAIR_B)
ch.poly([(25, 14), (28, 10), (31, 11), (30, 15), (28, 17), (26, 16)], HAIR_B)
ch.poly([(30, 14), (33, 10), (36, 12), (35, 16), (32, 17), (29, 16)], HAIR_B)
ch.poly([(35, 14), (38, 13), (40, 16), (38, 19), (36, 18)], HAIR_B)

# goggles strap
# hair wisps right (wind)
ch.set(44, 10, HAIR_B)
ch.set(45, 11, HAIR_B)
ch.set(46, 12, HAIR_B)
ch.set(45, 13, HAIR_B)
ch.set(47, 10, HAIR_B)
ch.line(12, 17, 50, 17, GOG_G)
ch.circle(24, 16, 4, GOG_F)
ch.circle(33, 16, 4, GOG_F)
ch.circle(24, 16, 3, GOG_L)
ch.circle(33, 16, 3, GOG_L)
ch.rect(27, 15, 6, 2, GOG_D)
ch.set(22, 14, EYE_W)
ch.set(23, 15, EYE_W)
ch.set(31, 14, EYE_W)
ch.set(32, 15, EYE_W)

# eyes
ch.rect(22, 23, 7, 5, EYE_W)
ch.rect(30, 23, 7, 5, EYE_W)
ch.ellipse(25, 25, 1, 2, EYE_I)
ch.ellipse(33, 25, 1, 2, EYE_I)
ch.rect(25, 25, 2, 2, EYE_P)
ch.rect(33, 25, 2, 2, EYE_P)
ch.set(24, 24, EYE_W)
ch.set(25, 24, EYE_W)
ch.set(32, 24, EYE_W)
ch.set(33, 24, EYE_W)
ch.rect(22, 23, 7, 1, LASH)
ch.rect(30, 23, 7, 1, LASH)
ch.set(28, 24, LASH)
ch.set(29, 24, LASH)

# brows
ch.line(21, 21, 28, 20, BROW)
ch.set(20, 22, BROW)
ch.line(30, 20, 37, 21, BROW)
ch.set(38, 22, BROW)

# nose, mouth, blush
ch.set(27, 27, SKIN_S)
ch.set(28, 28, SKIN_S)
ch.line(25, 32, 30, 33, LIP)
ch.set(31, 33, LIP)
ch.set(32, 32, LIP)
ch.set(24, 32, LIP)
ch.line(27, 34, 33, 34, SKIN_S)
ch.set(22, 29, BLUSH)
ch.set(23, 30, BLUSH)
ch.set(24, 29, BLUSH)
ch.set(32, 29, BLUSH)
ch.set(33, 30, BLUSH)
ch.set(34, 29, BLUSH)

# shirt
ch.poly([(25, 39), (31, 38), (37, 39), (35, 45), (30, 45), (27, 44)], SHIRT)
# coat body
ch.poly([(13, 42), (21, 38), (29, 37), (38, 37), (47, 39), (53, 44), (52, 56), (55, 63), (50, 63), (46, 60), (40, 63), (34, 60), (28, 63), (22, 60), (17, 63), (12, 60), (8, 63), (9, 52), (10, 45), (13, 42)], COAT)
ch.line(11, 46, 13, 58, COAT_S)
ch.line(48, 44, 51, 53, COAT_S)
# collar flaps
ch.poly([(15, 43), (20, 39), (25, 42), (22, 45), (17, 44)], COAT_H)
ch.poly([(36, 39), (43, 39), (48, 43), (45, 45), (40, 44), (37, 42)], COAT_H)
# buttons
ch.set(27, 47, GOLD)
ch.set(26, 51, GOLD)
ch.set(25, 55, GOLD)
ch.set(30, 38, GOLD)

# scarf
ch.rect(20, 37, 23, 4, SCARF)
ch.line(20, 40, 42, 40, SCARF_S)
ch.line(20, 37, 42, 37, SCARF_H)
ch.poly([(23, 39), (19, 41), (14, 42), (10, 44), (6, 46), (4, 48), (5, 51), (8, 49), (12, 47), (16, 46), (20, 44), (21, 41)], SCARF)
ch.line(18, 43, 8, 46, SCARF_H)

# shoulder highlight
ch.line(15, 44, 12, 52, COAT_H)

ch.outline(DARK)

result = flatten([bg, ch], name="sky_pirate_girl")
finish(result)
