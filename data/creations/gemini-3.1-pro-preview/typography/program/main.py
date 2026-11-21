import pixelbench_api as api
import random

c = api.new_canvas(64, 64)

# Sky gradient
c.rect(0, 0, 64, 16, "#0d081b")
c.rect(0, 16, 64, 16, "#1a1235")
c.rect(0, 32, 64, 16, "#291d4f")
c.rect(0, 48, 64, 16, "#3b286d")

c.dither(0, 14, 64, 4, ["#0d081b", "#1a1235"])
c.dither(0, 30, 64, 4, ["#1a1235", "#291d4f"])
c.dither(0, 46, 64, 4, ["#291d4f", "#3b286d"])

# Stars
random.seed(42)
for _ in range(30):
    sx = random.randint(0, 63)
    sy = random.randint(0, 55)
    c.set(sx, sy, random.choice(["#5d4099", "#8b6bc4", "#ffffff"]))

# Sword shadow
ss = api.new_canvas(64, 64)
ss.rect(13, 36, 48, 3, "#000000") # blade
ss.rect(11, 34, 2, 7, "#000000") # crossguard
ss.rect(6, 36, 5, 3, "#000000") # grip
ss.rect(4, 35, 2, 5, "#000000") # pommel
ss.outline("#000000")
c.blit(ss, 0, 2)

# Sword
sword = api.new_canvas(64, 64)
sword.line(13, 36, 58, 36, "#b4b4b4")
sword.line(13, 37, 58, 37, "#ffffff")
sword.line(13, 38, 58, 38, "#7a7a7a")
sword.set(59, 36, "#b4b4b4")
sword.set(59, 37, "#ffffff")
sword.set(60, 37, "#ffffff")
sword.rect(12, 34, 1, 7, "#f6d741")
sword.rect(11, 34, 1, 7, "#c25e00")
sword.rect(6, 36, 5, 3, "#543012")
sword.rect(4, 35, 2, 5, "#f6d741")
sword.outline("#111111")
c.blit(sword, 0, 0)

pixel_art = [
    "PPPPPP  IIIIII XX    XX EEEEEE LLL   ",
    "PPPPPPP IIIIII  XX  XX  EEEEEE LLL   ",
    "PP   PP   II     XXXX   EE     LLL   ",
    "PPPPPPP   II      XX    EEEE   LLL   ",
    "PPPPPP    II      XX    EEEE   LLL   ",
    "PP        II     XXXX   EE     LLL   ",
    "PP      IIIIII  XX  XX  EEEEEE LLLLLL",
    "PP      IIIIII XX    XX EEEEEE LLLLLL"
]

quest_art = [
    " QQQQ  UU  UU EEEEEE  SSSS  TTTTTT",
    "QQ  QQ UU  UU EEEEEE SSSSSS TTTTTT",
    "QQ  QQ UU  UU EE     SS       TT  ",
    "QQ  QQ UU  UU EEEEE   SSSS    TT  ",
    "QQ  QQ UU  UU EEEEE    SSSS   TT  ",
    "QQ  QQ UU  UU EE         SS   TT  ",
    "QQ  QQ UUUUUU EEEEEE SSSSSS   TT  ",
    " QQQQQ  UUUU  EEEEEE  SSSS    TT  ",
    "    QQ                            "
]

def render_text(art, x, y, c_top, c_mid, c_bot, out_col, shadow_col, shadow_dy):
    t = api.new_canvas(64, 64)
    s = api.new_canvas(64, 64)
    
    for dy, row in enumerate(art):
        for dx, char in enumerate(row):
            if char != ' ':
                if dy < 3:
                    col = c_top
                elif dy < 6:
                    col = c_mid
                else:
                    col = c_bot
                t.set(x + dx, y + dy, col)
                s.set(x + dx, y + dy, shadow_col)
                
    t.outline(out_col)
    s.outline(shadow_col)
    
    c.blit(s, 0, shadow_dy)
    c.blit(t, 0, 0)

render_text(pixel_art, 13, 14, "#ffffff", "#41a6f6", "#29366f", "#111111", "#000000", 2)
render_text(quest_art, 15, 32, "#ffffff", "#f6d741", "#c25e00", "#111111", "#000000", 2)

# Crown on 'P'
crown_x, crown_y = 14, 10
crown = [
    "X X X",
    "XXXXX",
    "XXXXX"
]
cr_canvas = api.new_canvas(64, 64)
cr_shadow = api.new_canvas(64, 64)
for dy, row in enumerate(crown):
    for dx, char in enumerate(row):
        if char == 'X':
            cr_canvas.set(crown_x + dx, crown_y + dy, "#f6d741")
            cr_shadow.set(crown_x + dx, crown_y + dy, "#000000")
cr_canvas.outline("#111111")
cr_shadow.outline("#000000")
c.blit(cr_shadow, 0, 2)
c.blit(cr_canvas, 0, 0)

# Sparkles
sparkles = [
    (9, 12), (52, 15), (12, 28), (48, 29), (55, 42), (8, 40),
    (56, 52), (10, 58)
]
for sx, sy in sparkles:
    c.set(sx, sy, "#ffffff")
    c.set(sx-1, sy, "#f6d741")
    c.set(sx+1, sy, "#f6d741")
    c.set(sx, sy-1, "#f6d741")
    c.set(sx, sy+1, "#f6d741")

# Start button
c.poly([(14, 52), (14, 58), (18, 55)], "#000000")
c.poly([(13, 51), (13, 57), (17, 54)], "#f6d741")

c.text(22, 52, "START", "#000000", font="5x7")
c.text(21, 51, "START", "#ffffff", font="5x7")

api.finish(c)
