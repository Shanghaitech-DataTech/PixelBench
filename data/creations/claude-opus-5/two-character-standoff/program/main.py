### 128x128 anime-style standoff: red knight (left) vs green rogue (right)

W = H = 128
bg = new_canvas(W, H, name="standoff")

# ---------------------------------------------------------------- palette
def C(hexv, name):
    bg.color(hexv, name)
    return name

ink      = C('#0b0712', 'ink')
# sky
sky1     = C('#1b1033', 'sky1')
sky2     = C('#331a4a', 'sky2')
sky3     = C('#5a2450', 'sky3')
sky4     = C('#8e3350', 'sky4')
sky5     = C('#c75b43', 'sky5')
sky6     = C('#e58a4d', 'sky6')
cloud_d  = C('#241540', 'cloud_d')
cloud_m  = C('#5e2a50', 'cloud_m')
sun_o    = C('#f0a24f', 'sun_o')
sun_m    = C('#ffd27a', 'sun_m')
sun_c    = C('#fff4c8', 'sun_c')
# ground
gnd_d    = C('#160e22', 'gnd_d')
gnd_m    = C('#241733', 'gnd_m')
gnd_l    = C('#3d2342', 'gnd_l')
gnd_hi   = C('#6b3a4c', 'gnd_hi')
shadow   = C('#100a1a', 'shadow')
# knight reds / steel / gold
red_d    = C('#4e0f1e', 'red_d')
red_m    = C('#9b1f2e', 'red_m')
red_l    = C('#cf3b40', 'red_l')
red_rim  = C('#f59a76', 'red_rim')
cape_d   = C('#3a0a16', 'cape_d')
cape_m   = C('#6d1524', 'cape_m')
stl_d    = C('#2e3648', 'stl_d')
stl_m    = C('#6f7e97', 'stl_m')
stl_l    = C('#bfcddd', 'stl_l')
stl_w    = C('#f2f7ff', 'stl_w')
gold_d   = C('#9a6c22', 'gold_d')
gold_m   = C('#e3b149', 'gold_m')
gold_l   = C('#ffe79a', 'gold_l')
plume_d  = C('#b32b26', 'plume_d')
plume_m  = C('#ef5a3a', 'plume_m')
# rogue greens / leather
grn_d    = C('#0d2c20', 'grn_d')
grn_m    = C('#1b6342', 'grn_m')
grn_l    = C('#2f9a5f', 'grn_l')
grn_rim  = C('#86e0a2', 'grn_rim')
lth_d    = C('#2b1d16', 'lth_d')
lth_m    = C('#5a3b26', 'lth_m')
lth_l    = C('#8a6038', 'lth_l')
face_sh  = C('#17120f', 'face_sh')
eye      = C('#ffe36b', 'eye')

# ---------------------------------------------------------------- sky
bg.rect(0, 0, W, 26, sky1)
bg.rect(0, 26, W, 18, sky2)
bg.rect(0, 44, W, 20, sky3)
bg.rect(0, 64, W, 16, sky4)
bg.rect(0, 80, W, 12, sky5)
bg.rect(0, 92, W, 9, sky6)
# soft band transitions
bg.dither(0, 23, W, 6, [sky1, sky2], pattern="bayer4")
bg.dither(0, 41, W, 6, [sky2, sky3], pattern="bayer4")
bg.dither(0, 61, W, 6, [sky3, sky4], pattern="bayer4")
bg.dither(0, 77, W, 6, [sky4, sky5], pattern="bayer4")
bg.dither(0, 89, W, 5, [sky5, sky6], pattern="bayer4")

# setting sun behind the gap
bg.circle(64, 99, 27, sun_o)
bg.circle(64, 99, 18, sun_m)
bg.circle(64, 100, 9, sun_c)

# cloud bands
bg.path("M0 22 Q 22 16, 44 22 Q 66 28, 92 21 Q 112 16, 127 22 L127 28 "
        "Q 104 33, 74 28 Q 44 23, 0 30 Z", cloud_d)
bg.path("M0 51 Q 26 46, 52 52 Q 78 58, 127 50 L127 55 "
        "Q 84 63, 50 57 Q 24 52, 0 56 Z", cloud_m)
bg.path("M8 70 Q 34 66, 58 71 L58 74 Q 30 77, 8 74 Z", cloud_m)
bg.path("M74 74 Q 100 70, 124 75 L124 78 Q 98 81, 74 78 Z", cloud_m)

