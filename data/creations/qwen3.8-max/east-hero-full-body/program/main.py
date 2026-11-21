import math

W = H = 256
BAYER = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]

# ---------------- palette ----------------
INK = "#0b0e16"

S0 = "#121a2b"; S1 = "#1a2540"; S2 = "#243454"; S3 = "#31496e"
S4 = "#43628a"; S5 = "#5b7ea3"; S6 = "#779cb8"; S7 = "#9abdcf"
S8 = "#bcd7e0"; S9 = "#d8e8ea"

MOON = "#f2ecd8"; MOON2 = "#d5d3c1"
M_FAR = "#7b9ab4"; M_FAR_D = "#688aa8"
M_MID = "#4e6f90"; M_MID_D = "#3f5d7c"
M_NEAR = "#2d4560"; M_NEAR_D = "#22364c"
TREE = "#182634"
MIST1 = "#a8c4d2"; MIST2 = "#c6dce4"; MIST3 = "#e2eef0"

ROCK1 = "#39424f"; ROCK2 = "#2a323d"; ROCK3 = "#1d232c"; ROCK4 = "#4d5967"
GRASS = "#2c4238"; GRASS2 = "#3f5c46"
BAMBOO = "#141b25"; BAMBOO2 = "#243341"

HAT_L = "#e0bd85"; HAT_M = "#c19a63"; HAT_D = "#9a7444"; HAT_DD = "#74552e"; HAT_RIM = "#452f15"
SKIN = "#c99a72"; SKIN_L = "#e2b78e"; SKIN_D = "#9a6c4a"; SKIN_DD = "#59392a"
HAIR = "#14161f"; HAIR_L = "#252a3a"; HAIR_HL = "#3d4560"
ROBE = "#252e46"; ROBE_L = "#354260"; ROBE_LL = "#48587a"; ROBE_D = "#1a2132"; ROBE_DD = "#111623"
TRIM = "#66789a"; TRIM_L = "#8fa2c0"
SASH = "#8e2c35"; SASH_L = "#b9454c"; SASH_D = "#5e1a22"; SASH_H = "#d4666e"
INNER = "#c6cbd6"; INNER_D = "#949baa"
BLADE_L = "#eef4f9"; BLADE = "#bcc9d6"; BLADE_D = "#7c8998"; BLADE_DD = "#596574"
GOLD = "#cfa64e"; GOLD_D = "#8b6a2c"; GOLD_L = "#e8c97e"
GRIP = "#3b2b21"; GRIP_L = "#5d4533"
BOOT = "#1b2130"; BOOT_L = "#2d3548"
RIM = "#7e9fba"

bg = new_canvas(W, H, name="bg")
ch = new_canvas(W, H, name="ch")

# ================= SKY =================
sky_stops = [(0, S0), (26, S1), (52, S2), (78, S3), (104, S4),
             (130, S5), (154, S6), (176, S7), (196, S8), (216, S9)]
for y in range(0, 230):
    i = 0
    while i < len(sky_stops) - 2 and y >= sky_stops[i + 1][0]:
        i += 1
    ya = sky_stops[i][0]; yb = sky_stops[i + 1][0]
    ha = sky_stops[i][1]; hb = sky_stops[i + 1][1]
    t = (y - ya) / float(yb - ya)
    bg.rect(0, y, W, 1, ha)
    if 0.02 < t < 0.98:
        for x in range(W):
            if (BAYER[y & 3][x & 3] + 0.5) / 16.0 < t:
                bg.set(x, y, hb)

# ================= MOON =================
bg.circle(46, 46, 27, "#1b2740")
bg.circle(46, 46, 21, "#2b4266")
bg.circle(46, 46, 17, "#6d8aa6")
bg.circle(46, 46, 14, MOON)
bg.circle(41, 42, 3, MOON2)
bg.circle(51, 50, 2, MOON2)
bg.circle(49, 39, 2, MOON2)
bg.circle(43, 53, 1, MOON2)

# ================= FAR RANGE =================
bg.path("M 0,200 L 0,152 L 10,128 L 20,146 L 30,92 L 44,130 L 58,112 L 74,150 "
        "L 96,170 L 124,178 L 152,172 L 172,154 L 186,116 L 196,138 L 206,80 "
        "L 220,124 L 236,102 L 250,148 L 255,140 L 255,200 Z", M_FAR)
