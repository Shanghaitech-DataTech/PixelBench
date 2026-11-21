from pixelbench_api import new_canvas, finish

def draw():
    c = new_canvas(64, 64)
    
    bg = "#1a1a24"
    bg_d = "#0f0f14"

    skin_d = "#7a4841"
    skin_m = "#b57265"
    skin_l = "#e0a396"

    met_d = "#242830"
    met_m = "#4f5866"
    met_l = "#8b9bb4"
    met_h = "#d4e0f0"

    hair_d = "#5e6470"
    hair_m = "#9ba4b5"
    hair_l = "#e4e8f0"

    coat_d = "#4a4a45"
    coat_m = "#7a7a73"
    coat_l = "#b5b5ab"

    apr_d = "#2e1a10"
    apr_m = "#54311c"
    apr_l = "#855132"

    belt_d = "#1a1a1a"
    belt_m = "#333333"
    belt_l = "#666666"
    gold_m = "#a88422"
    gold_l = "#e6c245"

    glow_c = "#42ff6b"
    glow_m = "#12c93a"
    glow_d = "#066e1b"

    mouth = "#1a0c0e"
    teeth = "#c7c3b1"
    blood = "#701118"

    # 1. Background
    c.rect(0, 0, 64, 64, bg)
    for i in range(4, 64, 12):
        c.line(i, 0, i, 63, "#1f1f2e")
        c.line(0, i, 63, i, "#1f1f2e")
    c.rect(4, 10, 10, 16, "#1a3320")
    c.rect(5, 11, 8, 14, "#24472d")
    c.line(6, 13, 11, 13, glow_d)
    c.line(6, 15, 10, 15, glow_d)
    c.line(6, 17, 12, 17, glow_d)
    
    c.rect(0, 0, 64, 4, bg_d)
    c.rect(0, 60, 64, 4, bg_d)
    c.rect(0, 0, 4, 64, bg_d)
    c.rect(60, 0, 4, 64, bg_d)
    c.rect(4, 4, 4, 4, bg_d)
    c.rect(56, 4, 4, 4, bg_d)
    c.rect(4, 56, 4, 4, bg_d)
    c.rect(56, 56, 4, 4, bg_d)

    # 3. Base coat and torso
    c.rect(16, 32, 32, 32, coat_d)

    # 4. Left arm (coat)
    c.poly([(16, 32), (6, 42), (10, 63), (20, 63), (22, 46)], coat_m)
    c.poly([(14, 32), (6, 42), (10, 63), (14, 63)], coat_d)
    c.poly([(16, 32), (18, 42), (20, 63), (18, 63)], coat_l)

    # 5. Right arm (metal)
    c.poly([(32, 32), (44, 32), (46, 36), (42, 40), (32, 40)], coat_m)
    c.poly([(44, 32), (46, 36), (42, 40)], coat_l)

    c.poly([(42, 36), (52, 36), (56, 44), (46, 46)], met_d)
    c.poly([(43, 37), (51, 37), (54, 43), (47, 45)], met_m)
    c.circle(54, 46, 4, met_d)
    c.circle(54, 46, 2, met_l)
    c.poly([(52, 48), (56, 44), (62, 54), (56, 58)], met_d)
    c.poly([(53, 49), (55, 45), (60, 53), (55, 57)], met_m)
    c.poly([(56, 58), (62, 54), (63, 58), (58, 62)], met_d)
    c.line(62, 56, 63, 62, met_h)
    c.line(60, 58, 62, 63, met_h)
    c.path("M 48 36 C 52 40 50 46 56 50", glow_d, fill=False)
    c.path("M 49 37 C 53 41 51 47 57 51", glow_c, fill=False)

    # 5.5 Coat lapels
    c.poly([(20, 32), (28, 32), (26, 46), (22, 46)], coat_l)
    c.poly([(40, 32), (44, 32), (42, 46), (38, 46)], coat_l)

    # 6. Apron and Belt
    c.poly([(22, 63), (20, 46), (24, 32), (40, 32), (44, 46), (42, 63)], apr_m)
    c.line(24, 32, 20, 28, apr_d)
    c.line(40, 32, 44, 28, apr_d)
    c.poly([(22, 63), (20, 46), (24, 32), (32, 32), (32, 63)], apr_l)

    c.rect(20, 52, 24, 4, belt_m)
    c.rect(28, 51, 8, 6, gold_m)
    c.rect(29, 52, 6, 4, belt_d)
    c.rect(30, 53, 4, 2, gold_l)

    # 7. Neck
    c.rect(28, 28, 4, 4, skin_d)
    c.rect(32, 28, 4, 4, met_d)
    c.line(29, 28, 29, 31, skin_m)
    c.line(33, 28, 33, 31, met_l)
    c.path("M 34 28 C 36 30 36 32 34 34", glow_d, fill=False)
    c.path("M 35 28 C 37 30 37 32 35 34", glow_c, fill=False)

    # 8. Head base
    c.poly([(22, 8), (42, 8), (44, 18), (38, 28), (26, 28), (20, 18)], skin_m)
    c.poly([(32, 8), (42, 8), (44, 18), (38, 28), (32, 28)], met_m)

    # 9. Head shading
    c.poly([(20, 18), (26, 28), (32, 28), (32, 18)], skin_d)
    c.poly([(22, 8), (32, 8), (32, 18), (20, 18)], skin_m)
    c.poly([(24, 10), (30, 10), (30, 16), (22, 16)], skin_l)

    c.poly([(32, 28), (38, 28), (44, 18), (32, 18)], met_d)
    c.poly([(32, 8), (42, 8), (44, 18), (32, 18)], met_m)
    c.poly([(34, 10), (40, 10), (42, 16), (34, 16)], met_l)

    # 10. Eyes, Nose, Mouth
    c.rect(25, 16, 3, 2, "#ffffff")
    c.set(26, 16, "#000000")
    c.line(24, 15, 28, 15, skin_d)
    
    c.rect(34, 14, 6, 5, glow_d)
    c.rect(35, 15, 4, 3, glow_m)
    c.rect(36, 16, 2, 2, glow_c)
    c.set(37, 16, "#ffffff")
    c.line(35, 13, 38, 13, glow_d)
    c.line(35, 19, 38, 19, glow_d)
    c.set(34, 16, glow_c)
    c.set(39, 16, glow_c)
    c.line(34, 14, 38, 15, met_d)

    c.line(31, 18, 31, 21, skin_d)
    c.line(31, 21, 29, 21, skin_d)
    c.set(30, 20, skin_l)
    c.line(33, 19, 33, 21, met_d)
    c.line(34, 20, 35, 20, met_d)

    c.poly([(25, 22), (32, 23), (39, 22), (37, 26), (32, 27), (27, 26)], mouth)
    c.poly([(26, 23), (32, 24), (38, 23), (36, 25), (32, 26), (28, 25)], teeth)
    c.poly([(32, 23), (38, 23), (36, 25), (32, 26)], met_l)
    c.line(26, 24, 38, 24, mouth)
    for x in range(27, 38, 2):
        c.line(x, 23, x, 25, mouth)

    # 11. Face details
    c.line(32, 8, 32, 28, met_d)
    c.line(32, 20, 42, 20, met_d)
    c.line(39, 8, 39, 18, met_d)
    c.line(32, 24, 38, 24, met_d)
    c.set(34, 10, met_h)
    c.set(40, 10, met_h)
    c.set(34, 22, met_h)
    c.set(40, 22, met_h)
    c.set(34, 26, met_h)
    c.path("M 38 28 C 40 30 42 26 44 24", glow_d, fill=False)

    # 12. Hair
    c.circle(22, 8, 6, hair_m)
    c.circle(26, 6, 5, hair_m)
    c.circle(30, 5, 5, hair_m)
    c.circle(18, 12, 4, hair_m)
    c.circle(20, 18, 3, hair_m)

    c.circle(22, 7, 4, hair_l)
    c.circle(26, 5, 3, hair_l)
    c.circle(30, 4, 3, hair_l)
    c.circle(18, 11, 2, hair_l)

    c.poly([(22, 8), (12, 4), (18, 10)], hair_l)
    c.poly([(26, 6), (20, 2), (24, 8)], hair_l)
    c.poly([(30, 5), (32, 0), (28, 6)], hair_l)
    c.poly([(18, 12), (10, 14), (16, 16)], hair_l)
    c.poly([(20, 18), (12, 22), (18, 20)], hair_l)
    
    c.poly([(30, 5), (36, 2), (34, 8)], hair_m)
    c.poly([(31, 6), (35, 3), (34, 8)], hair_l)

    # 13. Brain plugs
    c.poly([(32, 4), (38, 6), (42, 10), (32, 10)], met_d)
    c.poly([(32, 5), (37, 7), (40, 10), (32, 10)], met_m)
    c.rect(36, 2, 2, 4, met_l)
    c.rect(35, 1, 4, 2, met_h)
    c.rect(41, 6, 3, 2, met_l)
    c.rect(43, 5, 2, 4, met_h)
    c.path("M 37 1 C 38 0 44 0 46 4", met_d, fill=False)
    c.path("M 44 7 C 48 8 50 14 46 18", met_d, fill=False)

    # 14. Dirt, blood
    c.rect(26, 40, 2, 2, blood)
    c.set(25, 41, blood)
    c.rect(34, 42, 3, 2, blood)
    c.set(35, 44, blood)
    c.set(36, 45, blood)

    c.rect(14, 48, 2, 2, coat_d)
    c.rect(18, 54, 3, 2, coat_d)
    c.rect(12, 58, 2, 3, coat_d)

    # 15. Tools
    c.rect(22, 56, 2, 6, met_l)
    c.rect(21, 62, 4, 2, met_h)
    c.set(23, 63, bg)

    c.rect(36, 56, 2, 4, glow_d)
    c.rect(37, 60, 1, 4, met_h)

    finish(c)

if __name__ == "__main__":
    draw()
