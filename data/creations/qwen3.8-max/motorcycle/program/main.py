import math

c = new_canvas(128, 128, background=None, name="motorcycle")

# ---------------- palette ----------------
INK      = '#0a0b0e'
BLACK    = '#17181e'
BLACK2   = '#22242c'
DGRAY    = '#363c46'
DGRAY_D  = '#272c34'
MGRAY    = '#525a66'
SILVER   = '#a9b2bd'
SILVER_L = '#d6dce4'
SILVER_D = '#767e89'
RED      = '#cf2029'
RED_D    = '#8a1219'
RED_L    = '#f4575c'
WHITE    = '#eef3f8'
TIRE     = '#1c1d23'
TIRE_HI  = '#31333c'
HUB      = '#8d959f'
GLASS    = '#1d212a'
GLASS_L  = '#3d4655'

# ---------------- helpers ----------------
def Pt(cx, cy, r, a):
    rad = math.radians(a)
    return (cx + r * math.cos(rad), cy - r * math.sin(rad))

def arc(cx, cy, r, a0, a1, step=4):
    n = max(1, int(round(abs(a1 - a0) / step)))
    return [Pt(cx, cy, r, a0 + (a1 - a0) * i / n) for i in range(n + 1)]

def ringsector(cx, cy, ro, ri, a0, a1, col, step=4):
    pts = arc(cx, cy, ro, a0, a1, step) + arc(cx, cy, ri, a1, a0, step)
    c.poly(pts, col, fill=True)

def tube(x0, y0, w0, x1, y1, w1, col):
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy) or 1.0
    px, py = -dy / L, dx / L
    c.poly([(x0 + px * w0 / 2, y0 + py * w0 / 2),
            (x1 + px * w1 / 2, y1 + py * w1 / 2),
            (x1 - px * w1 / 2, y1 - py * w1 / 2),
            (x0 - px * w0 / 2, y0 - py * w0 / 2)], col, fill=True)

def outlined(pts, col, grow=1.3, ocol=INK):
    cx = sum(p[0] for p in pts) / len(pts)
    cy = sum(p[1] for p in pts) / len(pts)
    big = []
    for (x, y) in pts:
        dx, dy = x - cx, y - cy
        L = math.hypot(dx, dy) or 1.0
        big.append((x + dx / L * grow, y + dy / L * grow))
    c.poly(big, ocol, fill=True)
    c.poly(list(pts), col, fill=True)

# ---------------- geometry ----------------
RW = (30, 98)
FW = (97, 98)
R_TIRE = 22
R_IN = 13

def wheel(cx, cy, disc=False):
    c.circle(cx, cy, R_TIRE, INK, fill=True)
    c.circle(cx, cy, R_TIRE - 1, TIRE, fill=True)
    for a in range(0, 360, 18):
        p0 = Pt(cx, cy, R_TIRE - 1, a)
        p1 = Pt(cx, cy, R_TIRE - 4, a + 4)
        c.line(int(round(p0[0])), int(round(p0[1])), int(round(p1[0])), int(round(p1[1])), INK)
    ringsector(cx, cy, 18.5, 17, 55, 150, TIRE_HI)
    ringsector(cx, cy, 18.5, 17, 235, 320, TIRE_HI)
    c.circle(cx, cy, R_IN, None, fill=True)
    ringsector(cx, cy, 14.5, 12.5, 0, 360, SILVER_D)
    ringsector(cx, cy, 14.2, 13.2, 0, 360, SILVER)
    if disc:
        ringsector(cx, cy, 10.5, 8.0, 0, 360, SILVER_D)
        for a in range(0, 360, 60):
            p = Pt(cx, cy, 9.2, a)
            c.set(int(round(p[0])), int(round(p[1])), INK)
    for i in range(10):
        a = 360 * i / 10.0 + 9
        p0 = Pt(cx, cy, 4.5, a)
        p1 = Pt(cx, cy, 13.0, a)
        tube(p0[0], p0[1], 2.4, p1[0], p1[1], 2.4, INK)
    for i in range(10):
        a = 360 * i / 10.0 + 9
        p0 = Pt(cx, cy, 4.5, a)
        p1 = Pt(cx, cy, 13.0, a)
        tube(p0[0], p0[1], 1.4, p1[0], p1[1], 1.4, WHITE)
    c.circle(cx, cy, 5, HUB, fill=True)
    c.circle(cx, cy, 4, SILVER, fill=True)
    c.circle(cx, cy, 2, SILVER_D, fill=True)
    c.set(cx, cy, INK)

