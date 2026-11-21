import numpy as np

W = H = 256

# ---------------- palette ----------------
SKY = ["#2c3850", "#41506b", "#5a6a84", "#7c8ba0", "#9dabb9", "#bcc7d1"]
MOON = "#e9e3cf"; MOON_L = "#f5f1e3"; MOON_D = "#d9d2ba"
CLOUD = "#c9d2da"
BIRD = "#3d4c66"
MT_FAR = "#8797a9"; MT_MID = "#687a90"; MT_NEAR = "#485a72"
GROUND = "#28334a"; ROCK = "#3a4759"; ROCK_D = "#1f2940"
PINE = "#2c3b4d"
MIST_B = "#aebbc7"; MIST_C = "#c6d0d8"
OUT = "#14101c"

ROBE = "#252231"; ROBE_D = "#191624"; ROBE_L = "#3a3549"; ROBE_H = "#4e4863"
INNER = "#6e6880"; COLLAR = "#aaa3b6"
SASH = "#8e2f3a"; SASH_D = "#671f2a"; SASH_L = "#b04a52"
SKIN = "#e6bf97"; SKIN_D = "#c39a72"; SKIN_S = "#a37a58"; SKIN_H = "#f2d2ab"
MOUTH = "#8a5548"
HAIR = "#1b1724"; HAIR_L = "#37304a"
HAT = "#c3a86b"; HAT_L = "#dcc48a"; HAT_D = "#7c6539"; HAT_RIB = "#8d7442"
BLADE = "#dfe7ee"; BLADE_L = "#f8fbfe"; BLADE_D = "#8b98a6"
BRASS = "#8f7a4d"; BRASS_L = "#b39a63"
GRIP = "#3a2c22"; GRIP_L = "#5a4430"
SHOE = "#2b2537"; SHOE_D = "#151220"

bg = new_canvas(W, H, name="bg")
char = new_canvas(W, H, name="char")
fx = new_canvas(W, H, name="fx")


def pine(c, cx, base, h, col):
    w = h * 0.8
    c.poly([(cx, base - h), (cx - w * 0.45, base - h * 0.45), (cx + w * 0.45, base - h * 0.45)], col)
    c.poly([(cx, base - h * 0.70), (cx - w * 0.72, base - h * 0.10), (cx + w * 0.72, base - h * 0.10)], col)
    c.rect(cx - 1, base - 2, 3, 5, col)


# ================= BACKGROUND =================
ys = [0, 46, 86, 126, 166, 210, 256]
for i in range(6):
    bg.rect(0, ys[i], W, ys[i + 1] - ys[i], SKY[i])
for i in range(5):
    bg.dither(0, ys[i + 1] - 3, W, 6, [SKY[i], SKY[i + 1]], "checker")

# moon
bg.circle(198, 46, 22, MOON)
bg.circle(192, 40, 14, MOON_L)
bg.circle(206, 55, 3, MOON_D)
bg.circle(189, 52, 2, MOON_D)
bg.circle(201, 34, 2, MOON_D)
bg.rect(176, 41, 44, 3, CLOUD)
bg.dither(176, 38, 44, 3, [SKY[0], CLOUD], "checker")
bg.dither(176, 44, 44, 3, [CLOUD, SKY[0]], "checker")
bg.rect(182, 54, 38, 2, CLOUD)

# birds
for bx, by, s in [(56, 50, 4), (78, 62, 3), (150, 32, 3)]:
    bg.line(bx - s, by - 2, bx, by, BIRD)
    bg.line(bx, by, bx + s, by - 2, BIRD)

# mountain ridges
bg.poly([(0, 132), (24, 118), (44, 126), (66, 108), (88, 122), (110, 104), (134, 118),
         (156, 100), (180, 116), (204, 106), (228, 120), (256, 112), (256, 212), (0, 212)], MT_FAR)
