from pixelbench_api import *

W = H = 128
c = new_canvas(W, H)

# ---- Sky gradient bands (sunset) ----
sky_cols = [
    (24, 9, 38),
    (44, 20, 58),
    (66, 31, 74),
    (92, 46, 86),
    (116, 55, 87),
    (138, 66, 84),
    (156, 77, 76),
    (172, 92, 66),
    (190, 110, 56),
    (206, 128, 50),
]
band = 8
for i, col in enumerate(sky_cols):
    c.rect(0, i * band, W, band, col)
# fill to ensure full top region covered down to y=80
c.rect(0, 10 * band, W, 128 - 10 * band, sky_cols[-1])

# ---- Large orange sun (partially setting) ----
c.circle(64, 66, 20, (255, 178, 50))
c.circle(64, 66, 16, (255, 200, 66))
c.circle(64, 67, 11, (255, 214, 92))

# ---- Thin high streaky clouds ----
cloud_hi = [(138, 66, 84), (180, 96, 72), (205, 133, 60)]
# streaks at upper sky
c.ellipse(26, 30, 16, 2, cloud_hi[0])
c.ellipse(20, 31, 20, 2, cloud_hi[1])
c.ellipse(96, 26, 18, 2, cloud_hi[0])
c.ellipse(92, 27, 22, 2, cloud_hi[1])
c.ellipse(40, 44, 20, 3, cloud_hi[1])
c.ellipse(110, 42, 16, 2, cloud_hi[1])
c.ellipse(8, 18, 14, 2, cloud_hi[0])

# ---- Layered clouds near horizon (over sun lower edge) ----
# back pink layer
c.ellipse(22, 56, 28, 6, (216, 96, 96))
c.ellipse(64, 54, 34, 7, (216, 96, 96))
c.ellipse(104, 58, 28, 6, (216, 96, 96))
# warm mid layer
c.ellipse(14, 66, 24, 5, (240, 138, 74))
c.ellipse(52, 62, 30, 6, (240, 138, 74))
c.ellipse(88, 68, 26, 5, (240, 138, 74))
c.ellipse(116, 66, 22, 5, (240, 138, 74))
# bright thin bottom glow band
c.ellipse(6, 74, 32, 3, (255, 168, 70))
c.ellipse(64, 76, 36, 3, (255, 168, 70))
c.ellipse(122, 76, 30, 3, (255, 168, 70))

# ---- Sea ----
sea_cols = [
    (150, 74, 58),
    (130, 62, 60),
    (108, 50, 60),
    (86, 40, 54),
    (66, 31, 46),
    (50, 24, 40),
    (40, 20, 36),
    (32, 17, 31),
]
sea_y0 = 82
seab = (116 - sea_y0) // len(sea_cols)
for i, col in enumerate(sea_cols):
    y0 = sea_y0 + i * seab
    c.rect(0, y0, W, seab, col)
# fill rest of sea down to 116
c.rect(0, sea_y0 + len(sea_cols) * seab, W, 116 - (sea_y0 + len(sea_cols) * seab), sea_cols[-1])

# ---- Sun reflection column in the sea ----
ref_cols = [
    (255, 206, 90),
    (235, 160, 80),
    (200, 116, 92),
    (160, 88, 96),
    (120, 62, 98),
]
# bright core near horizon
for yy in range(86, 118, 2):
    w = 10 if yy < 94 else 6 if yy < 104 else 4
    c.rect(64 - w // 2, yy, w, 2, ref_cols[min((yy - 86) // 5, len(ref_cols) - 1)])
# scattered sparkles
c.set(58, 98, ref_cols[0]); c.set(70, 100, ref_cols[0])
c.set(60, 106, ref_cols[1]); c.set(72, 108, ref_cols[1])
c.set(62, 112, ref_cols[2]); c.set(66, 111, ref_cols[0])

# ==== Central cliff / landmass ====
cliff = (37, 24, 44)
c.poly([(24, 116), (30, 92), (40, 82), (88, 82), (98, 92), (104, 116)], cliff)
# rugged cliff top detail
c.poly([(44, 84), (52, 79), (58, 83), (66, 80), (74, 83), (84, 79), (90, 85), (60, 86)], cliff)

# ==== Castle silhouette ====
cast = (35, 20, 43)
# keep
c.rect(52, 50, 24, 34, cast)
# keep crenellations
for x in range(52, 76, 6):
    c.rect(x, 46, 4, 4, cast)
# side wings
c.rect(46, 56, 6, 28, cast)
c.rect(76, 56, 6, 28, cast)
# gate arch
c.poly([(58, 84), (58, 78), (70, 78), (70, 84)], cast)
c.rect(58, 78, 12, 6, cast)

# towers
c.rect(38, 44, 10, 40, cast)
c.rect(80, 44, 10, 40, cast)
# tower roofs (spires)
c.poly([(38, 44), (43, 22), (48, 44)], cast)
c.poly([(80, 44), (85, 22), (90, 44)], cast)
# small top pennants (short)
c.rect(52, 44, 24, 3, cast)

# ---- Flags on the two towers ----
fk = (214, 54, 46)
c.line(43, 14, 43, 4, (60, 34, 60))   # left pole
c.poly([(43, 6), (43, 2), (56, 2), (56, 5)], fk)  # left flag flying right
c.line(85, 14, 85, 4, (60, 34, 60))   # right pole
c.poly([(85, 6), (85, 2), (98, 2), (98, 5)], fk)

# lit windows
win = (255, 206, 120)
c.rect(56, 58, 3, 4, win)
c.rect(63, 58, 3, 6, win)
c.rect(69, 58, 3, 4, win)
c.rect(40, 50, 2, 3, win)
c.rect(44, 50, 2, 3, win)
c.rect(82, 50, 2, 3, win)
c.rect(86, 50, 2, 3, win)

# rim light on left (sun side) of castle
rim = (255, 168, 110)
for yy in range(56, 84):
    c.set(52, yy, rim)
for yy in range(52, 58):
    c.set(52, yy, rim)  # main body edge highlight
for yy in range(58, 84):
    c.set(46, yy, rim)  # left wing edge
for yy in range(50, 66):
    c.set(38, yy, rim)  # left tower edge

# ==== Dark foreground rocks ====
rock1 = (26, 16, 32)
rock2 = (18, 12, 24)
rock3 = (12, 8, 17)
# main bottom band
c.rect(0, 116, W, 12, rock3)
# jagged peaks roaring up
c.poly([(0, 116), (10, 104), (20, 112), (30, 106), (42, 114), (54, 108), (62, 116),
        (66, 112), (78, 116)], rock1)
c.poly([(70, 116), (80, 102), (92, 110), (102, 100), (112, 110), (120, 103), (128, 116)], rock1)
# darker accents
c.poly([(8, 116), (16, 108), (26, 116)], rock2)
c.poly([(96, 116), (104, 106), (112, 112), (122, 103), (128, 116)], rock2)
c.poly([(40, 116), (48, 112), (58, 116)], rock2)
# a watchtower silhouette rock rising left foreground extends
c.poly([(0, 116), (16, 96), (30, 110), (44, 116)], rock1)
c.poly([(88, 116), (100, 98), (114, 112), (128, 116)], rock1)

# light shimmer on some rock tops from sunset
gl = (170, 96, 74)
c.rect(16, 96, 3, 2, gl)
c.rect(100, 98, 3, 2, gl)
c.rect(80, 102, 3, 2, gl)

print(c.stats_text())
finish(c)
