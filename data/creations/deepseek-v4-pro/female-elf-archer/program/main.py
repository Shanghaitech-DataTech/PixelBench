from pixelbench_api import *

c = new_canvas(64, 64, name="output")

# ---------- palette ----------
outline  = c.color("#26262e", "outline")
skin     = c.color("#e9b78f", "skin")
skin_s   = c.color("#c9926b", "skin_shadow")
skin_l   = c.color("#f4d2ae", "skin_light")
hair_d   = c.color("#1f5a38", "hair_dark")
hair     = c.color("#2f7d4d", "hair_mid")
hair_l   = c.color("#4aa869", "hair_light")
hair_hi  = c.color("#74c98f", "hair_hi")
out_d    = c.color("#3f7d4e", "outfit_dark")
out      = c.color("#63a06c", "outfit_mid")
out_l    = c.color("#8fc292", "outfit_light")
out_hi   = c.color("#bcdcae", "outfit_hi")
leather_d= c.color("#5e4026", "leather_dark")
leather  = c.color("#7d5a34", "leather_mid")
leather_l= c.color("#9a7444", "leather_light")
wood_d   = c.color("#5a3a1e", "wood_dark")
wood     = c.color("#7c5328", "wood_mid")
wood_l   = c.color("#9c6e38", "wood_light")
white    = c.color("#ffffff", "white")
eye      = c.color("#3fae6a", "eye_green")
dark     = c.color("#1c2a20", "dark")
fletch_r = c.color("#c05040", "fletch_red")
string_c = c.color("#e8e0cc", "string")

# ---------- back hair (long, behind body) ----------
c.ellipse(31, 26, 11, 18, hair_d, fill=True)
c.ellipse(31, 25, 10, 16, hair, fill=True)

# ---------- bow on back (behind body) ----------
c.path("M 46 15 C 40 23 32 35 21 48", wood_d, fill=False)
c.path("M 45 15 C 39 23 31 35 21 48", wood, fill=False)
c.path("M 44 15 C 38 22 30 34 21 48", wood_l, fill=False)
c.line(45, 15, 21, 48, string_c)

# ---------- quiver + arrows (behind body, left side) ----------
c.rect(15, 26, 7, 19, leather_d, fill=True)
c.rect(16, 27, 5, 17, leather, fill=True)
c.rect(16, 27, 1, 17, leather_l, fill=True)
# arrow shafts
c.line(16, 27, 16, 16, wood)
c.line(18, 27, 18, 15, wood_l)
c.line(20, 27, 20, 17, wood)
# fletching
c.rect(15, 14, 2, 3, white)
c.rect(17, 13, 2, 3, fletch_r)
c.rect(19, 15, 2, 3, white)

# ---------- torso ----------
c.poly([(21,25),(41,25),(39,34),(37,40),(36,42),(31,43),(26,42),(25,40),(23,34)], outline, fill=True)
c.poly([(23,26),(39,26),(37,34),(35,39),(31,41),(27,39),(25,34)], out, fill=True)
c.poly([(25,28),(29,27),(28,35),(25,36)], out_l, fill=True)

# neck (over torso top)
c.rect(28, 25, 6, 2, skin, fill=True)
c.rect(28, 25, 2, 2, skin_l, fill=True)
c.rect(32, 25, 2, 2, skin_s, fill=True)

# ---------- arms ----------
c.rect(19, 26, 5, 17, outline, fill=True)
c.rect(38, 26, 5, 17, outline, fill=True)
c.rect(20, 27, 3, 15, skin, fill=True)
c.rect(39, 27, 3, 15, skin, fill=True)
c.rect(20, 27, 1, 15, skin_l, fill=True)
c.rect(41, 27, 1, 15, skin_s, fill=True)
# hands
c.rect(19, 42, 5, 4, outline, fill=True)
c.rect(38, 42, 5, 4, outline, fill=True)
c.rect(20, 43, 3, 2, skin, fill=True)
c.rect(39, 43, 3, 2, skin, fill=True)

# ---------- legs ----------
c.rect(25, 42, 8, 16, outline, fill=True)
c.rect(33, 42, 8, 16, outline, fill=True)
c.rect(26, 43, 6, 14, out_d, fill=True)
c.rect(34, 43, 6, 14, out_d, fill=True)
c.rect(26, 43, 1, 14, out, fill=True)
c.rect(34, 43, 1, 14, out, fill=True)

# ---------- boots ----------
c.rect(24, 57, 9, 4, outline, fill=True)
c.rect(33, 57, 9, 4, outline, fill=True)
c.rect(25, 58, 7, 3, leather_d, fill=True)
c.rect(34, 58, 7, 3, leather_d, fill=True)
c.rect(25, 58, 2, 3, leather, fill=True)
c.rect(34, 58, 2, 3, leather, fill=True)

# ---------- head / hair / face (hand placed) ----------
sym = {
    '.': None,
    'O': outline,
    's': skin,
    'c': skin_s,
    'd': skin_l,
    'e': hair_d,
    'f': hair,
    'g': hair_l,
    'h': hair_hi,
    't': eye,
    'w': white,
    'u': dark,
}

head_rows = [
    (29, "hhhh"),
    (27, "gghhhhgg"),
    (26, "egghhhhgge"),
    (25, "effgggggffe"),
    (24, "effgggggggffe"),
    (23, "e" + "f"*14 + "e"),
    (23, "e" + "f"*14 + "e"),
    (23, "e" + "f"*14 + "e"),
    (23, "efff" + "s"*8 + "fffe"),
    (23, "eff" + "s"*10 + "ffe"),
    (23, "efsssfssssfssfe"),
    (22, "effeesssseessssffe"),
    (22, "effwtsssswtssssffe"),
    (22, "effttssssttssssffe"),
    (22, "effsscsssssssssffe"),
    (22, "effsscsssssssssffe"),
    (22, "effssuussssssssffe"),
    (23, "ef" + "s"*12 + "fe"),
    (23, "efccsssssssccfe"),
    (24, "efcssssssscfe"),
    (23, "ef" + "s"*11 + "fe"),
]

def draw_map(x0, y0, rows):
    for dy, (sx, content) in enumerate(rows):
        x = sx
        for ch in content:
            col = sym.get(ch)
            if col is not None:
                c.set(x, y0 + dy, col)
            x += 1

draw_map(0, 4, head_rows)

# ---------- pointed ears (over hair) ----------
# left (near) ear, high pointed
c.poly([(25,12),(17,7),(23,14)], outline, fill=True)
c.poly([(24,12),(18,8),(22,13)], skin, fill=True)
# right (far) ear
c.poly([(37,12),(45,7),(39,14)], outline, fill=True)
c.poly([(38,12),(44,8),(40,13)], skin, fill=True)

# ---------- hair light streaks on side strands ----------
for y in range(15, 23):
    c.set(23, y, hair_l)
    c.set(38, y, hair_l)

# ---------- outfit details ----------
# quiver strap across chest
c.line(17, 26, 36, 38, leather_d)
c.line(18, 27, 35, 37, leather)
# belt
c.rect(26, 38, 10, 2, leather_d, fill=True)
c.rect(26, 38, 10, 1, leather, fill=True)
# buckle
c.rect(30, 37, 2, 3, wood_l, fill=True)

print(c.stats_text())
print(c.matrix_text())
finish(c)
