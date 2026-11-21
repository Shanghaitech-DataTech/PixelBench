from pixelbench_api import *

c = new_canvas(64, 64, name="store")

# --- Palette ---
sky = c.color("#0a1430")
sky_dk = c.color("#060a1c")
glow = c.color("#182048")
silent = c.color("#0c1026")
ground = c.color("#0a1026")
ground_dk = c.color("#070a18")

# Building materials
wall = c.color("#2e3558")
wall_dk = c.color("#232844")
roof = c.color("#1c2240")
frame = c.color("#3a3350")
frame_hi = c.color("#6a6080")

# Warm interior light
L0 = c.color("#fff7d8")   # white-hot
L1 = c.color("#ffe698")   # bright
L2 = c.color("#ffd070")   # warm
L3 = c.color("#e8a848")   # medium
L4 = c.color("#b88030")   # darker
L5 = c.color("#e8b060")   # mid-warm

# Awning stripes
stripe1 = c.color("#d64038")
stripe2 = c.color("#b02020")

# Sign
sign = c.color("#d8c878")
sign_dk = c.color("#907030")

# Rain
rain = c.color("#4a5a8a")
rain_hi = c.color("#7080b0")

# Umbrella rack
umbrella_red = c.color("#c83838")
umbrella_blue = c.color("#3a78c0")
umbrella_pole = c.color("#8890a8")
umbrella_handle = c.color("#a07040")

# Bicycle
bike = c.color("#d05040")
bike_dk = c.color("#884028")
tire = c.color("#181820")
wheel = c.color("#606070")

# Person raincoat
coat = c.color("#ffd740")
coat_dk = c.color("#c89800")
mask = c.color("#c89040")

# Puddle
puddle = c.color("#183060")
puddle_hi = c.color("#285088")
reflect = c.color("#ffe698")
ref_dk = c.color("#d0a850")

# Street lamp glow
lamp = c.color("#ffd880")
lamp_core = c.color("#fff0b0")

# --- Base ---
c.rect(0, 0, 64, 64, sky)
# Night sky gradient bands
c.rect(0, 0, 64, 10, sky_dk)
c.rect(0, 10, 64, 5, sky)
# horizon glow band
c.rect(0, 15, 64, 4, glow)
# ground
c.rect(0, 48, 64, 16, ground)

# --- Distant city silhouettes ---
# Low buildings far left
c.rect(0, 28, 6, 20, silent)
c.rect(2, 25, 3, 13, silent)
c.rect(5, 31, 4, 12, silent)
# far right
c.rect(52, 26, 12, 22, silent)
c.rect(56, 23, 8, 15, silent)
# scattered distant glowing windows
for wx, wy in [(1,31),(3,27),(7,34),(54,30),(57,26),(59,29),(61,25),(55,33),(60,32)]:
    c.set(wx, wy, ref_dk)

# --- Store building ---
# Main wall
c.rect(8, 20, 42, 28, wall)
# building outline top
c.rect(8, 20, 42, 1, frame_hi)

# --- Sign panel above ---
c.rect(24, 10, 16, 9, sign)
c.rect(24, 10, 16, 1, sign_dk)
c.rect(24, 18, 16, 1, sign_dk)
# generic symbol (bell/24h style)
c.poly([(31,13),(35,13),(36,16),(28,16)], sign_dk)
# sign mount poles
c.line(26, 19, 26, 22, frame)
c.line(38, 19, 38, 22, frame)
# roof cap under sign
c.rect(8, 20, 42, 2, frame_hi)

# --- Awning overhang ---
c.rect(4, 15, 56, 5, roof)
# awning stripes
for x in range(4, 60, 8):
    c.rect(x, 15, 4, 4, stripe1)
    c.rect(x+4, 15, 4, 4, stripe2)
# awning edge
c.rect(4, 19, 56, 1, frame_hi)

# --- Store front facade below awning ---
# Left window (big)
c.rect(9, 22, 22, 24, L2)          # window opening
# interior: ceiling light glow at top
c.rect(10, 23, 20, 3, L1)
# shelves (horizontal lines) and goods
c.rect(10, 27, 20, 1, L4)          # shelf top 1
c.rect(10, 31, 20, 1, L4)          # shelf top 2
c.rect(10, 35, 20, 1, L4)          # shelf 3
c.rect(10, 39, 20, 1, L4)
# goods silhouettes on shelves (small vertical marks)
for gx, gy in [(11,26),(14,26),(17,26),(20,26),(23,26),(26,26),(12,30),(16,30),(20,30),(24,30),(27,30),(11,34),(15,34),(19,34),(23,34),(26,34)]:
    c.set(gx, gy, L5)
for gx in [(11,38),(14,38),(18,38),(22,38),(26,38)]:
    c.set(gx[0], gx[1], L5)
# floor inside window darker
c.rect(10, 42, 20, 3, L4)
# bright highlight reflections on glass
c.rect(9, 22, 22, 1, L0)
c.rect(9, 23, 1, 20, L0)

# --- Door ---
# Door frame area
c.rect(32, 20, 8, 28, frame_hi)
# door panel with glass
c.rect(33, 23, 6, 22, L2)          # door glass warm
# door glass highlights
c.rect(34, 25, 2, 4, L0)
c.rect(36, 29, 2, 4, L0)
# door bottom panel
c.rect(33, 40, 6, 4, frame)
# door handle
c.line(37, 30, 37, 32, frame_hi)

# --- Right window ---
c.rect(41, 22, 14, 24, L2)
c.rect(42, 23, 12, 3, L1)
# shelves
c.rect(42, 28, 12, 1, L4)
c.rect(42, 32, 12, 1, L4)
c.rect(42, 36, 12, 1, L4)
# goods
for gx, gy in [(43,27),(46,27),(49,27),(52,27),(44,31),(48,31),(51,31),(43,35),(47,35),(50,35),(53,35)]:
    c.set(gx, gy, L5)
