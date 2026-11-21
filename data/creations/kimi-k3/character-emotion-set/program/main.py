# 64x64: 2x2 grid of big-head emotion portraits of the same character
# TL=calm, TR=smiling, BL=angry, BR=surprised

DARK    = '#2a2130'
SKIN    = '#ffd2a1'
SKIN_SH = '#f0b184'
BLUSH   = '#f79a8a'
HAIR    = '#b5542a'
HAIR_HI = '#d9803f'
HAIR_DK = '#8a3d20'
WHITE   = '#ffffff'
MOUTH   = '#6e2f3a'
TONGUE  = '#e0696e'
TEAL    = '#2f8f8a'
TEAL_DK = '#1e5c60'
TEAL_LT = '#5bbdb3'
RED     = '#e04545'
SWEAT   = '#9fdcf2'

c = new_canvas(64, 64, name="emotions")
iSKIN = c.color(SKIN)
iHAIR = c.color(HAIR)

def base(ox, oy):
    c.ellipse(ox+16, oy+27, 8, 3, TEAL_DK)      # hood behind neck
    c.rect(ox+13, oy+22, 6, 5, SKIN)            # neck
    c.rect(ox+4, oy+27, 24, 4, TEAL)            # shoulders
    c.rect(ox+3, oy+29, 26, 2, TEAL)
    c.circle(ox+6, oy+16, 2, SKIN)              # ears
    c.circle(ox+26, oy+16, 2, SKIN)
    c.ellipse(ox+16, oy+15, 9, 9, SKIN)         # head
    c.ellipse(ox+16, oy+9, 11, 7, HAIR)         # hair cap
    c.rect(ox+5, oy+10, 3, 6, HAIR)             # side locks
    c.rect(ox+25, oy+10, 3, 6, HAIR)
    c.ellipse(ox+16, oy+16, 8, 8, SKIN)         # face opening
    c.line(ox+16, oy+2, ox+19, oy+0, HAIR)      # cowlick
    c.line(ox+16, oy+3, ox+19, oy+1, HAIR)
    for px, py in [(10,6),(11,5),(12,4),(13,4),(14,5)]:
        c.set(ox+px, oy+py, HAIR_HI)            # hair shine
    for x in range(ox+7, ox+26):                # bang shadow line
        for y in range(oy+7, oy+18):
            if c.get(x, y) == iSKIN and c.get(x, y-1) == iHAIR:
                c.set(x, y-1, HAIR_DK)
    c.set(ox+6, oy+16, SKIN_SH)                 # ear detail
    c.set(ox+26, oy+16, SKIN_SH)
    c.line(ox+14, oy+26, ox+17, oy+26, SKIN_SH) # neck shade
    c.line(ox+13, oy+27, ox+19, oy+27, TEAL_DK) # collar
    c.line(ox+16, oy+28, ox+16, oy+30, TEAL_DK) # zipper
    c.set(ox+5, oy+28, TEAL_LT)                 # hoodie shine
    c.set(ox+6, oy+28, TEAL_LT)
    c.set(ox+16, oy+19, SKIN_SH)                # nose

def face_calm(ox, oy):
    c.set(ox+10, oy+13, DARK)
    c.line(ox+11, oy+12, ox+13, oy+12, DARK)
    c.set(ox+22, oy+13, DARK)
    c.line(ox+19, oy+12, ox+21, oy+12, DARK)
    c.ellipse(ox+11, oy+16, 1, 2, DARK)
    c.ellipse(ox+20, oy+16, 1, 2, DARK)
    c.set(ox+11, oy+15, WHITE)
    c.set(ox+20, oy+15, WHITE)
    c.set(ox+14, oy+21, DARK)
    c.line(ox+15, oy+22, ox+17, oy+22, DARK)
    c.set(ox+18, oy+21, DARK)

def face_smile(ox, oy):
    c.set(ox+10, oy+13, DARK)
    c.line(ox+11, oy+12, ox+13, oy+12, DARK)
    c.set(ox+22, oy+13, DARK)
    c.line(ox+19, oy+12, ox+21, oy+12, DARK)
    for ex in (11, 20):
        c.set(ox+ex-1, oy+17, DARK)
        c.set(ox+ex,   oy+16, DARK)
        c.set(ox+ex+1, oy+16, DARK)
        c.set(ox+ex+2, oy+17, DARK)
        c.set(ox+ex,   oy+17, DARK)
        c.set(ox+ex+1, oy+17, DARK)
    c.rect(ox+13, oy+20, 6, 3, MOUTH)
    c.rect(ox+14, oy+20, 4, 1, WHITE)
    c.rect(ox+14, oy+22, 4, 1, TONGUE)
    c.set(ox+12, oy+19, DARK)
    c.set(ox+19, oy+19, DARK)
    for bx, by in [(8,18),(9,18),(9,19)]:
        c.set(ox+bx, oy+by, BLUSH)
    for bx, by in [(23,18),(24,18),(23,19)]:
        c.set(ox+bx, oy+by, BLUSH)

def face_angry(ox, oy):
    for px, py in [(9,11),(10,12),(11,12),(12,13),(13,13),
                   (9,12),(10,13),(11,13),(12,14),(13,14)]:
        c.set(ox+px, oy+py, DARK)
    for px, py in [(23,11),(22,12),(21,12),(20,13),(19,13),
                   (23,12),(22,13),(21,13),(20,14),(19,14)]:
        c.set(ox+px, oy+py, DARK)
    c.rect(ox+10, oy+16, 3, 2, DARK)
    c.rect(ox+19, oy+16, 3, 2, DARK)
    c.rect(ox+13, oy+20, 6, 4, MOUTH)
    c.rect(ox+14, oy+21, 4, 2, WHITE)
    c.set(ox+16, oy+21, DARK)
    c.set(ox+16, oy+22, DARK)
    c.set(ox+12, oy+23, DARK)
    c.set(ox+19, oy+23, DARK)
    for px, py in [(28,4),(27,5),(28,5),(29,5),(28,6)]:
        c.set(ox+px, oy+py, RED)

def face_surprised(ox, oy):
    for px, py in [(10,12),(11,11),(12,11),(13,12),(10,13),(13,13),
                   (22,12),(21,11),(20,11),(19,12),(22,13),(19,13)]:
        c.set(ox+px, oy+py, DARK)
    for ex in (11, 20):
        c.ellipse(ox+ex, oy+16, 2, 3, DARK)
        c.ellipse(ox+ex, oy+16, 1, 2, WHITE)
        c.set(ox+ex, oy+16, DARK)
        c.set(ox+ex, oy+17, DARK)
        c.set(ox+ex-1, oy+15, WHITE)
    c.ellipse(ox+16, oy+21, 1, 2, MOUTH)
    c.set(ox+16, oy+22, TONGUE)

base(0, 0);   face_calm(0, 0)
base(32, 0);  face_smile(32, 0)
base(0, 32);  face_angry(0, 32)
base(32, 32); face_surprised(32, 32)

c.outline(DARK)
print(c.stats_text())
print(c.matrix_text(region=(0, 32, 31, 63)))
print(c.matrix_text(region=(32, 32, 63, 63)))
view(c)
finish(c)
