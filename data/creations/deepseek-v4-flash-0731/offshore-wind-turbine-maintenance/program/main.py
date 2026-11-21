from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="offshore_wind_platform")

def col(h):
    return c.color(h)

def dash(x0, x1, y, colour):
    for x in range(x0, x1 + 1):
        c.set(x, y, colour)

# ---------------- SKY ----------------
sky = [col(h) for h in ["#2b5aa8", "#3568ba", "#4377c9", "#5589d8", "#6d9ce2", "#8ab2e8"]]
for y0, y1, i in [(0, 2, 0), (3, 7, 1), (8, 13, 2), (14, 20, 3), (21, 27, 4), (28, 34, 5)]:
    c.rect(0, y0, 64, y1 - y0 + 1, sky[i])

sun_c = col("#f4e9c8")
c.circle(49, 5, 2, sun_c, fill=True)
cloud_hi = col("#eef5fd")
cloud_sh = col("#c9dcf0")
c.rect(7, 6, 13, 3, cloud_hi)   # x7..19 y6..8
c.rect(8, 8, 11, 1, cloud_sh)
c.rect(44, 12, 14, 3, cloud_hi)  # x44..57 y12..14
c.rect(45, 14, 12, 1, cloud_sh)

# ---------------- SEA ----------------
sea = [col(h) for h in ["#35639c", "#2c5790", "#244c84", "#1c4277", "#153768", "#102e5c"]]
for y0, y1, i in [(35, 38, 0), (39, 43, 1), (44, 48, 2), (49, 54, 3), (55, 59, 4), (60, 63, 5)]:
    c.rect(0, y0, 64, y1 - y0 + 1, sea[i])

wv = col("#4f83c0")
foam = col("#d6e8f8")
dashes = {
    37: [(4, 7), (14, 17), (46, 49), (56, 59)],
    40: [(9, 12), (49, 52), (60, 62)],
    44: [(3, 6), (15, 18), (45, 48), (58, 60)],
    48: [(7, 10), (52, 55), (61, 63)],
    52: [(4, 7), (13, 16), (47, 50)],
    56: [(8, 11), (18, 20), (43, 45), (55, 58)],
    60: [(3, 6), (14, 17), (49, 52), (58, 61)],
}
for y, segs in dashes.items():
    for x0, x1 in segs:
        dash(x0, x1, y, wv)
for x, y in [(12, 39), (15, 43), (56, 46), (8, 49), (19, 50), (50, 53), (5, 56), (13, 59), (58, 62), (9, 63), (60, 39), (2, 42), (55, 44), (42, 40), (7, 46)]:
    c.set(x, y, foam)

# ---------------- DISTANCE TURBINES ----------------
dt1 = col("#c8d4e4"); dt1e = col("#a8b8cc"); dt1b = col("#bccbdf")
c.rect(9, 23, 3, 13, dt1)        # tower x9..11 y23..35
for y in range(23, 36):
    c.set(9, y, dt1e)
c.rect(8, 21, 5, 3, dt1)         # nacelle x8..12 y21..23
c.rect(8, 23, 5, 1, dt1e)
c.line(10, 23, 10, 19, dt1b)
c.line(10, 23, 7, 26, dt1b)
c.line(10, 23, 13, 26, dt1b)
c.circle(10, 23, 1, dt1)

dt2 = col("#dde4ef"); dt2b = col("#cdd8e8")
c.rect(54, 26, 2, 10, dt2)        # tower x54..55 y26..35
c.rect(52, 25, 5, 2, dt2)         # nacelle x52..56 y25..26
c.line(54, 26, 54, 24, dt2b)
c.line(54, 26, 52, 28, dt2b)
c.line(54, 26, 56, 28, dt2b)
c.circle(54, 26, 1, dt2)

# ---------------- MAIN TURBINE ----------------
tw = col("#e6ebf2"); tw_sh = col("#c6cede")
for y0, y1, x0, x1 in [(9, 16, 30, 32), (17, 24, 29, 33), (25, 32, 28, 34), (33, 44, 27, 35)]:
    c.rect(x0, y0, x1 - x0 + 1, y1 - y0 + 1, tw)
    for y in range(y0, y1 + 1):
        c.set(x0, y, tw_sh)
        c.set(x1, y, tw_sh)

nac = col("#dfe5ee")
c.rect(27, 4, 11, 6, nac)         # nacelle x27..37 y4..9
c.rect(27, 9, 11, 1, tw_sh)

blade = col("#d3dae6")
c.line(31, 1, 31, 9, blade)       # up blade
c.line(31, 9, 25, 15, blade)      # down-left blade
c.line(31, 9, 37, 15, blade)      # down-right blade
hub = col("#c2cbdb")
c.circle(31, 9, 1, hub)

ladder_c = col("#9aa8bc")
for y in range(11, 41):
    c.set(31, y, ladder_c)
    c.set(32, y, ladder_c)

deck = col("#4b5870"); decktop = col("#64738d"); rail = col("#f0a23c")
leg = col("#37435c"); fender = col("#f2c14e")
c.rect(21, 43, 21, 3, deck)       # deck y43..45
c.rect(21, 43, 21, 1, decktop)
c.line(21, 41, 41, 41, rail)       # handrail
for x in [21, 25, 29, 33, 37, 41]:
    c.set(x, 42, rail)
c.rect(21, 45, 2, 6, leg)         # legs x21..22 y45..50
c.rect(39, 45, 2, 6, leg)         # legs x39..40 y45..50
for y in (47, 49):                 # steel braces between legs
    for x in range(23, 39):
        c.set(x, y, leg)
for x in (20, 41):
    c.set(x, 47, fender)
    c.set(x, 48, fender)

# ---------------- WATER DETAILS ----------------
ref = col("#1d4278")
c.rect(27, 37, 9, 8, ref)         # tower reflection x27..35 y37..44
shim = col("#6fa0d4")
for x, y in [(29, 39), (32, 41), (35, 43), (30, 42)]:
    c.set(x, y, shim)
for x, y in [(20, 44), (23, 45), (40, 44), (41, 45), (24, 47), (38, 48)]:
    c.set(x, y, foam)

# ---------------- TECHNICIAN ON LADDER ----------------
helmet = col("#ffcf3f"); vest = col("#ed6a2f"); dark = col("#39415a")
c.set(31, 21, helmet)
c.set(30, 22, dark)
c.set(31, 22, vest)
c.set(32, 22, dark)
c.set(31, 23, dark)

print(c.stats_text())
print("--- technician region ---")
print(c.matrix_text(region=(24, 17, 45, 27), indices=False))
print("--- sea floor region ---")
print(c.matrix_text(region=(0, 53, 20, 63), indices=False))
print("--- top region ---")
print(c.matrix_text(region=(24, 0, 40, 9), indices=False))

finish(c)
