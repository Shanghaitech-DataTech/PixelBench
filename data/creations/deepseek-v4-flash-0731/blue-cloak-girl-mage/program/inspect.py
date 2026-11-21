from pixelbench_api import *

W = H = 64
c = new_canvas(W, H)

HAIR = (0xff, 0xd6, 0x77)
HAIRD= (0xd4, 0xa3, 0x45)
SKIN = (0xff, 0xdf, 0xc2)
SKND = (0xe8, 0xa7, 0x7b)
EYE  = (0xff, 0xb3, 0x00)
PUP  = (0x8f, 0x53, 0x00)
HL  = (0xff, 0xf6, 0xd8)
MOUTH=(0xd9, 0x6f, 0x66)
CLOAK = (0x2e, 0x5c, 0x9e)
CLKD  = (0x1b, 0x3a, 0x6e)
CLKH  = (0x4f, 0x86, 0xc8)
BOOT  = (0xf0, 0xf0, 0xee)
BOOTD = (0xb6, 0xb6, 0xb4)
WOOD  = (0x84, 0x54, 0x26)
WOODD = (0x4b, 0x2d, 0x10)
GLOW  = (0xff, 0xe8, 0x99)
AMBR2 = (0xff, 0xc4, 0x3d)
SHAD  = (20, 22, 40, 100)

rows = [
 "", "", "", "",
 "..........................HHHHHHHHHHHHHH",
 ".........................HHHHHHHHHHHHHHHH",
 ".........................HHHHHHHHHHHHHHHH",
 "........................HHHHHHHHHHHHHHHHHH",
 "........................HHHHHHHHHHHHHHHHHH",
 "........................HHHHHHHHHHHHHHHHHH",
 "........................HHSSSSSSSSSSSSHH",
 "........................HHSSYYYYSSYYYYSSHH",
 "........................HHSSYYeeSSeeYYSSHH",
 "........................HHSSSSSSSSSSSSHH",
 "........................HHSSSSSSSSRRSSSSSSHH",
 "........................HHHHSSSSSSSSSSSSHHHH",
 ".........................HHHHSSSSSSSSSSHHHH",
 ".........................HHHHSSSSSSSSHHHH",
]
colors = {"H": HAIR, "S": SKIN, "Y": EYE, "e": PUP, "R": MOUTH}
for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch in colors:
            c.set(x, y, colors[ch])

# robe rows 18-48: (L, R)
robe = [
 (21, 45), (20, 46), (20, 46), (19, 47), (19, 47),
 (19, 47), (18, 48), (18, 48), (18, 48), (17, 48),
 (17, 48), (17, 48), (17, 48), (17, 48), (17, 48),
 (17, 48), (17, 48), (17, 48), (17, 48), (17, 48),
 (17, 48), (17, 48), (17, 48), (17, 48), (17, 48),
 (17, 48), (17, 48), (17, 48), (17, 48), (17, 48),
 (17, 48),
]
for y, (L, R) in enumerate(robe, start=18):
    c.set(L, y, CLKH)
    c.set(R, y, CLKD)
    for x in range(L+1, R):
        c.set(x, y, CLOAK)

tights = [(18,47),(18,47),(19,46),(19,46),(20,45),(20,45),(21,44),(22,43)]
for y, (L, R) in enumerate(tights, start=49):
    for x in range(L, R+1):
        c.set(x, y, CLOAK)

for y, (L, R) in enumerate([(23,42),(24,41)], start=57):
    for x in range(L, R+1):
        c.set(x, y, BOOT)
c.set(23,57,BOOTD); c.set(42,57,BOOTD)
c.set(24,58,BOOTD); c.set(41,58,BOOTD)

for y in range(13,51):
    c.set(45,y,WOOD); c.set(46,y,WOODD)
for x in range(44,49):
    c.set(x,29,SKIN); c.set(x,30,SKIN); c.set(x,31,SKIN)
c.set(48,30,SKND); c.set(48,31,SKND)
c.set(44,32,CLKD); c.set(44,33,CLKD)

c.rect(19,29,4,4,CLOAK)
c.set(19,33,SKIN); c.set(20,34,SKIN); c.set(21,33,SKIN)
c.set(18,32,SKND)

c.circle(45,13,4,GLOW)
c.circle(45,13,3,AMBR2)
c.circle(45,13,2,AMBR2)
c.set(44,12,GLOW); c.set(43,12,GLOW); c.set(44,11,GLOW)
c.set(47,13,GLOW); c.set(43,14,GLOW); c.set(46,15,AMBR2)

c.set(29,29,HL); c.set(34,29,HL)
c.set(26,30,HAIRD); c.set(27,30,HAIRD)
c.set(38,30,HAIRD); c.set(37,30,HAIRD)
c.set(30,33,SKND); c.set(35,33,SKND)

c.ellipse(32,58,14,2,SHAD)

print(c.stats_text())
print("bbox", c.stats()["bbox"])
print("=== HEAD (15,0)-(50,18) ===")
print(c.matrix_text(region=(15,0,50,18)))
print("=== BODY (14,16)-(50,60) ===")
print(c.matrix_text(region=(14,16,50,60)))
