# Cozy indoor tavern - 64x64 pixel art
# Layers: base (wall/floor) -> wall glow -> objects -> fx (halos/smoke) -> flatten

OUT    = '#160f08'   # dark warm outline
WALL   = '#38220f'
PLANK  = '#281608'
SH0    = '#1c0e05'
SH1    = '#251406'
SH2    = '#2e1b0b'
FLOOR  = '#2c1a0c'
FLINE  = '#1d1004'
FPOOL  = '#3a2412'
WOOD   = '#6b4226'
WOODL  = '#8a5a32'
WOODH  = '#b07a44'
WOODD  = '#472a13'
CTOP   = '#b97f42'
CTOPL  = '#e0aa60'
BAND   = '#332e2c'
BRASS  = '#c9963c'
FOAM   = '#f6ecc9'
BEER   = '#e2a437'
BULB   = '#fff3b0'
CORK   = '#caa06a'
CANDLE = '#e8d8b0'
GLASS  = '#e8dcb0'
WINE   = '#b04040'
SHADE  = '#7a5226'
RIM    = '#ffca6a'

# ---------------- layer 1: wall + floor ----------------
L1 = new_canvas(64, 64, background=WALL, name='base')
L1.rect(0, 0, 64, 1, SH0)
L1.rect(0, 1, 64, 1, SH1)
L1.rect(0, 2, 64, 1, SH2)
for x in range(7, 64, 8):
    L1.line(x, 3, x, 33, PLANK)
L1.rect(0, 33, 64, 1, PLANK)
# floor
L1.rect(0, 53, 64, 11, FLOOR)
L1.ellipse(32, 58, 18, 5, FPOOL)          # warm pool of lamplight on floor
for y in (56, 59, 62):
    L1.line(0, y, 63, y, FLINE)
for jx, jy, je in [(8,53,55),(24,53,55),(40,53,55),(56,53,55),
                   (16,57,58),(32,57,58),(48,57,58),
                   (8,60,61),(24,60,61),(40,60,61),(56,60,61)]:
    L1.line(jx, jy, jx, je, FLINE)

# ---------------- layer: wall glow from lamps ----------------
Lg = new_canvas(64, 64, name='wallglow')
for x in (14, 32, 50):
    Lg.ellipse(x, 14, 10, 12, (255, 190, 90, 20))
    Lg.ellipse(x, 13, 5, 7, (255, 205, 110, 30))

# ---------------- layer 2: solid objects ----------------
L2 = new_canvas(64, 64, name='objects')

# barrel behind the bar (left, tucked under the shelf)
L2.ellipse(7, 30, 4, 4, OUT)
L2.ellipse(7, 30, 3, 3, WOOD)
L2.line(5, 27, 5, 33, WOODD)
L2.line(7, 26, 7, 34, WOODD)
L2.line(9, 27, 9, 33, WOODD)
L2.line(3, 28, 11, 28, BAND)
L2.line(3, 32, 11, 32, BAND)
L2.line(5, 27, 6, 27, WOODH)

# back shelf
L2.rect(9, 23, 48, 4, OUT)
L2.rect(10, 24, 46, 2, WOOD)
L2.rect(10, 24, 46, 1, WOODH)
L2.set(14, 27, OUT); L2.set(15, 27, OUT); L2.set(14, 28, OUT)
L2.set(48, 27, OUT); L2.set(49, 27, OUT); L2.set(49, 28, OUT)

# bottles on the shelf (base row 22)
def bottle(x, base, w, h, col, hi):
    L2.rect(x, base-h+1, w, h, OUT)
    if w > 2 and h > 2:
        L2.rect(x+1, base-h+2, w-2, h-2, col)
        L2.rect(x+1, base-h+2, 1, max(1, h-3), hi)
    nw = 2 if w >= 4 else 1
    nx = x + (w-nw)//2
    L2.rect(nx, base-h-2, nw, 3, col)
    L2.rect(nx, base-h-3, nw, 1, CORK)

bottle(12, 22, 4, 6, '#2f6b33', '#55a35c')
bottle(17, 22, 3, 5, '#a34a2a', '#d97a45')
bottle(21, 22, 4, 8, '#7a2e35', '#a34848')
bottle(26, 22, 3, 4, '#3a5a7a', '#5f85a8')
bottle(30, 22, 4, 6, '#b5741e', '#e0a04a')
bottle(35, 22, 3, 7, '#2f6b5a', '#4f9a7f')
bottle(39, 22, 4, 5, '#5a3a6b', '#8260a0')
bottle(44, 22, 3, 6, '#a34a2a', '#d97a45')
bottle(48, 22, 4, 7, '#3f7a3a', '#63a85a')
bottle(53, 22, 3, 5, '#8a6a2a', '#bd9645')

# mugs hanging under the shelf
for mx in (20, 32, 44):
    L2.set(mx+1, 27, OUT)
    L2.rect(mx, 28, 4, 3, OUT)
    L2.rect(mx+1, 29, 2, 1, WOODL)
    L2.set(mx+4, 29, OUT)