bg.poly([(0, 168), (30, 150), (58, 164), (86, 144), (114, 160), (146, 140), (176, 158),
         (206, 146), (232, 160), (256, 150), (256, 234), (0, 234)], MT_MID)
bg.poly([(0, 208), (36, 190), (70, 204), (104, 186), (140, 202), (176, 188), (210, 204),
         (240, 192), (256, 200), (256, 256), (0, 256)], MT_NEAR)

# mist behind the figure
bg.ellipse(128, 150, 122, 16, MIST_B)
bg.ellipse(126, 118, 86, 22, MIST_B)
bg.ellipse(52, 190, 82, 12, MIST_C)
bg.ellipse(208, 172, 62, 10, MIST_C)
bg.ellipse(128, 226, 132, 16, MIST_C)

# pines
for px, pb, ph in [(20, 202, 18), (38, 196, 14), (54, 205, 16), (98, 192, 12),
                   (168, 194, 12), (204, 209, 18), (222, 200, 14), (240, 209, 16)]:
    pine(bg, px, pb, ph, PINE)

# ground + rocks + shadow
bg.rect(0, 238, W, 18, GROUND)
bg.ellipse(40, 244, 34, 8, ROCK)
bg.ellipse(212, 246, 40, 9, ROCK)
bg.ellipse(120, 251, 62, 10, ROCK_D)
bg.ellipse(130, 246, 56, 7, ROCK_D)

# ================= CHARACTER =================
# ---- hair (behind head, over shoulders) ----
char.path("M 136 48 C 158 52 172 68 178 90 C 184 112 182 134 172 152 "
          "C 167 159 160 160 158 152 C 165 132 167 110 161 92 C 155 74 147 60 136 48 Z", HAIR)
char.path("M 174 92 C 186 98 194 108 198 120 L 194 122 C 189 111 181 102 172 96 Z", HAIR)
char.path("M 176 118 C 186 124 192 134 194 144 L 190 145 C 187 136 181 127 173 121 Z", HAIR)
char.path("M 103 54 C 96 62 93 76 95 90 C 96 99 101 104 106 101 C 101 88 101 70 107 58 Z", HAIR)

# ---- neck ----
char.poly([(115, 74), (129, 74), (130, 96), (114, 96)], SKIN)
char.rect(114, 88, 16, 4, SKIN_D)

# ---- face (lower half visible under the brim) ----
char.path("M 102 48 L 140 46 C 143 60 140 74 130 83 C 122 89 110 88 104 80 "
          "C 99 72 99 58 102 48 Z", SKIN)
char.path("M 100 62 C 113 70 129 68 140 58 L 140 64 C 128 72 112 73 100 68 Z", SKIN_S)
char.poly([(101, 66), (108, 68), (104, 76)], SKIN_D)
char.ellipse(126, 74, 3, 4, SKIN_H)
char.line(109, 79, 121, 78, MOUTH)
char.line(109, 80, 121, 79, MOUTH)
char.line(112, 83, 120, 83, SKIN_D)
char.path("M 138 60 C 140 70 136 78 130 83", SKIN_D)

# ---- shoes (behind hem) ----
char.poly([(96, 230), (117, 227), (121, 239), (113, 244), (94, 241)], SHOE)
char.poly([(143, 231), (163, 229), (166, 241), (158, 246), (141, 242)], SHOE)
char.line(95, 241, 120, 239, SHOE_D)
char.line(142, 242, 165, 241, SHOE_D)

# ---- robe body ----
char.path("M 94 94 "
          "C 90 110 90 126 95 142 "
          "C 84 170 78 200 82 224 "
          "L 86 228 "
          "L 100 216 L 114 228 L 128 215 L 142 227 L 158 214 L 172 226 L 186 212 "
          "C 190 204 192 194 191 184 "
          "C 190 170 182 156 173 142 "
          "C 178 124 178 106 170 92 "
          "C 152 86 114 86 94 94 Z", ROBE)

