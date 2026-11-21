#
# 2x2 skill icon set, 64x64, four 32x32 icons, dark outline, transparent bg
#

OUT = "#191326"

# fire
F_D = "#c43a16"
F_M = "#f2792a"
F_L = "#ffc martian"
# (placeholder fixed below)
F_L = "#ffc23d"
F_W = "#fff2b0"

# ice
I_D = "#2b5fa8"
I_M = "#4f9ed8"
I_L = "#a6e2f7"
I_W = "#eafaff"

# heal
H_D = "#1d7a46"
H_M = "#3cbd68"
H_L = "#8ded9f"
H_W = "#e8ffee"

# lightning
L_D = "#b86f12"
L_M = "#f5ae28"
L_L = "#ffe24d"
L_W = "#fff8cf"


def icon_fire():
    c = new_canvas(32, 32, name="fire")
    # body of the fireball + rising tongue
    c.circle(16, 20, 9, F_D)
    c.path("M16,2 C18,8 21,9 22,14 L10,14 C11,9 14,8 16,2 Z", F_D)
    c.path("M22,8 C24,11 25,13 25,16 L20,16 Z", F_D)
    c.path("M10,8 C8,11 7,13 7,16 L12,16 Z", F_D)
    # mid tone
    c.circle(16, 21, 6, F_M)
    c.path("M16,7 C17,11 19,13 19,16 L13,16 C13,13 15,11 16,7 Z", F_M)
    # light core
    c.circle(16, 22, 4, F_L)
    c.path("M16,12 C17,14 17,16 17,17 L15,17 C15,16 15,14 16,12 Z", F_L)
    # hot centre
    c.circle(16, 22, 2, F_W)
    c.outline(OUT)
    return c


def icon_ice():
    c = new_canvas(32, 32, name="ice")
    shield = "M16,2 L28,6 C28,18 24,27 16,31 C8,27 4,18 4,6 Z"
    c.path(shield, I_D)
    c.path("M16,5 L25,8 C25,18 22,25 16,28 C10,25 7,18 7,8 Z", I_M)
    # left-side lighter facet
    c.path("M16,5 L16,28 C10,25 7,18 7,8 Z", I_L)
    # snowflake
    # snowflake: vertical + two mirrored diagonals, symmetric about (16,16)
    c.line(16, 9, 16, 23, I_W)
    c.line(10, 12, 22, 20, I_W)
    c.line(10, 20, 22, 12, I_W)
    # arm branches
    c.line(16, 12, 13, 10, I_W)
    c.line(16, 12, 19, 10, I_W)
    c.line(16, 20, 13, 22, I_W)
    c.line(16, 20, 19, 22, I_W)
    c.set(13, 14, I_W)
    c.set(19, 18, I_W)
    c.set(13, 18, I_W)
    c.set(19, 14, I_W)
    c.circle(16, 16, 1, I_W)
    c.outline(OUT)
    return c


def icon_heal():
    c = new_canvas(32, 32, name="heal")
    # cross
    c.rect(12, 4, 8, 24, H_D)
    c.rect(4, 12, 24, 8, H_D)
    c.rect(13, 5, 6, 22, H_M)
    c.rect(5, 13, 22, 6, H_M)
    # 2px bevel along the top/left edges of every arm
    c.rect(13, 5, 6, 2, H_L)
    c.rect(13, 5, 2, 8, H_L)
    c.rect(13, 19, 2, 8, H_L)
    c.rect(5, 13, 2, 6, H_L)
    c.rect(5, 13, 8, 2, H_L)
    c.rect(19, 13, 8, 2, H_L)
    # 1px shadow along the bottom/right edges
    c.rect(13, 26, 6, 1, H_D)
    c.rect(18, 5, 1, 8, H_D)
    c.rect(18, 19, 1, 8, H_D)
    c.rect(26, 13, 1, 6, H_D)
    c.rect(5, 18, 8, 1, H_D)
    c.rect(19, 18, 8, 1, H_D)
    # specular
    c.rect(13, 5, 2, 4, H_W)
    c.rect(5, 13, 4, 2, H_W)
    # sparkles
    for (sx, sy) in ((7, 7), (25, 24)):
        c.set(sx, sy, H_W)
        c.set(sx - 1, sy, H_L)
        c.set(sx + 1, sy, H_L)
        c.set(sx, sy - 1, H_L)
        c.set(sx, sy + 1, H_L)
    c.outline(OUT)
    return c


DX = -1
BOLT = [(16, 3), (26, 3), (18, 13), (25, 13), (12, 29), (15, 17), (9, 17)]
BOLT_IN = [(17, 6), (24, 6), (18, 14), (23, 14), (13, 26), (16, 17), (11, 17)]
BOLT = [(x + DX, y) for (x, y) in BOLT]
BOLT_IN = [(x + DX, y) for (x, y) in BOLT_IN]


def icon_bolt():
    c = new_canvas(32, 32, name="bolt")
    c.poly(BOLT, L_D)
    c.poly(BOLT_IN, L_M)
    d = DX
    c.line(18 + d, 7, 17 + d, 13, L_L)
    c.line(19 + d, 7, 18 + d, 13, L_L)
    c.line(14 + d, 18, 13 + d, 24, L_L)
    c.line(15 + d, 18, 14 + d, 24, L_L)
    c.line(18 + d, 7, 17 + d, 11, L_W)
    c.line(14 + d, 18, 13 + d, 22, L_W)
    c.outline(OUT)
    return c


result = new_canvas(64, 64, name="skill_icons")
result.blit(icon_fire(), 0, 0)
result.blit(icon_ice(), 32, 0)
result.blit(icon_heal(), 0, 32)
result.blit(icon_bolt(), 32, 32)

print(result.stats_text())
view(result)
save("skill_icons", result)
finish(result)
