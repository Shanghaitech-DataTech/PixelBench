# Subway platform, 64x64 — side view, train arriving, screen doors,
# bench, signs, three passengers. Layers flattened so glass tints blend.

bg    = new_canvas(64, 64, name="bg")
train = new_canvas(64, 64, name="train")
glass = new_canvas(64, 64, name="glass")
floor = new_canvas(64, 64, name="floor")
folk  = new_canvas(64, 64, name="people")

INK = "#11141d"   # silhouette
RIM = "#3d4763"   # rim light

# ---------------- background: ceiling / wall / signs / tunnel ----------------
bg.rect(0, 0, 64, 64, "#1f2432")              # base
bg.rect(0, 0, 64, 8, "#141826")               # ceiling
bg.rect(0, 8, 64, 8, "#242a3c")               # wall band
bg.line(0, 7, 63, 7, "#0e1120")               # ceiling edge
bg.rect(6, 1, 50, 1, "#3a3c46")               # light halo top
bg.rect(6, 2, 50, 2, "#f2ecd8")               # main ceiling light
bg.rect(6, 4, 50, 1, "#3a3c46")               # halo bottom
bg.rect(48, 6, 12, 1, "#cfc9b4")              # far small light (depth)
bg.line(20, 8, 20, 15, "#2c3347")             # wall seams
bg.line(44, 8, 44, 15, "#2c3347")
# tunnel mouth beyond the train nose
bg.rect(57, 16, 7, 26, "#0d1017")
bg.rect(59, 18, 5, 22, "#080a10")
bg.line(58, 25, 63, 25, "#232a3a")
bg.line(58, 34, 62, 34, "#232a3a")
bg.set(61, 20, "#e0483c")                     # tunnel signal dot
# speed streaks along the wall (train arriving from the left)
bg.line(20, 9, 34, 9, "#8b96ab")
bg.line(6, 12, 14, 12, "#8b96ab")
bg.line(24, 13, 36, 13, "#8b96ab")
bg.line(40, 11, 48, 11, "#8b96ab")
bg.line(0, 15, 20, 15, "#7c879c")
# hanging station sign (no brand: line number, dashes, arrow)
bg.rect(25, 2, 1, 4, "#0c0e14")               # rods
bg.rect(42, 2, 1, 4, "#0c0e14")
bg.rect(22, 6, 24, 9, "#0d1017")              # board
bg.rect(22, 6, 24, 9, "#aab2c2", fill=False)  # bezel
bg.rect(23, 7, 8, 7, "#38d188")               # line colour box
bg.text(24, 7, "2", "#eafff2", font="5x7")    # line number
bg.rect(32, 8, 7, 1, "#e8ecf4")               # fake text rows
bg.rect(32, 11, 6, 1, "#9fb0c8")
bg.line(39, 10, 42, 10, "#ffb84d")            # direction arrow >
bg.set(43, 9, "#ffb84d"); bg.set(43, 11, "#ffb84d"); bg.set(44, 10, "#ffb84d")
# wall sign (left): line map style
bg.rect(3, 9, 16, 6, "#0d1017")
bg.rect(3, 9, 16, 6, "#aab2c2", fill=False)
bg.rect(5, 10, 5, 2, "#2fb3a3")
bg.rect(11, 10, 5, 1, "#e8ecf4")
bg.rect(5, 13, 9, 1, "#9fb0c8")

# ---------------- train (arriving, nose at right) ----------------
train.rect(0, 16, 50, 24, "#9aa3b2")          # body
train.rect(0, 16, 50, 2, "#c9cfda")           # roof
train.rect(0, 18, 50, 1, "#7c8593")           # gutter
train.rect(0, 21, 50, 7, "#131926")           # window band
for x in range(1, 49, 5):                     # motion streaks in windows
    train.rect(x, 21, 2, 7, "#2c3648")
train.line(15, 21, 15, 39, "#78808e")         # door seams
train.line(31, 21, 31, 39, "#78808e")
train.rect(0, 29, 50, 3, "#2fb3a3")           # livery stripe
train.rect(0, 32, 50, 5, "#8e97a5")           # lower body
train.rect(0, 37, 50, 3, "#5d6572")           # skirt
train.rect(0, 40, 57, 4, "#10131b")           # under-train shadow
train.rect(8, 40, 8, 2, "#05070b")            # bogies
train.rect(34, 40, 8, 2, "#05070b")
# nose
train.rect(50, 17, 7, 23, "#828b9a")
train.rect(50, 17, 7, 1, "#c9cfda")
train.rect(51, 20, 4, 5, "#0e1219")           # cab window
train.rect(50, 29, 7, 3, "#2fb3a3")           # stripe continues
train.rect(50, 37, 7, 3, "#525a68")
train.rect(51, 18, 3, 1, "#ffb84d")           # destination dots
train.set(56, 17, None)                       # rounded corners
train.set(56, 39, None)
train.circle(54, 33, 3, "#fff0b855")          # headlight glow
train.rect(54, 32, 2, 2, "#fff3c0")           # headlight
train.rect(57, 32, 6, 2, "#fff0b826")         # beam into tunnel

