c = new_canvas(32, 32, name="microscope")

# colours
M = c.color("#2b2b3a")   # dark body
L = c.color("#4a4a66")   # light body
G = c.color("#8a8aa0")   # metal grey
W = c.color("#d9e6f2")   # glass / highlight
K = c.color("#1a1a26")   # outline dark
B = c.color("#3a3a50")   # mid tone
S = c.color("#6e6e8a")   # stage grey

def px(x, y, col): c.set(x, y, col)
def rect(x, y, w, h, col, fill=True): c.rect(x, y, w, h, col, fill)

# --- base (bottom), three-quarter: base slab from x=6..27
rect(6, 27, 21, 3, M)
rect(6, 27, 21, 1, L)
rect(8, 25, 17, 2, B)
# arm rising from base right side, curving up
rect(22, 10, 4, 16, B)      # arm column
rect(22, 10, 1, 16, L)
# --- body tube tilted (three-quarter): eyepiece top-left
# eyepiece
rect(8, 2, 5, 5, G)
rect(8, 2, 5, 1, W)
rect(9, 3, 3, 3, M)
# eyepiece slanted down-right into body tube
# tube from (10,7) going down-right
for i in range(10):
    x = 10 + i
    y = 7 + i
    rect(x, y, 3, 2, M)
    rect(x, y, 3, 1, L)
# nosepiece at bottom of tube
rect(19, 16, 5, 3, G)
# objective pointing down-left
rect(17, 19, 3, 3, M)
rect(16, 22, 2, 2, K)
# --- stage
rect(6, 21, 13, 3, S)
rect(6, 21, 13, 1, W)
rect(9, 24, 3, 1, K)   # slide clip hint
# stage light hole
rect(11, 22, 2, 1, K)
# illuminator under stage
rect(10, 25, 4, 2, G)

# dark outline pass: simple edge darkening
for x in range(6, 28):
    px(x, 29, K)
for y in range(2, 30):
    if c.get(5, y) if False else False: pass

print(c.stats_text())
finish(c)
