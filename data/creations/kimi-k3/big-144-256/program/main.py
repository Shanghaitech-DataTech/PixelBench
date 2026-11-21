from pixelbench_api import *
import random
random.seed(7)

out = input_canvas.copy(name="output")
torch = out.select(33, 207, 9, 12)   # preserve the left torch glow

# ---- palette ----
STEM  = out.color("#2b4127")
LEAF  = out.color("#2a4f31")
LEAFD = out.color("#1d3d2c")
LEAFM = out.color("#3a6b3e")
LEAFH = out.color("#5f7f4e")

CLOAK = out.color("#2a2438")
CLOAKD= out.color("#1d1929")
CLOAKH= out.color("#3a3350")
RIMW  = out.color("#9a7a48")
RIMC  = out.color("#5fa3a6")
STAFF = out.color("#5b4630")
STAFFD= out.color("#443322")
SKIN  = out.color("#b98d63")
CORE  = out.color("#fff3d0")
ORB   = out.color("#ffd98a")
G1    = out.color("#d9b877")
G2    = out.color("#a5824c")
G3    = out.color("#6e5a36")

LEAFW = [LEAFD, LEAF, LEAFM, LEAFH]
WTS   = [3, 4, 2.2, 0.9]

def leafc():
    return random.choices(LEAFW, weights=WTS)[0]

def strand(pts, tuft=0.5, r=1):
    for a, b in zip(pts, pts[1:]):
        out.line(a[0], a[1], b[0], b[1], STEM)
    for a, b in zip(pts, pts[1:]):
        n = max(abs(b[0]-a[0]), abs(b[1]-a[1]), 1)
        for i in range(n+1):
            t = i/n
            x = round(a[0]+(b[0]-a[0])*t)
            y = round(a[1]+(b[1]-a[1])*t)
            if random.random() < tuft:
                out.set(x+random.randint(-r, r), y+random.randint(-r, r), leafc())
                if random.random() < 0.3:
                    out.set(x+random.randint(-r, r), y+random.randint(-r, r), leafc())

def blob(cx, cy, rx, ry, gap=0.14, jagged=0.55):
    for yy in range(cy-ry-1, cy+ry+2):
        for xx in range(cx-rx-1, cx+rx+2):
            e = ((xx-cx)/rx)**2 + ((yy-cy)/ry)**2
            if e < 1.0 - random.random()*jagged and random.random() >= gap:
                out.set(xx, yy, leafc())

