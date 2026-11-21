"""Subway platform, side view - 64x64 pixel art."""

c = new_canvas(64, 64, background="#0d1018", name="subway")

# ------------------------------------------------------------------ helpers
def hx(h):
    h = h.lstrip('#')
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

def rgbhex(t):
    return '#%02x%02x%02x' % (max(0, min(255, int(round(t[0])))),
                              max(0, min(255, int(round(t[1])))),
                              max(0, min(255, int(round(t[2])))))

def mixc(a, b, t):
    return (a[0] * (1 - t) + b[0] * t,
            a[1] * (1 - t) + b[1] * t,
            a[2] * (1 - t) + b[2] * t)

def tint_region(cv, x0, y0, x1, y1, glass, t):
    g = hx(glass)
    pal = {p['index']: p['rgba'] for p in cv.palette()}
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            if x < 0 or y < 0 or x > 63 or y > 63:
                continue
            idx = cv.get(x, y)
            r, gg, bb, a = pal[idx]
            if a == 0:
                continue
            cv.set(x, y, rgbhex(mixc((r, gg, bb), g, t)))

# ------------------------------------------------------------------ palette
CEIL      = "#0f131c"
CEIL_EDGE = "#1a202c"
WALL      = "#232b3b"
WALL_LN   = "#1b2230"
WALL_HI   = "#2c3547"
TUNNEL    = "#121827"
STEEL_D   = "#2b3342"
STEEL_M   = "#3b4557"
STEEL_L   = "#566377"
FLOOR     = "#3f4653"
FLOOR_L   = "#4b5361"
FLOOR_LN  = "#353b47"
LIP       = "#20242e"
EDGE      = "#5c6579"
YELLOW    = "#e6b93c"
YELLOW_D  = "#a97f22"

ROOF_A    = "#6d798a"
ROOF_B    = "#4a5464"
TRAIN_HI  = "#d6dee6"
TRAIN     = "#adb9c5"
TRAIN_MID = "#7e8998"
WIN       = "#123049"
WIN_HI    = "#2f6f97"
WARM      = "#f6d69a"
WARM_HI   = "#fff2cf"
STRIPE    = "#1fc9ba"
SKIRT     = "#333c49"
GLASS     = "#6f95ad"
GLASS_HI  = "#c3dded"

WOOD      = "#a4683c"
WOOD_D    = "#7a4a24"
WOOD_L    = "#c08550"
SHADOW    = "#1c212b"
SIGNW     = "#eef3f7"
SIGND     = "#12161f"

SKIN_A    = "#f0c39a"
SKIN_B    = "#c98b60"
SKIN_C    = "#8a5537"
HAIR_A    = "#2a2320"
HAIR_B    = "#6b4326"
HAIR_C    = "#191c22"
EYE       = "#201410"
COAT_R    = "#d1495b"
COAT_R_D  = "#a33246"
COAT_B    = "#4a7ae0"
COAT_B_D  = "#2f56a8"
COAT_G    = "#4fa860"
COAT_G_D  = "#357a45"
JEANS     = "#2b3247"
JEANS_D   = "#1e2432"
PANTS_D   = "#242b3a"
SHOE      = "#15181f"
BAG       = "#d9a441"
BAG_D     = "#a87a26"

# ------------------------------------------------------------------ ceiling
c.rect(0, 0, 64, 3, CEIL)
c.rect(0, 2, 64, 1, CEIL_EDGE)
for lx in (1, 45):
    c.rect(lx, 0, 18, 2, WARM_HI)
    c.rect(lx, 1, 18, 1, WARM)

# ------------------------------------------------------------------ upper wall
c.rect(0, 3, 64, 8, WALL)
c.rect(0, 3, 64, 1, WALL_HI)
for tx in range(2, 64, 9):
    c.line(tx, 4, tx, 10, WALL_LN)
c.line(0, 7, 63, 7, WALL_LN)

# ---- route map panel (right of the hanging sign) --------------------
c.rect(49, 4, 13, 7, STEEL_D)
c.rect(50, 5, 11, 5, "#93a1b0")
c.rect(51, 6, 9, 1, COAT_R)
c.rect(51, 8, 9, 1, COAT_B)
c.set(53, 6, "#e9eef3")
c.set(57, 8, "#e9eef3")
c.rect(51, 7, 1, 1, "#5d6a78")

