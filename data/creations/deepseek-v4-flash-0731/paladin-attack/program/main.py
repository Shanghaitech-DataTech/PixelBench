from pixelbench_api import *

W, H = 52, 62
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, 0)

f2 = f1.copy(name="f2")

# ============ FRAME 2 : paladin heavy down-swing ============
# 0) footing: LEFT (near) leg block steps FORWARD -> shift left 3 (lunge)
f2.select(0, 44, 20, 15).move_to(-3, 44, f2)
#    right (back) leg braces -> shift right 2
f2.select(20, 44, 20, 15).move_to(22, 44, f2)

# 1) remove old raised sword + old raised arm cleanly (keep head/plume/crest/robe)
f2.clear(16, 0, 28, 8)          # old blade tip  x16..43 y0..8
f2.clear(24, 9, 20, 6)          # old blade base x24..43 y9..13
f2.clear(25, 14, 19, 11)        # old wrist/hand x25..43 y14..24
f2.clear(19, 24, 17, 13)        # old forearm    x19..35 y24..36
f2.clear(35, 25, 9, 9)          # old blade tail x35..43 y25..33

# 2) WHITE motion trail streaming out behind the swing (arc up-right)
f2.path("M24,2 C33,6 41,12 41,20 L36,19 C37,14 32,10 25,7 Z", '#ffffff')
f2.path("M26,4 C32,9 38,14 37,20 L33,19 C34,14 30,10 25,8 Z", '#ffe38c')
f2.path("M21,3 C29,6 36,11 36,17 L32,17 C33,12 28,8 22,6 Z", '#ffefc6')
f2.path("M30,10 C36,13 39,17 38,22", '#ffffff', fill=False)
f2.path("M34,5 C39,9 42,14 41,19", '#ffffff', fill=False)
for (sx, sy) in [(38,8),(41,12),(37,16),(41,19),(39,22),(30,24),(35,21)]:
    f2.set(sx, sy, '#ffffff')
f2.set(40, 10, '#ffe38c')

# 3) arm driving the weapon DOWN along the body right side
f2.line(16, 27, 19, 32, '#332d32')        # dark arm
f2.line(17, 27, 20, 32, '#5a565a')        # arm shade
f2.line(15, 28, 18, 32, '#101010')        # arm outline
#    white gauntlet hand gripping the grip (down position, at body side)
for (hx, hy) in [(19,31),(20,31),(21,31),(22,31),(23,31),
                (18,32),(19,32),(20,32),(21,32),(22,32),(23,32),(24,32),
                (19,33),(20,33),(21,33),(22,33),(23,33),(24,33),
                (20,34),(21,34),(22,34),(23,34),(24,34),
                (21,35),(22,35),(23,35),(24,35),
                (22,36),(23,36)]:
    f2.set(hx, hy, '#ffffff')
f2.set(24, 32, '#dccaca'); f2.set(18, 33, '#c9886d')
#    crossguard
f2.line(18, 37, 27, 37, '#af7a18')
f2.line(18, 36, 27, 36, '#ffcc43')
#    heavy gold blade pointing DOWN, slightly right, tapering to a point
f2.line(21, 37, 27, 53, '#ffcc43')       # front edge
f2.line(25, 38, 29, 52, '#ffcc43')       # back edge
f2.line(23, 38, 26, 52, '#af7a18')       # fill
f2.line(21, 38, 23, 47, '#ffe38c')       # gleam
f2.line(19, 38, 22, 45, '#101010')       # dark edge
f2.set(28, 52, '#af7a18'); f2.set(29, 50, '#af7a18')
f2.set(28, 51, '#101010'); f2.set(27, 53, '#101010')
#    impact sparkle at the strike point
for (px, py) in [(20,50),(25,54),(31,48),(23,53),(28,55),(19,53)]:
    f2.set(px, py, '#ffffff')
f2.set(22, 53, '#ffe38c')

# 4) ground dust kicked up by the forward step
for (dx, dy) in [(0,56),(1,55),(2,57),(3,55),(4,56),(1,54)]:
    f2.set(dx, dy, '#5a565a')

print("=== FRAME 2 CHECK ===")
print(f2.matrix_text(region=(14, 2, 47, 40)))
print("--- legs ---")
print(f2.matrix_text(region=(0, 42, 46, 58)))
save("f1", f1)
save("f2", f2)
finish([f1, f2])
