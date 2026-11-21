# ============================================================
#  Polar researcher - 48x48 pixel art sprite
#  Bracing into a hard headwind, heavy parka, sample case.
# ============================================================

c = new_canvas(48, 48, background=None, name="polar-researcher")

# ---------------- palette (24 colours) ----------------
O   = c.color("#1A1E2A", "outline")
R   = c.color("#C4452C", "parka")
Rd  = c.color("#8F2A1D", "parka_shadow")
Rl  = c.color("#E07A4A", "parka_light")
F   = c.color("#E9DFC6", "fur")
Fd  = c.color("#C3B18E", "fur_shadow")
S   = c.color("#E8B48C", "skin")
Sd  = c.color("#C08A66", "skin_shadow")
G   = c.color("#22303E", "goggle_frame")
L   = c.color("#BFE4F4", "lens")
Lm  = c.color("#8FC6E0", "lens_mid")
W   = c.color("#FFFFFF", "glint")
P   = c.color("#33415E", "pants")
Pd  = c.color("#232D44", "pants_shadow")
Bt  = c.color("#4C3A2A", "boot")
Bl  = c.color("#6F5738", "boot_light")
M   = c.color("#4E6078", "mitten")
Md  = c.color("#3A4A5E", "mitten_shadow")
Cs  = c.color("#8A9DB2", "case")
Csd = c.color("#5F7186", "case_shadow")
Ck  = c.color("#B7C8D8", "case_light")
K   = c.color("#2C3848", "strap")
Xp  = c.color("#C9E4F2", "snow_pale")
Xs  = c.color("#9FBFD6", "snow_shadow")


