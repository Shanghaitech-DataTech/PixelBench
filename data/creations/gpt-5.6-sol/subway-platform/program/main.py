# 64x64 subway platform scene
bg = new_canvas(64, 64, "#101620", name="tunnel")
train = new_canvas(64, 64, None, name="arriving train")
station = new_canvas(64, 64, None, name="platform doors")
people = new_canvas(64, 64, None, name="passengers and furniture")

# Compact urban-night palette.
ink = "#101620"
deep = "#17212c"
navy = "#20303c"
steel = "#394b56"
steel2 = "#50636b"
lightsteel = "#8fa0a2"
silver = "#b9c3bf"
cream = "#e5dfc8"
white = "#f4edcf"
yellow = "#f5c84b"
red = "#d84a3f"
red_dark = "#84333b"
teal = "#3f9a98"
cyan = "#82c7bd"
blue = "#477d9d"
skin1 = "#d99a6c"
skin2 = "#8c5a45"
skin3 = "#efc28e"
coat1 = "#c8564c"
coat2 = "#386786"
coat3 = "#d6a23f"
shoe = "#20242a"

# Tunnel ceiling, conduit and distant strips.
bg.rect(0, 0, 64, 7, "#0a0f17")
bg.rect(0, 7, 64, 2, steel)
bg.rect(0, 10, 64, 2, navy)
bg.line(0, 13, 63, 13, "#273844")
bg.rect(2, 3, 15, 2, cream)
bg.rect(3, 5, 13, 1, "#877f6e")
bg.rect(45, 3, 14, 2, cream)
bg.rect(46, 5, 12, 1, "#877f6e")
# Speed streaks in the dark approach.
for x, y, w, col in [(1,17,9,steel),(4,21,13,lightsteel),(0,26,7,blue),(2,31,15,red_dark),(0,35,11,steel2)]:
    bg.rect(x, y, w, 1, col)

# Train body rushing in from left, with tapered nose and horizontal bands.
train.poly([(0,15),(5,13),(63,14),(63,39),(0,39)], silver)
train.rect(0, 16, 64, 2, cream)
train.rect(0, 35, 64, 4, steel2)
train.rect(0, 33, 64, 2, red)
train.rect(0, 19, 64, 2, lightsteel)
# Windshield / window ribbon, strongest detail toward right.
train.poly([(1,22),(8,20),(15,20),(15,31),(1,31)], "#243743")
train.rect(3, 23, 10, 1, blue)
train.rect(2, 29, 11, 1, "#18252f")
for x in [18, 30, 42, 54]:
    train.rect(x, 21, 9, 11, "#1a2a35")
    train.rect(x+1, 22, 7, 1, "#41606c")
    train.rect(x+7, 23, 1, 7, "#263d49")
# Blurred interior lights and passing figures.
for x in [20, 32, 44, 56]:
    train.rect(x, 23, 5, 2, yellow)
    train.rect(x+1, 25, 3, 1, "#8e7542")
train.rect(24, 27, 2, 5, "#38464b")
train.rect(36, 26, 2, 6, "#38464b")
train.rect(58, 27, 2, 5, "#38464b")
# Kinetic highlights on the carriage.
train.rect(0, 17, 22, 1, white)
train.rect(0, 37, 27, 1, "#829094")
train.rect(7, 34, 15, 1, "#ef7261")

# Overhead station sign and directional plaques.
station.rect(22, 1, 20, 8, "#26343d")
station.rect(23, 2, 18, 6, "#d8d7c5")
station.text(24, 2, "NORTH", ink, font="5x7", spacing=0)
station.rect(46, 8, 16, 6, blue)
station.text(47, 8, "WAY", white, font="5x7", spacing=0)
station.poly([(44,10),(46,8),(46,12)], yellow)
# Platform screen-door header and base.
station.rect(0, 12, 64, 2, "#60737a")
station.rect(0, 14, 64, 1, "#b5c1bb")
station.rect(0, 39, 64, 3, "#26363e")
station.rect(0, 39, 64, 1, "#93a19c")
# Glass tint strips and door frames.
station.rect(0, 15, 64, 1, "#87a6a344")
station.rect(0, 37, 64, 2, "#6f8f8b44")
for x in [0, 16, 32, 48, 63]:
    station.rect(x, 12, 2 if x < 63 else 1, 30, "#334750")
    if x < 63:
        station.rect(x+2, 15, 1, 23, "#98aaa7")
# Door joins, warning decals, handles.
for x in [8, 24, 40, 56]:
    station.rect(x, 15, 1, 24, "#526a70")
    station.rect(x-1, 28, 1, 3, "#d9ddd1")
    station.rect(x+1, 28, 1, 3, "#d9ddd1")