# ---------------- platform screen doors (end at x48; nose stays clear) ----
glass.rect(0, 24, 49, 20, "#bcd6e62c")        # glass tint (blends over train)
glass.line(6, 24, 14, 43, "#e6f4ff2e")        # reflections
glass.line(7, 24, 15, 43, "#e6f4ff2e")
glass.line(38, 24, 44, 40, "#e6f4ff2e")
glass.rect(0, 21, 49, 3, "#5c6474")           # top beam
glass.rect(0, 21, 49, 1, "#8d96a6")           # beam highlight
for x in (0, 16, 32, 48):                     # posts
    glass.rect(x, 24, 1, 20, "#525a68")
for x in (2, 18, 34):                         # sliding door frames
    glass.rect(x, 25, 12, 18, "#7b8494", fill=False)
for cx in (8, 24, 40):                        # yellow door-direction decals
    glass.set(cx-4, 27, "#ffd23f"); glass.set(cx-3, 26, "#ffd23f"); glass.set(cx-3, 28, "#ffd23f")
    glass.set(cx+4, 27, "#ffd23f"); glass.set(cx+3, 26, "#ffd23f"); glass.set(cx+3, 28, "#ffd23f")
glass.rect(0, 44, 49, 1, "#4a5262")           # threshold

# ---------------- platform floor ----------------
floor.rect(0, 45, 64, 19, "#3a4150")
floor.rect(0, 56, 64, 8, "#333a48")
floor.rect(0, 60, 64, 4, "#2b313d")
floor.rect(0, 45, 64, 1, "#4d5568")           # platform edge
floor.line(32, 46, 2, 63, "#454d5e")          # perspective tile seams
floor.line(32, 46, 16, 63, "#454d5e")
floor.line(32, 46, 48, 63, "#454d5e")
floor.line(32, 46, 62, 63, "#454d5e")
floor.line(0, 51, 63, 51, "#454d5e")
floor.line(0, 57, 63, 57, "#454d5e")
floor.rect(0, 46, 64, 1, "#ecc63e")           # yellow safety line
floor.ellipse(11, 59, 5, 1, "#252b37")        # contact shadows
floor.ellipse(30, 58, 6, 1, "#252b37")
floor.ellipse(48, 58, 5, 1, "#252b37")

# ---------------- bench + passengers ----------------
folk.rect(40, 48, 14, 2, "#8a6a42")           # bench seat
folk.rect(40, 48, 14, 1, "#a57e4e")           # seat highlight
folk.rect(41, 50, 1, 5, "#3f4652")            # legs
folk.rect(51, 50, 1, 5, "#3f4652")

# A: standing, checking phone
folk.circle(11, 36, 2, INK)
folk.rect(8, 39, 5, 9, INK)
folk.rect(9, 48, 3, 3, INK)
folk.rect(8, 51, 2, 6, INK)
folk.rect(11, 51, 2, 6, INK)
folk.rect(7, 57, 3, 2, INK)
folk.rect(11, 57, 3, 2, INK)
folk.rect(6, 40, 2, 6, INK)                   # arm hanging
folk.set(13, 41, INK); folk.set(13, 42, INK); folk.set(14, 43, INK)
folk.set(15, 42, "#bfe0ff"); folk.set(15, 43, "#bfe0ff")   # phone screen
folk.set(16, 42, "#bfe0ff44")
folk.set(13, 35, RIM); folk.line(13, 40, 13, 45, RIM)

# B: walking, mid-stride, bag on hip
folk.circle(30, 35, 2, INK)
folk.rect(28, 38, 5, 8, INK)
folk.rect(28, 46, 4, 2, INK)
folk.line(31, 48, 34, 55, INK); folk.line(32, 48, 35, 55, INK)
folk.rect(34, 56, 3, 2, INK)
folk.line(29, 48, 26, 54, INK); folk.line(28, 48, 25, 53, INK)
folk.rect(23, 54, 3, 2, INK)
folk.line(32, 40, 34, 44, INK)                # forward arm
folk.line(28, 40, 26, 43, INK)                # back arm
folk.rect(24, 44, 3, 4, "#0a0d14")            # bag
folk.set(32, 34, RIM); folk.line(33, 39, 33, 43, RIM)

# C: sitting on bench
folk.circle(45, 37, 2, INK)
folk.rect(43, 40, 4, 8, INK)
folk.set(44, 48, INK); folk.set(45, 48, INK)
folk.rect(46, 45, 5, 3, INK)                  # thighs
folk.rect(49, 48, 2, 6, INK)                  # shins
folk.rect(48, 54, 3, 2, INK)                  # feet
folk.line(46, 42, 49, 46, INK)                # arm to lap
folk.set(47, 36, RIM); folk.set(51, 45, RIM); folk.set(51, 46, RIM)

# ---------------- composite ----------------
result = flatten([bg, train, glass, floor, folk], name="subway")
print(result.stats_text())
view(result)
finish(result)
