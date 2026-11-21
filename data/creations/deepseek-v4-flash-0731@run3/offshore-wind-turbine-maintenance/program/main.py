c = new_canvas(64, 64, name="offshore_wind_maintenance")

def col(spec, name):
    return c.color(spec, name)

# ---------------- palette ----------------
sky0 = col((66, 132, 238), "sky_top")
sky1 = col((94, 156, 242), "sky1")
sky2 = col((122, 178, 246), "sky2")
sky3 = col((152, 200, 248), "sky3")
sky4 = col((186, 222, 250), "sky4")
cloudw = col((250, 252, 255), "cloud_white")
clouds = col((214, 232, 248), "cloud_shade")
sun = col((255, 246, 210), "sun")
sea_h = col((106, 168, 202), "sea_horizon")
sea_u = col((72, 140, 180), "sea_up")
sea_m = col((62, 118, 162), "sea_mid")
sea_l = col((46, 92, 134), "sea_low")
sea_d = col((30, 66, 104), "sea_deep")
w_up = col((150, 202, 226), "wave_light")
w_md = col((104, 158, 194), "wave_mid")
w_lo = col((78, 120, 160), "wave_low")
glint = col((218, 240, 252), "glint")
steel_d = col((48, 52, 60), "steel_dark")
steel = col((88, 94, 106), "steel")
steel_h = col((142, 148, 160), "steel_light")
steel_b = col((184, 190, 202), "steel_bright")
safe = col((216, 120, 48), "safety_orange")
safe_d = col((150, 82, 32), "orange_dark")
wt = col((238, 240, 246), "turbine_white")
wsh = col((196, 202, 214), "white_shade")
wdk = col((154, 160, 176), "white_dark")
dist = col((152, 172, 200), "dist_turbine")
dist_d = col((116, 138, 168), "dist_turbine_dark")
helmet = col((244, 190, 46), "helmet")
vest = col((250, 132, 36), "vest")
suit = col((38, 56, 108), "suit")
boot = col((30, 34, 44), "boot")

# ---------------- sky ----------------
for y in range(0, 6):
    c.rect(0, y, 64, 1, sky0)
for y in range(6, 12):
    c.rect(0, y, 64, 1, sky1)
for y in range(12, 20):
    c.rect(0, y, 64, 1, sky2)
for y in range(20, 30):
    c.rect(0, y, 64, 1, sky3)
for y in range(30, 41):
    c.rect(0, y, 64, 1, sky4)

# sun, clouds, birds
c.circle(52, 9, 3, sun)

def cloud(x0, y0, w, ccol, shcol):
    c.rect(x0, y0, w, 1, ccol)
    c.rect(x0 + 1, y0 - 1, w - 2, 1, ccol)
    c.rect(x0, y0 + 1, w, 1, shcol)

cloud(35, 12, 9, cloudw, clouds)
cloud(6, 20, 8, cloudw, clouds)
cloud(50, 16, 6, cloudw, clouds)

c.set(27, 9, steel_d)
c.set(28, 10, steel_d)
c.set(29, 9, steel_d)
c.set(45, 14, steel_d)
c.set(46, 15, steel_d)
c.set(47, 14, steel_d)

# ---------------- sea ----------------
for y in range(41, 48):
    c.rect(0, y, 64, 1, sea_h)
for y in range(48, 55):
    c.rect(0, y, 64, 1, sea_u)
for y in range(55, 60):
    c.rect(0, y, 64, 1, sea_m)
for y in range(60, 62):
    c.rect(0, y, 64, 1, sea_l)
for y in range(62, 64):
    c.rect(0, y, 64, 1, sea_d)

