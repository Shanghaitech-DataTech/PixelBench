# ============================================================
# fountain-flow : turn the waterless fountain into a running one
#   * head-room is added above the finial for a central jet
#   * every tier overflows into the one below
#   * splashes + ripples mark where the water lands
# ============================================================
src = input_canvas

DY = 12  # extra head-room above the finial for the jet
out = new_canvas(64, 88, background=None, name='output')
out.blit(src, 0, DY)

# ---------------- colours ----------------
LIGHT = out.color('#2ec7dc')                    # light water (already in palette)
DEEP  = out.color('#1d8baa')                    # deep water  (already in palette)
PALE  = out.color('#a9eef6', name='spray')      # pale spray / ripple highlight
FOAM  = out.color('#ffffff')                    # white foam sparkle

def P(x, y, col):
    """draw using input-image coordinates (fountain body)"""
    out.set(x, y + DY, col)

# ---------------- 1. central jet above the finial ----------------
jet = [
    (30, 3), (31, 3), (32, 3), (33, 3),
    (31, 4), (32, 4),
    (30, 5), (31, 5), (32, 5), (33, 5),
    (31, 6), (32, 6),
    (31, 7), (32, 7),
    (30, 8), (31, 8), (32, 8), (33, 8),
    (31, 9), (32, 9),
    (31, 10), (32, 10),
    (31, 11), (32, 11),
]
for x, y in jet:
    out.set(x, y, LIGHT)
out.set(31, 1, FOAM); out.set(32, 1, FOAM)          # bright apex
out.set(31, 2, FOAM); out.set(32, 2, FOAM)
out.set(30, 2, PALE); out.set(33, 2, PALE)
for x, y in [(31, 4), (32, 6), (30, 8), (31, 10)]:  # shimmer down the column
    out.set(x, y, PALE)
for x, y in [(28, 4), (35, 4)]:                     # spray droplets
    out.set(x, y, PALE)
for x, y in [(28, 7), (35, 7), (27, 10), (36, 10)]:
    out.set(x, y, LIGHT)

# ---------------- 2. overflow streams between the tiers ----------------
# bowl 1 -> bowl 2
A_L = [(23, 10), (22, 10), (22, 11), (21, 11), (21, 12), (21, 13), (21, 14)]
A_R = [(40, 10), (41, 10), (41, 11), (42, 11), (42, 12), (42, 13), (42, 14)]
# bowl 2 -> bowl 3
B_L = [(18, 16), (17, 17), (16, 17), (15, 18), (15, 19), (15, 20), (15, 21), (16, 22)]
B_R = [(45, 16), (46, 17), (47, 17), (48, 18), (48, 19), (48, 20), (48, 21), (47, 22)]
# bowl 3 -> gold basin (long fall, in front of the basin wall)
C_L = [(14, 24), (13, 24), (12, 24)] + [(x, y) for y in range(25, 48) for x in (11, 12)]
C_R = [(49, 24), (50, 24), (51, 24)] + [(x, y) for y in range(25, 48) for x in (51, 52)]

for x, y in A_L + A_R + B_L + B_R + C_L + C_R:
    P(x, y, LIGHT)
# sparkling highlights down the two long falls
for x, y in [(11, 28), (11, 36), (11, 44), (12, 32), (12, 40)]:
    P(x, y, PALE)
for x, y in [(52, 28), (52, 36), (52, 44), (51, 32), (51, 40)]:
    P(x, y, PALE)

# ---------------- 3. splashes where the water lands ----------------
def splash(x, y):
    P(x,     y,     FOAM)   # upward spurt  (row above the pool edge)
    P(x - 1, y + 1, PALE)
    P(x + 1, y + 1, PALE)
    P(x - 2, y + 2, PALE)
    P(x + 2, y + 2, PALE)
    P(x - 1, y + 2, LIGHT)
    P(x + 1, y + 2, LIGHT)

splash(21, 13)   # bowl 1 -> bowl 2, left
splash(42, 13)   # bowl 1 -> bowl 2, right
splash(16, 21)   # bowl 2 -> bowl 3, left
splash(47, 21)   # bowl 2 -> bowl 3, right
splash(11, 46)   # bowl 3 -> basin, left
splash(52, 46)   # bowl 3 -> basin, right

# spray around the cap, where the jet's water falls back into bowl 1
for x, y in [(27, 7), (36, 7)]:
    P(x, y, FOAM)
for x, y in [(26, 8), (27, 8), (28, 8), (35, 8), (36, 8), (37, 8), (26, 9), (37, 9)]:
    P(x, y, PALE)

# stray droplets flying off the streams
for x, y in [(19, 11), (44, 11), (13, 19), (50, 19), (9, 33), (54, 33)]:
    P(x, y, PALE)

# ---------------- 4. ripples on the pool surfaces ----------------
RIPPLES = [
    (25, 10), (26, 10), (37, 10), (38, 10),   # bowl 1
    (21, 16), (22, 16), (41, 16), (42, 16),   # bowl 2
    (24, 17), (39, 17),
    (18, 26), (19, 26), (44, 26), (45, 26),   # bowl 3
    (22, 27), (41, 27),
    (16, 45), (15, 46), (47, 45), (48, 46),   # basin, near the landings
    (17, 46), (46, 46),                       # waterline at the pedestal
    (20, 49), (43, 49), (25, 51), (38, 51),   # basin, mid pool
    (22, 53), (41, 53), (28, 55), (35, 55),   # basin, lower pool
]
for x, y in RIPPLES:
    P(x, y, PALE)

# ---------------- report & submit ----------------
print(out.stats_text())
finish(out)
