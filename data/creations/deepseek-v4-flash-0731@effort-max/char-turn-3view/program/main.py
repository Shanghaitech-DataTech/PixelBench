from pixelbench_api import *

c = input_canvas
# shared palette indices: 1..6 hair browns, 7 skin, 8 skin shade, 9 dark purple
# 10 red, 11 cyan, 12 white, 13 blue, 14 navy, 15 tan, 16 coat mid, 17 coat light,
# 18 white, 19 coat pale, 20 gray-blue, 21 pale skin, 22 dark navy, 23 plum

def new(w, h, name):
    return new_canvas(w, h, name=name)

# ---------- draw a 3/4 view facing viewer-LEFT (character's left) ----------
def body_front():
    cv = new(66, 122, "f1")
    h1, h2, h3 = 1, 2, 3
    skin, shn, red, cyan, wht, blue, navy, tan = 7, 8, 10, 11, 12, 13, 14, 15
    g1, g2, g3, wh2, pale, bsh, ww, nvy2 = 16, 17, 18, 19, 20, 21, 22, 23
    # head center: 31; face toward left
    hc = 31
    # ---- hair (fluffy) ----
    cv.ellipse(hc, 14, 17, 13, h1)       # main
    cv.ellipse(hc, 10, 15, 10, h2)
    cv.ellipse(hc, 7, 11, 7, h3)
    cv.ellipse(hc - 6, 8, 9, 8, h2)
    cv.ellipse(hc + 6, 8, 9, 8, h2)
    cv.ellipse(hc - 10, 12, 7, 8, h2)
    cv.ellipse(hc + 10, 12, 7, 8, h2)
    cv.ellipse(hc - 12, 18, 6, 7, h1)
    cv.ellipse(hc + 12, 18, 6, 7, h1)
    cv.ellipse(hc - 14, 23, 5, 6, h1)
    cv.ellipse(hc + 14, 23, 5, 6, h1)
    cv.ellipse(hc - 11, 25, 6, 6, h2)
    cv.ellipse(hc + 11, 25, 6, 6, h2)
    # shine
    cv.circle(hc - 8, 8, 3, h3)
    cv.circle(hc + 2, 6, 4, h3)
    cv.circle(hc + 9, 10, 3, h3)
    # ---- face (left side) ----
    fc = 26
    cv.ellipse(fc, 20, 10, 10, skin)
    cv.ellipse(fc - 3, 24, 8, 8, skin)
    cv.ellipse(fc - 6, 27, 5, 5, skin)
    # face shade on right of face
    cv.rect(fc + 4, 13, 3, 18, shn)
    cv.circle(fc + 9, 15, 2, shn)
    cv.circle(fc + 10, 20, 2, shn)
    # ---- goggles ----
    cv.rect(fc - 16, 16, 32, 7, navy)     # strap band
    cv.rect(fc - 16, 23, 32, 3, navy)     # strap lower band
    cv.circle(fc - 5, 20, 5, blue)        # near lens
    cv.circle(fc + 4, 19, 4, blue)        # far lens
    cv.circle(fc - 7, 18, 2, wht)
    cv.rect(fc - 4, 18, 4, 2, wht)
    cv.circle(fc + 3, 17, 1, wht)
    cv.rect(fc - 9, 24, 4, 2, navy)
    cv.rect(fc, 23, 2, 2, navy)
    # blush / nose shade + mouth
    cv.rect(fc + 2, 26, 2, 3, shn)
    cv.rect(fc - 1, 27, 4, 2, shn)
    cv.rect(fc - 2, 30, 4, 1, 8)
    cv.rect(fc - 3, 31, 2, 1, 8)
    # chin
    cv.ellipse(fc - 1, 28, 6, 5, skin)
    # ---- neck ----
    cv.rect(fc - 4, 32, 11, 5, skin)
    cv.rect(fc - 6, 33, 13, 4, shn)
    # ---- scarf / collar ----
    cv.rect(fc - 9, 36, 24, 5, red)
    cv.rect(fc - 2, 36, 10, 4, red)
    cv.rect(fc - 4, 39, 6, 2, cyan)
    cv.rect(fc - 9, 38, 6, 3, red)
    # scarf tail flying to the right (behind character -> viewer right)
    cv.rect(fc + 7, 40, 16, 2, red)
    cv.rect(fc + 15, 43, 10, 2, cyan)
    cv.rect(fc + 7, 42, 14, 2, cyan)
    cv.rect(fc - 13, 40, 6, 2, cyan)
    cv.rect(fc - 13, 43, 4, 4, red)
    # ---- torso: coat ----
    cv.ellipse(hc, 47, 16, 9, navy)       # collar base
    cv.ellipse(hc, 46, 14, 8, g1)
    cv.rect(hc - 14, 48, 28, 20, g1)
    cv.ellipse(hc - 12, 49, 5, 6, g2)
    cv.ellipse(hc + 12, 49, 5, 6, g2)
    # left (near) shoulder pad
    cv.ellipse(hc - 10, 42, 8, 7, g2)
    cv.ellipse(hc + 12, 43, 7, 6, g1)
    cv.ellipse(hc + 15, 44, 4, 5, navy)
    # chest shading
    cv.rect(hc - 12, 52, 4, 14, g2)
    cv.rect(hc + 8, 52, 4, 14, g2)
    # collar lapels
    cv.poly([(fc - 8, 41), (fc + 10, 41), (fc - 4, 54), (fc - 13, 47)], g2, fill=True)
    cv.poly([(fc + 8, 41), (fc - 8, 41), (fc - 2, 50), (fc + 14, 45)], navy, fill=True)
    # front opening pale panel
    cv.rect(fc - 6, 48, 12, 22, wh2)
    cv.rect(fc - 4, 48, 9, 20, pale)
    cv.rect(fc - 2, 50, 5, 13, 19)
    # buttons
    cv.circle(fc - 4, 53, 1, navy)
    cv.circle(fc - 5, 58, 1, navy)
    cv.circle(fc - 4, 63, 1, navy)
    # wing pins on chest
    cv.poly([(hc + 14, 56), (hc + 22, 54), (hc + 23, 58), (hc + 16, 60), (hc + 12, 58)], g3, fill=True)
    cv.rect(hc + 14, 58, 6, 2, g3)
    cv.poly([(hc - 10, 56), (hc - 18, 54), (hc - 19, 58), (hc - 12, 60), (hc - 8, 58)], g3, fill=True)
    # ---- sleeves ----
    cv.rect(9, 46, 9, 18, g1)
    cv.rect(45, 48, 9, 16, g1)
    cv.rect(10, 47, 5, 14, g2)
    cv.rect(8, 49, 3, 12, navy)
    cv.rect(46, 49, 3, 12, navy)
    cv.rect(10, 61, 7, 5, navy)          # cuffs
    cv.rect(45, 61, 7, 5, navy)
    cv.rect(11, 62, 5, 4, g2)
    # ---- hands clasped ----
    gx = fc - 3
    cv.ellipse(gx, 68, 8, 5, tan)
    cv.ellipse(gx + 5, 69, 7, 5, tan)
    cv.rect(gx - 3, 66, 14, 6, tan)
    cv.rect(gx - 1, 66, 10, 6, shn)
    cv.rect(gx + 1, 71, 6, 2, shn)
    cv.rect(gx - 2, 63, 3, 9, navy)
    # ---- belt ----
    cv.rect(hc - 13, 74, 27, 5, navy)
    cv.rect(fc - 5, 73, 10, 8, wh2)
    cv.rect(fc - 4, 74, 8, 6, g2)
    cv.rect(fc - 2, 75, 4, 3, 18)
    # ---- coat skirt ----
    cv.rect(hc - 16, 80, 10, 22, navy)
    cv.rect(hc + 9, 80, 10, 22, navy)
    cv.rect(hc - 12, 79, 25, 9, g1)
    cv.rect(hc - 9, 84, 19, 16, navy)
    cv.rect(hc - 6, 88, 9, 16, g2)
    cv.rect(hc + 2, 84, 7, 18, navy)
    # front skirt edge white lining (visible for 3/4-left)
    cv.rect(fc - 3, 80, 6, 22, wh2)
    cv.rect(hc + 1, 86, 6, 18, wh2)
    # ---- legs ----
    cv.rect(hc - 12, 92, 11, 24, pale)
    cv.rect(hc + 1, 92, 10, 24, pale)
    cv.rect(hc - 11, 92, 7, 22, wh2)
    cv.rect(hc + 2, 92, 6, 22, wh2)
    cv.rect(hc - 14, 94, 3, 18, g1)
    cv.rect(hc + 13, 94, 3, 18, g1)
    cv.rect(hc - 3, 94, 6, 20, 18)
    # knee shading
    cv.rect(hc - 10, 102, 7, 8, g1)
    cv.rect(hc + 3, 102, 6, 8, g1)
    # ---- boots ----
    cv.rect(hc - 13, 112, 13, 8, g2)
    cv.rect(hc + 1, 112, 12, 8, g2)
    cv.rect(hc - 12, 112, 5, 10, g1)
    cv.rect(hc + 3, 112, 5, 10, g1)
    cv.rect(hc - 15, 118, 16, 4, navy)
    cv.rect(hc, 118, 16, 4, navy)
    cv.rect(hc - 13, 120, 12, 2, ww)
    cv.rect(hc + 2, 120, 12, 2, ww)
    return cv