# ------------------------------------------------------------------ beam over the screen doors
c.rect(0, 11, 64, 3, STEEL_D)
c.rect(0, 11, 64, 1, STEEL_M)
c.rect(0, 13, 64, 1, LIP)

# ------------------------------------------------------------------ tunnel + train
c.rect(0, 14, 64, 18, TUNNEL)              # y14..31
c.rect(0, 14, 64, 1, "#171e2c")

# --- train -----------------------------------------------------------
c.rect(0, 14, 64, 1, ROOF_A)
c.rect(0, 15, 64, 2, ROOF_B)
c.rect(0, 17, 64, 2, TRAIN_HI)
c.rect(0, 19, 64, 7, TRAIN)                # y19..25 window band
c.rect(0, 26, 64, 1, TRAIN)
c.rect(0, 27, 64, 1, STRIPE)
c.rect(0, 28, 64, 3, TRAIN_MID)            # y28..30
c.rect(0, 31, 64, 1, SKIRT)

# windows
for wx in (1, 12, 23, 46, 57):
    c.rect(wx, 19, 8, 7, WIN)
    c.rect(wx, 19, 8, 1, WIN_HI)
    c.set(wx + 1, 20, "#1d4a68")
# two lit carriages
for wx in (12, 57):
    c.rect(wx, 19, 8, 7, "#8a6a35")
    c.rect(wx + 1, 20, 6, 5, WARM)
    c.rect(wx + 1, 20, 6, 1, WARM_HI)
    c.set(wx + 2, 22, "#c79a52")

# --- open train doorway (lit interior) ------------------------------
c.rect(31, 18, 13, 13, "#20242e")
c.rect(32, 19, 11, 11, WARM)
c.rect(33, 20, 9, 9, WARM_HI)
c.rect(33, 20, 9, 1, WARM)
c.rect(35, 21, 1, 9, "#b9884a")            # interior poles
c.rect(39, 21, 1, 9, "#b9884a")
c.rect(33, 28, 9, 1, "#b9884a")            # interior floor line
c.rect(32, 29, 11, 1, "#8a6a35")

# --- cab nose (left, arriving) --------------------------------------
c.poly([(0, 31), (0, 25), (2, 20), (5, 17), (13, 17), (13, 31)], TRAIN)
c.poly([(0, 26), (2, 21), (5, 18), (12, 18), (12, 25)], WIN)
c.poly([(1, 25), (3, 22), (5, 20), (10, 19), (10, 23)], "#24506e")
c.rect(0, 17, 4, 1, ROOF_A)
c.rect(0, 26, 3, 1, STRIPE)
c.rect(1, 28, 3, 2, WARM_HI)
c.set(0, 28, WARM)
c.set(0, 29, WARM)
c.rect(0, 30, 13, 1, TRAIN_MID)

# --- steel base of the screen wall ----------------------------------
c.rect(0, 32, 64, 5, STEEL_D)              # y32..36
c.rect(0, 32, 64, 1, STEEL_M)
c.rect(0, 36, 64, 1, LIP)

# ------------------------------------------------------------------ glass panes
for (bx0, bx1) in [(2, 14), (17, 28), (45, 56), (59, 63)]:
    tint_region(c, bx0, 14, bx1, 31, GLASS, 0.42)
    c.line(bx0 + 1, 30, bx0 + 7, 15, GLASS_HI)
    c.line(bx0 + 2, 30, bx0 + 8, 15, "#9fc3d9")
    c.line(bx0 + 8, 30, bx0 + 12, 20, "#9fc3d9")

# open door bay x31..42 : leaves stacked at the sides, clear glass
c.rect(30, 14, 1, 18, STEEL_L)
c.rect(43, 14, 1, 18, STEEL_L)
c.rect(31, 14, 1, 18, STEEL_M)
c.rect(42, 14, 1, 18, STEEL_M)
c.rect(31, 14, 12, 1, STEEL_M)
c.rect(31, 30, 12, 1, STEEL_M)
c.set(32, 15, "#3ddc84")
c.set(33, 15, "#3ddc84")

