c = input_canvas.copy(name='output')
W, H = c.w, c.h

wsh  = c.color('#12466e', 'water_shadow')
wmid = c.color('#1f6fa6', 'water_mid')
wlit = c.color('#37a8d6', 'water_lit')
whi  = c.color('#7fd8f2', 'water_high')
wfo  = c.color('#e6fbff', 'water_foam')

def hs(y, x0, x1, col):
    if x1 >= x0:
        c.rect(x0, y, x1 - x0 + 1, 1, col)

def arc(cx, y, w, col):
    """shallow wave crest: flat run with the two tips one row lower"""
    for dx in range(-w, w + 1):
        c.set(cx + dx, y, col)
    c.set(cx - w - 1, y + 1, col)
    c.set(cx + w + 1, y + 1, col)

# ------------------------------------------------------------------
# 1. water in the top crown cup (brimming, surface toward viewer)
# ------------------------------------------------------------------
hs(9, 26, 37, whi)
hs(10, 25, 38, wlit)
hs(11, 24, 39, wmid)
hs(12, 23, 40, wsh)
hs(9, 28, 29, wfo)
hs(9, 34, 35, wfo)
c.set(25, 10, wfo)
c.set(38, 10, wfo)
c.set(30, 10, whi)
c.set(33, 10, whi)
# the brim overflows at both shoulders
hs(12, 20, 22, wlit)
hs(12, 41, 43, wlit)
c.set(20, 12, whi)
c.set(21, 12, wfo)
c.set(43, 12, whi)
c.set(42, 12, wfo)

# ------------------------------------------------------------------
# 2. overflow sheeting down the bulb's shoulders (left + right)
# ------------------------------------------------------------------
left_pts = [(20, 13), (19, 14), (18, 15), (17, 16), (17, 17), (16, 18),
            (16, 19), (15, 20), (15, 21), (14, 22), (14, 23), (14, 24),
            (14, 25), (13, 26), (14, 27), (14, 28), (15, 29), (15, 30),
            (16, 31), (17, 32), (18, 33), (19, 33)]

def vstream(pts, side):
    for i, (x, y) in enumerate(pts):
        a = wlit if i % 3 else wmid
        b = whi if i % 4 == 1 else wmid
        if i in (3, 10, 16):
            a, b = whi, wfo
        if side == 'l':
            c.set(x, y, a)
            c.set(x + 1, y, b)
        else:
            c.set(x, y, a)
            c.set(x - 1, y, b)

vstream(left_pts, 'l')
vstream([(W - 1 - x, y) for (x, y) in left_pts], 'r')

# droplets flying beside the falling sheets (in open air)
for (x, y) in [(11, 20), (9, 24), (10, 29)]:
    c.set(x, y, whi)
for (x, y) in [(W - 1 - 11, 20), (W - 1 - 9, 24), (W - 1 - 10, 29)]:
    c.set(x, y, whi)

# ------------------------------------------------------------------
# 3. water in the middle bowl
# ------------------------------------------------------------------
hs(34, 20, 43, whi)
hs(35, 20, 43, wlit)
hs(36, 21, 42, wmid)
hs(37, 22, 41, wmid)
hs(38, 23, 40, wmid)
hs(39, 24, 39, wsh)
hs(40, 26, 37, wsh)
hs(34, 21, 22, wfo)
hs(34, 41, 42, wfo)
c.set(20, 35, wfo)
c.set(43, 35, wfo)
arc(31, 37, 3, whi)
arc(28, 36, 2, whi)

# ------------------------------------------------------------------
# 4. spill from the middle bowl into the lower basin
# ------------------------------------------------------------------
sp_l = [(26, 41), (24, 42), (22, 43), (21, 44), (21, 45)]
sp_r = [(W - 1 - x, y) for (x, y) in sp_l]
for pts in (sp_l, sp_r):
    for i, (x, y) in enumerate(pts):
        c.set(x, y, wlit if i % 2 == 0 else whi)
    c.set(pts[2][0], pts[2][1] + 1, wmid)

# ------------------------------------------------------------------
# 5. the big basin, brimming with water
# ------------------------------------------------------------------
basin = [(44, 16, 47, whi), (45, 14, 49, wlit), (46, 13, 50, wmid),
         (47, 12, 51, wmid), (48, 12, 51, wmid), (49, 12, 51, wmid),
         (50, 13, 50, wmid), (51, 14, 49, wmid), (52, 16, 47, wmid),
         (53, 18, 45, wsh), (54, 21, 42, wsh), (55, 24, 39, wsh),
         (56, 27, 36, wsh), (57, 29, 34, wsh)]
for (y, x0, x1, col) in basin:
    hs(y, x0, x1, col)

# broken foam line on the far edge of the water
hs(44, 18, 20, wfo)
hs(44, 30, 31, wfo)
hs(44, 42, 44, wfo)
# ripples
arc(24, 46, 3, whi)
arc(42, 46, 3, whi)
arc(33, 48, 4, whi)
arc(20, 49, 2, whi)
arc(44, 49, 2, whi)
arc(31, 51, 3, wlit)
arc(24, 53, 2, wlit)
arc(40, 54, 2, wsh)
# splash where the two spills land
for cx in (21, 42):
    for dx in (-1, 0, 1):
        c.set(cx + dx, 46, wfo)
    c.set(cx, 47, wfo)
    c.set(cx - 2, 45, wfo)
    c.set(cx + 2, 45, wfo)

save('fountain_flow', c)
print(c.stats_text())
finish(c)
