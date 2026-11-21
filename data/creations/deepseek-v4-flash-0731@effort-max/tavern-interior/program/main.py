from pixelbench_api import *

W = 64
c = new_canvas(W, W, name="tavern")
OUTC = c.color("#100905")

# ---------------- ceiling & wall ----------------
c.rect(0, 0, W, 7, "#150c06")
c.rect(0, 5, W, 2, "#0f0804")
c.rect(0, 7, W, 30, "#2a1b11")
for x in (6, 14, 22, 30, 38, 46, 54, 61):
    c.rect(x, 8, 1, 2, "#201309")

# warm lamp glow pools on the wall (drawn behind everything)
for cx in (19, 45):
    c.circle(cx, 17, 11, "#553514")
    c.circle(cx, 17, 6, "#8a501c")

# ---------------- upper shelf + bottles ----------------
c.rect(9, 22, 46, 1, "#7a4e24")
c.rect(9, 23, 46, 1, "#4e3118")
c.rect(9, 24, 46, 1, "#180e06")


def bottle(cx, body, liq, cap):
    x = cx - 2
    c.rect(x - 1, 11, 6, 13, OUTC)
    c.rect(x, 12, 4, 1, cap)
    c.rect(x + 1, 13, 2, 3, body)
    c.rect(x, 16, 4, 7, body)
    c.rect(x, 17, 4, 4, liq)
    c.rect(x, 17, 1, 3, "#e8e8de")


BOTS = [
    (13, "#2f7a36", "#1f5c24", "#8f9499"),
    (17, "#b07a26", "#8a5c1c", "#6b4a24"),
    (22, "#2a5f96", "#1c4170", "#8f9499"),
    (26, "#96362a", "#c98f2e", "#6b4a24"),
    (31, "#2f7a36", "#7a4a1a", "#8f9499"),
    (36, "#b07a26", "#8a5c1c", "#6b4a24"),
    (41, "#2a5f96", "#c98f2e", "#8f9499"),
    (46, "#96362a", "#7a4a1a", "#6b4a24"),
    (50, "#6b4120", "#1f5c24", "#8f9499"),
]
for b in BOTS:
    bottle(*b)

# ---------------- lower shelf + mugs ----------------
c.rect(11, 29, 42, 1, "#7a4e24")
c.rect(11, 30, 42, 1, "#4e3118")
c.rect(11, 31, 42, 1, "#180e06")


def mug(cx, base):
    x = cx - 2
    c.rect(x - 1, base - 6, 7, 7, OUTC)
    c.rect(x, base - 5, 5, 5, "#7a5326")
    c.rect(x, base - 5, 5, 1, "#9a6a30")
    c.rect(x, base - 3, 5, 1, "#5e3d1c")
    c.rect(x + 4, base - 4, 2, 3, OUTC)
    c.rect(x + 4, base - 3, 1, 1, "#7a5326")


for cx in (16, 21, 27, 33, 39, 45):
    mug(cx, 29)

# ---------------- barrels behind the bar ----------------
for cx in (6, 57):
    c.ellipse(cx, 32, 6, 6, OUTC)
    c.ellipse(cx, 32, 5, 5, "#6b4120")
    c.ellipse(cx, 32, 4, 3, "#7a4b20")
    c.ellipse(cx, 32, 3, 2, "#8a5628")
    c.rect(cx - 4, 31, 9, 2, "#3a2412")

# warm dark band near the counter
c.rect(0, 33, W, 5, "#1e1208")

# ---------------- wooden bar ----------------
c.rect(0, 37, W, 1, "#b4773a")
c.rect(0, 38, W, 2, "#8a5a2c")
c.rect(0, 40, W, 1, "#3a2412")
c.rect(0, 41, W, 10, "#593718")
for x in range(5, 60, 6):
    c.rect(x, 42, 1, 8, "#3a2412")
c.rect(0, 51, W, 2, "#3a2412")


def tumbler(cx, base):
    x = cx - 2
    c.rect(x - 1, base - 6, 7, 7, OUTC)
    c.rect(x, base - 5, 5, 5, "#9aa08f")
    c.rect(x, base - 5, 5, 1, "#c9d0c8")
    c.rect(x, base - 4, 5, 3, "#d2942e")
    c.rect(x + 1, base - 4, 1, 2, "#e8e8de")


tumbler(25, 39)
tumbler(41, 39)
mug(33, 39)

# ---------------- hanging lamps ----------------
for cx in (19, 45):
    c.line(cx, 0, cx, 13, "#120a04")
    c.rect(cx - 3, 12, 7, 3, "#2e1e0e")
    c.rect(cx - 2, 15, 5, 2, "#1a1007")
    c.circle(cx, 18, 3, "#ffd874")
    c.rect(cx - 1, 16, 3, 2, "#fdf0b8")

# ---------------- floor ----------------
c.rect(0, 53, W, 11, "#3d2914")
c.rect(0, 53, W, 1, "#241606")
c.rect(0, 56, W, 1, "#1e1106")
c.rect(0, 59, W, 1, "#1e1106")
c.rect(0, 62, W, 1, "#1e1106")
for x in range(7, W, 8):
    c.rect(x, 54, 1, 9, "#1e1106")

# ---------------- stools ----------------
def stool(cx):
    c.ellipse(cx, 48, 6, 3, OUTC)
    c.ellipse(cx, 48, 5, 2, "#7a4b20")
    c.ellipse(cx, 48, 4, 1, "#965e2a")
    c.line(cx - 4, 50, cx - 6, 60, "#241208")
    c.line(cx + 4, 50, cx + 6, 60, "#241208")
    c.rect(cx - 4, 58, 9, 1, "#3a2412")
    c.rect(cx - 1, 54, 3, 1, "#3a2412")


for cx in (19, 32, 45):
    stool(cx)

# ---------------- atmosphere overlay: smoke + vignette ----------------
ov = new_canvas(W, W, name="haze")
S = (206, 194, 178, 78)
ov.ellipse(12, 8, 9, 3, S)
ov.ellipse(26, 10, 7, 2, S)
ov.ellipse(43, 6, 6, 2, S)
ov.ellipse(50, 13, 6, 2, S)
ov.ellipse(9, 21, 7, 3, S)
ov.ellipse(55, 18, 6, 3, S)
ov.ellipse(15, 31, 7, 2, S)
V1 = (7, 3, 1, 58)
V2 = (7, 3, 1, 105)
ov.rect(0, 0, 2, W, V1)
ov.rect(62, 0, 2, W, V1)
ov.rect(0, 60, W, 4, V1)
ov.rect(0, 0, 4, 4, V2)
ov.rect(60, 0, 4, 4, V2)
ov.rect(0, 60, W, 4, V2)

result = flatten([c, ov], name="tavern")

print(result.stats_text())

finish([result])
