c = new_canvas(32, 32, name="output")

SKY   = "#c3e5f2"
ROAD  = "#7b868f"
ROAD2 = "#5c666e"
CURB  = "#9aa4ab"
DECK  = "#4a505a"
DECK2 = "#2e333b"
BAR   = "#3a4048"
BARD  = "#23272d"
GRIP  = "#17191c"
WHEEL = "#1b1e22"
TIRE  = "#34393f"
HUB   = "#9aa3ad"
HELM  = "#e04b3c"
HELMD = "#a8332a"
HELML = "#f58d7c"
SKIN  = "#f0c09a"
SKIND = "#cf9b74"
EYE   = "#2a2228"
SHIRT = "#3f7fd0"
SHIRTD= "#2a5a9b"
SHIRTL= "#6ea6ec"
PANT  = "#3b4760"
PANTD = "#283044"
SHOE  = "#eef1f4"
SHOED = "#b4bbc3"


def row(y, x0, x1, col):
    c.rect(x0, y, x1 - x0 + 1, 1, col)


# ---------- background ----------
c.rect(0, 0, 32, 29, SKY)
row(29, 0, 31, CURB)
row(30, 0, 31, ROAD)
row(31, 0, 31, ROAD2)

# ---------- wheels ----------
for wx in (6, 27):
    c.circle(wx, 26, 3, WHEEL)
    c.circle(wx, 26, 1, TIRE)
    c.set(wx, 26, HUB)

# ---------- scooter frame ----------
# deck
row(25, 9, 23, DECK)
row(26, 9, 22, DECK2)
# rear fender hugging the back wheel
for px, py in ((3, 25), (3, 24), (4, 23), (5, 22), (6, 22), (7, 22), (8, 23), (9, 24)):
    c.set(px, py, DECK)
c.set(3, 25, DECK2)
c.set(8, 23, DECK2)
# steering stem, 2 px wide, raked forward at the bottom
for y in range(11, 25):
    xl = 25 + int(round((y - 11) * 2 / 13.0))
    c.set(xl, y, BAR)
    c.set(xl + 1, y, BARD)
# handlebar: seen end-on, short T with a grip toward the viewer
row(11, 23, 28, BAR)
row(12, 25, 26, BARD)
c.rect(23, 11, 2, 1, GRIP)
c.rect(27, 11, 2, 1, GRIP)
c.set(25, 10, BAR)
c.set(26, 10, BARD)

# ---------- rider: legs ----------
# rear leg: thigh back, shin down
row(17, 13, 14, PANT)
row(18, 13, 14, PANT)
row(19, 12, 13, PANT)
row(20, 12, 13, PANT)
row(21, 12, 13, PANT)
row(22, 12, 13, PANT)
row(23, 12, 13, PANT)
for y in range(19, 24):
    c.set(12, y, PANTD)
c.set(13, 17, PANTD)
# front leg
for y in range(17, 24):
    c.set(16, y, PANT)
    c.set(17, y, PANTD)
# shoes
row(24, 11, 14, SHOE)
c.set(14, 24, SHOED)
row(24, 15, 18, SHOE)
c.set(18, 24, SHOED)

# ---------- rider: torso ----------
row(16, 13, 17, SHIRT)
row(15, 13, 18, SHIRT)
row(14, 14, 18, SHIRT)
row(13, 14, 19, SHIRT)
row(12, 15, 19, SHIRT)
# shading: back dark, chest light
for y in (12, 13, 14, 15, 16):
    c.set(13 if y >= 15 else 14 if y >= 13 else 15, y, SHIRTD)
c.set(14, 16, SHIRTD)
c.set(18, 14, SHIRTL)
c.set(18, 15, SHIRTL)
c.set(19, 13, SHIRTL)
c.set(17, 16, SHIRTD)

# ---------- rider: arm ----------
c.set(20, 12, SHIRT)
c.set(20, 13, SHIRTD)
c.set(21, 12, SKIN)
c.set(22, 12, SKIND)
c.set(22, 11, SKIN)

# ---------- rider: head ----------
row(11, 18, 19, SKIND)      # neck
row(8, 17, 20, SKIN)
row(9, 17, 21, SKIN)
row(10, 17, 20, SKIN)
c.set(21, 9, SKIND)         # nose
c.set(19, 9, EYE)
c.set(20, 10, SKIND)        # jaw shade
c.set(17, 10, SKIND)

# ---------- helmet ----------
row(4, 18, 20, HELM)
row(5, 17, 21, HELM)
row(6, 16, 21, HELM)
row(7, 16, 21, HELM)
c.set(18, 4, HELML)
c.set(19, 4, HELML)
c.set(17, 5, HELML)
c.set(16, 6, HELMD)
c.set(16, 7, HELMD)
c.set(21, 7, HELMD)
c.set(22, 7, HELM)          # visor peak
c.set(16, 8, HELMD)         # strap
c.set(20, 5, HELML)         # dome highlight

# ---------- ground shadow ----------
for sx in range(4, 30):
    c.set(sx, 29, ROAD2)
c.set(3, 29, CURB)
c.set(30, 29, CURB)

view(c)
finish(c)
