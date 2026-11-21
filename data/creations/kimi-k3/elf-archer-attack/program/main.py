W, H = 44, 47

# Frame 1: original content
f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, 0, 0)

# Frame 2: full draw
f2 = f1.copy(name="f2")
f2.clear(24, 0, 20, 34)   # erase old bow, slack string, extended arm (keep greave y34+)

TAN = '#c5956a'; TANL = '#f6d39b'; TAND = '#a9794f'
GRN = '#687862'; GRNL = '#a4b496'; DARK = '#252a23'
YEL = '#ffe75a'; BRN = '#7b4231'; GOLD = '#fcc44c'
MAGL = '#ef5ba1'; MAG = '#c30074'; MAGD = '#9e005d'
BLK = '#121311'

# taut string: tips -> anchor at chin (17,18)
f2.line(32, 2, 16, 18, TANL)
f2.line(16, 19, 32, 37, TANL)

# bow arm (extended horizontal) + shoulder pad
for x in range(24, 30):
    f2.set(x, 20, GRN); f2.set(x, 21, GRN); f2.set(x, 22, DARK)
for x in range(25, 29):
    f2.set(x, 19, GRNL)
f2.set(24, 19, DARK); f2.set(29, 19, GRN); f2.set(25, 20, GRNL)
f2.set(23, 19, GRN); f2.set(23, 20, GRN); f2.set(23, 21, DARK)
# hand on grip
f2.rect(30, 19, 2, 4, TAN)
f2.set(30, 19, TANL); f2.set(31, 22, TAND)

# bow on separate layer (so outline() only affects the bow)
bow = new_canvas(W, H, name="bow")
# outer-edge x per row for the slim limbs (bulge max x35 at mid limb)
outer_map = {2:32, 3:33, 4:33, 5:34, 6:34, 7:35, 8:35, 9:34, 10:34,
             11:33, 12:33, 13:32, 14:32,
             23:32, 24:32, 25:32, 26:33, 27:33, 28:34, 29:34, 30:35,
             31:35, 32:34, 33:34, 34:33, 35:33, 36:32}
for y, ox in outer_map.items():
    bow.set(ox, y, YEL)       # outer highlight
    bow.set(ox - 1, y, GOLD)  # body
    bow.set(ox - 2, y, BRN)   # inner shadow (toward string)
# magenta bands near tips
for y in (4, 5, 33, 34):
    ox = outer_map[y]
    bow.set(ox, y, MAGL); bow.set(ox - 1, y, MAG); bow.set(ox - 2, y, MAGD)
# nocks
bow.set(32, 1, GOLD); bow.set(33, 1, BRN)
bow.set(32, 37, GOLD); bow.set(33, 37, BRN)
# riser / grip block
bow.rect(32, 15, 2, 8, BLK)
bow.set(33, 15, DARK); bow.set(33, 22, DARK)
bow.set(32, 18, GOLD); bow.set(32, 19, GOLD)
f2.blit(bow, 0, 0)
# fingers wrapping the grip
f2.set(32, 20, TAN); f2.set(32, 21, TAN)

# draw arm (bent, pulled back to chin)
for (x, y) in [(12,17),(13,17),(14,18),(15,18),               # forearm
               (12,18),(13,19),(14,20),(15,21)]:              # upper arm
    f2.set(x, y, GRN)
for (x, y) in [(12,16),(13,16),(14,17),(15,17),               # forearm top light
               (13,18),(14,19),(15,20)]:                      # upper arm top light
    f2.set(x, y, GRNL)
for (x, y) in [(11,17),(10,17),(10,18),(11,18),               # elbow
               (12,19),(13,20),(14,21),(15,22)]:              # upper arm bottom
    f2.set(x, y, DARK)
# draw fist at anchor (covers string corner)
f2.set(16, 18, TANL); f2.set(17, 18, TAN)
f2.set(16, 19, TAN);  f2.set(17, 19, TAND)

view(f1)
view(f2)
finish([f1, f2])
