import random

# ---------- palette ----------
SKY      = '#0d1226'
SKY2     = '#151b36'
CITY     = '#090d1c'
CITYWIN  = '#6a5a34'
RAIN     = '#8a94b8'
WALL     = '#3a4056'
WALL_D   = '#2a2f42'
PARAPET  = '#20253a'
PARA_E   = '#4a5168'
SIGN_W   = '#f7f2df'
SIGN_R   = '#e05244'
SIGN_O   = '#f0963c'
SIGN_G   = '#4aa66a'
FRAME    = '#1b2032'
GLOW_B   = '#ffe9a8'
GLOW_M   = '#ffd06a'
GLOW_D   = '#e0a040'
SHELF    = '#9a6a2a'
SILH     = '#7a4e20'
IT_R     = '#d05848'
IT_B     = '#4a80c8'
IT_G     = '#58a868'
IT_W     = '#f0ead8'
METAL    = '#c8c2b0'
COAT     = '#f2c230'
COAT_D   = '#c08f1c'
COAT_H   = '#f7dc6a'
SKIN     = '#e8b088'
BOOT     = '#2c3244'
UMB_R    = '#d04848'
UMB_B    = '#4878d0'
RACK     = '#6a7080'
BIKE     = '#141828'
BIKE_H   = '#8a90a0'
GROUND   = '#191d2e'
GROUND_L = '#232944'
AO       = '#101424'
PUD      = '#2a3252'
PUD_L    = '#46548a'
REF1     = '#8a6a34'
REF2     = '#c99a4a'
REF3     = '#f0d88a'

c = new_canvas(64, 64, background=SKY, name='convenience_store_rainy_night')

# ---------- sky ----------
c.rect(0, 2, 18, 3, SKY2)
c.rect(30, 0, 22, 3, SKY2)
c.rect(46, 5, 18, 3, SKY2)
# distant city silhouettes
c.rect(0, 4, 3, 5, CITY)
c.set(1, 5, CITYWIN); c.set(2, 7, CITYWIN)
c.rect(61, 3, 3, 6, CITY)
c.set(62, 4, CITYWIN); c.set(61, 6, CITYWIN)

# ---------- building ----------
c.rect(4, 9, 56, 43, WALL)           # x4-59, y9-51
c.rect(4, 9, 56, 3, PARAPET)
c.line(4, 9, 59, 9, PARA_E)
c.rect(4, 12, 2, 32, WALL_D)         # left edge shadow
c.rect(58, 12, 2, 32, WALL_D)        # right edge shadow
c.rect(4, 44, 56, 8, WALL_D)         # base wall y44-51
c.line(4, 44, 59, 44, WALL)

# ---------- sign band ----------
c.rect(7, 12, 50, 7, SIGN_W)
c.rect(7, 12, 50, 2, SIGN_R)
c.rect(7, 14, 50, 1, SIGN_O)
c.rect(9, 15, 4, 3, SIGN_G)          # abstract mark (no logo)
c.set(10, 16, SIGN_W)
# abstract sign lettering (no brand names)
c.rect(16, 15, 10, 1, METAL)
c.rect(28, 15, 7, 1, METAL)
c.rect(38, 15, 12, 1, METAL)
c.rect(16, 17, 6, 1, METAL)
c.rect(24, 17, 13, 1, METAL)
c.rect(40, 17, 8, 1, METAL)
c.rect(7, 19, 50, 1, GLOW_B)         # light strip under sign

# ---------- windows ----------
def window(x0, w, items1, items2):
    c.rect(x0, 21, w, 23, FRAME)         # frame
    c.rect(x0+1, 22, w-2, 21, GLOW_M)    # interior glow
    c.rect(x0+1, 22, w-2, 3, GLOW_B)     # ceiling light band
    c.rect(x0+1, 30, w-2, 1, SHELF)      # shelf 1
    c.rect(x0+1, 37, w-2, 1, SHELF)      # shelf 2
    c.rect(x0+1, 39, w-2, 3, GLOW_D)     # counter
    for (ix, iy, iw, ih, col) in items1:
        c.rect(ix, iy, iw, ih, col)
    for (ix, iy, iw, ih, col) in items2:
        c.rect(ix, iy, iw, ih, col)

# left window x6-25
window(6, 20,
    [(8,27,3,3,IT_R), (12,26,2,4,IT_B), (15,27,3,3,IT_G), (19,26,2,4,IT_W), (22,28,2,2,IT_R)],
    [(9,34,2,3,IT_G), (12,33,3,4,IT_W), (16,34,2,3,IT_B), (19,33,3,4,IT_R), (23,34,1,3,IT_G)])

# right window x42-57
window(42, 16,
    [(44,27,2,3,IT_W), (54,27,2,3,IT_R)],
    [(44,34,2,3,IT_B), (54,34,2,3,IT_G)])
# customer silhouette inside right window
c.circle(51, 27, 2, SILH)
c.rect(49, 30, 5, 11, SILH)

# ---------- door ----------
c.rect(28, 21, 11, 29, FRAME)        # x28-38, y21-49
c.rect(29, 22, 9, 27, GLOW_D)        # glass
c.rect(29, 22, 9, 2, GLOW_B)         # top light
c.line(33, 22, 33, 48, FRAME)        # center stile
c.rect(29, 45, 9, 2, FRAME)          # bottom rail
c.rect(35, 34, 1, 3, METAL)          # handle
c.rect(28, 50, 11, 1, PARA_E)        # threshold
c.rect(29, 51, 9, 1, RACK)

