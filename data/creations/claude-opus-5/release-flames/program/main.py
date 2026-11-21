W, H = 88, 63
OX = 3

# ---- colours -------------------------------------------------------------
ORANGE = "#f27219"
AMBER  = "#f4a30c"
YELLOW = "#fed32c"
HOT    = "#fff2c0"
EMBER  = "#c0400c"
BOOT   = "#4a222d"
BLACK  = "#0b0102"
CLOTH  = "#455363"
CLOTHD = "#211d2c"
GREY   = "#443d45"

# ---- frame 1: original content, same canvas size as frame 2 -------------
f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, OX, 0)

# ---- figure stripped of its idle flame ----------------------------------
fig = input_canvas.copy(name="fig")
flame_ids = {fig.color(ORANGE), fig.color(AMBER), fig.color(YELLOW)}
for y in range(63):
    for x in range(47):
        if fig.get(x, y) in flame_ids:
            fig.set(x, y, None)

f2 = new_canvas(W, H, name="frame2")
f2.blit(fig, OX, 0)

# ---- lean the upper body in (shear rows 0..31, +4 at the head) ----------
for y in range(0, 32):
    dx = round((31 - y) * 4 / 31)
    if dx:
        f2.select(0, y, 60, 1).move_to(dx, y, f2)

# ---- thrust the arm: cuff + hand pushed 5px forward, sleeve extended ----
f2.select(33, 20, 12, 5).move_to(38, 20, f2)
f2.line(33, 20, 37, 20, CLOTHD)   # arm top outline
f2.rect(33, 21, 5, 2, CLOTH)      # sleeve
f2.line(33, 23, 37, 23, GREY)     # sleeve shadow
f2.line(33, 24, 37, 24, BLACK)    # underside outline

# ---- left foot steps forward --------------------------------------------
f2.select(22, 53, 11, 8).move_to(26, 53, f2)
f2.line(22, 53, 26, 53, CLOTHD)   # hem / shin
f2.line(22, 54, 26, 54, CLOTHD)
f2.line(23, 55, 26, 55, BOOT)     # boot shaft
f2.line(24, 56, 26, 56, BOOT)
f2.line(25, 57, 26, 57, BLACK)

# ---- the fireball, flying forward ---------------------------------------
# teardrop body: tail swept back, rounded leading edge
f2.path("M56 22 C62 18 64 14 70 15 C75 16 78 19 78 22 "
        "C78 26 75 29 70 29 C64 30 62 26 56 22 Z", ORANGE)
f2.path("M63 22 C67 19 68 18 71 18 C75 19 76 20 76 22 "
        "C76 25 75 26 71 26 C68 26 67 25 63 22 Z", AMBER)
f2.ellipse(72, 22, 3, 2, YELLOW)
f2.set(72, 21, HOT)
f2.set(72, 22, HOT)
f2.set(73, 22, HOT)

# flame licks off the leading edge
f2.set(79, 20, AMBER)
f2.set(79, 24, ORANGE)
f2.set(77, 17, AMBER)
f2.set(77, 27, ORANGE)

# thin streak linking the hand to the ball
f2.line(48, 22, 56, 22, ORANGE)
f2.line(51, 21, 56, 21, EMBER)
f2.line(51, 23, 56, 23, EMBER)

# broken trail: puffs shrinking back toward the hand
f2.ellipse(53, 22, 2, 2, ORANGE)
f2.ellipse(53, 22, 1, 1, AMBER)
f2.ellipse(49, 22, 1, 1, ORANGE)
f2.set(49, 22, AMBER)
f2.set(47, 21, EMBER)
f2.set(47, 23, EMBER)

# wisps shed sideways along the path
f2.line(50, 18, 52, 17, ORANGE)
f2.line(51, 27, 53, 28, EMBER)
f2.line(56, 16, 58, 14, AMBER)
f2.line(57, 28, 59, 30, ORANGE)
f2.line(62, 14, 64, 12, ORANGE)
f2.line(63, 30, 65, 32, EMBER)

# sparks scattered through the trail
for (sx, sy, sc) in [(55, 19, AMBER), (58, 25, ORANGE), (60, 17, AMBER),
                     (66, 13, AMBER), (68, 31, ORANGE), (54, 12, EMBER),
                     (52, 31, EMBER), (73, 14, ORANGE), (74, 30, EMBER),
                     (48, 25, EMBER), (50, 14, ORANGE)]:
    f2.set(sx, sy, sc)

view(f1)
view(f2)

finish([f1, f2])