for x in [4, 20, 36, 52]:
    station.rect(x, 17, 8, 1, "#d6b84c")
    station.set(x, 18, yellow)
# Small glass reflections.
station.line(13, 17, 10, 25, "#b9d4cd66")
station.line(47, 18, 44, 26, "#b9d4cd66")
station.line(62, 20, 59, 28, "#b9d4cd66")

# Platform floor with strong depth lines.
station.rect(0, 42, 64, 22, "#586066")
station.rect(0, 42, 64, 3, yellow)
station.rect(0, 45, 64, 2, "#d39c37")
station.rect(0, 47, 64, 17, "#4a5156")
station.line(0, 51, 63, 48, "#697177")
station.line(0, 59, 63, 52, "#697177")
station.line(14, 63, 24, 47, "#323a40")
station.line(39, 63, 42, 47, "#323a40")
station.line(60, 63, 57, 47, "#323a40")
station.rect(0, 62, 64, 2, "#30373c")
# Tactile paving pixels.
for x in range(1,64,4):
    station.set(x, 43, "#fff09a")

# Bench, right foreground.
people.rect(43, 43, 18, 3, "#24323a")
people.rect(44, 40, 16, 3, teal)
people.rect(44, 41, 16, 1, cyan)
people.rect(45, 46, 2, 8, "#26343a")
people.rect(57, 46, 2, 8, "#26343a")
people.rect(42, 53, 7, 2, "#30383c")
people.rect(55, 53, 7, 2, "#30383c")

# Passenger 1: standing left, leaning toward train, backpack and raised arm.
people.rect(9, 23, 5, 5, skin2)
people.rect(10, 22, 4, 2, ink)
people.set(8, 24, ink)
people.poly([(8,28),(14,28),(16,39),(13,42),(8,40),(7,32)], coat1)
people.rect(6, 29, 3, 9, "#732f39")
people.rect(5, 30, 2, 7, red_dark)
people.line(13, 29, 15, 23, skin2)
people.rect(15, 21, 2, 4, skin2)
people.set(16, 20, skin2)
people.poly([(9,40),(12,40),(11,51),(8,51)], deep)
people.poly([(13,40),(16,40),(17,50),(14,50)], deep)
people.rect(6, 50, 6, 2, shoe)
people.rect(14, 49, 6, 2, shoe)
# Backpack profile.
people.rect(5, 29, 3, 8, navy)
people.rect(4, 31, 2, 6, "#283a49")

# Passenger 2: walking mid-frame, scarf, long stride, carrying tote.
people.rect(27, 25, 5, 5, skin3)
people.rect(26, 24, 6, 2, "#40302c")
people.set(32, 26, "#40302c")
people.poly([(26,30),(33,30),(35,41),(31,43),(25,41)], coat2)
people.rect(25, 30, 8, 2, cyan)
people.line(26, 32, 22, 39, skin3)
people.line(33, 32, 37, 38, skin3)
people.rect(36, 37, 5, 8, "#c38c35")
people.rect(37, 36, 3, 2, coat3)
people.poly([(26,40),(30,41),(27,51),(23,54),(21,52),(25,48)], "#223540")
people.poly([(31,41),(34,41),(38,51),(36,53),(32,48)], "#223540")
people.rect(19, 52, 7, 2, shoe)
people.rect(35, 51, 6, 2, shoe)

# Passenger 3: seated, hunched over phone.
people.rect(49, 31, 5, 5, skin1)
people.rect(48, 30, 6, 3, "#2b2024")
people.set(54, 32, "#2b2024")
people.poly([(47,36),(53,35),(56,42),(53,47),(47,44)], coat3)
people.line(49, 37, 54, 40, skin1)
people.line(54, 40, 57, 38, skin1)
people.rect(56, 36, 2, 3, "#9bc6c2")
people.poly([(49,44),(54,44),(58,48),(57,51),(53,48),(48,47)], navy)
people.rect(56, 49, 6, 2, shoe)
people.rect(46, 46, 7, 3, "#273640")
# Grounding shadows.
people.rect(6, 54, 14, 2, "#252c31aa")
people.rect(19, 55, 23, 2, "#252c31aa")
people.rect(43, 55, 20, 2, "#252c31aa")

result = flatten([bg, train, station, people], name="subway-platform")
assert tuple(result.stats()["size"]) == (64, 64)
assert result.stats()["colors_used"] <= 86
view(result, scale=8, margin=0)
finish(result)