# posts
for px in (0, 15, 29, 44, 57):
    c.rect(px, 11, 2, 26, STEEL_D)
    c.rect(px, 11, 1, 26, STEEL_L)

# ------------------------------------------------------------------ platform edge
c.rect(0, 37, 64, 1, EDGE)
c.rect(0, 38, 64, 2, YELLOW)               # y38..39
for x in range(0, 64, 3):
    c.set(x, 38, YELLOW_D)
    c.set(x + 1, 39, YELLOW_D)

# ------------------------------------------------------------------ platform floor
c.rect(0, 40, 64, 22, FLOOR)
c.rect(0, 40, 64, 1, FLOOR_L)
c.rect(0, 41, 64, 1, "#4e5665")
for ty in (48, 56):
    c.line(0, ty, 63, ty, FLOOR_LN)
for tx in range(3, 64, 13):
    c.line(tx, 42, tx, 47, FLOOR_LN)
for tx in range(9, 64, 13):
    c.line(tx, 49, tx, 55, FLOOR_LN)
for tx in range(5, 64, 13):
    c.line(tx, 57, tx, 61, FLOOR_LN)
c.rect(0, 62, 64, 2, LIP)

# ------------------------------------------------------------------ bench
c.rect(54, 45, 3, 10, WOOD)                # back rest x54..56
c.rect(54, 45, 3, 1, WOOD_L)
c.line(55, 47, 55, 53, WOOD_D)
c.rect(45, 55, 12, 2, WOOD)                # seat x45..56
c.rect(45, 55, 12, 1, WOOD_L)
c.rect(45, 56, 12, 1, WOOD_D)
c.rect(46, 57, 2, 5, STEEL_D)              # legs
c.rect(53, 57, 2, 5, STEEL_D)

# ------------------------------------------------------------------ passenger A: sitting
c.rect(48, 43, 5, 5, SKIN_C)               # head  y43..47
c.rect(48, 43, 5, 1, HAIR_A)
c.rect(48, 43, 1, 3, HAIR_A)
c.set(52, 44, HAIR_A)
c.set(50, 45, EYE)
c.rect(48, 48, 6, 5, COAT_G)               # torso y48..52
c.rect(52, 48, 2, 5, COAT_G_D)
c.rect(48, 48, 1, 5, COAT_G_D)
c.rect(48, 53, 6, 1, COAT_G_D)             # waist
c.rect(44, 53, 8, 2, JEANS)                # thighs y53..54
c.rect(44, 54, 8, 1, JEANS_D)
c.rect(43, 55, 3, 5, JEANS)                # shins y55..59
c.rect(43, 55, 1, 5, JEANS_D)
c.rect(42, 60, 4, 1, SHOE)                 # shoes
c.line(51, 49, 46, 54, COAT_G_D)           # arm to knee
c.set(45, 54, SKIN_C)

# ------------------------------------------------------------------ passenger B: waiting
c.rect(7, 41, 5, 5, SKIN_A)                # head y41..45
c.rect(7, 41, 5, 1, HAIR_C)
c.set(7, 42, HAIR_C)
c.set(7, 43, HAIR_C)
c.set(11, 42, HAIR_C)
c.set(9, 43, EYE)
c.rect(6, 46, 7, 9, COAT_B)                # torso y46..54
c.rect(10, 46, 3, 9, COAT_B_D)             # near arm
c.rect(6, 46, 1, 9, COAT_B_D)
c.rect(7, 46, 3, 1, COAT_B_D)              # collar
c.rect(12, 54, 1, 2, SKIN_A)               # hand at the side
c.rect(7, 55, 2, 5, JEANS)                 # legs y55..59
c.rect(10, 55, 2, 5, JEANS)
c.rect(7, 55, 1, 5, JEANS_D)
c.rect(10, 55, 1, 5, JEANS_D)
c.rect(6, 60, 3, 1, SHOE)
c.rect(9, 60, 4, 1, SHOE)
c.rect(5, 47, 2, 6, BAG)                   # backpack on the back
c.rect(5, 47, 2, 1, BAG_D)
c.set(5, 50, BAG_D)

