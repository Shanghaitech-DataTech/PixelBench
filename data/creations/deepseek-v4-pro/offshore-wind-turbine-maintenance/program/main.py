from pixelbench_api import *

c = new_canvas(64, 64, name="output")

# ---------- palette ----------
SKY1 = c.color("#4F9CC8", "sky_top")
SKY2 = c.color("#6FB4DC", "sky_mid")
SKY3 = c.color("#A5D4E8", "sky_low")
CLOUD = c.color("#EAF6FC", "cloud")

SEA_H = c.color("#BFE0EE", "sea_horizon")
SEA1 = c.color("#7FB8D8", "sea_1")
SEA2 = c.color("#4A93B8", "sea_2")
SEA3 = c.color("#2E6F96", "sea_3")
SEA4 = c.color("#1E587E", "sea_4")
SEA5 = c.color("#164866", "sea_5")
SEA6 = c.color("#0E3A56", "sea_6")
SEA7 = c.color("#0A2E46", "sea_7")
WAVE = c.color("#6FAECC", "wave")
FOAM = c.color("#DFF3FA", "foam")

TOWER = c.color("#C8D2D8", "tower")
TOWER_SH = c.color("#8FA0A8", "tower_shadow")
TOWER_HI = c.color("#E8EEF0", "tower_highlight")
TOWER_DK = c.color("#4A555C", "tower_dark")

YELLOW = c.color("#F5C518", "safety_yellow")
YELLOW_SH = c.color("#C99A10", "safety_shadow")
YELLOW_HI = c.color("#FADF6A", "safety_hi")

ORANGE = c.color("#F07818", "vest_orange")
ORANGE_SH = c.color("#C05A08", "vest_shadow")
HELMET = c.color("#FFE24A", "helmet")
DARK = c.color("#2E3A44", "legs")

NACELLE = c.color("#E8ECF0", "nacelle")
NACELLE_SH = c.color("#A0A8B0", "nacelle_shadow")

DIST = c.color("#9FB8C8", "dist_turbine")
DIST_SH = c.color("#7C99AC", "dist_shadow")


def band(y0, y1, col):
    if y0 <= y1:
        c.rect(0, y0, 64, y1 - y0 + 1, col)


def wave_row(y, col, dash=4, gap=3, x0=0, x1=63):
    x = x0
    on = True
    while x <= x1:
        if on:
            end = min(x + dash - 1, x1)
            c.rect(x, y, end - x + 1, 1, col)
        x += dash if on else gap
        on = not on


# ---------- sky ----------
band(0, 6, SKY1)
band(7, 13, SKY2)
band(14, 22, SKY3)

# clouds
c.rect(42, 4, 6, 2, CLOUD)
c.rect(44, 3, 3, 1, CLOUD)
c.rect(52, 9, 6, 2, CLOUD)
c.rect(54, 8, 3, 1, CLOUD)
c.rect(5, 11, 5, 2, CLOUD)
c.rect(7, 10, 2, 1, CLOUD)

# ---------- distant sea ----------
band(23, 23, SEA_H)
band(24, 26, SEA1)
band(27, 31, SEA2)
band(32, 36, SEA3)
band(37, 42, SEA4)
band(43, 47, SEA5)

# ---------- distant turbines ----------
# turbine A
c.rect(44, 14, 2, 10, DIST_SH)          # tower
c.rect(43, 12, 4, 2, DIST)              # nacelle
c.rect(43, 8, 2, 4, DIST)               # blade
c.rect(43, 12, 1, 2, DIST_SH)           # hub shadow
# turbine B (farther)
c.rect(55, 16, 1, 8, DIST_SH)           # tower
c.rect(54, 14, 3, 2, DIST)              # nacelle
c.rect(55, 11, 1, 3, DIST)              # blade

# ---------- main platform (deck under tower) ----------
c.rect(4, 39, 33, 3, YELLOW)            # deck x=4..36
c.rect(4, 39, 33, 1, YELLOW_HI)         # top highlight
c.rect(4, 41, 33, 1, YELLOW_SH)         # bottom shadow

# diagonal braces under deck
c.line(12, 45, 4, 41, YELLOW_SH)
c.line(25, 45, 35, 41, YELLOW_SH)

# ---------- main tower ----------
c.rect(13, 8, 12, 49, TOWER)            # x=13..24, y=8..56
c.rect(13, 8, 3, 49, TOWER_SH)          # left shadow
c.rect(21, 8, 4, 49, TOWER_HI)          # right highlight
c.rect(13, 8, 12, 1, TOWER_HI)          # top edge

# nacelle on top
c.rect(11, 2, 15, 6, NACELLE)           # x=11..25, y=2..7
c.rect(11, 2, 15, 1, TOWER_HI)
c.rect(11, 6, 15, 2, NACELLE_SH)        # underside shadow
# hub + blade
c.rect(11, 3, 3, 3, NACELLE_SH)         # hub
c.rect(11, 0, 3, 2, NACELLE)            # blade going up
c.rect(12, 0, 1, 2, TOWER_HI)           # blade highlight

# ---------- platform railings ----------
# left deck railing
c.rect(4, 36, 10, 1, YELLOW_HI)         # x=4..13
for px in (4, 6, 8, 10, 12):
    c.rect(px, 36, 1, 3, YELLOW_SH)
# right deck railing
c.rect(24, 36, 13, 1, YELLOW_HI)        # x=24..36
for px in (24, 26, 28, 30, 32, 34, 36):
    c.rect(px, 36, 1, 3, YELLOW_SH)

# ---------- ladder on tower ----------
c.rect(16, 12, 1, 28, TOWER_DK)         # left rail
c.rect(19, 12, 1, 28, TOWER_DK)         # right rail
for rung_y in range(14, 39, 2):
    c.rect(16, rung_y, 4, 1, TOWER_DK)

# ---------- technician ----------
# right hand reaching up to a rung
c.set(19, 20, ORANGE)
# left hand and forearm on the left rail
c.set(16, 21, ORANGE)
c.set(16, 22, ORANGE)
# safety helmet
c.rect(17, 21, 2, 2, HELMET)
# torso (safety vest)
c.rect(16, 23, 3, 2, ORANGE)
c.rect(16, 24, 1, 1, ORANGE_SH)
# waist + harness strap
c.rect(17, 25, 3, 1, ORANGE_SH)
# legs
c.rect(17, 26, 2, 2, DARK)
# boots on the rung
c.rect(16, 28, 3, 1, DARK)

# ---------- foreground waves (cover tower base) ----------
band(48, 52, SEA5)
band(53, 57, SEA6)
band(58, 63, SEA7)

# wave crests / foam
wave_row(48, FOAM, dash=3, gap=5)
wave_row(52, WAVE, dash=4, gap=4)
wave_row(57, WAVE, dash=4, gap=5, x0=2)
wave_row(61, WAVE, dash=3, gap=4, x0=6)

# foam where tower meets water
c.rect(8, 48, 22, 1, FOAM)
c.rect(10, 49, 18, 1, FOAM)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 63)))

finish(c)
