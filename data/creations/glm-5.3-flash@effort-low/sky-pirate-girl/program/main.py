from pixelbench_api import *

c = new_canvas(64, 64, background="#8ec8e8", name="sky-pirate-girl")

# --- palette ---
SKIN   = c.color("#f6d3b3")
SKINSH = c.color("#e0b391")
HAIR   = c.color("#6b4226")
HAIRHL = c.color("#8a5a34")
HAIRSH = c.color("#4c2c18")
NAVY   = c.color("#243a5e")
NAVYL  = c.color("#33507e")
NAVYSH = c.color("#182742")
RED    = c.color("#c8362e")
REDD   = c.color("#96221f")
BRASS  = c.color("#d9a441")
LENS   = c.color("#7fd4e8")
LENSD  = c.color("#3f8ba8")
EYE    = c.color("#2b2330")
WHITE  = c.color("#ffffff")
CLOUD  = c.color("#eaf6fb")
SKY2   = c.color("#a9d8ee")
GOLD   = c.color("#e8c56a")
BELT   = c.color("#5a4632")

# --- sky background ---
for y in range(64):
    t = y / 63
    col = c.color("#bfe3f2") if y < 8 else None
for y in range(64):
    # vertical gradient by bands
    if y < 12: col = "#bfe3f2"
    elif y < 28: col = "#a9d8ee"
    elif y < 46: col = "#8ec8e8"
    else: col = "#79b8de"
    c.line(0, y, 63, y, col)

# clouds
c.ellipse(12, 10, 7, 2, CLOUD)
c.ellipse(17, 9, 4, 2, CLOUD)
c.ellipse(52, 20, 6, 2, CLOUD)
c.ellipse(55, 18, 3, 2, CLOUD)
c.ellipse(6, 34, 5, 2, CLOUD)
c.ellipse(58, 44, 5, 2, CLOUD)

# --- hair back mass (behind face) ---
c.ellipse(32, 25, 11, 12, HAIR)
# wind-swept strands to the right
c.line(42, 18, 52, 14, HAIR)
c.line(43, 22, 55, 20, HAIRHL)
c.line(42, 26, 54, 27, HAIR)
c.line(41, 30, 51, 33, HAIRSH)
c.line(43, 21, 52, 17, HAIRHL)
c.line(20, 18, 12, 22, HAIR)
c.line(21, 24, 11, 27, HAIRSH)

# --- neck & shoulders / coat ---
c.rect(29, 38, 6, 6, SKINSH)          # neck
c.rect(30, 38, 4, 5, SKIN)
# coat body
c.poly([(16,64),(18,50),(24,44),(40,44),(46,50),(48,64)], NAVY)
# coat highlight left
c.poly([(18,64),(19,52),(24,46),(27,46),(25,64)], NAVYL)
# lapels
c.poly([(26,44),(30,50),(26,56),(23,50)], NAVYSH)
c.poly([(38,44),(34,50),(38,56),(41,50)], NAVYSH)
# collar
c.line(24,45,29,43, NAVYSH)
c.line(40,45,35,43, NAVYSH)
# buttons
c.set(32, 52, GOLD); c.set(32, 56, GOLD); c.set(32, 60, GOLD)
# belt
c.line(20, 62, 44, 62, BELT)

# --- scarf ---
c.rect(26, 41, 12, 5, RED)
c.rect(26, 41, 12, 1, REDD)
# scarf tail flying right
c.poly([(38,42),(52,44),(54,47),(50,48),(38,46)], RED)
c.line(39,46,52,48, REDD)
c.poly([(37,43),(48,40),(50,42),(38,45)], REDD)

# --- face ---
c.ellipse(32, 27, 9, 9, SKIN)
c.ellipse(32, 29, 7, 6, SKIN)   # jaw/chin
# shading right side
c.line(40, 22, 41, 30, SKINSH)
c.set(40, 31, SKINSH)

# --- bangs (over forehead) ---
c.poly([(22,26),(24,19),(30,16),(38,16),(43,20),(42,26),(38,22),(34,25),(30,21),(26,25)], HAIR)
c.line(30,17,32,22, HAIRHL)
c.line(36,17,37,23, HAIRHL)
c.line(26,19,27,24, HAIRSH)

# side locks
c.poly([(22,25),(21,33),(24,36),(25,28)], HAIR)
c.poly([(42,25),(43,34),(40,37),(40,28)], HAIR)
c.line(22,28,23,34, HAIRHL)

# --- goggles on bangs ---
c.ellipse(27, 19, 3, 2, BRASS)
c.ellipse(37, 19, 3, 2, BRASS)
c.ellipse(27, 19, 2, 1, LENS)
c.ellipse(37, 19, 2, 1, LENS)
c.set(26, 19, LENS)
c.set(36, 19, LENS)
c.line(29, 19, 35, 19, BRASS)   # strap across

# --- eyes (three-quarter, looking left-ish) ---
for ex, ey in ((28, 30), (36, 30)):
    c.rect(ex, ey, 3, 3, EYE)
    c.set(ex, ey, WHITE)
    c.set(ex+2, ey+2, WHITE)
# eyebrows
c.line(27, 27, 30, 27, HAIRSH)
c.line(35, 27, 38, 27, HAIRSH)
# nose + mouth
c.set(32, 33, SKINSH)
c.line(31, 35, 33, 35, "#c46a5a")

# blush
c.set(26, 32, "#f0b090")
c.set(38, 32, "#f0b090")

print(c.stats_text())
print(c.matrix_text(region=(0,0,64,64)))