bg.path("M 30,92 L 44,130 L 36,130 L 25,106 Z", M_FAR_D)
bg.path("M 206,80 L 220,124 L 211,124 L 199,98 Z", M_FAR_D)
bg.path("M 0,200 L 0,178 L 22,166 L 46,180 L 72,168 L 98,182 L 132,188 "
        "L 166,182 L 192,168 L 218,180 L 242,166 L 255,178 L 255,200 Z", M_FAR_D)


def mist(c, y0, y1, color, dens=1.0, fade=5, phase=0.0):
    for y in range(y0, y1 + 1):
        edge = min(y - y0, y1 - y)
        base = dens * min(1.0, (edge + 1) / float(fade))
        for x in range(W):
            d = base * (0.72 + 0.28 * math.sin(x * 0.042 + phase + y * 0.11))
            if (BAYER[y & 3][x & 3] + 0.5) / 16.0 < d:
                c.set(x, y, color)


mist(bg, 146, 176, MIST1, 0.75, 7, 0.4)
mist(bg, 156, 172, MIST2, 0.55, 5, 2.1)

# ================= MID RANGE =================
bg.path("M 0,212 L 0,170 L 16,146 L 34,168 L 52,134 L 74,166 L 92,152 "
        "L 112,182 L 140,192 L 166,184 L 184,158 L 198,136 L 214,164 "
        "L 232,142 L 248,170 L 255,158 L 255,212 Z", M_MID)
bg.path("M 52,134 L 74,166 L 63,166 L 46,146 Z", M_MID_D)
bg.path("M 198,136 L 214,164 L 205,164 L 192,146 Z", M_MID_D)
bg.path("M 232,142 L 248,170 L 239,170 L 226,152 Z", M_MID_D)

mist(bg, 176, 202, MIST2, 0.7, 7, 1.2)
mist(bg, 184, 198, MIST3, 0.5, 5, 3.4)

# ================= NEAR HILLS =================
bg.path("M 0,226 L 0,200 L 24,190 L 48,202 L 74,192 L 100,206 L 132,211 "
        "L 164,204 L 190,192 L 214,202 L 240,190 L 255,202 L 255,226 Z", M_NEAR)
bg.path("M 24,190 L 48,202 L 37,202 L 20,196 Z", M_NEAR_D)
bg.path("M 190,192 L 214,202 L 203,202 L 186,196 Z", M_NEAR_D)


