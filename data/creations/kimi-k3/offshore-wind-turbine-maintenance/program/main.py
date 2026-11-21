# Offshore wind turbine maintenance platform - 64x64
c = new_canvas(64, 64, background=None, name="offshore_maintenance")

# ---------- palette ----------
SKY1 = '#8fc8ec'; SKY2 = '#b3dbf1'; SKY3 = '#d9eef8'
CLOUD = '#ffffff'; CLOUDSH = '#dcecf5'
FARA = '#a9c3d2'; FARB = '#9cb8c8'
SEA1 = '#33739f'; SEA2 = '#285e85'; SEA3 = '#1e4a6c'; SEA4 = '#173a56'
WAVE = '#6fadd0'; WAVE2 = '#4788ab'; WAVE3 = '#3a7398'; SEADK = '#123049'
FOAM = '#e4f3fa'
TWR = '#f2f6f8'; TWRM = '#d3dde3'; TWRS = '#aebbc3'
NAC = '#e9f0f4'; NACS = '#aebcc4'
BLADE = '#eef3f6'; BLADES = '#c3cfd6'
YEL = '#f5a623'; YELH = '#ffbe4a'; YELD = '#c8801a'; YELS = '#9a6210'
STEEL = '#8a939a'; STEELD = '#566068'
ORG = '#ff7a1a'; ORGD = '#d95e0f'; HIV = '#ffd23f'
DARK = '#2c3944'
BIRD = '#41606f'

# ---------- sky ----------
c.rect(0, 0, 64, 12, SKY1)
c.rect(0, 12, 64, 12, SKY2)
c.rect(0, 24, 64, 12, SKY3)

# clouds
c.rect(5, 6, 5, 1, CLOUD);  c.rect(4, 7, 8, 1, CLOUD);  c.rect(6, 8, 5, 1, CLOUDSH)
c.rect(22, 12, 5, 1, CLOUD); c.rect(20, 13, 9, 1, CLOUD); c.rect(23, 14, 5, 1, CLOUDSH)
c.rect(38, 4, 6, 1, CLOUD); c.rect(37, 5, 8, 1, CLOUD);  c.rect(39, 6, 5, 1, CLOUDSH)

# ---------- distant turbines ----------
# turbine A (left, nearer of the two)
c.line(12, 22, 12, 25, FARA)          # blade up
c.line(11, 27, 9, 29, FARA)           # blade down-left
c.line(13, 27, 15, 29, FARA)          # blade down-right
c.line(12, 26, 12, 36, FARA)          # tower
c.set(13, 26, FARA)                   # nacelle nub
# turbine B (right, farther/faded)
c.line(31, 26, 31, 28, FARB)
c.line(30, 30, 28, 32, FARB)
c.line(32, 30, 34, 32, FARB)
c.line(31, 29, 31, 36, FARB)
c.set(32, 29, FARB)

# ---------- ocean ----------
c.rect(0, 36, 64, 8, SEA1)
c.rect(0, 44, 64, 8, SEA2)
c.rect(0, 52, 64, 6, SEA3)
c.rect(0, 58, 64, 6, SEA4)

# wave strokes: (x, y, length, colour)
waves = [
    (0, 37, 3, FOAM), (7, 37, 2, WAVE), (20, 37, 3, FOAM), (33, 37, 2, WAVE),
    (60, 37, 3, FOAM),
    (4, 38, 2, WAVE), (13, 38, 3, WAVE), (25, 38, 2, WAVE), (41, 38, 2, WAVE),
    (1, 40, 3, WAVE), (18, 40, 2, WAVE), (30, 40, 3, WAVE), (52, 40, 2, WAVE),
    (9, 42, 2, WAVE), (22, 42, 3, WAVE), (36, 42, 2, WAVE), (60, 42, 2, WAVE),
    (3, 45, 3, WAVE2), (15, 45, 2, WAVE2), (28, 45, 4, WAVE2), (49, 45, 3, WAVE2),
    (7, 48, 2, WAVE2), (20, 48, 3, WAVE2), (40, 48, 2, WAVE2), (57, 48, 3, WAVE2),
    (0, 51, 2, WAVE2), (12, 51, 3, WAVE2), (33, 51, 2, WAVE2), (52, 51, 2, WAVE2),
    (5, 54, 3, WAVE3), (25, 54, 2, WAVE3), (45, 54, 3, WAVE3), (60, 54, 2, WAVE3),
    (15, 57, 3, WAVE3), (35, 57, 2, WAVE3), (55, 57, 3, WAVE3),
    (2, 60, 3, WAVE3), (22, 60, 2, WAVE3), (42, 60, 3, WAVE3),
    (10, 62, 2, WAVE3), (30, 62, 3, WAVE3), (50, 62, 2, WAVE3),
    (8, 58, 3, SEADK), (28, 60, 4, SEADK), (48, 58, 3, SEADK), (40, 62, 3, SEADK),
]
for x, y, ln, col in waves:
    c.line(x, y, x + ln - 1, y, col)

