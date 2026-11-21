from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

PAL = {
    "outline": "#1a0c04",
    "bg0": "#2b1508",
    "bg1": "#3a1f0e",
    "bg2": "#472613",
    "glow1": "#ffd878",
    "glow2": "#d8983a",
    "glow3": "#b06a20",
    "wood_dk": "#201006",
    "wood_mid": "#4e2a12",
    "wood_lt": "#6e3c1c",
    "wood_hi": "#915a2c",
    "shelf_hi": "#9c5c2a",
    "counter": "#7c4622",
    "counter_hi": "#a8662e",
    "front": "#5a2e14",
    "front_dk": "#3f1f0c",
    "front_hi": "#70401c",
    "floor": "#2e1a0c",
    "floor_lt": "#3d2412",
    "seat": "#6b3418",
    "seat_hi": "#8a4a22",
    "leg": "#2c1507",
    "band": "#3a2010",
    "cork": "#a06a38",
    "label": "#d8c89a",
    "grass": "#2f6b3a",
    "grass_hi": "#4d9455",
    "grass_dk": "#1d4226",
    "amber": "#b07a2a",
    "amber_hi": "#d69a4a",
    "amber_dk": "#7a4e18",
    "redw": "#8c2a20",
    "red_hi": "#b04a3a",
    "red_dk": "#5e1812",
    "blue": "#2a4a78",
    "blue_hi": "#4a6a9c",
    "blue_dk": "#1a2e4e",
    "glass": "#d8e8d8",
    "glass_hi": "#f0f8e8",
    "shade": "#c8862a",
    "shade_dk": "#8a5a16",
    "shade_hi": "#e8b04a",
    "bulb": "#ffe9a8",
    "smoke": "#c8b494",
    "smoke_dk": "#9c8a6a",
}
for k, v in PAL.items():
    c.color(v, k)

# ---- WALL (rows 0..63 backdrop) ----
c.rect(0, 0, 64, 64, "outline")
c.rect(1, 0, 62, 64, "bg0")
for y in (2, 6, 10, 18, 22, 26, 30):
    c.rect(0, y, 64, 1, "bg1")
for x in range(5, 64, 7):
    c.line(x, 0, x, 31, "bg0")
for cx in (12, 52):
    c.ellipse(cx, 12, 8, 9, "glow1")
    c.ellipse(cx, 12, 5, 6, "glow2")
    c.ellipse(cx, 13, 3, 4, "glow3")

# ---- SHELVES ----
def shelf(g):
    c.rect(0, g, 64, 1, "shelf_hi")
    c.rect(0, g + 1, 64, 1, "wood_mid")
    c.rect(0, g + 2, 64, 1, "wood_dk")
    c.rect(0, g + 3, 64, 1, "outline")

shelf(14)
shelf(23)

# ---- BOTTLES ----
def bottleA(cx, body, hi, dk, label):
    c.rect(cx - 3, 5, 6, 9, "outline")
    c.rect(cx - 2, 8, 5, 6, body)
    c.rect(cx - 1, 5, 2, 3, dk)
    c.rect(cx - 1, 5, 2, 1, "cork")
    c.rect(cx - 2, 9, 1, 3, hi)
    if label:
        c.rect(cx - 1, 10, 3, 2, "label")
    c.rect(cx - 2, 12, 5, 1, dk)

def bottleB(cx, body, hi, dk, label):
    c.rect(cx - 3, 18, 6, 5, "outline")
    c.rect(cx - 2, 18, 5, 5, body)
    c.rect(cx - 2, 18, 1, 3, hi)
    if label:
        c.rect(cx - 1, 19, 3, 2, "label")
    c.rect(cx - 2, 21, 5, 1, dk)

kinds = [
    ("grass", "grass_hi", "grass_dk", False),
    ("amber", "amber_hi", "amber_dk", True),
    ("redw", "red_hi", "red_dk", False),
    ("blue", "blue_hi", "blue_dk", True),
]
for i in range(15):
    cx = 3 + i * 4
    b, hi, dk, lb = kinds[i % 4]
    bottleA(cx, b, hi, dk, lb)
    bottleB(cx, b, hi, dk, lb)

# ---- LAMPS ----
def lamp(cx):
    c.line(cx, 0, cx, 8, "outline")
    c.rect(cx - 4, 9, 8, 1, "outline")
    c.rect(cx - 4, 10, 8, 1, "shade_hi")
    c.rect(cx - 3, 10, 6, 5, "shade")
    c.rect(cx - 4, 14, 8, 1, "outline")
    c.rect(cx - 2, 15, 4, 1, "bulb")

# ---- COUNTER ----
c.rect(0, 32, 64, 10, "outline")
c.rect(0, 33, 64, 1, "counter_hi")
c.rect(0, 34, 64, 1, "front_hi")
c.rect(0, 35, 64, 5, "front")
c.rect(0, 40, 64, 1, "front_dk")
for x in range(6, 64, 8):
    c.line(x, 35, x, 39, "front_dk")

# ---- FLOOR ----
c.rect(0, 42, 64, 22, "outline")
c.rect(1, 42, 62, 20, "floor")
for y in (46, 50, 54, 58):
    c.rect(0, y, 64, 1, "floor_lt")

# ---- GLASSES ON COUNTER ----
def glass(cx, fill):
    c.rect(cx - 2, 27, 5, 5, "outline")
    c.rect(cx - 1, 27, 3, 1, "glass_hi")
    c.rect(cx - 1, 28, 3, 3, fill)
    c.rect(cx - 1, 28, 1, 2, "glass_hi")

glass(8, "glass")
glass(10, "amber")
glass(21, "glass")
glass(30, "amber")
glass(39, "glass")
glass(46, "amber")

# ---- BARRELS ----
def barrel(cx):
    c.rect(cx - 5, 48, 10, 14, "outline")
    c.rect(cx - 4, 49, 8, 11, "wood_lt")
    c.rect(cx - 4, 49, 1, 7, "wood_hi")
    c.rect(cx - 4, 52, 8, 1, "outline")
    c.rect(cx - 4, 56, 8, 1, "outline")

# ---- STOOLS ----
def stool(cx):
    c.rect(cx - 6, 47, 12, 2, "outline")
    c.rect(cx - 5, 47, 10, 1, "seat_hi")
    c.rect(cx - 1, 49, 2, 9, "outline")
    c.rect(cx - 1, 50, 2, 4, "leg")
    c.rect(cx - 4, 53, 8, 2, "outline")
    c.rect(cx - 3, 53, 6, 1, "leg")
    c.rect(cx - 3, 56, 6, 2, "outline")

# ---- BARRELS & STOOLS ----
barrel(6)
barrel(58)
for sx, sy in ((18, 47), (30, 47), (42, 47)):
    stool(sx)

# ---- LIGHTS IN FRONT ----
lamp(12)
lamp(52)
c.rect(4, 33, 16, 1, "shade_hi")
c.rect(44, 33, 16, 1, "shade_hi")

# ---- SHADOWS & SMOKE ----
for cx in (20, 32, 44):
    c.rect(cx - 5, 60, 10, 1, "outline")
c.path("M 7 5 q 5 -3 10 0 q 5 3 11 0 q 5 -2 9 -1", "smoke", fill=False)
c.path("M 30 3 q 6 -2 12 1 q 5 -1 8 -3", "smoke_dk", fill=False)
c.path("M 44 6 q 6 -3 12 1 q 6 2 10 -2", "smoke_dk", fill=False)
c.path("M 16 2 q 5 -1 9 1 q 5 -2 9 -1", "smoke", fill=False)

print(c.stats_text())
finish(c)