# skirt folds
char.path("M 112 152 C 108 182 106 206 108 224", ROBE_D)
char.path("M 132 150 C 130 182 132 206 134 226", ROBE_D)
char.path("M 154 152 C 158 180 162 202 164 220", ROBE_D)
char.path("M 122 152 C 120 182 121 206 122 226", ROBE_L)
char.path("M 144 152 C 147 180 150 202 152 222", ROBE_L)
char.path("M 170 96 C 177 110 177 126 173 141", ROBE_H)
char.path("M 100 100 C 95 114 94 128 97 140", ROBE_D)

# ---- sash ----
char.path("M 96 138 C 120 133 148 131 170 134 L 172 150 C 148 147 120 149 98 154 Z", SASH)
char.path("M 98 149 C 120 144 148 142 172 145 L 172 150 C 148 147 120 149 98 154 Z", SASH_D)
char.ellipse(106, 148, 6, 5, SASH_D)
char.ellipse(104, 146, 3, 2, SASH_L)
char.path("M 102 154 C 98 172 102 190 94 208 L 101 211 C 109 192 106 172 110 156 Z", SASH)
char.path("M 112 155 C 117 172 113 188 122 204 L 128 201 C 120 186 124 170 119 155 Z", SASH_D)

# ---- collar ----
char.poly([(106, 92), (152, 88), (128, 126)], INNER)
char.poly([(102, 92), (109, 89), (132, 124), (125, 128)], COLLAR)
char.poly([(155, 86), (160, 91), (131, 126), (125, 121)], COLLAR)
char.path("M 128 126 C 126 133 123 138 119 142", ROBE_D)

# ---- sword arm sleeve (viewer left) ----
char.path("M 102 92 "
          "C 92 96 82 108 78 124 "
          "C 75 138 78 150 87 157 "
          "L 97 150 "
          "C 94 134 98 116 107 104 Z", ROBE)
char.path("M 88 112 C 84 124 84 138 88 150", ROBE_D)
char.path("M 97 108 C 93 122 93 138 96 150", ROBE_L)

# ---- jian sword ----
char.poly([(76, 182), (85, 182), (77, 242), (74, 246), (71, 242)], BLADE)
char.line(83, 184, 76, 240, BLADE_L)
char.line(72, 186, 75, 238, BLADE_D)
char.poly([(88, 180), (90, 185), (70, 183), (69, 178)], BRASS)
char.line(71, 180, 89, 182, BRASS_L)
char.poly([(79, 163), (86, 164), (84, 181), (77, 180)], GRIP)
for gy in (167, 171, 175, 179):
    char.line(78, gy, 85, gy + 1, GRIP_L)
char.ellipse(83, 160, 5, 5, BRASS)
char.circle(82, 159, 2, BRASS_L)
# tassel
char.path("M 87 157 C 94 161 98 169 99 179 L 95 180 C 94 171 91 165 86 161 Z", SASH_L)
char.poly([(93, 179), (101, 180), (100, 195), (96, 198), (92, 193)], SASH_L)
char.line(95, 181, 95, 195, SASH_D)
char.line(98, 181, 98, 194, SASH_D)

# ---- hand resting on the pommel ----
char.ellipse(84, 155, 8, 7, SKIN)
char.line(77, 152, 91, 153, SKIN_D)
char.line(77, 156, 91, 157, SKIN_D)
char.line(78, 160, 90, 161, SKIN_D)
char.ellipse(76, 151, 3, 2, SKIN)

# ---- free arm sleeve (billowing right) ----
char.path("M 158 92 "
          "C 172 96 184 110 190 128 "
          "C 194 144 192 158 184 165 "
          "C 177 169 170 164 168 155 "
          "C 165 136 161 116 156 102 Z", ROBE)
