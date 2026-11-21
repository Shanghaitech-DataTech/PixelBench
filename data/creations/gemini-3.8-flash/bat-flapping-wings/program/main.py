w, h = 39, 27
dx, dy = 6, 4

# Frame 1: Keeps original picture content on the shared canvas
f1 = new_canvas(w, h, name="f1")
f1.blit(input_canvas, dx, dy)

# Clean body extraction from input_canvas
body = new_canvas(27, 22, name="body")
for y in range(22):
    for x in range(27):
        is_body = False
        if y == 0 and x in (10, 16):
            is_body = True
        elif y in (1, 2, 3) and 9 <= x <= 17:
            is_body = True
        elif y in (4, 5) and 9 <= x <= 17:
            is_body = True
        elif y in (6, 7) and 10 <= x <= 16:
            is_body = True
        elif y in (8, 9, 10) and 9 <= x <= 17:
            is_body = True
        elif y in (11, 12, 13, 14) and 10 <= x <= 16:
            is_body = True
        elif y == 15 and x in (11, 15):
            is_body = True
        if is_body:
            body.set(x, y, input_canvas.get(x, y))

# Frame 2: Flapping wings in spread, raised position
f2 = new_canvas(w, h, name="f2")

# Left wing map (x=0..18, center line is x=19)
# 1: #1d181e (dark outline)
# 2: #7784a2 (body highlight)
# 3: #b572b1 (pink highlight on bones and tips)
# 4: #432f53 (dark purple wing bone/shade)
# 5: #5f5f7b (blue-gray tone)
# 8: #5c436f (wing membrane purple)
wing_map = [
#0123456789012345678
 "...................", # 0
 "......1............", # 1 (wrist thumb claw at 6, 1)
 "...444344..........", # 2 (wrist peak)
 ".44333333444.......", # 3 (forearm and arm highlight)
 "4333448883344......", # 4 (tip 1 highlight at x=1..2)
 "14884888884434.....", # 5 (tip 1 point at x=0)
 ".148488888844444...", # 6 (scallop 1 curve)
 ".448488888888444...", # 7
 "1334488488888444...", # 8 (tip 2 point at x=0, highlight at 1..2)
 ".148888488888844...", # 9
 "..14888488848844...", # 10 (scallop 2 curve, solid shoulder attach)
 "..44884488848844...", # 11
 ".434488888488844...", # 12 (tip 3 starting)
 "1334888884888844...", # 13 (tip 3 highlight at x=1..2)
 ".14488884888884....", # 14 (tip 3 point at x=1)
 "..1488848888881....", # 15 (scallop 3 curving in)
 "...1144888881......", # 16 (scallop 3 bottom)
 ".....1111111.......", # 17 (inner connection to body)
]

for y, row in enumerate(wing_map):
    for x, ch in enumerate(row):
        if ch in "12345678":
            f2.set(x, y, int(ch))

# Mirror left wing across center line x=19 (x -> 38 - x)
for y in range(h):
    for x in range(16):
        val = f2.get(x, y)
        if val != 0:
            f2.set(38 - x, y, val)

# Blit clean body on top
f2.blit(body, dx, dy)

view(f1)
view(f2)

finish([f1, f2])