# ---------- rear view ----------
def body_rear():
    cv = new(66, 122, "f3")
    h1, h2, h3 = 1, 2, 3
    skin, shn, red, cyan, wht, blue, navy, tan = 7, 8, 10, 11, 12, 13, 14, 15
    g1, g2, g3, wh2, pale, bsh, ww, nvy2 = 16, 17, 18, 19, 20, 21, 22, 23
    hc = 32
    # ---- hair from behind ----
    cv.ellipse(hc, 13, 17, 13, h1)
    cv.ellipse(hc, 10, 15, 10, h2)
    cv.ellipse(hc, 7, 11, 7, h3)
    cv.ellipse(hc - 6, 8, 9, 8, h2)
    cv.ellipse(hc + 6, 8, 9, 8, h2)
    cv.ellipse(hc - 11, 12, 7, 8, h2)
    cv.ellipse(hc + 11, 12, 7, 8, h2)
    cv.ellipse(hc - 13, 18, 6, 7, h1)
    cv.ellipse(hc + 13, 18, 6, 7, h1)
    cv.ellipse(hc - 15, 24, 5, 6, h1)
    cv.ellipse(hc + 15, 24, 5, 6, h1)
    # back-shine on hair
    cv.circle(hc - 5, 7, 3, h3)
    cv.circle(hc - 9, 12, 3, h3)
    cv.circle(hc + 8, 11, 3, h3)
    # side hair over nape
    cv.ellipse(hc - 11, 27, 5, 7, h2)
    cv.ellipse(hc + 11, 27, 5, 7, h2)
    cv.rect(hc - 9, 31, 18, 7, h1)
    cv.ellipse(hc, 34, 9, 5, h1)
    # hair strands over nape
    cv.rect(hc - 7, 33, 5, 4, h2)
    cv.rect(hc + 2, 33, 5, 4, h2)
    # ---- goggle strap behind head ----
    cv.rect(hc - 14, 21, 28, 3, navy)
    cv.rect(hc - 13, 24, 26, 2, 22)
    # ---- scarf behind neck ----
    cv.rect(hc - 13, 35, 26, 6, red)
    cv.rect(hc - 11, 37, 22, 5, red)
    cv.ellipse(hc, 40, 8, 4, red)
    cv.rect(hc - 6, 42, 12, 3, cyan)
    cv.rect(hc - 8, 45, 16, 2, cyan)
    cv.rect(hc + 6, 47, 10, 2, red)
    # collar
    cv.ellipse(hc - 13, 44, 6, 7, navy)
    cv.ellipse(hc + 13, 44, 6, 7, navy)
    cv.ellipse(hc, 47, 13, 7, g1)
    cv.rect(hc - 10, 46, 12, 9, g1)
    cv.rect(hc + 2, 46, 9, 9, g1)
    # ---- torso back ----
    cv.ellipse(hc, 47, 16, 9, navy)
    cv.ellipse(hc, 46, 14, 8, g1)
    cv.rect(hc - 14, 48, 28, 22, g1)
    cv.ellipse(hc - 11, 49, 5, 6, g2)
    cv.ellipse(hc + 12, 49, 5, 6, g2)
    # back center seam and vent
    vline = hc
    cv.rect(vline, 48, 2, 24, navy)
    cv.rect(vline - 2, 52, 5, 18, 19)
    # shoulder blades shading
    cv.rect(hc - 10, 53, 4, 12, g2)
    cv.rect(hc + 8, 53, 4, 12, g2)
    cv.rect(hc - 2, 60, 6, 10, g2)
    # back belt
    cv.rect(hc - 12, 74, 24, 5, navy)
    cv.rect(hc - 2, 75, 6, 3, g2)
    # sleeves (arms slightly out to sides)
    cv.rect(8, 46, 9, 18, g1)
    cv.rect(46, 46, 9, 18, g1)
    cv.rect(9, 47, 5, 14, g2)
    cv.rect(8, 49, 3, 12, navy)
    cv.rect(47, 49, 3, 12, navy)
    # hands behind back
    cv.rect(13, 63, 7, 7, tan)
    cv.rect(47, 63, 7, 7, tan)
    cv.rect(14, 64, 5, 5, shn)
    cv.rect(48, 64, 5, 5, shn)
    cv.rect(11, 61, 8, 4, navy)
    cv.rect(46, 61, 8, 4, navy)
    # coat skirt back
    cv.rect(hc - 16, 80, 12, 22, navy)
    cv.rect(hc + 4, 80, 12, 22, navy)
    cv.rect(hc - 10, 79, 20, 9, g1)
    cv.rect(hc - 8, 86, 8, 16, g2)
    cv.rect(hc + 2, 86, 8, 16, g2)
    cv.rect(hc - 2, 84, 6, 20, navy)   # back vent
    # ---- legs ----
    cv.rect(hc - 12, 92, 11, 24, pale)
    cv.rect(hc + 1, 92, 11, 24, pale)
    cv.rect(hc - 11, 92, 7, 22, wh2)
    cv.rect(hc + 2, 92, 7, 22, wh2)
    cv.rect(hc - 15, 94, 4, 18, g1)
    cv.rect(hc + 11, 94, 4, 18, g1)
    cv.rect(hc - 3, 94, 6, 22, 18)
    # ---- boots (rear: plain, heel) ----
    cv.rect(hc - 13, 112, 13, 8, g2)
    cv.rect(hc + 1, 112, 13, 8, g2)
    cv.rect(hc - 12, 112, 6, 10, g1)
    cv.rect(hc + 3, 112, 6, 10, g1)
    cv.rect(hc - 13, 119, 14, 3, navy)
    cv.rect(hc + 1, 119, 14, 3, navy)
    return cv

f1 = body_front()
f3 = body_rear()
f2 = f1.copy(name="f2").mirror("h")

for i, f in enumerate([f1, f2, f3]):
    print(i, f.stats()["size"], "colors", f.stats()["colors_used"], "visible", f.stats()["visible_pixels"])
finish([f1, f2, f3])