# ---------------------------------------------------------------- ground
bg.rect(0, 101, W, H - 101, gnd_m)
bg.rect(0, 101, W, 2, gnd_hi)
bg.dither(0, 103, W, 4, [gnd_hi, gnd_l], pattern="bayer4")
bg.dither(0, 107, W, 5, [gnd_l, gnd_m], pattern="checker")
bg.rect(0, 119, W, 9, gnd_d)
bg.dither(0, 115, W, 5, [gnd_m, gnd_d], pattern="bayer4")
# ground cracks / pebbles
bg.line(6, 122, 22, 116, gnd_m)
bg.line(104, 118, 120, 123, gnd_m)
bg.line(54, 112, 70, 114, gnd_d)
bg.set(44, 124, gnd_l)
bg.set(80, 121, gnd_l)
bg.set(96, 126, gnd_l)

# cast shadows (characters stand on y=104): contact pool + soft dithered fall-off
bg.ellipse(30, 105, 16, 3, gnd_d)
bg.ellipse(99, 105, 17, 3, gnd_d)
bg.ellipse(30, 105, 10, 2, shadow)
bg.ellipse(99, 105, 11, 2, shadow)
for i, y in enumerate(range(107, 114)):
    half = 15 - i
    bg.dither(30 - half, y, half * 2, 1, [gnd_d, shadow], pattern="bayer4")
    half2 = 16 - i
    bg.dither(99 - half2, y, half2 * 2, 1, [gnd_d, shadow], pattern="bayer4")

# ================================================================ KNIGHT
k = new_canvas(W, H, name="knight")

# cape
k.poly([(27, 51), (18, 61), (10, 84), (13, 103), (25, 101), (30, 80), (31, 57)], cape_d)
k.poly([(26, 54), (21, 66), (18, 87), (21, 100), (27, 98), (29, 78)], cape_m)
k.line(20, 70, 19, 92, cape_d)

# legs
k.rect(23, 74, 9, 14, red_d)
k.rect(33, 74, 9, 14, red_m)
k.rect(24, 86, 8, 12, stl_d)
k.rect(34, 86, 8, 12, stl_m)
k.line(41, 87, 41, 97, stl_l)
k.rect(20, 97, 13, 7, stl_d)
k.rect(33, 97, 13, 7, stl_m)
k.line(45, 98, 45, 102, stl_l)
k.rect(24, 85, 8, 2, gold_d)
k.rect(34, 85, 8, 2, gold_m)

# torso
k.poly([(22, 51), (40, 51), (43, 64), (40, 77), (24, 77), (20, 64)], red_m)
k.poly([(34, 52), (40, 52), (43, 64), (40, 76), (36, 76)], red_l)
k.line(43, 58, 42, 71, red_rim)
k.line(42, 56, 42, 60, red_rim)
# belt
k.rect(22, 72, 19, 4, gold_d)
k.rect(28, 72, 6, 4, gold_m)
# chest emblem
k.rect(29, 56, 4, 11, gold_m)
k.rect(25, 59, 12, 3, gold_m)
k.set(31, 58, gold_l)
# pauldrons
k.circle(21, 53, 5, red_d)
k.circle(42, 53, 5, red_m)
k.path("M38 50 Q 44 48, 46 55", red_rim, fill=False)
k.line(18, 50, 17, 55, red_m)
# gorget
k.rect(27, 47, 10, 4, stl_d)
k.line(36, 47, 36, 50, stl_m)

# helmet
k.ellipse(32, 41, 7, 7, red_m)
k.poly([(37, 36), (39, 41), (38, 47), (34, 48)], red_l)
k.line(39, 39, 39, 44, red_rim)
k.rect(26, 40, 13, 5, stl_d)
k.line(27, 42, 38, 42, ink)
k.line(27, 43, 38, 43, ink)
k.line(26, 39, 38, 39, red_l)
k.line(39, 41, 39, 44, stl_m)
k.rect(31, 45, 6, 2, stl_m)
# visor eye glow
k.set(30, 42, eye)
k.set(36, 42, eye)
# crest plume
k.path("M31 33 C 29 25, 20 18, 10 21 C 16 25, 21 30, 27 35 Z", plume_d)
k.path("M30 33 C 28 27, 22 21, 14 21 C 19 26, 24 30, 28 34 Z", plume_m)
k.rect(28, 32, 7, 3, gold_d)
k.set(31, 32, gold_m)

# sword arm
k.poly([(40, 50), (46, 46), (51, 40), (47, 37), (43, 44), (38, 48)], red_m)
k.line(46, 45, 50, 40, red_rim)
k.rect(46, 36, 7, 6, stl_m)
k.line(52, 36, 52, 41, stl_l)
# sword
k.rect(47, 32, 5, 5, lth_d)
k.rect(43, 30, 13, 3, gold_m)
k.line(43, 30, 55, 30, gold_l)
k.poly([(47, 30), (52, 30), (53, 14), (50, 8), (47, 15)], stl_m)
k.poly([(50, 29), (52, 29), (53, 15), (50, 9)], stl_l)
k.line(51, 26, 52, 16, stl_w)