# ---------------- bar counter ----------------
L2.rect(2, 34, 60, 19, OUT)          # outline block
L2.rect(3, 35, 58, 2, CTOP)          # top surface
L2.rect(3, 35, 58, 1, CTOPL)         # surface highlight
L2.rect(3, 37, 58, 15, WOOD)         # front face
L2.rect(3, 38, 58, 1, WOODL)         # bevel under the top
for px in range(12, 60, 9):
    L2.line(px, 39, px, 48, WOODD)   # panel divisions
L2.line(4, 44, 59, 44, WOODD)
L2.rect(3, 49, 58, 3, WOODD)         # kick plate

# items on the counter
def counter_mug(x):
    L2.rect(x, 32, 4, 4, OUT)
    L2.rect(x+1, 33, 2, 2, BEER)
    L2.set(x+1, 32, FOAM); L2.set(x+2, 32, FOAM)
    L2.set(x+3, 31, FOAM)
    L2.line(x+4, 33, x+4, 34, OUT)

counter_mug(8)
counter_mug(20)
counter_mug(44)

# wine glass
L2.rect(25, 31, 4, 3, OUT)
L2.set(26, 32, GLASS); L2.set(27, 32, WINE)
L2.set(26, 34, OUT)
L2.rect(25, 35, 4, 1, OUT)

# beer tap
L2.rect(31, 28, 5, 2, OUT)
L2.rect(32, 28, 3, 1, BRASS)
L2.rect(32, 29, 3, 5, OUT)
L2.rect(33, 30, 1, 3, BRASS)
L2.rect(30, 34, 7, 2, OUT)
L2.rect(31, 34, 5, 1, BRASS)

# tumbler glass
L2.rect(39, 33, 3, 3, OUT)
L2.set(40, 34, GLASS)

# candle
L2.rect(53, 34, 4, 2, OUT)
L2.rect(54, 34, 2, 1, '#8a6a3a')
L2.rect(54, 31, 2, 3, CANDLE)
L2.set(54, 30, '#ffe29a')
L2.set(54, 29, '#ff9a3a')

# ---------------- bar stools ----------------
def stool(cx):
    L2.line(cx-3, 54, cx-4, 62, WOODD)
    L2.line(cx+3, 54, cx+4, 62, WOODD)
    L2.line(cx-3, 58, cx+3, 58, WOODD)
    L2.set(cx-4, 63, OUT); L2.set(cx+4, 63, OUT)
    L2.ellipse(cx, 52, 5, 2, OUT)
    L2.ellipse(cx, 52, 4, 1, WOODL)
    L2.line(cx-3, 51, cx+2, 51, WOODH)
    L2.line(cx-3, 53, cx+3, 53, WOODD)

stool(12)
stool(30)
stool(47)

# ---------------- barrel, foreground right ----------------
L2.ellipse(59, 56, 6, 7, OUT)
L2.ellipse(59, 56, 5, 6, WOOD)
L2.line(56, 50, 62, 50, WOODH)      # light catching the top rim
L2.line(56, 51, 56, 61, WOODD)
L2.line(59, 51, 59, 62, WOODD)
L2.line(62, 51, 62, 61, WOODD)
L2.line(54, 53, 63, 53, BAND)
L2.line(55, 60, 63, 60, BAND)

# ---------------- hanging lamps ----------------
def lamp(x):
    L2.line(x, 0, x, 3, OUT)
    L2.rect(x-1, 4, 3, 1, OUT)
    for y, hw in [(5,1),(6,2),(7,3),(8,4)]:
        L2.line(x-hw, y, x+hw, y, OUT)
    for y, hw in [(5,0),(6,1),(7,2),(8,3)]:
        L2.line(x-hw, y, x+hw, y, SHADE)
    L2.line(x-1, 8, x+1, 8, RIM)
    L2.rect(x-1, 9, 3, 1, BULB)
    L2.set(x, 10, '#ffd873')

lamp(14)
lamp(32)
lamp(50)

# ---------------- layer: light halos + smoke ----------------
Lfx = new_canvas(64, 64, name='fx')
for x in (14, 32, 50):
    Lfx.circle(x, 9, 6, (255, 200, 100, 24))
    Lfx.circle(x, 9, 3, (255, 220, 130, 36))
Lfx.circle(54, 29, 3, (255, 200, 100, 26))

SM = (220, 210, 190, 52)
for sx, sy in [(21,18),(23,16),(25,14),(26,12),
               (44,26),(46,24),(48,22),(49,20),
               (10,29),(12,27),(36,21),(38,19),
               (55,26),(57,24),(54,22),(40,16),(42,14),(22,25),(24,23)]:
    Lfx.set(sx, sy, SM)

# ---------------- flatten ----------------
result = flatten([L1, Lg, L2, Lfx], name='tavern')
print(result.stats_text())
view(result)
finish(result)