# ------------------------------------------------------------------ passenger C: running
c.rect(24, 40, 5, 5, SKIN_B)               # head y40..44
c.rect(24, 40, 5, 1, HAIR_B)
c.rect(24, 41, 1, 2, HAIR_B)
c.rect(28, 41, 1, 3, HAIR_B)
c.set(27, 43, EYE)
c.rect(26, 45, 2, 1, SKIN_B)               # neck
c.rect(23, 45, 6, 3, COAT_R)               # torso leaning right
c.rect(24, 47, 6, 3, COAT_R)
c.rect(25, 49, 6, 3, COAT_R)
c.rect(26, 51, 6, 2, COAT_R)
c.rect(27, 45, 2, 3, COAT_R_D)
c.rect(28, 47, 2, 3, COAT_R_D)
c.rect(29, 49, 2, 3, COAT_R_D)
c.rect(30, 51, 2, 2, COAT_R_D)
c.line(29, 46, 33, 49, COAT_R_D)           # front arm forward
c.line(29, 47, 33, 50, COAT_R_D)
c.rect(33, 49, 2, 2, SKIN_B)
c.line(23, 47, 19, 50, COAT_R)             # back arm behind
c.line(23, 48, 19, 51, COAT_R)
c.rect(18, 50, 2, 2, SKIN_B)
c.rect(26, 52, 6, 2, PANTS_D)              # hips
c.poly([(31, 53), (33, 54), (33, 60), (30, 60)], PANTS_D)   # front leg
c.rect(29, 60, 5, 1, SHOE)
c.poly([(26, 53), (29, 53), (24, 58), (21, 57)], PANTS_D)   # back leg
c.rect(19, 57, 3, 1, SHOE)

# ------------------------------------------------------------------ hanging sign
c.rect(21, 1, 1, 3, STEEL_M)
c.rect(42, 1, 1, 3, STEEL_M)
c.rect(17, 4, 30, 9, SIGND)
c.rect(18, 5, 28, 7, SIGNW)
c.rect(19, 5, 7, 7, COAT_R)
c.text(20, 5, "2", "#ffffff")
c.rect(29, 7, 11, 3, "#1c2430")
c.poly([(40, 5), (45, 8), (40, 11)], "#1c2430")

# ------------------------------------------------------------------ finishing touches
c.set(36, 16, GLASS_HI)
c.line(45, 21, 56, 21, GLASS_HI)

# speed streaks trailing the runner
c.line(14, 45, 16, 45, FLOOR_L)
c.line(15, 49, 17, 49, FLOOR_L)

# ------------------------------------------------------------------ suitcase beside the bench
c.rect(58, 55, 5, 6, "#a3503e")
c.rect(58, 55, 5, 1, "#c06a52")
c.rect(58, 57, 5, 1, "#7c3a2c")
c.rect(59, 53, 3, 1, "#3a3f4a")
c.set(59, 54, "#3a3f4a")
c.set(61, 54, "#3a3f4a")
c.set(60, 58, "#d9b06a")

# contact shadows
c.ellipse(8, 61, 6, 1, SHADOW)
c.ellipse(27, 61, 7, 1, SHADOW)
c.ellipse(45, 61, 6, 1, SHADOW)
c.ellipse(54, 61, 5, 1, SHADOW)

def ascii_render(cv, x0=0, y0=0, x1=63, y1=63):
    ramp = " .:-=+*#%@"
    pal = {p['index']: p['rgba'] for p in cv.palette()}
    out = ['    ' + ''.join(str((x // 10) % 10) for x in range(x0, x1 + 1)),
           '    ' + ''.join(str(x % 10) for x in range(x0, x1 + 1))]
    for y in range(y0, y1 + 1):
        row = ''
        for x in range(x0, x1 + 1):
            r, g, b, a = pal[cv.get(x, y)]
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
            row += ramp[max(0, min(9, int(lum * 10)))]
        out.append('%3d ' % y + row)
    return '\n'.join(out)

result = c
save("subway_platform", c)
print(c.stats_text())
print(ascii_render(c))
finish(result)