# shield
k.poly([(12, 57), (25, 52), (28, 65), (20, 82), (11, 69)], stl_d)
k.poly([(14, 59), (24, 55), (26, 65), (20, 78), (13, 68)], red_m)
k.poly([(20, 56), (24, 55), (26, 65), (20, 78), (19, 70)], red_l)
k.rect(19, 58, 3, 17, gold_m)
k.rect(15, 63, 11, 3, gold_m)
k.line(25, 57, 27, 66, red_rim)
k.circle(20, 66, 2, gold_l)

# backlight from the sun on the knight's inner (right) edge
k.line(42, 88, 42, 96, red_rim)
k.line(46, 98, 46, 102, gold_l)
k.line(40, 78, 41, 83, gold_l)
k.outline(ink)
bg.blit(k, 0, 0)

# ================================================================ ROGUE
r = new_canvas(W, H, name="rogue")

# cloak mass
r.poly([(101, 48), (112, 56), (120, 76), (118, 98), (104, 103), (92, 101),
        (87, 90), (90, 64), (95, 50)], grn_d)
r.poly([(97, 54), (92, 70), (92, 92), (100, 100), (109, 97), (112, 82),
        (109, 64), (103, 52)], grn_m)
r.line(104, 60, 107, 96, grn_d)
r.line(96, 62, 94, 94, grn_d)
r.path("M90 60 Q 87 76, 89 92", grn_rim, fill=False)
r.line(88, 94, 92, 100, grn_rim)
# hem ragged
r.poly([(92, 96), (97, 103), (102, 97), (108, 102), (112, 92), (116, 96),
        (118, 90), (118, 98), (104, 103), (92, 101)], grn_d)

# tunic / belt
r.poly([(93, 51), (104, 51), (105, 66), (92, 66)], lth_d)
r.rect(92, 64, 15, 3, lth_m)
r.rect(97, 64, 4, 3, gold_m)
r.line(94, 53, 103, 58, lth_m)

# legs (cloak open in front)
r.rect(95, 86, 6, 12, lth_m)
r.rect(103, 86, 6, 11, lth_d)
r.rect(90, 97, 12, 7, lth_d)
r.rect(102, 97, 11, 7, lth_m)
r.line(90, 98, 90, 102, lth_l)
r.rect(95, 84, 6, 2, lth_l)

# hood
r.ellipse(99, 44, 8, 8, grn_m)
r.poly([(103, 37), (114, 29), (117, 35), (107, 45)], grn_d)
r.poly([(100, 36), (106, 38), (107, 46), (101, 51)], grn_d)
r.path("M92 38 Q 90 44, 92 51", grn_rim, fill=False)
r.line(93, 37, 98, 36, grn_l)
# shadowed face
r.poly([(92, 41), (99, 42), (100, 50), (93, 51)], face_sh)
r.rect(93, 45, 2, 2, eye)
r.rect(96, 45, 2, 2, eye)
r.line(92, 52, 99, 52, grn_d)
# scarf
r.poly([(91, 51), (104, 51), (106, 55), (92, 56)], grn_l)
r.line(92, 53, 104, 53, grn_rim)

# front arm with dagger
r.poly([(95, 57), (90, 64), (84, 70), (87, 73), (93, 66), (99, 60)], lth_m)
r.line(86, 70, 90, 65, lth_l)
r.rect(83, 67, 6, 5, lth_d)
r.poly([(84, 71), (88, 73), (79, 81), (77, 79)], stl_m)
r.poly([(86, 72), (88, 73), (79, 81)], stl_l)
# back arm with raised dagger
r.poly([(106, 56), (112, 54), (116, 50), (118, 53), (113, 58), (107, 60)], lth_d)
r.rect(114, 48, 5, 5, lth_m)
r.poly([(115, 48), (119, 48), (122, 33), (117, 38)], stl_m)
r.poly([(117, 47), (119, 47), (121, 35)], stl_l)

# backlight from the sun on the rogue's inner (left) edge
r.line(89, 61, 88, 72, grn_rim)
r.line(90, 98, 90, 102, gold_l)
r.line(84, 69, 83, 71, gold_l)
r.outline(ink)
bg.blit(r, 0, 0)

# ---------------------------------------------------------------- accents
# wind-blown specks between the rivals
for (x, y, col) in [(60, 60, gnd_hi), (68, 72, sky6), (58, 84, sun_m),
                    (72, 50, cloud_m), (64, 40, sky4), (70, 92, sun_m)]:
    bg.set(x, y, col)

print(bg.stats_text())
view(bg)
save("standoff", bg)
finish(bg)