char.path("M 172 108 C 180 120 184 134 184 148", ROBE_D)
char.path("M 164 106 C 170 118 173 132 173 146", ROBE_L)
char.path("M 186 116 C 191 130 191 146 186 158", ROBE_H)
char.poly([(168, 152), (179, 153), (182, 165), (176, 170), (168, 162)], SKIN)
char.line(170, 158, 180, 159, SKIN_D)
char.line(170, 162, 179, 163, SKIN_D)

# ---- hat (douli) ----
char.path("M 116 12 C 100 20 84 40 74 62 C 98 70 140 66 168 50 C 152 32 134 16 116 12 Z", HAT)
for tx, ty in [(88, 63), (102, 64), (116, 63), (132, 60), (150, 55)]:
    char.line(116, 14, tx, ty, HAT_RIB)
    char.line(117, 14, tx + 1, ty, HAT_RIB)
char.path("M 74 62 C 98 70 140 66 168 50 L 166 45 C 140 60 100 64 76 57 Z", HAT_D)
char.path("M 116 12 C 134 18 152 34 166 48 C 160 51 154 53 148 54 C 138 38 128 22 118 15 Z", HAT_L)
char.circle(116, 11, 3, HAT_D)
char.path("M 120 14 C 136 20 151 34 164 47", HAT_L)

# hair rim light
char.path("M 176 88 C 181 108 180 130 172 148", HAIR_L)

# ---- dark outline around the whole figure ----
char.outline(OUT)

# ================= FOREGROUND MIST / PETALS =================
MISTF = "#cdd6dd"
fx.rect(0, 236, W, 20, MISTF + "5e")
fx.ellipse(128, 244, 84, 10, MISTF + "80")
fx.ellipse(34, 200, 36, 6, MISTF + "64")
fx.ellipse(202, 202, 44, 7, MISTF + "64")
fx.ellipse(120, 172, 52, 6, MISTF + "50")
fx.ellipse(48, 234, 38, 7, MISTF + "7a")
fx.ellipse(200, 238, 44, 8, MISTF + "7a")
for px, py in [(52, 86), (214, 120), (86, 176), (228, 72), (36, 150), (180, 60), (150, 108)]:
    fx.poly([(px, py - 2), (px + 2, py), (px, py + 2), (px - 2, py)], SASH_L)

result = flatten([bg, char, fx], name="result")


# ---------------- inspection helpers ----------------
def ascii_map(c, step=4, x0=0, y0=0, x1=None, y1=None, label=""):
    w, h, rgba = c.to_rgba()
    a = np.frombuffer(rgba, dtype=np.uint8).reshape(h, w, 4).astype(int)
    x1 = w if x1 is None else x1
    y1 = h if y1 is None else y1
    print(f"--- {label} ({x0},{y0})-({x1},{y1}) step={step} ---")
    print("    " + "".join((str((x // 10) % 10) if x % 10 == 0 else ("+" if x % 5 == 0 else " "))
                            for x in range(x0, x1, step)))
    for y in range(y0, y1, step):
        row = ""
        for x in range(x0, x1, step):
            r, g, b, al = a[y, x]
            if al < 40:
                row += " "
                continue
            lum = (r * 299 + g * 587 + b * 114) // 1000
            if r > 160 and g > 130 and b < 130 and (r - b) > 40:
                ch = "Y"
            elif r > 110 and g < 90 and b < 90:
                ch = "R"
            elif r > 190 and g > 150 and b > 130:
                ch = "S"
            elif lum > 200:
                ch = "#"
            elif lum > 140:
                ch = "+"
            elif lum > 95:
                ch = "="
            elif lum > 55:
                ch = "-"
            elif lum > 28:
                ch = "@"
            else:
                ch = "%"
            row += ch
        print(f"{y:3d} {row}")


print(result.stats_text())
ascii_map(result, 4, 0, 0, 256, 256, "full")
print("### HEM / SHOES ###")
print(result.matrix_text(region=(80, 214, 176, 250)))

finish(result)
