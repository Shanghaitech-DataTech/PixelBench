from pixelbench_api import *
import math

out = input_canvas.copy(name="output")
c = out

# ---------- palette ----------
VL = c.color("#3f7a42", "vine_light")
VM = c.color("#2a5e33", "vine_mid")
VD = c.color("#1c4626", "vine_dark")
VH = c.color("#5c944f", "vine_hi")
VS = c.color("#14351f", "vine_shade")

hh  = c.color("#1b2634", "hood")
hhs = c.color("#111a27", "hood_shade")
hhl = c.color("#2e4056", "hood_light")
rb  = c.color("#1a2431", "robe")
rbs = c.color("#0f1620", "robe_shade")
rbl = c.color("#2e4054", "robe_light")
st  = c.color("#513d2a", "staff")
std = c.color("#2c2318", "staff_dark")
g1  = c.color((120,212,255,55), "glow1")
g2  = c.color((105,196,255,130), "glow2")
g3  = c.color((168,232,255), "glow3")
g4  = c.color((240,252,255), "glow4")

def inb(x, y):
    return 0 <= x < 144 and 0 <= y < 256

def leaf(x, y, d):
    pts = [(x, y, VM), (x + d, y, VL), (x + d, y - 1, VH),
           (x + d * 2, y, VM), (x + d, y + 1, VD),
           (x + d * 2, y + 1, VS), (x + d, y + 2, VS)]
    for px, py, col in pts:
        if inb(px, py):
            c.set(px, py, col)

def stem(x0, y0, y1, amp=2, ph=0.0):
    step = 6
    k = 0
    for y in range(y0, y1 + 1):
        x = x0 + int(round(amp * math.sin((y - y0) * 0.22 + ph)))
        c.set(x, y, VD)
        if y % 2 == 0:
            c.set(x + 1, y, VD)
    for y in range(y0 + 3, y1 + 1, step):
        x = x0 + int(round(amp * math.sin((y - y0) * 0.22 + ph)))
        d = 1 if k % 2 == 0 else -1
        leaf(x, y, d)
        if k % 3 == 1:
            leaf(x + d, y + 2, -d)
        k += 1

# ---------- vines on left wall ----------
stem(38, 30, 214, 2, 0.0)
stem(44, 26, 158, 2, 1.3)
stem(50, 38, 180, 1, 2.1)
# extra left clusters
leaf(33, 48, 1); leaf(41, 60, -1); leaf(35, 84, 1)
leaf(47, 96, -1); leaf(39, 118, 1); leaf(52, 132, -1)
leaf(44, 150, 1); leaf(37, 186, -1); leaf(49, 202, 1)

# ---------- vines on right wall ----------
stem(85, 54, 206, 2, 0.5)
stem(92, 44, 200, 2, 1.8)
stem(98, 58, 182, 1, 0.9)
leaf(88, 62, 1); leaf(95, 74, -1); leaf(90, 92, 1)
leaf(97, 104, -1); leaf(93, 124, 1); leaf(99, 140, -1)
leaf(88, 158, 1); leaf(94, 172, -1); leaf(86, 190, 1)

# ---------- vines draping over the arch top ----------
leaf(50, 146, 1); leaf(53, 149, -1); leaf(51, 153, 1)
leaf(80, 146, -1); leaf(83, 149, 1); leaf(81, 153, -1)
leaf(55, 151, 1); leaf(79, 151, -1)

# ---------- cloaked mage at the archway entrance (back view) ----------
# soft light from staff, behind the figure
c.circle(75, 162, 6, g1)
c.circle(75, 162, 4, g2)
# feet stepping into the tower
for x in range(62, 66):
    c.set(x, 211, rbs); c.set(x, 212, rbs)
for x in range(71, 75):
    c.set(x, 211, rbs); c.set(x, 212, rbs)
# cloak body (seen from behind, tapering robe)
c.poly([(60, 196), (77, 196), (75, 213), (62, 213)], rb)
# hood (back of head)
c.ellipse(68, 190, 5, 6, hh)
c.set(65, 183, hh); c.set(66, 183, hh); c.set(67, 183, hh); c.set(68, 183, hh)
# hood back seam / shading
for y in range(185, 197):
    c.set(68, y, hhs)
    if y < 194:
        c.set(67, y, hhs)
# hood rim light (left)
c.set(63, 184, hhl); c.set(63, 185, hhl); c.set(64, 184, hhl)
c.set(64, 189, hhl); c.set(64, 193, hhl)
# cloak rim light (left edge)
for y in range(197, 212):
    c.set(61, y, rbl)
# staff-lit rim on cloak (right side)
for y in range(198, 210):
    c.set(75, y, hhl)
c.set(76, 197, hhl)
# robe folds
for x in (64, 68, 72):
    for y in range(200, 212):
        c.set(x, y, rbs)
# hem shade
for x in range(61, 77):
    c.set(x, 212, rbs)
# staff (held at his side, tip glowing above the shoulder)
c.line(75, 164, 204, std)
c.line(74, 164, 204, st)
c.set(73, 164, st)
# hand gripping staff
c.set(74, 197, hhl); c.set(75, 198, hhl)
# glowing staff head
c.set(74, 163, g3); c.set(75, 163, g3); c.set(73, 162, g3); c.set(74, 162, g3); c.set(75, 162, g4)
c.set(75, 161, g4); c.set(74, 161, g3)
# glow accents down the staff
c.set(75, 166, g2); c.set(75, 170, g2); c.set(75, 175, g2)

print(c.stats_text())
finish(out)
