from pixelbench_api import new_canvas, finish

c = new_canvas(64, 32)

# palette
BODY    = "#e8eef2"  # main body
ROOF    = "#b7c4cc"
AC      = "#8fa0aa"
GLASS   = "#22303a"  # side windows
GLASS_L = "#64808f"  # window reflection
WINDS   = "#3d5a6b"  # windshield
WINDS_L = "#7fa6b8"
SIGN    = "#101418"  # route display background
SIGN_T  = "#ffb02e"  # route display text
DOOR    = "#d3dde2"  # door panels
SEAM    = "#9fb0b8"
STRIPE  = "#1e6fba"
SKIRT   = "#5a6a72"
SKIRT_D = "#46545c"
HL      = "#ffe9a0"  # headlight
TL      = "#e03030"  # taillight
ARCH   = "#0d0d0d"   # wheel well
TIRE   = "#1c1c1c"
RIM    = "#9aa3a8"
HUB    = "#4a4a4a"
BUMP   = "#2e3a42"   # bumper

# body shell
c.rect(3, 4, 58, 23, BODY)      # x3..60, y4..26
c.rect(3, 4, 58, 2, ROOF)       # roof band
c.rect(20, 3, 12, 2, AC)        # roof air-con unit

# side windows (row of windows y7..14)
for x in (16, 26, 36):
    c.rect(x, 7, 8, 8, GLASS)
    c.rect(x + 1, 8, 6, 1, GLASS_L)

# windshield (front, facing right)
c.rect(46, 7, 13, 7, WINDS)
c.line(48, 8, 57, 8, WINDS_L)

# electronic route display "23"
c.rect(46, 4, 13, 3, SIGN)
c.rect(47, 4, 2, 1, SIGN_T)
c.rect(48, 5, 1, 1, SIGN_T)
c.rect(47, 6, 2, 1, SIGN_T)
c.rect(50, 4, 2, 1, SIGN_T)
c.rect(50, 5, 1, 1, SIGN_T)
c.rect(51, 5, 1, 1, SIGN_T)
c.rect(50, 6, 2, 1, SIGN_T)

# beltline / doors
c.rect(3, 15, 58, 1, ROOF)
c.rect(6, 8, 7, 18, DOOR)       # rear door  x6..12
c.rect(6, 8, 7, 5, GLASS)      # rear door window
c.rect(13, 8, 1, 18, SEAM)
c.rect(52, 14, 7, 12, DOOR)    # front door x52..58
c.rect(51, 14, 1, 12, SEAM)
c.rect(53, 15, 4, 2, GLASS)   # front door window

# stripe and skirt
c.rect(3, 17, 58, 3, STRIPE)
c.rect(3, 20, 58, 7, SKIRT)
c.rect(3, 26, 58, 1, SKIRT_D)

# bumper, headlight, taillight
c.rect(60, 20, 2, 6, BUMP)
c.rect(57, 14, 3, 3, HL)
c.rect(3, 9, 2, 5, TL)

# wheels
for cx in (14, 49):
    c.circle(cx, 26, 5, ARCH)
    c.circle(cx, 26, 4, TIRE)
    c.circle(cx, 26, 2, RIM)
    c.circle(cx, 26, 1, HUB)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 31), indices=True))
finish(c)
