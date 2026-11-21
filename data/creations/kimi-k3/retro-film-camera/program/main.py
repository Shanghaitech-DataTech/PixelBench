# Retro film camera - 32x32 RPG item portrait
c = new_canvas(32, 32, background=None, name="camera")

# palette
OUT    = '#201512'  # dark outline
SIL    = '#b9bec8'  # silver top plate
SIL_D  = '#7d838f'
SIL_L  = '#eef1f6'
LEA    = '#4a2c18'  # leather
LEA_L  = '#6e4626'
LEA_D  = '#33200f'
RING   = '#33302e'  # lens barrel
RING_M = '#6f6a63'
TICK   = '#45413b'
G1 = '#10181f'      # glass edge
G2 = '#1c3348'
G3 = '#284a66'
HI  = '#c9ecf4'     # glass highlight
HI2 = '#eaf7fb'
RED   = '#b8402f'
RED_L = '#e0684f'
AMB   = '#d8b13a'

# --- silhouette ---
c.rect(2, 10, 28, 18, OUT)                      # body
c.poly([(11, 10), (13, 6), (19, 6), (21, 10)], OUT)  # prism hump
c.rect(14, 4, 5, 2, OUT)                        # hot shoe
c.rect(1, 12, 1, 3, OUT)                        # strap lug L
c.rect(30, 12, 1, 3, OUT)                       # strap lug R
c.rect(23, 8, 4, 2, OUT)                        # shutter button base
c.circle(6, 9, 2, OUT)                          # rewind dial
for x, y in [(2, 10), (29, 10), (2, 27), (29, 27)]:
    c.set(x, y, None)                           # rounded corners

# --- top plate ---
c.rect(3, 11, 26, 6, SIL)
c.line(4, 11, 27, 11, SIL_L)
c.line(3, 16, 28, 16, SIL_D)
c.line(3, 12, 3, 15, SIL_D)
c.line(28, 12, 28, 15, SIL_L)
c.line(15, 4, 18, 4, SIL_D)                     # hot shoe slot

# rewind dial detail
c.circle(6, 9, 1, SIL_D)
c.set(6, 8, SIL_L)

# shutter button (red top)
c.set(24, 8, RED)
c.set(25, 8, RED_L)

# prism front + nameplate
c.poly([(12, 10), (14, 7), (18, 7), (20, 10)], SIL)
c.rect(13, 8, 6, 2, OUT)
c.set(14, 9, RED)
c.set(16, 8, '#8b93a0')

# self-timer lamp
c.circle(9, 13, 1, OUT)
c.set(9, 13, AMB)

# --- leather body with texture ---
c.rect(3, 17, 26, 10, LEA)
c.dither(3, 17, 26, 10, [LEA, LEA_L], 'bayer4')
c.line(4, 17, 27, 17, LEA_L)
c.line(3, 26, 28, 26, LEA_D)
c.line(3, 18, 3, 25, LEA_D)
c.line(28, 18, 28, 25, LEA_L)

# --- lens ---
c.circle(16, 20, 7, OUT)
c.circle(16, 20, 6, RING)
c.circle(16, 20, 5, RING_M)
c.set(16, 15, TICK); c.set(16, 25, TICK)
c.set(11, 20, TICK); c.set(21, 20, TICK)
c.circle(16, 20, 4, G1)
c.circle(16, 20, 3, G2)
c.circle(16, 20, 2, G3)
c.set(16, 20, G1)
c.set(14, 17, HI)
c.set(13, 18, HI)
c.set(14, 18, HI2)
c.set(19, 22, '#3a6788')
# subtle light arc on the outer ring (upper-left)
c.set(11, 16, '#8a857d')
c.set(12, 15, '#8a857d')

view(c)
print(c.stats_text())
finish(c)