wave_rows = {
 42: [3, 18, 35, 49, 58],
 43: [8, 25, 41],
 44: [13, 30, 47, 60],
 45: [5, 22, 38, 54],
 46: [10, 28, 44],
 47: [16, 33, 50, 60],
 48: [6, 23, 39, 55],
 49: [11, 29, 46],
 50: [17, 33, 51, 60],
 51: [4, 21, 38, 55],
 52: [9, 26, 43, 59],
 53: [14, 31, 48],
 54: [20, 36, 53, 60],
 55: [5, 23, 40, 57],
 56: [11, 28, 45, 60],
 57: [16, 33, 50],
 58: [22, 38, 55, 60],
 59: [7, 25, 42, 58],
 60: [13, 30, 47, 60],
 61: [19, 36, 52],
}
for y, xs in wave_rows.items():
    wc = w_up if y <= 47 else (w_md if y <= 54 else w_lo)
    for x in xs:
        c.rect(x, y, 2, 1, wc)

for gx, gy in [(12, 45), (20, 48), (27, 52), (33, 47), (40, 53),
              (47, 50), (56, 46), (58, 55), (50, 59), (16, 56), (24, 60), (34, 58)]:
    c.set(gx, gy, glint)

# distant turbines
c.rect(41, 30, 2, 11, dist)
c.line(42, 29, 42, 25, dist)
c.line(42, 29, 38, 32, dist)
c.line(43, 29, 47, 32, dist)
c.rect(40, 28, 5, 2, dist_d)
c.rect(41, 29, 3, 1, dist)

c.rect(52, 31, 2, 9, dist)
c.line(53, 29, 53, 26, dist)
c.line(53, 30, 50, 31, dist)
c.line(54, 30, 56, 31, dist)
c.rect(51, 29, 4, 2, dist_d)
c.rect(52, 29, 2, 1, dist)

# platform structure
c.rect(8, 35, 2, 27, steel)
c.rect(32, 35, 2, 27, steel)
c.rect(9, 35, 1, 27, steel_h)
c.rect(33, 35, 1, 27, steel_h)
c.rect(10, 40, 22, 1, steel_d)
c.line(10, 42, 31, 48, steel_d)
c.line(31, 42, 10, 48, steel_d)
c.rect(10, 51, 22, 1, steel_d)
c.line(11, 53, 30, 58, steel_d)
c.line(30, 53, 11, 58, steel_d)
c.rect(7, 33, 28, 1, steel_b)
c.rect(7, 34, 28, 1, steel)
c.rect(7, 35, 28, 1, steel_d)

# main turbine
c.rect(18, 10, 5, 22, wt)
c.rect(22, 10, 1, 22, wsh)
c.rect(16, 31, 9, 2, wt)
c.rect(19, 0, 3, 4, wt)
c.rect(21, 0, 1, 4, wsh)
c.line(20, 6, 11, 14, wt)
c.line(21, 6, 12, 14, wt)
c.line(20, 6, 28, 14, wt)
c.line(19, 6, 27, 14, wt)
c.rect(15, 4, 11, 4, wt)
c.rect(25, 4, 1, 4, wdk)
c.rect(15, 7, 10, 1, wsh)
c.rect(19, 6, 3, 1, wt)

# technician
for y in range(14, 31, 2):
    c.rect(23, y, 2, 1, steel_h)
c.rect(20, 14, 2, 1, helmet)
c.rect(20, 15, 3, 2, helmet)
c.rect(20, 17, 3, 1, vest)
c.rect(20, 18, 3, 1, vest)
c.set(23, 18, vest)
c.rect(20, 19, 2, 1, suit)
c.set(23, 19, suit)
c.set(22, 20, suit)
c.set(21, 20, boot)
c.set(20, 20, boot)
c.set(21, 21, boot)

# railing
c.rect(7, 31, 28, 1, safe)
for px in range(7, 35, 3):
    c.set(px, 32, safe)

# foam
for fx, fy in [(6, 46), (7, 45), (8, 47), (9, 48), (30, 45), (31, 47),
              (32, 46), (33, 48), (7, 52), (32, 53)]:
    c.set(fx, fy, w_up)
c.rect(5, 50, 3, 1, w_up)
c.rect(32, 44, 3, 1, w_up)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 35, 40), indices=False))
print(c.matrix_text(region=(36, 0, 63, 40), indices=False))
print(c.matrix_text(region=(0, 36, 63, 63), indices=False))

finish(c)