# ================= VINES =================
blob(32, 204, 8, 10)                 # left base mass beside the door
blob(30, 218, 7, 6)
torch.copy_to(33, 207, out)          # restore torch over the ivy
strand([(31,196),(29,172),(30,150),(28,128),(29,104),(27,84)], 0.6)  # up the left edge
strand([(40,78),(39,96),(40,118)], 0.5)   # beside upper slit window
strand([(57,84),(58,98),(57,112)], 0.5)
for x, ln in [(38,16),(56,24),(71,14),(86,28),(95,16)]:               # corbel hangers
    strand([(x,70),(x+1,70+ln//2),(x,70+ln)], 0.65)
blob(88, 110, 9, 8)                  # drape over bare brick patch
strand([(86,96),(88,104)], 0.5)
for x in range(30, 99, 6):           # garland resting on the ledge
    if random.random() < 0.8:
        out.set(x+random.randint(-1,1), 150+random.randint(-1,1), leafc())
        out.set(x+random.randint(-1,1), 151+random.randint(0,1), leafc())
for x, ln in [(33,16),(68,18),(74,13),(88,20),(96,12)]:               # hangers from ledge
    strand([(x,158),(x+1,158+ln//2),(x,158+ln)], 0.5)
strand([(80,120),(79,136),(80,152)], 0.4)   # beside lower slit window
strand([(69,226),(70,212),(69,201)], 0.35)  # right of the door frame
strand([(143,108),(132,105),(120,108),(111,112)], 0.5)  # annex creep
blob(137, 126, 7, 10)
strand([(118,112),(119,124),(118,138)], 0.5)
blob(105, 167, 8, 5)
strand([(26,227),(38,225),(50,229)], 0.5)   # ground spill
for _ in range(22):
    out.set(random.randint(24,52), random.randint(224,233), leafc())

# ================= MAGE =================
rows = [
 (200,54,56),(201,53,56),(202,52,57),(203,52,57),(204,51,58),
 (205,51,59),(206,50,59),(207,50,60),(208,49,60),(209,49,61),
 (210,48,61),(211,48,62),(212,48,62),(213,47,62),(214,47,63),
 (215,47,63),(216,46,63),(217,46,64),(218,46,64),(219,46,64),
 (220,46,64),(221,45,64),(222,45,65),(223,45,65),(224,45,65),
]
for y, x0, x1 in rows:
    for x in range(x0, x1+1):
        if y == 224 and x in (47, 50, 63):
            continue
        out.set(x, y, CLOAK)
# hood shading
out.set(53,201,CLOAKD); out.set(54,202,CLOAKD); out.set(55,202,CLOAKD)
out.set(54,203,CLOAKD); out.set(53,203,CLOAKD)
out.set(55,200,CLOAKH); out.set(56,201,CLOAKH); out.set(56,202,CLOAKH)
# cloak folds
for y in range(206, 222, 3):
    out.set(53, y, CLOAKD); out.set(54, y+1, CLOAKD)
for y in range(208, 220, 4):
    out.set(58, y, CLOAKH)
for x in range(47, 64, 3):
    out.set(x, 223, CLOAKD)
# boots (right foot stepping forward)
for x in (50,51,52): out.set(x, 225, "#171421")
for x,y in [(59,225),(60,225),(61,225),(60,226),(61,226)]: out.set(x, y, "#171421")
# staff
for y in range(196, 225):
    out.set(44, y, STAFFD if y % 4 == 0 else STAFF)
out.set(44, 195, "#7a5f3e")
# sleeve + hand gripping staff
for x,y in [(48,207),(47,208),(46,208),(46,209),(47,209)]: out.set(x, y, CLOAK)
out.set(45,208,SKIN); out.set(45,209,SKIN)
# rim lights
for y, x0, x1 in rows:
    if 206 <= y <= 220 and y % 2 == 0: out.set(x0, y, RIMW)
    if 203 <= y <= 221 and y % 2 == 1: out.set(x1, y, RIMC)
out.set(52,204,RIMW); out.set(57,202,RIMC); out.set(57,203,RIMC)
out.set(49,212,RIMW); out.set(49,218,RIMW)
# glowing orb
out.set(43,190,ORB); out.set(44,190,ORB); out.set(45,190,ORB)
out.set(42,191,ORB); out.set(43,191,CORE); out.set(44,191,CORE); out.set(45,191,CORE); out.set(46,191,ORB)
out.set(42,192,ORB); out.set(43,192,CORE); out.set(44,192,CORE); out.set(45,192,CORE); out.set(46,192,ORB)
out.set(43,193,ORB); out.set(44,193,ORB); out.set(45,193,ORB)
out.set(44,194,"#e8bd6d")
# glow halo (solid approximation over dark recess)
for x,y in [(41,190),(47,190),(41,192),(47,192),(41,194),(47,194),(42,189),(46,189),
            (43,188),(44,188),(45,188),(42,195),(46,195),(43,196),(45,196)]: out.set(x,y,G1)
for x,y in [(40,191),(48,191),(40,193),(48,193),(39,192),(49,192),(41,188),(47,188),
            (44,187),(43,187),(45,187),(40,196),(48,196),(42,197),(46,197)]: out.set(x,y,G2)
for x,y in [(38,191),(50,191),(38,193),(50,193),(41,186),(47,186),(44,185),(43,186),
            (45,186),(37,192),(51,192),(41,198),(47,198)]: out.set(x,y,G3)
# light catching arch stones + ground pool
for x,y in [(36,193),(36,197),(52,195),(53,200)]: out.set(x,y,G3)
for x,y in [(42,225),(46,225),(43,226),(45,226),(44,227)]: out.set(x,y,G3)
out.set(43,225,G2); out.set(45,224,G3)

def crop(c, x, y, w, h, name):
    n = new_canvas(w, h, name=name)
    n.blit(c, -x, -y)
    return n

print(view(out))
print(view(crop(out, 30, 180, 45, 52, "mage_zoom"), scale=6, margin=0))
print(view(crop(out, 24, 60, 85, 105, "vines_zoom"), scale=4, margin=0))
finish(out)
