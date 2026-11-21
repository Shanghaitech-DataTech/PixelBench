from pixelbench_api import *

c = new_canvas(64, 64)

# ---------- palette ----------
OUT  = c.color("#1c1006", "outline")
SHB  = c.color("#6e5234", "bowl_shadow")
WL   = c.color("#e4ac74", "wood_light")
WM   = c.color("#c4844c", "wood_mid")
WD   = c.color("#965a28", "wood_dark")
GRAIN= c.color("#b07640", "grain")
WARM = c.color("#eac092", "warm")
CW   = c.color("#a06432", "chair_wood")
CW2  = c.color("#7c4820", "chair_dark")
CUSH = c.color("#c65c34", "cushion")
CSH  = c.color("#9e4626", "cushion_shade")
CHL  = c.color("#de8060", "cushion_hl")
BR   = c.color("#f0e4c8", "bowl_rim")
BI   = c.color("#dfc8a0", "bowl_inner")
BN   = c.color("#f0ce40", "banana")
BNH  = c.color("#fcea82", "banana_hl")
GP   = c.color("#80b046", "green_apple")
GPH  = c.color("#a8d263", "green_hl")
OR   = c.color("#f08c2c", "orange")
ORH  = c.color("#fcba5e", "orange_hl")
AP   = c.color("#c8342c", "apple")
APH  = c.color("#f47850", "apple_hl")
GR   = c.color("#804c96", "grape")
GRH  = c.color("#a86eb4", "grape_hl")

# ---------- floor shadow ----------
c.ellipse(32, 33, 21, 16, SHB)
c.ellipse(32, 33, 19, 14, WM)

# ---------- table ----------
c.rect(15, 21, 34, 22, OUT)          # table outline
c.rect(16, 22, 32, 20, WM)          # table top base
c.rect(16, 22, 32, 5, WL)           # top plank
c.rect(16, 33, 32, 5, WL)           # lower plank
c.ellipse(31, 31, 14, 9, WARM)       # warm glow on the table

# wood grain streaks
c.line(18, 24, 23, 24, GRAIN)
c.line(45, 36, 47, 36, GRAIN)
c.line(19, 40, 23, 40, GRAIN)
c.line(45, 28, 47, 29, GRAIN)
c.set(21, 35, WD)
c.set(46, 32, WD)

# ---------- bowl of fruit ----------
c.ellipse(32, 33, 11, 8, SHB)        # bowl shadow
c.ellipse(32, 32, 10, 7, OUT)        # bowl rim outline
c.ellipse(32, 32, 9, 6, BR)          # bowl body
c.ellipse(32, 32, 8, 5, BI)          # bowl inner
c.ellipse(32, 27, 4, 2, BN)          # banana
c.set(30, 26, BNH)
c.circle(27, 31, 3, GP)               # green apple
c.set(25, 29, GPH)
c.circle(36, 30, 3, OR)              # orange
c.set(34, 30, ORH)
c.circle(31, 33, 3, AP)               # red apple
c.set(30, 32, APH)
c.circle(33, 36, 2, GR)              # grapes
c.set(34, 36, GRH)

# ---------- chairs ----------
# top chair
c.rect(25, 6, 14, 6, OUT)
c.rect(26, 7, 12, 4, CW2)
c.rect(24, 10, 16, 13, OUT)
c.rect(25, 11, 14, 11, CW)
c.rect(27, 12, 10, 9, CUSH)
c.rect(29, 13, 6, 1, CHL)
c.rect(27, 18, 10, 3, CSH)

# bottom chair
c.rect(24, 43, 16, 13, OUT)
c.rect(25, 44, 14, 11, CW)
c.rect(27, 45, 10, 9, CUSH)
c.rect(29, 46, 6, 1, CHL)
c.rect(27, 51, 10, 3, CSH)
c.rect(25, 55, 14, 6, OUT)
c.rect(26, 56, 12, 4, CW2)

# left chair
c.rect(6, 22, 6, 14, OUT)
c.rect(7, 23, 4, 12, CW2)
c.rect(10, 24, 13, 16, OUT)
c.rect(11, 25, 11, 14, CW)
c.rect(12, 27, 9, 10, CUSH)
c.rect(13, 28, 7, 1, CHL)
c.rect(12, 33, 9, 4, CSH)

# right chair
c.rect(39, 24, 13, 16, OUT)
c.rect(40, 25, 11, 14, CW)
c.rect(41, 27, 9, 10, CUSH)
c.rect(41, 28, 7, 1, CHL)
c.rect(41, 33, 9, 4, CSH)
c.rect(52, 22, 6, 14, OUT)
c.rect(53, 23, 4, 12, CW2)

print(c.stats_text())
print("---- top chair ----")
print(c.matrix_text(region=(20, 3, 44, 22)))
print("---- left chair ----")
print(c.matrix_text(region=(5, 20, 23, 40)))
print("---- right chair ----")
print(c.matrix_text(region=(41, 20, 59, 41)))
print("---- bottom chair ----")
print(c.matrix_text(region=(20, 41, 44, 61)))

finish(c)