# ---------- ground ----------
c.rect(0, 52, 64, 12, GROUND)
c.rect(0, 52, 64, 2, GROUND_L)
c.rect(4, 52, 56, 1, AO)

# ---------- light reflections on wet ground ----------
# door pool
c.rect(29, 52, 9, 1, REF3)
c.rect(28, 53, 11, 1, REF2)
c.rect(30, 54, 7, 1, REF2)
c.rect(29, 55, 9, 1, REF1)
for x in (31, 33, 35): c.set(x, 56, REF1)
for x in (32, 34):     c.set(x, 57, REF1)
# left window pool
c.rect(7, 52, 18, 1, REF2)
c.rect(9, 53, 14, 1, REF1)
for x in (11, 14, 18): c.set(x, 54, REF1)
for x in (13, 16):     c.set(x, 55, REF1)
# right window pool
c.rect(43, 52, 14, 1, REF2)
c.rect(45, 53, 10, 1, REF1)
for x in (47, 50, 53): c.set(x, 54, REF1)

# ---------- puddles ----------
# p1 under door
c.rect(26, 58, 14, 1, PUD)
c.rect(24, 59, 18, 2, PUD)
c.rect(26, 61, 14, 1, PUD)
c.rect(28, 58, 10, 1, PUD_L)         # sky sheen on top edge
c.rect(28, 59, 9, 1, REF2)           # warm door reflection
c.rect(30, 60, 5, 1, REF3)
c.set(31, 58, COAT_D); c.set(32, 58, COAT_D); c.set(33, 58, COAT)  # raincoat reflection
# p2 right
c.rect(47, 55, 12, 1, PUD)
c.rect(45, 56, 16, 1, PUD)
c.rect(47, 57, 12, 1, PUD)
c.rect(48, 55, 10, 1, PUD_L)
c.rect(48, 56, 8, 1, REF1)
c.rect(50, 56, 4, 1, REF2)
# p3 left
c.rect(6, 60, 9, 1, PUD)
c.rect(4, 61, 13, 1, PUD)
c.rect(6, 62, 9, 1, PUD)
c.rect(7, 60, 6, 1, PUD_L)
c.set(9, 61, REF1); c.set(10, 61, REF1)

# ---------- bicycle ----------
c.circle(10, 48, 4, BIKE, fill=False)
c.circle(21, 48, 4, BIKE, fill=False)
c.line(10, 48, 14, 44, BIKE)         # seat tube
c.line(14, 44, 18, 44, BIKE)         # top tube
c.line(18, 44, 21, 48, BIKE)         # fork
c.line(18, 44, 13, 48, BIKE)         # down tube
c.line(13, 48, 10, 48, BIKE)         # chainstay
c.set(13, 43, BIKE); c.set(14, 43, BIKE)   # saddle
c.line(18, 44, 19, 43, BIKE)         # stem
c.set(19, 43, BIKE); c.set(20, 43, BIKE)   # handlebar
c.set(7, 46, BIKE_H); c.set(8, 45, BIKE_H) # wheel highlights
c.set(18, 45, BIKE_H); c.set(14, 49, BIKE_H)

# ---------- umbrella rack ----------
c.rect(38, 48, 5, 4, RACK)           # stand x38-42 y48-51
c.line(38, 48, 42, 48, BIKE_H)       # rim
# red umbrella
c.line(39, 40, 39, 47, UMB_R)
c.rect(38, 44, 3, 3, UMB_R)
c.set(40, 40, UMB_R)                 # hook
# blue umbrella
c.line(42, 42, 42, 47, UMB_B)
c.rect(41, 45, 3, 3, UMB_B)
c.set(43, 42, UMB_B)

# ---------- person in raincoat entering ----------
c.rect(29, 37, 8, 11, COAT)          # body x29-36 y37-47
c.rect(29, 37, 2, 11, COAT_D)        # shaded side
c.rect(35, 38, 1, 9, COAT_H)         # lit side
c.line(29, 47, 36, 47, COAT_D)       # hem
c.circle(32, 33, 3, COAT)            # hood
c.set(30, 36, COAT_D); c.set(31, 36, COAT_D)
c.set(33, 31, COAT_H); c.set(34, 32, COAT_H)
c.line(35, 39, 36, 36, COAT)         # arm reaching to handle
c.set(35, 35, SKIN)                  # hand on handle
# legs / boots
c.rect(31, 48, 2, 3, BOOT)
c.set(31, 51, BOOT); c.set(32, 51, BOOT)
c.rect(35, 48, 2, 3, BOOT)
c.set(36, 51, BOOT)

# ---------- rain ----------
rng = random.Random(7)
for _ in range(26):
    x = rng.randrange(1, 63)
    y = rng.randrange(0, 40)
    c.line(x, y, x - 1, y + 2, RAIN)
# splash ticks near puddles
for (sx, sy) in [(25, 57), (40, 58), (46, 55), (59, 56), (5, 60), (15, 61), (36, 57)]:
    c.set(sx, sy, RAIN)

stats = c.stats()
print('visible colors:', stats['colors_used'], '| visible px:', stats['visible_pixels'])

view(c)
finish(c)