wheel(*RW)
wheel(*FW, disc=True)

# ---------------- rear: hugger, shock, swingarm, chain ----------------
ringsector(RW[0], RW[1], 25.5, 22, 60, 150, DGRAY_D)
ringsector(RW[0], RW[1], 25.5, 24, 65, 145, DGRAY)

tube(50, 66, 5.5, 42, 86, 4.5, INK)      # rear shock
tube(50, 66, 3.8, 42, 86, 3.2, DGRAY_D)
for t in (0.25, 0.45, 0.65, 0.85):       # spring coils
    px, py = 50 + (42 - 50) * t, 66 + (86 - 66) * t
    tube(px - 3.4, py + 0.6, 1.8, px + 3.4, py - 0.6, 1.8, SILVER_D)

c.circle(RW[0], RW[1], 7, MGRAY, fill=True)
c.circle(RW[0], RW[1], 6, DGRAY_D, fill=True)
tube(58, 93, 9, RW[0] + 2, 98, 7, INK)   # swingarm
tube(58, 93, 7, RW[0] + 2, 98, 5, SILVER)
tube(58, 92, 3, RW[0] + 4, 96, 2, SILVER_L)
tube(56, 89, 2.2, RW[0], 92, 2.2, INK)   # chain
tube(56, 96, 2.2, RW[0], 104, 2.2, INK)

# ---------------- tail / seat / tank ----------------
outlined([(52, 49), (40, 44), (27, 39), (18, 36), (14, 40), (18, 45), (34, 53), (50, 59)],
         BLACK, grow=1.3)
c.poly([(46, 48), (36, 44.5), (26, 40.5), (21, 40), (34, 46), (45, 51.5)], BLACK2, fill=True)
c.poly([(42, 47), (30, 42.5), (22, 40.5), (21, 41.8), (30, 45), (41, 49.5)], MGRAY, fill=True)
outlined([(11, 38), (17, 35.5), (19.5, 43), (13.5, 45.5)], RED, grow=1.0)   # tail light
c.poly([(12.5, 39), (16.5, 37.3), (17.8, 41.8), (14.3, 43.5)], RED_L, fill=True)
c.set(14, 39, WHITE)
c.poly([(24, 48), (36, 54), (50, 59), (48, 63), (34, 57), (23, 51)], DGRAY_D, fill=True)

outlined([(46, 52), (58, 47), (68, 48), (69, 55), (60, 58), (46, 58)], BLACK, grow=1.2)  # seat
c.poly([(48, 52.5), (58, 49), (67, 50), (67, 53.5), (59, 56), (48, 56)], BLACK2, fill=True)
tube(50, 52, 1.2, 65, 50.5, 1.2, MGRAY)

outlined([(60, 52), (64, 42), (76, 36), (90, 42), (94, 50), (88, 58), (66, 60)],
         BLACK, grow=1.3)   # tank
c.poly([(63, 51), (67, 43), (77, 38.5), (88, 44), (90, 49), (85, 55), (67, 57)], BLACK2, fill=True)
c.poly([(67, 45), (77, 39.5), (86, 44), (84, 47), (76, 43), (68, 48)], MGRAY, fill=True)
c.poly([(63, 55), (85, 51.5), (89, 55), (87, 59.5), (65, 61.5)], RED, fill=True)   # tank stripe
c.poly([(65, 55.6), (84, 52.8), (86.5, 55), (67, 58)], RED_L, fill=True)