# ---------- platform legs & bracing (in water) ----------
c.rect(38, 33, 2, 3, YELD)            # legs above waterline
c.rect(45, 33, 2, 3, YELD)
c.rect(38, 36, 2, 11, YELS)           # legs below waterline
c.rect(45, 36, 2, 11, YELS)
c.line(40, 34, 45, 44, YELS)          # X bracing
c.line(44, 34, 39, 44, YELS)

# ---------- boat landing (right of TP) ----------
c.line(57, 31, 57, 42, STEELD)
c.line(59, 31, 59, 42, STEELD)
for ry in (33, 36, 39):
    c.line(56, ry, 59, ry, STEELD)

# ---------- deck ----------
c.rect(36, 31, 12, 1, YEL)            # deck top x36..47
c.rect(36, 32, 12, 1, YELD)           # deck underside
# railing
for rx in (36, 39, 42, 45, 47):
    c.line(rx, 28, rx, 30, STEEL)
c.line(36, 28, 47, 28, STEEL)
# small jib crane on deck
c.line(37, 26, 37, 30, YELD)
c.line(37, 26, 42, 26, YELD)
c.line(42, 27, 42, 28, STEELD)
# supply crate
c.rect(40, 29, 3, 2, ORGD)
c.set(41, 29, HIV)

# ---------- transition piece (yellow base of turbine) ----------
c.rect(48, 30, 8, 8, YEL)             # x48..55, y30..37
c.rect(48, 30, 8, 1, YELH)            # top highlight
c.rect(48, 36, 8, 2, YELD)            # bottom shading
c.rect(54, 31, 2, 5, YELD)            # right shading
c.rect(48, 33, 2, 3, DARK)            # access door
c.set(50, 33, STEELD)                 # door frame hint

# ---------- main tower ----------
c.rect(50, 12, 3, 9, TWRM)            # x50..52 y12..20
c.rect(50, 21, 4, 9, TWRM)            # x50..53 y21..29
c.line(50, 12, 50, 29, TWR)           # lit left edge
c.line(52, 12, 52, 20, TWRS)          # shaded right edge, upper
c.line(53, 21, 53, 29, TWRS)          # shaded right edge, lower
# door high on tower + landing platform
c.rect(50, 19, 2, 3, DARK)
c.rect(46, 22, 4, 1, YELD)            # landing
c.set(46, 21, YELD)                   # landing post

# ---------- nacelle + blades ----------
c.rect(49, 8, 7, 4, NAC)              # nacelle body x49..55 y8..11
c.rect(49, 8, 7, 1, TWR)              # top highlight
c.line(55, 9, 55, 10, NACS)           # rear shade
c.rect(47, 9, 2, 2, TWRS)             # hub x47..48 y9..10
c.rect(47, 1, 2, 8, BLADE)            # blade up
c.line(48, 1, 48, 8, BLADES)
c.line(47, 11, 40, 18, BLADE)         # blade down-left
c.line(48, 11, 41, 18, BLADES)
c.line(49, 11, 57, 19, BLADE)         # blade down-right
c.line(49, 12, 56, 19, BLADES)

# ---------- ladder (deck -> landing) ----------
c.line(45, 22, 45, 31, STEELD)        # rails
c.line(48, 22, 48, 31, STEELD)
for ry in (24, 26, 28, 30):
    c.line(45, ry, 48, ry, STEELD)

# ---------- technician climbing ladder ----------
c.rect(46, 23, 2, 2, '#ffffff')       # helmet
c.set(46, 25, ORG)                    # torso
c.set(47, 25, ORG)
c.line(46, 26, 47, 26, HIV)           # hi-vis stripe
c.set(46, 27, ORG); c.set(47, 27, ORG)
c.line(46, 28, 47, 28, ORGD)          # legs
c.line(46, 29, 47, 29, ORGD)
c.line(46, 30, 47, 30, DARK)          # boots on rung
c.set(48, 24, ORG)                    # arm reaching up rail
c.set(45, 27, ORG)                    # other arm on rail

# ---------- foam around structures ----------
for fx, fy in [(47, 37), (56, 37), (47, 38), (49, 38), (52, 38), (55, 38),
               (48, 39), (54, 39), (37, 36), (40, 36), (44, 36), (47, 36),
               (57, 43), (59, 43), (58, 42), (11, 36), (13, 36), (30, 36), (32, 36)]:
    c.set(fx, fy, FOAM)
c.set(37, 37, WAVE); c.set(46, 37, WAVE)

# ---------- birds ----------
c.set(13, 16, BIRD); c.set(14, 15, BIRD); c.set(15, 16, BIRD)
c.set(20, 13, BIRD); c.set(21, 12, BIRD); c.set(22, 13, BIRD)

print(c.stats_text())
view(c)
finish(c)