def report(cv):
    """Run-length dump, one line per row: col-col CODE."""
    abbr = {'outline': '#', 'parka': 'R', 'parka_shadow': 'r', 'parka_light': 'L',
            'fur': 'F', 'fur_shadow': 'f', 'skin': 'S', 'skin_shadow': 's',
            'goggle_frame': 'g', 'lens': 'l', 'lens_mid': 'm', 'glint': 'W',
            'pants': 'P', 'pants_shadow': 'p', 'boot': 'B', 'boot_light': 'b',
            'mitten': 'M', 'mitten_shadow': 'd', 'case': 'C', 'case_shadow': 'c',
            'case_light': 'k', 'strap': 'K', 'snow_pale': 'x', 'snow_shadow': 'z'}
    names = {e['index']: abbr.get(e['name'], '?') for e in cv.palette()}

    def gi(x, y):
        i = cv.get(x, y)
        return i if i else None

    print("     " + "".join(str((x // 10) % 10) for x in range(48)))
    print("     " + "".join(str(x % 10) for x in range(48)))
    for y in range(48):
        runs, prev, start = [], None, 0
        for x in range(49):
            cur = gi(x, y) if x < 48 else None
            if cur != prev:
                if prev:
                    t = names.get(prev, '?')
                    runs.append(f"{start}-{x-1}{t}" if x - 1 > start else f"{start}{t}")
                prev, start = cur, x
        print(f"{y:3d}  " + " ".join(runs))


# ---------------- 1. far arm, trailing back ----------------
c.poly([(25,19),(28,19),(19,25),(17,23)], Rd)
c.rect(13,24, 6,4, M)
c.line(14,26, 17,26, Md)

# ---------------- 2. legs, wide bracing stance ----------------
c.poly([(22,35),(27,35),(24,42),(19,42)], Pd)
c.poly([(31,35),(36,35),(38,42),(33,42)], P)
c.line(33,37, 35,40, Pd)

# ---------------- 3. boots ----------------
c.rect(19,42, 10,3, Bt)
c.line(21,43, 27,43, Bl)
c.rect(32,42, 10,3, Bt)
c.line(34,43, 40,43, Bl)

# ---------------- 4. coat flap streaming back + torn scrap ----------------
c.poly([(23,29),(10,29),(6,33),(12,36),(23,35)], Rd)
c.line(14,30, 21,30, R)
c.line(9,32, 14,32, R)
c.poly([(7,38),(3,41),(8,41)], Rd)
c.set(5,40, R)

# ---------------- 5. torso, sheared forward into the wind ----------------
c.poly([(27,18),(42,18),(40,27),(37,35),(23,35),(22,27)], R)
c.line(27,19, 24,27, Rd)
c.line(24,28, 25,33, Rd)
c.line(39,24, 37,32, Rl)
c.line(23,34, 37,34, Rd)
c.line(34,20, 30,29, Rd)
c.line(24,26, 39,26, K)
c.rect(31,25, 2,2, Ck)

# ---------------- 6. collar ----------------
c.rect(26,16, 18,2, F)
c.line(26,17, 43,17, Fd)

# ---------------- 7. hood, swept back off the forehead ----------------
c.poly([(31,2),(38,2),(40,3),(41,4),(41,6),(28,6),(26,5),(27,3),(29,2)], R)
c.line(32,3, 39,3, Rl)
c.set(40,4, Rl); c.set(40,5, Rl); c.set(41,5, Rl)
c.set(27,4, Rd); c.set(27,5, Rd); c.set(28,5, Rd)

# ---------------- 8. fur ruff ----------------
c.rect(28,6, 15,2, F)
c.rect(29,8, 2,8, Fd)
c.rect(41,8, 2,8, F)
c.set(32,6, Fd); c.set(36,6, Fd); c.set(39,6, Fd)
c.set(41,10, Fd); c.set(42,13, Fd)
c.set(29,11, F); c.set(30,14, F)

# ---------------- 9. goggles ----------------
c.rect(31,8, 10,6, G)
c.rect(32,9, 8,4, L)
c.set(32,9,Lm); c.set(32,10,Lm); c.set(32,11,Lm); c.set(32,12,Lm)
c.set(33,12,Lm); c.set(38,12,Lm); c.set(39,12,Lm)
c.set(37,9,W); c.set(38,9,W)
c.set(36,10,W); c.set(37,10,W)
c.set(35,11,W); c.set(36,11,W)
c.set(34,12,W); c.set(35,12,W)

# ---------------- 10. chin ----------------
c.rect(31,14, 10,2, S)
c.set(31,14,Sd); c.set(31,15,Sd); c.set(32,15,Sd)

# ---------------- 11. near arm reaching to the case ----------------
c.poly([(39,18),(43,18),(45,24),(41,25)], R)
c.line(40,19, 41,23, Rd)
c.line(42,19, 44,22, Rl)
c.rect(41,24, 5,2, F)

# ---------------- 12. mitten, handle, sample case ----------------
c.rect(41,26, 4,4, M)
c.line(42,29, 44,29, Md)
c.line(39,30, 44,30, K)
c.rect(38,31, 7,8, Cs)
c.line(39,31, 43,31, Ck)
c.line(38,32, 38,37, Csd)
c.rect(40,33, 3,3, Ck)
c.set(41,34, K); c.set(41,35, K)
c.set(43,32, K); c.set(43,37, K)
c.line(45,27, 45,30, Ck)      # sample probe
c.set(45,26, W)

# ---------------- 13. silhouette ----------------
c.outline(O)

# ---------------- 14. loose fur, torn loose by the wind ----------------
c.set(28,7, Fd); c.set(27,8, F); c.set(26,9, Fd)
c.set(28,11, Fd); c.set(27,13, F)
c.set(25,16, Fd); c.set(24,17, F)

# ---------------- 14b. snow caught on the fur ----------------
c.set(29,6, W); c.set(33,6, W); c.set(37,6, W)
c.set(30,7, W); c.set(35,7, W)
c.set(31,14, W); c.set(33,14, W)

# ---------------- 15. wind and driving snow ----------------
c.line(2,4, 7,4, Xp)
c.line(1,9, 4,9, W)
c.line(3,14, 8,14, Xp)
c.line(1,20, 5,20, W)
c.line(2,26, 6,26, Xp)
c.line(1,32, 4,32, W)
c.line(3,38, 7,38, Xp)
c.line(45,3, 47,3, Xp)
c.line(44,9, 47,9, W)
c.line(46,22, 47,22, Xp)
c.line(45,39, 47,39, Xp)
c.set(10,7, W); c.set(11,12, Xp); c.set(9,17, W); c.set(12,23, Xp)
c.set(8,30, W); c.set(13,36, Xp)
c.set(46,15, Xp); c.set(45,28, W); c.set(47,34, Xp)

# ---------------- 16. snow ground + cast shadow ----------------
c.line(13,45, 43,45, Xs)
c.set(12,45, Xp); c.set(44,45, Xp)
c.set(17,46, W); c.set(23,46, Xp); c.set(31,46, W); c.set(39,46, Xp)
c.set(19,47, Xp); c.set(36,47, W)

print(c.stats_text())
report(c)
finish(c)