# ---------------- mid body / side panel ----------------
outlined([(52, 56), (86, 56), (88, 72), (74, 80), (58, 74), (50, 64)], DGRAY, grow=1.3)
c.poly([(54, 59), (84, 59), (85, 70), (73, 77), (60, 71), (53, 64)], DGRAY_D, fill=True)
c.poly([(58, 62), (78, 62), (77, 66), (58, 66)], INK, fill=True)   # vent

# ---------------- engine ----------------
outlined([(56, 72), (76, 68), (84, 76), (84, 94), (76, 100), (58, 100), (52, 90), (52, 78)],
         DGRAY_D, grow=1.3)
c.poly([(60, 64), (78, 61), (82, 70), (62, 74)], MGRAY, fill=True)   # cylinder
for i, y in enumerate((64, 67, 70)):
    tube(60 + i, y, 1.4, 79 + i, y - 2.6, 1.4, SILVER_D)
c.poly([(56, 88), (84, 86), (84, 94), (76, 100), (58, 100), (52, 92)], BLACK, fill=True)

# ---------------- frame (silver tubular) ----------------
tube(90, 52, 10, 70, 82, 8, INK)      # main spar
tube(90, 52, 8, 70, 82, 6.2, SILVER)
tube(89, 50, 3, 71, 79, 2.2, SILVER_L)
tube(84, 57, 6, 64, 80, 5, INK)       # second spar
tube(84, 57, 4.4, 64, 80, 3.6, SILVER_D)
tube(72, 82, 7, 58, 94, 6, INK)       # down tube to pivot
tube(72, 82, 5.4, 58, 94, 4.6, SILVER)
outlined([(86, 44), (96, 46), (97, 56), (88, 58), (84, 52)], SILVER, grow=1.2)  # steering head
c.circle(58, 94, 5, INK, fill=True)   # pivot boss
c.circle(58, 94, 3.6, SILVER_D, fill=True)

# round silver-gray engine cover
c.circle(70, 86, 11, INK, fill=True)
c.circle(70, 86, 10, SILVER_D, fill=True)
c.circle(70, 86, 8.6, SILVER, fill=True)
c.circle(70, 86, 5.4, SILVER_L, fill=True)
c.circle(70, 86, 3.0, MGRAY, fill=True)
c.circle(70, 86, 1.4, INK, fill=True)
for a in range(0, 360, 60):
    p = Pt(70, 86, 7.2, a + 30)
    c.set(int(round(p[0])), int(round(p[1])), SILVER_D)
ringsector(70, 86, 10, 8.6, 100, 175, SILVER_L)

# ---------------- belly pan ----------------
outlined([(54, 97), (80, 93), (86, 100), (80, 108), (58, 108), (50, 102)], DGRAY, grow=1.3)
c.poly([(56, 99), (79, 95.5), (83, 100), (78, 105.5), (59, 105.5), (53, 101.5)], DGRAY_D, fill=True)
tube(58, 106, 2, 78, 106, 2, INK)
tube(62, 99, 3, 69, 101, 3, INK)            # footpeg
tube(63, 99, 2, 69, 100.6, 2, SILVER_D)

# ---------------- muffler (upswept, over the rear wheel) ----------------
tube(64, 94, 10, 26, 78, 12, INK)
tube(64, 94, 8, 26, 78, 10, SILVER_D)
tube(64, 93, 5.6, 27, 77, 7, SILVER)
tube(60, 90.5, 2.0, 32, 78.5, 2.2, SILVER_L)
tube(47, 87, 10.4, 41, 84.6, 10.4, RED)     # red band
c.circle(26, 78, 5.6, INK, fill=True)
c.circle(26, 78, 4.2, BLACK2, fill=True)
c.circle(26, 78, 2.4, INK, fill=True)

