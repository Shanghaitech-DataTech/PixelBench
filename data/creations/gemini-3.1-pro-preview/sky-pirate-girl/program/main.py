from pixelbench_api import *

c = new_canvas(64, 64)

# Palette
black = c.color("#1a1c23", "black")
skin = c.color("#ffe1c5", "skin")
skin_shadow = c.color("#dfb597", "skin_shadow")
hair = c.color("#fde047", "hair")
hair_shadow = c.color("#ca8a04", "hair_shadow")
hair_hl = c.color("#fef08a", "hair_hl")
navy = c.color("#1e3a8a", "navy")
navy_shadow = c.color("#172554", "navy_shadow")
navy_hl = c.color("#3b82f6", "navy_hl")
red = c.color("#dc2626", "red")
red_shadow = c.color("#991b1b", "red_shadow")
red_hl = c.color("#ef4444", "red_hl")
goggle_strap = c.color("#451a03", "strap")
goggle_rim = c.color("#94a3b8", "rim")
goggle_lens = c.color("#0891b2", "lens")
goggle_lens_hl = c.color("#67e8f9", "lens_hl")
eye_white = c.color("#ffffff", "eye_white")
eye_color = c.color("#10b981", "eye")
gold = c.color("#eab308", "gold")

# 1. Back hair
c.path("M 28 14 C 15 15 12 30 14 44 C 18 36 22 35 22 35 C 28 45 38 48 48 46 C 58 44 64 40 64 40 C 58 36 48 30 42 26 C 40 22 34 14 28 14 Z", hair)
c.path("M 22 35 C 28 45 38 48 48 46 C 55 45 60 42 64 40 C 58 43 50 45 45 42 Z", hair_shadow)

# 2. Body (Coat)
c.path("M 24 44 C 16 46 12 52 10 64 L 36 64 L 36 44 Z", navy)
c.path("M 36 44 L 36 64 L 54 64 C 52 52 48 46 40 44 Z", navy)
# Lapels
c.path("M 24 48 L 18 54 L 24 60 Z", navy_shadow)
c.path("M 24 48 L 18 54 L 24 60", gold, fill=False)
c.path("M 40 48 L 50 54 L 40 60 Z", navy_shadow)
c.path("M 40 48 L 50 54 L 40 60", gold, fill=False)
# Buttons
c.circle(36, 54, 1, gold)
c.circle(36, 60, 1, gold)
# Highlight
c.path("M 10 64 C 12 55 16 48 24 44 C 20 50 18 58 18 64 Z", navy_hl)

# 3. Head base
c.rect(28, 40, 8, 6, skin)
c.rect(28, 40, 8, 6, skin_shadow)
c.path("M 22 20 L 42 20 L 42 32 C 42 38 38 42 33 43 C 27 42 22 37 22 32 Z", skin)
c.ellipse(21, 30, 2, 3, skin)
c.ellipse(21, 30, 1, 2, skin_shadow)
c.path("M 22 32 C 22 37 27 42 33 43 L 33 40 C 28 39 24 35 24 32 Z", skin_shadow)
c.poly([(22,20), (42,20), (42,25), (32,27), (22,25)], skin_shadow)

# 4. Face details
c.path("M 24 27 Q 26 25 29 27", black, fill=False)
c.rect(25, 28, 3, 4, eye_white) 
c.rect(26, 28, 2, 3, eye_color) 
c.rect(27, 29, 1, 1, black)     
c.set(26, 28, eye_white)        

c.path("M 37 27 Q 38 25 40 27", black, fill=False) 
c.rect(38, 28, 2, 4, eye_white) 
c.rect(38, 28, 1, 3, eye_color) 
c.rect(39, 29, 1, 1, black)     
c.set(38, 28, eye_white)        

c.line(24, 25, 29, 26, hair_shadow)
c.line(37, 26, 40, 25, hair_shadow)
c.line(33, 33, 34, 34, skin_shadow)
c.line(25, 33, 27, 33, red_shadow)
c.line(38, 33, 39, 33, red_shadow)
c.path("M 33 37 Q 35 38 37 36", black, fill=False)
c.set(37, 36, black)

# 5. Goggles
c.path("M 22 20 C 28 22 36 22 42 20 L 42 24 C 36 26 28 26 22 24 Z", goggle_strap)
c.rect(22, 21, 2, 2, gold)
c.rect(40, 21, 2, 2, gold)
c.line(31, 20, 35, 20, goggle_rim)
c.line(31, 19, 35, 19, goggle_rim)
c.circle(27, 20, 4, goggle_rim)
c.circle(27, 20, 3, black)
c.circle(27, 20, 2, goggle_lens)
c.path("M 25 18 L 28 21", goggle_lens_hl, fill=False)
c.ellipse(38, 20, 3, 4, goggle_rim)
c.ellipse(38, 20, 2, 3, black)
c.ellipse(38, 20, 1, 2, goggle_lens)
c.path("M 37 18 L 39 21", goggle_lens_hl, fill=False)

# 6. Scarf
c.path("M 14 40 C 24 44 42 44 50 40 L 52 48 C 42 52 24 52 12 48 Z", red)
c.path("M 14 44 C 24 48 42 48 50 44 L 52 48 C 42 52 24 52 12 48 Z", red_shadow)
c.circle(42, 48, 3, red_shadow)
c.circle(42, 48, 2, red)
c.set(41, 47, red_hl)
c.path("M 42 48 C 48 48 56 52 62 54 C 64 54 64 56 64 56 C 58 58 50 58 42 54 Z", red)
c.path("M 42 51 C 48 51 56 55 62 56 C 58 58 50 58 42 54 Z", red_shadow)
c.path("M 44 50 C 50 50 56 53 60 55 C 56 54 50 52 44 51 Z", red_hl)
c.path("M 42 50 C 46 52 50 56 54 58 C 56 58 58 60 56 60 C 50 60 46 56 42 54 Z", red)

# 7. Front hair
c.path("M 34 12 C 26 14 18 20 18 32 C 20 28 24 24 28 22 L 26 28 C 28 24 32 20 34 18 L 32 24 C 36 20 40 18 43 22 C 44 18 40 14 34 12 Z", hair)
c.path("M 34 12 C 26 14 18 20 18 32 C 20 28 24 24 28 22 L 26 28 C 28 24 32 20 34 18 L 32 24 C 36 20 40 18 43 22 C 44 18 40 14 34 12 Z", hair_shadow, fill=False)
c.path("M 41 20 C 45 22 47 28 47 34 C 45 30 43 28 41 26 Z", hair)
c.path("M 41 20 C 45 22 47 28 47 34 C 45 30 43 28 41 26 Z", hair_shadow, fill=False)
c.path("M 20 20 C 16 24 14 30 16 36 C 18 32 20 28 22 26 Z", hair)
c.path("M 20 20 C 16 24 14 30 16 36 C 18 32 20 28 22 26 Z", hair_shadow, fill=False)
c.path("M 34 12 C 32 6 36 4 38 2 C 36 6 36 10 34 12 Z", hair)
c.path("M 34 12 C 32 6 36 4 38 2 C 36 6 36 10 34 12 Z", hair_shadow, fill=False)
c.path("M 28 16 C 32 14 36 14 41 16 C 39 18 34 18 30 18 Z", hair_hl)

# Outline
c.outline(black)

finish(c)
