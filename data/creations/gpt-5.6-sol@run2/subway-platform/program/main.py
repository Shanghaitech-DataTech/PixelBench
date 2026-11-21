# 64x64 subway platform scene
W, H = 64, 64

# Compact cool station palette with warm human accents.
C = {
    "ink": "#10151f", "deep": "#182332", "steel": "#26384a",
    "slate": "#3b5364", "mid": "#587181", "pale": "#a8bbc0",
    "white": "#e9eee9", "cyan": "#66c2c7", "cyan2": "#a6e0d7",
    "blue": "#347da0", "navy": "#23475c", "yellow": "#efc14b",
    "orange": "#e77c45", "red": "#bd4d4c", "skin": "#d89a72",
    "skin2": "#8e5d4a", "coat": "#6d4967", "green": "#4f876c",
    "floor": "#50616b", "floor2": "#687982", "glass": "#263e4d",
}

bg = new_canvas(W, H, C["deep"], name="station shell")
# Ceiling and receding beams.
bg.rect(0, 0, 64, 9, C["ink"])
bg.rect(0, 8, 64, 2, C["steel"])
bg.rect(2, 3, 16, 2, C["pale"])
bg.rect(22, 3, 13, 2, C["pale"])
bg.rect(39, 3, 19, 2, C["pale"])
bg.rect(4, 4, 12, 1, C["white"])
bg.rect(24, 4, 9, 1, C["white"])
bg.rect(41, 4, 15, 1, C["white"])
bg.line(0, 10, 17, 17, C["slate"])
bg.line(64, 10, 49, 17, C["slate"])
bg.line(12, 10, 22, 16, C["steel"])
bg.line(52, 10, 45, 16, C["steel"])
# Far wall and generic station sign.
bg.rect(0, 11, 64, 28, C["steel"])
bg.rect(0, 12, 64, 2, C["slate"])
bg.rect(17, 6, 30, 7, C["navy"])
bg.rect(18, 7, 28, 5, C["white"])
bg.text(20, 6, "CENTRAL", C["ink"], spacing=0, font="5x7")
bg.rect(2, 16, 10, 4, C["yellow"])
bg.text(3, 14, "EXIT", C["ink"], spacing=0, font="5x7")
bg.rect(52, 16, 10, 4, C["cyan"])
bg.line(54, 18, 59, 18, C["ink"])
bg.line(57, 16, 59, 18, C["ink"])
bg.line(57, 20, 59, 18, C["ink"])

train = new_canvas(W, H, None, name="arriving train")
# Speed trails and train mass, with a tapered cab at right.
train.rect(0, 19, 10, 2, C["pale"])
train.rect(0, 24, 15, 1, C["cyan"])
train.rect(0, 34, 12, 1, C["white"])
train.poly([(0,18),(53,18),(59,20),(63,25),(63,39),(58,42),(0,42)], C["pale"])
train.rect(0, 19, 54, 3, C["white"])
train.rect(0, 38, 60, 4, C["slate"])
train.rect(0, 36, 61, 2, C["blue"])
# Train windows, blurred highlights, and door divisions.
for x in [3, 17, 31, 45]:
    train.rect(x, 23, 10, 11, C["glass"])
    train.rect(x+1, 24, 8, 1, C["cyan"])
    train.rect(x+2, 26, 5, 1, C["mid"])
    train.rect(x+8, 24, 1, 9, C["ink"])
train.line(55, 21, 61, 26, C["ink"])
train.poly([(55,22),(60,26),(61,34),(54,34)], C["glass"])
train.rect(56, 23, 2, 1, C["cyan2"])
train.rect(61, 29, 2, 3, C["yellow"])
train.rect(7, 20, 9, 1, C["orange"])
train.rect(22, 20, 8, 1, C["orange"])
# Window speed streaks.
train.rect(1, 28, 7, 1, C["slate"])
train.rect(18, 30, 8, 1, C["mid"])
train.rect(32, 25, 6, 1, C["cyan2"])
train.rect(44, 32, 8, 1, C["slate"])

barrier = new_canvas(W, H, None, name="platform screen doors")
# Glass tint represented by sparse rails to preserve train visibility.
barrier.rect(0, 39, 64, 3, C["ink"])
barrier.rect(0, 20, 64, 2, C["slate"])
barrier.rect(0, 22, 64, 1, C["cyan"])
for x in [0, 15, 31, 47, 63]:
    barrier.rect(x, 20, 2, 23, C["ink"])
    barrier.rect(x+2 if x < 63 else x, 23, 1, 15, C["mid"])