# ---------------- front: fender, fork, fairing ----------------
ringsector(FW[0], FW[1], 28, 23.5, 20, 160, INK)
ringsector(FW[0], FW[1], 27, 24.5, 23, 157, DGRAY)
ringsector(FW[0], FW[1], 27, 25.4, 40, 140, MGRAY)

tube(93, 54, 7, 97, 96, 7, INK)        # fork upper
tube(93, 54, 5.2, 97, 96, 5.2, SILVER)
tube(92.2, 55, 1.8, 96.2, 95, 1.8, SILVER_L)
tube(94, 74, 9, 97, 96, 9, INK)        # fork lower
tube(94, 74, 7, 97, 96, 7, SILVER_D)
tube(93.2, 75, 2.4, 96.2, 95, 2.4, SILVER_L)
c.circle(97, 98, 3.4, INK, fill=True)
c.circle(97, 98, 2.2, SILVER, fill=True)
c.poly([(87, 48), (100, 50), (100, 56), (87, 54)], SILVER_D, fill=True)  # triple clamp

FAIR = [(92, 44), (106, 43), (117, 49), (124, 57), (120, 67), (111, 75),
        (100, 73), (90, 65), (86, 53)]
outlined(FAIR, DGRAY, grow=1.4)
c.poly([(93, 47), (105, 46), (115, 51), (121, 57), (117, 63), (105, 58), (94, 55), (90, 50)],
       MGRAY, fill=True)
c.poly([(96, 49), (105, 48.5), (113, 52.5), (116, 56), (105, 53.5), (96, 52)], DGRAY, fill=True)
c.poly([(90, 63), (96, 70), (104, 73), (112, 72), (119, 65), (111, 73), (100, 71), (92, 64)],
       DGRAY_D, fill=True)
tube(88, 70, 5.5, 118, 64, 4.0, RED_D)     # red swoosh
tube(88, 68.8, 4.4, 118, 62.8, 3.2, RED)
tube(90, 68, 1.8, 114, 62.6, 1.3, RED_L)
c.poly([(96, 59), (110, 63), (109, 67), (95, 63)], INK, fill=True)   # vent
c.poly([(97, 60.4), (108, 63.6), (107.6, 65.4), (96.6, 62.4)], BLACK2, fill=True)
outlined([(110, 48), (119, 52), (120, 62), (111, 59)], GLASS_L, grow=1.1)  # headlight
c.poly([(111.5, 50), (117.5, 53), (118, 60), (112, 57.5)], SILVER_L, fill=True)
c.poly([(113, 52), (116.5, 54), (116.5, 58), (113.5, 56.5)], WHITE, fill=True)
c.poly([(120, 60), (124, 58), (123, 66), (119, 66)], INK, fill=True)  # nose intake

# ---------------- windscreen ----------------
c.poly([(97, 45), (108, 46), (107, 50), (97, 49)], BLACK2, fill=True)   # mount
c.poly([(98, 46), (107, 47), (94, 33), (86, 32)], INK, fill=True)
c.poly([(99, 44.5), (105, 45.5), (93.5, 34.5), (88, 33.8)], GLASS, fill=True)
tube(97.5, 43.5, 1.4, 89.5, 35, 1.2, GLASS_L)

# ---------------- handlebar ----------------
tube(90, 46, 5, 80, 42, 5, INK)
tube(90, 46, 3.4, 81, 42.4, 3.4, SILVER_D)
tube(85, 44, 5.6, 76, 41.5, 5.6, BLACK)     # grip
tube(84, 43.2, 2, 77, 41.2, 2, BLACK2)
tube(84, 47, 2.2, 96, 50, 1.8, SILVER)      # lever

# ---------------- final touches ----------------
c.circle(RW[0], RW[1], 2.2, SILVER_D, fill=True)

print(c.stats_text())
view(c)
save("motorcycle", c)
finish(c)
