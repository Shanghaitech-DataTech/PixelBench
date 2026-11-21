from pixelbench_api import *

c = new_canvas(32, 32)

# palette
ink = c.color("#1a1a1a")       # black outline
deck_c = c.color("#9a9a9a")   # deck gray
wheel_c = c.color("#2b2b2b")  # wheel tire
hub_c = c.color("#c9c9c9")    # wheel hub
stem_c = c.color("#7a7a7a")   # stem
helmet_c = c.color("#d0342c") # red helmet
helmet_d = c.color("#a82a24") # dark helmet shade
jacket_c = c.color("#3478c0") # blue jacket
pants_c = c.color("#243d63")  # pants
skin_c = c.color("#f0b488")   # skin
grip_c = c.color("#3a3a3a")   # grips

# ================= scooter =================
# wheels
c.circle(7, 27, 2, wheel_c)
c.circle(7, 27, 1, hub_c)
c.circle(25, 27, 2, wheel_c)
c.circle(25, 27, 1, hub_c)
# wheel outlines
c.circle(7, 27, 2, ink, fill=False)
c.circle(25, 27, 2, ink, fill=False)

# rear wheel fender
c.rect(5, 25, 6, 1, deck_c)
c.rect(24, 25, 5, 1, deck_c)

# deck platform
c.rect(8, 24, 16, 2, deck_c)   # x8-23, y24-25

# stem (from front deck up to handlebars)
c.rect(22, 15, 2, 10, stem_c)  # x22-23, y15-24
c.rect(22, 15, 1, 9, ink)      # stem shade

# handlebar bar + grips
c.rect(18, 14, 11, 2, stem_c)  # x18-28, y14-15
c.rect(18, 14, 3, 2, grip_c)
c.rect(27, 14, 2, 2, grip_c)

# ================= rider =================
# legs (standing on deck)
c.line(14, 18, 11, 23, pants_c)   # back leg
c.line(15, 18, 19, 23, pants_c)   # front leg
c.rect(10, 23, 3, 2, pants_c)     # back foot
c.rect(18, 23, 3, 2, pants_c)     # front foot

# torso (leaning forward toward handlebars)
c.line(14, 17, 19, 12, jacket_c)
c.line(14, 18, 19, 13, jacket_c)
c.line(13, 18, 18, 13, jacket_c)
c.line(13, 17, 18, 12, jacket_c)
# jacket side shade
c.line(13, 18, 18, 13, ink)

# neck
c.rect(18, 11, 2, 1, skin_c)

# arm reaching to handlebar grip
c.line(19, 13, 26, 14, jacket_c)
c.rect(25, 14, 2, 1, skin_c)     # hand

# head & helmet (facing right)
c.circle(15, 7, 3, helmet_c)   # helmet shell x12-18 y4-10
c.rect(17, 5, 2, 4, helmet_d) # helmet dome shade
c.rect(19, 7, 2, 1, helmet_d) # brim
c.rect(18, 8, 2, 3, skin_c)   # face
c.rect(20, 9, 1, 2, skin_c)   # chin forward
c.rect(18, 7, 2, 1, helmet_d) # visor

print(c.stats_text())

finish(c)