# Door seams, caution strip, indicators and handles.
for x in [8, 23, 39, 55]:
    barrier.rect(x, 23, 1, 16, C["slate"])
    barrier.rect(x-2, 31, 2, 1, C["pale"])
for x in range(2, 63, 6):
    barrier.rect(x, 40, 3, 1, C["yellow"])
barrier.rect(14, 18, 4, 2, C["red"])
barrier.rect(46, 18, 4, 2, C["green"])

platform = new_canvas(W, H, None, name="platform and passengers")
platform.rect(0, 42, 64, 22, C["floor"])
platform.rect(0, 42, 64, 3, C["pale"])
platform.rect(0, 45, 64, 3, C["yellow"])
platform.rect(0, 48, 64, 16, C["floor"])
platform.line(0, 63, 40, 48, C["floor2"])
platform.line(27, 63, 45, 48, C["floor2"])
platform.line(63, 58, 52, 48, C["floor2"])
platform.rect(1, 53, 13, 1, C["slate"])
platform.rect(47, 55, 14, 1, C["slate"])
# Tactile paving dots.
for x in range(2, 63, 4):
    platform.set(x, 46, C["ink"])
# Bench with hard readable silhouette.
platform.rect(3, 42, 20, 2, C["ink"])
platform.rect(4, 40, 18, 3, C["orange"])
platform.rect(5, 44, 16, 2, C["red"])
platform.rect(6, 46, 2, 9, C["ink"])
platform.rect(19, 46, 2, 9, C["ink"])
platform.rect(4, 54, 6, 1, C["steel"])
platform.rect(17, 54, 6, 1, C["steel"])

# Passenger 1: seated, leaning forward with elbows on knees.
platform.rect(9, 33, 5, 5, C["ink"])
platform.rect(10, 32, 4, 4, C["skin2"])
platform.set(10, 32, C["ink"]); platform.set(13, 32, C["ink"])
platform.poly([(9,37),(15,37),(17,43),(13,45),(8,42)], C["coat"])
platform.line(14, 39, 19, 44, C["skin2"])
platform.line(10, 43, 15, 46, C["ink"])
platform.line(15, 46, 19, 51, C["ink"])
platform.line(13, 45, 10, 52, C["ink"])
platform.rect(8, 51, 4, 2, C["white"])
platform.rect(18, 50, 4, 2, C["white"])

# Passenger 2: standing and reading a phone.
platform.rect(29, 26, 5, 6, C["ink"])
platform.rect(30, 27, 4, 5, C["skin"])
platform.rect(29, 26, 5, 2, C["ink"])
platform.poly([(28,32),(35,32),(36,44),(27,44)], C["green"])
platform.rect(28, 44, 8, 2, C["ink"])
platform.line(29, 45, 29, 55, C["ink"])
platform.line(34, 45, 35, 55, C["ink"])
platform.rect(26, 54, 5, 2, C["white"])
platform.rect(34, 54, 5, 2, C["white"])
platform.line(28, 34, 31, 38, C["skin"])
platform.line(35, 34, 32, 38, C["skin"])
platform.rect(31, 36, 3, 3, C["cyan2"])
platform.set(32, 37, C["ink"])

# Passenger 3: walking stride, shoulder bag trailing.
platform.rect(48, 29, 5, 6, C["ink"])
platform.rect(49, 30, 4, 5, C["skin2"])
platform.set(52, 31, C["pale"])
platform.poly([(47,35),(53,34),(56,45),(49,47),(45,42)], C["orange"])
platform.line(47, 37, 42, 43, C["skin2"])
platform.line(53, 36, 57, 41, C["skin2"])
platform.line(50, 46, 44, 54, C["ink"])
platform.line(53, 46, 59, 52, C["ink"])
platform.rect(41, 53, 6, 2, C["white"])
platform.rect(58, 51, 5, 2, C["white"])
platform.line(46, 35, 42, 42, C["ink"])
platform.rect(39, 41, 6, 7, C["navy"])
platform.rect(40, 42, 4, 1, C["cyan"])
# Foreground motion accents and edge vignette.
platform.rect(0, 58, 17, 1, C["floor2"])
platform.rect(46, 60, 18, 1, C["steel"])
platform.rect(0, 63, 64, 1, C["ink"])

result = flatten([bg, train, barrier, platform], name="subway platform")
finish(result)
view(result, scale=8, margin=0)
