import math

W = H = 256

# ---------------------------------------------------------------- palette
SKY_T = "#e4ebf1"
SKY_M = "#cfdae5"
SKY_B = "#b7c6d6"
MIST1 = "#dde6ee"
MIST2 = "#f1f6fa"
MTN_F = "#8d9cb0"
MTN_M = "#6a7b92"
MTN_N = "#44536c"
MTN_D = "#30405a"
GND   = "#3d4c62"
GND2  = "#2e3b4e"
GND3  = "#232e3e"

bg = new_canvas(W, H, name="bg")

# ---------------------------------------------------------------- sky
bands = [(0, 44, SKY_T), (44, 84, SKY_T), (84, 120, SKY_M), (120, 150, SKY_B)]
bg.rect(0, 0, W, 90, SKY_T)
bg.rect(0, 90, W, 32, SKY_M)
bg.rect(0, 122, W, 34, SKY_B)
bg.dither(0, 84, W, 8, [SKY_T, SKY_M], pattern="bayer4")
bg.dither(0, 118, W, 8, [SKY_M, SKY_B], pattern="bayer4")

# ---------------------------------------------------------------- far range
bg.path("M 0 114 L 30 70 L 48 88 L 64 62 L 88 98 L 112 76 L 134 102 L 152 84"
        " L 178 108 L 202 78 L 226 102 L 255 86 L 255 150 L 0 150 Z", MTN_F)
for px, py in ((64, 62), (30, 70), (202, 78)):
    bg.path("M %d %d L %d %d L %d %d L %d %d Z" % (px, py, px + 9, py + 12,
                                                   px, py + 15, px - 9, py + 12), MIST2)
    bg.path("M %d %d L %d %d L %d %d Z" % (px, py + 2, px + 7, py + 12, px + 2, py + 13), MIST1)

# mist veil over the base of the far range
bg.dither(0, 100, W, 6, [MIST1, MTN_F], pattern="bayer4")
bg.rect(0, 106, W, 5, MIST1)
bg.rect(0, 108, W, 2, MIST2)

# ---------------------------------------------------------------- mid range
bg.path("M 0 150 L 0 124 L 24 98 L 46 120 L 72 96 L 98 126 L 122 106 L 150 130"
        " L 174 104 L 202 128 L 230 110 L 255 132 L 255 150 Z", MTN_M)
bg.dither(0, 126, W, 6, [MIST1, MTN_M], pattern="bayer4")
bg.rect(0, 132, W, 4, MIST1)
bg.rect(0, 133, W, 2, MIST2)

# ---------------------------------------------------------------- near range
bg.path("M 0 172 L 0 146 L 28 120 L 56 148 L 80 130 L 106 156 L 255 156 L 255 172 Z", MTN_N)
bg.path("M 255 172 L 255 134 L 232 116 L 208 142 L 184 126 L 158 154 L 118 152 L 98 172 Z", MTN_N)
bg.path("M 28 120 L 40 134 L 30 140 L 20 132 Z", MTN_D)
bg.path("M 232 116 L 244 130 L 234 136 L 224 128 Z", MTN_D)
bg.dither(0, 150, W, 8, [MIST1, MTN_N], pattern="bayer4")
bg.rect(0, 157, W, 3, MIST1)

# distant pines in the mist
for bx, by, bh, col in ((16, 152, 40, MTN_D), (40, 150, 28, MTN_N), (236, 154, 36, MTN_D),
                        (214, 151, 26, MTN_N)):
    bg.line(bx, by, bx, by - bh, col)
    for k in range(4):
        yy = by - bh + 5 + k * (bh // 5)
        s = 3 + k * 2
        bg.line(bx, yy, bx - s, yy + 4, col)
        bg.line(bx, yy, bx + s, yy + 4, col)

# ---------------------------------------------------------------- ground
bg.rect(0, 160, W, H - 160, GND)
bg.dither(0, 160, W, 7, [MIST1, GND], pattern="bayer4")
bg.rect(0, 196, W, H - 196, GND2)
bg.dither(0, 190, W, 8, [GND, GND2], pattern="bayer4")
bg.rect(0, 232, W, H - 232, GND3)
bg.dither(0, 226, W, 8, [GND2, GND3], pattern="bayer4")

# ---------------------------------------------------------------- figure
import figure

fig = figure.build(W, H)
fig.outline(figure.OUT)

# ground shadow beneath the figure
bg.ellipse(118, 236, 46, 6, "#1d2634")
bg.ellipse(118, 236, 34, 4, "#172030")

base = flatten([bg, fig], name="base")

# low drifting mist on its own layer so the alpha composites instead of replacing
mist = new_canvas(W, H, name="mist")
MISTF = "#b9c8d84d"
MISTG = "#cdd9e438"
mist.path("M 0 230 C 30 222 70 232 104 226 C 140 220 180 232 255 224 "
          "L 255 238 C 200 243 150 235 100 239 C 56 243 20 238 0 241 Z", MISTG)
mist.path("M 0 246 C 40 238 90 248 140 244 C 190 240 230 248 255 244 "
          "L 255 255 L 0 255 Z", MISTF)
mist.path("M 14 212 C 44 206 74 214 104 210 L 104 217 C 74 221 44 215 14 219 Z", MISTG)
mist.path("M 150 204 C 180 198 215 206 250 202 L 250 209 C 215 213 180 207 150 211 Z",
          MISTG)
result = flatten([base, mist], name="result")

# a few windblown leaves for motion
for (lx, ly) in ((44, 96), (58, 118), (198, 86), (212, 112), (76, 70), (226, 148),
                 (36, 160), (190, 60)):
    result.set(lx, ly, "#6f4a3a")
    result.set(lx + 1, ly + 1, "#8a5c42")
    result.set(lx + 1, ly, "#5a3a2e")
print(result.stats_text())
view(result)
save("east-hero-full-body", result, indexed=True)
finish(result)