c.rect(42, 42, 12, 3, L4)
# highlights
c.rect(41, 22, 14, 1, L0)

# --- Store sign strip (generic, no brand; just "24" feel but no letters) ---
# small decor strip between building top and windows
c.rect(9, 20, 44, 1, frame)

# --- Light spill onto ground from windows ---
c.rect(10, 47, 21, 2, L4)     # under left window
c.rect(11, 49, 19, 2, L3)
c.rect(42, 47, 13, 2, L4)
c.rect(43, 49, 11, 2, L3)

# --- Street lamp on far left ---
c.line(2, 8, 2, 38, frame_hi)
c.line(0, 38, 8, 38, frame_hi)
# lamp head
c.rect(1, 8, 3, 3, lamp_core)
c.circle(3, 10, 2, lamp)
# lamp glow ring
c.circle(4, 12, 3, ref_dk)

# --- Umbrella rack (left side, next to lamp) ---
# rack post
c.line(6, 34, 6, 44, umbrella_pole)
# rack arms
c.line(6, 35, 9, 35, umbrella_pole)
# red umbrella leaning
c.poly([(3,32),(9,32),(6,39)], umbrella_red)
c.poly([(7,32),(11,32),(9,38)], umbrella_blue)
# handles at bottom
c.line(6, 39, 6, 41, umbrella_handle)
c.line(9, 38, 9, 40, umbrella_handle)
# rack base
c.rect(5, 44, 3, 1, frame)

# --- Bicycle parked on right ---
# rear wheel
c.circle(54, 47, 3, tire)
c.circle(54, 47, 2, wheel)
c.circle(54, 47, 1, tire)
# front wheel
c.circle(60, 45, 3, tire)
c.circle(60, 45, 2, wheel)
c.circle(60, 45, 1, tire)
# frame
c.line(54, 47, 56, 43, bike)
c.line(56, 43, 59, 42, bike)
c.line(59, 42, 60, 45, bike)
c.line(56, 43, 59, 45, bike)
c.line(59, 45, 60, 45, bike)
c.line(54, 47, 57, 45, bike)
# handlebar
c.line(57, 40, 61, 41, bike_dk)
c.line(59, 42, 59, 40, bike_dk)
# seat
c.rect(55, 41, 3, 1, bike_dk)
c.line(56, 43, 56, 41, bike_dk)
# kickstand
c.line(58, 44, 58, 47, wheel)
# wheel shine
c.set(54, 46, wheel)
c.set(60, 44, wheel)

# --- Person in yellow raincoat entering (in front of door) ---
# Position person at x=34-40, standing on ground around y=38-48
# body
c.poly([(34,36),(41,36),(42,46),(33,46)], coat)
# hood
c.circle(37, 35, 3, coat)
c.circle(37, 35, 2, coat)
# face shadow under hood
c.circle(38, 36, 1, mask)
# coat folds (darker)
c.line(35, 40, 35, 46, coat_dk)
c.line(40, 40, 40, 46, coat_dk)
# arm reaching for door
c.line(38, 39, 35, 42, coat)
c.line(35, 42, 34, 43, coat_dk)
# legs
c.line(36, 46, 35, 49, coat_dk)
c.line(39, 46, 40, 49, coat_dk)

# --- Puddles with reflections ---
# center puddle (main reflection of store)
c.ellipse(30, 56, 10, 4, puddle)
c.ellipse(30, 56, 9, 3, puddle_hi)
# reflection streaks of window light
c.line(24, 54, 36, 54, reflect)
c.line(26, 56, 34, 56, ref_dk)
c.line(25, 57, 33, 57, reflect)
# puddle left
c.ellipse(16, 58, 5, 2, puddle)
c.rect(13, 58, 6, 1, ref_dk)
# puddle right
c.ellipse(50, 58, 6, 2, puddle)
c.line(46, 58, 53, 58, ref_dk)
# puddle reflection of sign
c.ellipse(31, 51, 6, 1, puddle_hi)
c.rect(27, 51, 8, 1, ref_dk)
c.rect(29, 50, 4, 1, reflect)

# --- Rain ---
rain_pts = [
    (3,2),(6,6),(12,3),(18,7),(24,2),(33,4),(40,8),(46,3),(55,5),(60,9),
    (9,11),(15,14),(28,10),(36,12),(43,15),(50,11),(58,16),(62,13),
    (4,20),(11,17),(19,21),(26,18),(34,20),(41,16),(53,20),(59,23),
    (7,25),(14,27),(38,24),(48,26),(56,28),(5,31),(16,30),(25,25),
    (8,36),(13,38),(20,35),(29,32),(36,37),(44,35),(51,33),(59,36),
    (2,40),(11,41),(17,44),(25,40),(33,43),(40,41),(47,44),(55,41),
    (6,46),(14,48),(23,46),(30,48),(37,46),(45,48),(53,47),(60,46),
    (3,52),(10,51),(18,53),(26,51),(34,54),(42,53),(49,52),(57,54),
    (8,58),(15,56),(22,59),(31,58),(39,57),(46,59),(54,58),(62,57),
]
for (x, y) in rain_pts:
    c.set(x, y, rain)
# brighter rain streaks (catch light)
for (x, y) in [(5,4),(21,5),(37,9),(50,7),(16,16),(27,22),(44,25),(3,34),(57,31),(12,42),(28,38),(61,20)]:
    c.set(x, y, rain_hi)

# --- final build save and report ---
save("store", c)
print(c.stats_text())
finish(c)