def tree(c, x, y, h, col):
    c.path("M %d,%d L %d,%d L %d,%d Z" % (x, y, x - h // 3, y + h, x + h // 3, y + h), col)
    c.path("M %d,%d L %d,%d L %d,%d Z" % (x, y - h // 2, x - h // 4, y + h // 3, x + h // 4, y + h // 3), col)


for tx, ty, th in [(8, 194, 12), (20, 198, 9), (36, 196, 14), (54, 202, 10),
                   (68, 198, 13), (198, 196, 13), (212, 200, 10), (226, 194, 15),
                   (242, 198, 11), (152, 206, 8), (166, 204, 10)]:
    tree(bg, tx, ty, th, TREE)

mist(bg, 202, 220, MIST2, 0.45, 6, 2.6)
mist(bg, 208, 216, MIST3, 0.3, 4, 0.7)

# ================= FOREGROUND ROCK =================
bg.path("M 0,255 L 0,242 L 26,246 L 54,248 L 78,244 L 104,236 L 140,231 "
        "L 178,229 L 212,233 L 240,229 L 255,233 L 255,255 Z", ROCK2)
bg.path("M 0,242 L 26,246 L 54,248 L 78,244 L 104,236 L 140,231 L 178,229 "
        "L 212,233 L 240,229 L 255,233 L 255,238 L 238,234 L 210,238 "
        "L 176,234 L 138,236 L 102,242 L 76,250 L 50,253 L 22,251 L 0,248 Z", ROCK1)
bg.path("M 0,252 L 30,254 L 70,255 L 0,255 Z", ROCK3)
bg.path("M 104,240 L 132,236 L 168,234 L 200,238 L 176,240 L 140,241 Z", ROCK4)
bg.path("M 18,248 L 44,250 L 62,252 L 36,253 Z", ROCK3)
bg.path("M 196,236 L 224,234 L 250,238 L 224,242 Z", ROCK3)


def tuft(c, x, y, col, s=1):
    c.line(x, y, x - 3 * s, y - 7 * s, col)
    c.line(x, y, x, y - 9 * s, col)
    c.line(x, y, x + 3 * s, y - 6 * s, col)
    c.line(x, y, x + 5 * s, y - 3 * s, col)


for gx, gy in [(16, 246), (34, 250), (58, 251), (86, 246), (110, 240),
               (150, 236), (186, 234), (206, 238), (232, 234), (248, 238)]:
    tuft(bg, gx, gy, GRASS)
    tuft(bg, gx + 4, gy + 1, GRASS2)

# ================= BAMBOO (right frame) =================
for bx, bw, top in [(226, 10, 18), (244, 8, 62)]:
    bg.rect(bx, top, bw, 256 - top, BAMBOO)
    bg.rect(bx, top, 2, 256 - top, BAMBOO2)
    for ny in range(top + 16, 256, 32):
        bg.rect(bx - 1, ny, bw + 2, 2, BAMBOO2)
        bg.rect(bx - 1, ny + 2, bw + 2, 1, BAMBOO)


def leaf(c, x, y, dx, dy, col):
    c.path("M %d,%d Q %d,%d %d,%d Q %d,%d %d,%d Z" %
           (x, y, x + dx // 2, y + dy // 2 - 6, x + dx, y + dy,
            x + dx // 2, y + dy // 2 + 6, x, y), col)


for lx, ly, dx, dy in [(226, 40, -36, 14), (226, 58, -40, 24), (232, 32, 14, -14),
                       (244, 76, -34, 16), (244, 96, -38, 26), (248, 70, 6, -16),
                       (226, 88, -28, 26), (232, 116, -36, 12), (244, 128, -32, 20),
                       (226, 150, -26, 16), (244, 160, -30, 10)]:
    leaf(bg, lx, ly, dx, dy, BAMBOO)

# ground shadow under figure
bg.ellipse(126, 236, 50, 6, "#171d26")
bg.ellipse(126, 236, 34, 4, "#12171f")
bg.ellipse(68, 242, 12, 3, "#171d26")

# =========================================================
#                    CHARACTER
# =========================================================

# ---- hair streaming behind (wind to the right), separate locks ----
ch.path("M 132,58 C 148,58 158,68 160,82 C 161,94 156,102 148,102 "
        "C 140,100 134,86 130,70 Z", HAIR)
ch.path("M 134,62 C 154,64 176,74 190,88 C 197,95 201,103 199,108 "
        "C 191,110 181,101 172,93 C 159,82 146,74 134,71 Z", HAIR)
ch.path("M 138,76 C 154,84 168,96 177,110 C 182,118 184,126 181,130 "
        "C 175,129 168,121 162,113 C 153,101 144,88 138,83 Z", HAIR)
ch.path("M 142,90 C 152,100 160,112 164,124 C 166,131 166,137 163,138 "
        "C 159,135 155,128 151,120 C 146,110 142,98 141,94 Z", HAIR)
ch.path("M 146,66 C 162,70 176,78 186,87 L 183,89 C 172,80 159,72 146,70 Z", HAIR_HL)
ch.path("M 136,62 C 142,62 148,66 152,72 L 149,74 C 145,68 140,65 136,65 Z", HAIR_L)
# long hair down the back
ch.path("M 144,78 C 157,104 164,138 164,170 C 164,186 158,196 151,192 "
        "C 158,166 155,126 140,98 Z", HAIR)
ch.path("M 149,88 C 158,110 161,140 161,166 C 161,178 158,186 156,186 "
        "C 159,162 156,126 146,100 Z", HAIR_L)

# ---- far arm / sleeve streaming right ----
ch.path("M 144,108 C 156,114 166,128 173,144 C 178,155 180,164 177,169 "
        "C 170,173 162,165 155,154 C 147,141 142,126 140,114 Z", ROBE)
ch.path("M 147,114 C 157,121 165,133 171,147 C 175,156 177,163 175,166 "
        "C 171,161 165,149 158,138 C 151,128 146,119 145,114 Z", ROBE_L)
ch.path("M 152,121 C 160,131 167,142 172,153 C 174,157 175,161 174,163 "
        "C 170,156 164,145 157,135 C 154,129 151,124 150,122 Z", ROBE_LL)

# ---- legs + boots ----
ch.path("M 104,188 L 122,188 L 122,212 L 104,212 Z", ROBE_DD)
ch.path("M 134,186 L 152,186 L 152,210 L 134,210 Z", ROBE_DD)
ch.path("M 100,202 L 122,202 L 124,218 L 127,232 L 92,232 L 92,226 L 97,212 Z", BOOT)
ch.path("M 100,204 L 118,204 L 120,218 L 121,227 L 100,227 Z", BOOT_L)
ch.path("M 132,200 L 152,200 L 154,216 L 158,230 L 128,230 L 128,222 Z", BOOT)
ch.path("M 134,202 L 148,202 L 150,216 L 151,225 L 134,225 Z", BOOT_L)
ch.rect(90, 230, 38, 2, INK)
ch.rect(127, 228, 32, 2, INK)

# ---- skirt ----
ch.path("M 101,144 L 153,144 C 157,162 162,178 169,192 L 179,189 L 174,200 "
        "C 156,207 124,209 103,203 L 96,196 C 96,176 98,160 101,144 Z", ROBE)
ch.path("M 101,144 L 115,144 C 111,164 108,182 106,203 C 101,202 98,199 96,196 "
        "C 96,176 98,160 101,144 Z", ROBE_L)
ch.path("M 137,144 L 153,144 C 157,162 162,178 169,192 L 179,189 L 174,200 "
        "C 167,203 158,205 149,206 C 147,184 142,162 137,144 Z", ROBE_D)
for fx in [112, 121, 130, 140]:
    ch.line(fx, 156, fx + 3, 202, ROBE_D)
ch.line(104, 158, 100, 200, ROBE_LL)
ch.line(160, 164, 167, 194, ROBE_DD)
# hem trim (partial, front)
ch.path("M 96,196 C 104,203 124,208 148,205 L 148,202 C 124,205 106,201 98,194 Z", TRIM)
ch.path("M 98,194 C 106,201 124,204 146,202 L 146,200 C 124,202 107,199 99,192 Z", TRIM_L)
# wind flutter tip
ch.path("M 169,192 L 179,189 L 174,200 L 168,198 Z", ROBE_L)

# ---- torso ----
ch.path("M 126,94 C 113,94 103,100 99,110 C 96,124 96,136 99,148 L 155,148 "
        "C 159,134 159,120 154,108 C 149,98 137,94 128,94 Z", ROBE)
ch.path("M 126,94 C 113,94 103,100 99,110 C 97,122 96,132 98,144 L 111,144 "
        "C 107,128 109,108 117,96 Z", ROBE_L)
ch.path("M 145,96 C 151,100 155,106 156,114 C 159,126 159,138 156,148 "
        "L 145,148 C 149,132 149,112 145,96 Z", ROBE_D)
ch.line(105, 116, 112, 140, ROBE_D)
ch.line(149, 118, 146, 142, ROBE_DD)

# ---- collar (crossed) ----
ch.path("M 118,94 L 140,94 L 130,144 L 121,144 Z", INNER)
ch.path("M 129,94 L 140,94 L 130,144 L 126,144 Z", INNER_D)
ch.path("M 135,93 L 146,98 L 133,146 L 125,144 Z", ROBE_L)
ch.path("M 110,98 L 121,93 L 130,144 L 119,148 Z", ROBE)
ch.path("M 119,93 L 123,93 L 132,144 L 128,145 Z", TRIM)
ch.path("M 138,94 L 142,96 L 130,145 L 126,144 Z", TRIM)

# ---- sash ----
ch.path("M 99,140 L 155,138 L 157,152 L 101,154 Z", SASH)
ch.path("M 99,140 L 155,138 L 155,142 L 99,144 Z", SASH_L)
ch.path("M 101,148 L 157,146 L 157,152 L 101,154 Z", SASH_D)
ch.path("M 117,139 C 124,137 130,140 131,145 C 131,150 125,153 119,152 "
        "C 113,151 111,143 114,140 Z", SASH)
ch.path("M 119,141 C 124,140 128,142 128,145 C 128,148 124,150 120,149 "
        "C 116,148 116,143 119,141 Z", SASH_D)
ch.path("M 118,140 C 121,139 124,140 125,142 L 122,143 C 121,141 119,141 118,140 Z", SASH_H)
# thin sash tails streaming right
ch.path("M 132,146 C 150,149 168,155 181,163 L 188,169 L 185,171 "
        "C 170,161 150,153 131,150 Z", SASH)
ch.path("M 132,146 C 150,149 168,155 181,163 L 184,166 C 169,157 150,150 132,148 Z", SASH_L)
ch.path("M 181,163 L 188,169 L 185,171 L 184,167 Z", SASH_D)
ch.path("M 128,153 C 141,160 152,172 158,186 L 161,192 L 156,190 "
        "C 148,176 137,164 124,158 Z", SASH_D)
ch.path("M 128,153 C 139,159 149,169 155,181 L 152,181 C 144,169 134,160 125,155 Z", SASH)
# jade pendant
ch.line(142, 154, 148, 170, GOLD_D)
ch.circle(149, 174, 4, "#4d7a63")
ch.circle(148, 173, 2, "#6fa387")

# ---- front hair strands ----
ch.path("M 106,72 C 98,86 94,104 98,120 L 109,118 C 103,102 105,86 111,74 Z", HAIR)
ch.path("M 108,74 C 102,88 99,102 102,114 L 106,113 C 103,100 105,86 111,76 Z", HAIR_L)
ch.path("M 144,74 C 150,88 152,104 150,118 L 142,116 C 145,102 144,86 140,76 Z", HAIR)

# ---- neck + face ----
ch.path("M 118,88 L 142,88 L 144,110 L 116,110 Z", SKIN_DD)
ch.path("M 120,100 L 142,100 L 144,110 L 118,110 Z", SKIN_D)
# head
ch.path("M 113,62 L 146,62 C 148,78 145,92 138,99 C 130,106 119,104 114,97 "
        "C 108,90 107,76 110,62 Z", SKIN)
# nose (small)
ch.path("M 110,80 L 105,88 L 108,91 L 112,89 Z", SKIN)
ch.path("M 105,88 L 108,91 L 110,90 L 107,87 Z", SKIN_L)
ch.path("M 111,81 L 113,90 L 115,89 L 113,80 Z", SKIN_D)
# hat shadow over upper face
ch.path("M 107,62 L 148,62 L 148,82 C 139,87 118,87 106,83 Z", SKIN_DD)
ch.path("M 106,81 C 118,87 139,87 148,81 L 148,85 C 137,90 118,90 106,85 Z", SKIN_D)
# cheek / jaw
ch.path("M 114,89 C 122,93 132,92 138,87 C 138,93 133,99 127,100 "
        "C 120,101 116,96 114,89 Z", SKIN)
ch.path("M 116,90 C 123,94 130,93 134,90 C 133,95 128,98 123,98 "
        "C 119,98 117,94 116,90 Z", SKIN_L)
# mouth
ch.path("M 114,93 L 123,94 L 123,96 L 114,95 Z", "#6b4433")
ch.path("M 115,96 L 121,96 L 120,98 L 116,97 Z", SKIN_D)
# jaw shadow right
ch.path("M 138,85 C 144,87 146,91 144,95 C 141,99 136,102 132,102 "
        "C 137,98 139,92 138,85 Z", SKIN_D)
# ear hint
ch.path("M 141,80 C 146,80 147,86 144,89 C 141,90 139,86 141,80 Z", SKIN_D)

# ---- hat ----
ch.path("M 128,32 L 176,54 C 153,82 102,88 82,70 Z", HAT_M)
ch.path("M 128,32 L 82,70 C 93,80 104,85 114,87 C 118,66 122,48 128,32 Z", HAT_L)
ch.path("M 128,32 L 176,54 C 167,66 156,76 145,82 C 140,64 134,46 128,32 Z", HAT_D)
ch.path("M 128,32 L 145,82 C 139,85 132,87 125,88 C 127,68 127,48 128,32 Z", HAT_M)
for wx in [92, 105, 118, 131, 145, 159, 170]:
    ch.line(128, 33, wx, 80, HAT_DD)
ch.path("M 96,60 C 114,74 150,72 166,50", HAT_DD, fill=False)
ch.path("M 88,68 C 108,82 152,80 172,58", HAT_DD, fill=False)
ch.path("M 106,48 C 118,58 142,57 152,44", HAT_DD, fill=False)
ch.path("M 126,34 L 98,62 C 105,68 112,72 118,74 L 127,36 Z", HAT_L)
ch.path("M 124,36 L 108,56 C 112,60 116,63 119,65 L 126,38 Z", "#efd3a2")
ch.path("M 176,54 C 153,82 102,88 82,70 L 82,77 C 102,95 153,89 176,61 Z", HAT_RIM)
ch.path("M 82,70 C 96,82 114,86 128,86 L 128,92 C 110,92 92,86 82,77 Z", HAT_RIM)
ch.circle(128, 33, 3, HAT_DD)
ch.circle(128, 32, 2, HAT_D)
ch.path("M 100,86 C 104,98 111,106 120,109", HAT_DD, fill=False)
ch.path("M 152,80 C 149,94 143,102 136,107", HAT_DD, fill=False)

# ---- near arm: sleeve ----
ch.path("M 112,100 C 100,104 92,116 90,130 C 88,144 90,154 95,162 "
        "L 114,158 C 116,140 116,116 114,102 Z", ROBE)
ch.path("M 112,100 C 102,104 95,114 92,128 C 90,140 92,150 95,157 "
        "L 102,155 C 98,144 97,127 101,112 C 104,105 108,101 112,100 Z", ROBE_L)
ch.path("M 109,102 C 113,116 114,138 113,158 L 114,158 C 116,140 116,116 114,102 Z", ROBE_D)
ch.path("M 95,162 L 114,158 L 115,164 L 96,168 Z", ROBE_DD)
# hanging drape below elbow
ch.path("M 95,160 C 92,176 95,190 101,197 L 112,192 C 108,180 110,170 113,160 Z", ROBE_D)
ch.path("M 98,162 C 96,176 98,188 102,194 L 106,192 C 101,182 100,172 102,162 Z", ROBE)
ch.path("M 101,197 L 112,192 L 110,199 L 102,202 Z", ROBE_DD)

# ---- forearm + wrist ----
ch.path("M 104,144 L 108,158 L 80,156 L 78,142 Z", SKIN)
ch.path("M 104,144 L 106,150 L 80,148 L 78,142 Z", SKIN_L)
ch.path("M 106,153 L 108,158 L 80,156 L 80,152 Z", SKIN_D)
ch.path("M 84,140 L 98,142 L 96,162 L 82,160 Z", ROBE_DD)
ch.path("M 82,141 L 86,141 L 84,161 L 80,160 Z", TRIM)

# ---- SWORD ----
# pommel
ch.ellipse(68, 132, 7, 4, GOLD)
ch.ellipse(67, 131, 4, 2, GOLD_L)
# grip (mostly hidden by fist)
ch.rect(65, 134, 7, 32, GRIP)
ch.rect(65, 134, 2, 32, GRIP_L)
# collar under fist
ch.rect(64, 164, 9, 4, GOLD)
ch.rect(64, 164, 9, 1, GOLD_L)
# guard
ch.path("M 55,172 L 60,167 L 76,167 L 81,172 L 79,178 L 57,178 Z", GOLD)
ch.path("M 55,172 L 60,167 L 76,167 L 81,172 L 79,174 L 60,174 L 57,173 Z", GOLD_L)
ch.path("M 57,176 L 79,176 L 79,178 L 57,178 Z", GOLD_D)
ch.circle(68, 172, 2, GOLD_D)
# blade
ch.path("M 62,176 L 74,176 L 73,216 L 68,242 L 63,216 Z", BLADE)
ch.path("M 62,176 L 66,176 L 66,216 L 68,242 L 63,216 Z", BLADE_L)
ch.path("M 71,176 L 74,176 L 73,216 L 68,242 L 70,216 Z", BLADE_D)
ch.line(68, 178, 68, 236, BLADE_DD)
ch.line(64, 180, 64, 214, "#ffffff")

# ---- hand resting on grip ----
ch.path("M 61,142 C 57,145 56,154 59,159 C 62,163 71,164 75,161 "
        "C 79,158 79,146 75,143 C 70,139 64,139 61,142 Z", SKIN)
ch.path("M 61,142 C 58,145 57,150 58,154 C 62,152 68,151 74,152 "
        "C 77,149 77,144 75,143 C 70,139 64,139 61,142 Z", SKIN_L)
ch.path("M 59,157 C 63,162 71,163 75,160 C 77,158 78,156 78,154 "
        "C 75,159 66,160 59,155 Z", SKIN_D)
ch.line(57, 148, 77, 146, SKIN_D)
ch.line(57, 153, 77, 152, SKIN_D)
# thumb
ch.path("M 70,141 C 76,141 78,145 77,149 C 75,152 71,151 70,148 Z", SKIN_L)
ch.path("M 71,147 C 74,149 76,148 77,146", SKIN_D, fill=False)

# ================= outline =================
ch.outline(INK)

# ---- subtle moon-side accents ----
ch.path("M 61,142 C 58,145 57,150 58,154 L 61,153 C 60,149 61,145 64,143 Z", RIM)
ch.path("M 61,131 C 63,129 65,128 67,128 L 67,131 C 65,131 63,132 62,133 Z", RIM)

flat = flatten([bg, ch], name="result")
print(flat.stats_text())
view(flat)
save("east_hero", flat, indexed=True)
finish(flat)
