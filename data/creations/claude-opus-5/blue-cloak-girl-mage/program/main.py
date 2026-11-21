"""64x64 anime-style girl mage sprite: dark blue cloak, white boots, amber staff."""

W = H = 64

INK      = "#0b1026"
CLOAK    = "#22356d"
CLOAK_D  = "#141f48"
CLOAK_L  = "#35508f"
TRIM     = "#e0a63c"
ROBE     = "#cdd4e6"
ROBE_D   = "#a3abc6"
BOOT     = "#f4f6fb"
BOOT_D   = "#c3cadb"
SKIN     = "#f6cfa8"
SKIN_D   = "#dba379"
MOUTH    = "#bf7363"
BLUSH    = "#ef9a88"
HAIR     = "#cdd3f2"
HAIR_D   = "#8e97c6"
HAIR_S   = "#e9ecff"
EYE      = "#2a2f4d"
IRIS     = "#f0b03e"
WHITE    = "#ffffff"
WOOD     = "#7d5531"
WOOD_D   = "#50341a"
ORB1     = "#fff6cf"
ORB2     = "#ffcf5a"
ORB3     = "#e8891c"
GLOW     = "#ffd97a"


def size_of(c):
    s = c.stats()["size"]
    if isinstance(s, dict):
        return s.get("width", s.get("w")), s.get("height", s.get("h"))
    return s[0], s[1]


def mask_of(c):
    w, h = size_of(c)
    pal = {p["index"]: p["rgba"] for p in c.palette()}
    m = [[False] * w for _ in range(h)]
    for y in range(h):
        row = m[y]
        for x in range(w):
            rgba = pal.get(c.get(x, y))
            if rgba is None:
                continue
            a = rgba[3] if len(rgba) > 3 else 255
            row[x] = a > 0
    return m


def outline_layer(c, colour=INK):
    w, h = size_of(c)
    m = mask_of(c)
    out = new_canvas(w, h, name="ink")
    for y in range(h):
        for x in range(w):
            if m[y][x]:
                continue
            hit = False
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    yy, xx = y + dy, x + dx
                    if 0 <= yy < h and 0 <= xx < w and m[yy][xx]:
                        hit = True
                        break
                if hit:
                    break
            if hit:
                out.set(x, y, colour)
    return out


# ---------------------------------------------------------------- figure
body = new_canvas(W, H, name="body")

# --- hair mass (behind everything on the head) ---------------------
body.ellipse(28, 26, 8, 7, HAIR_D)
body.rect(20, 24, 3, 12, HAIR)
body.rect(34, 24, 3, 12, HAIR_D)
body.set(20, 35, HAIR_D)
body.set(36, 35, HAIR_D)

# --- face ----------------------------------------------------------
body.ellipse(28, 26, 5, 5, SKIN)
body.rect(22, 22, 1, 10, HAIR_D)
body.rect(34, 22, 1, 10, HAIR_D)
body.line(24, 31, 32, 31, SKIN_D)

# bangs
body.rect(23, 21, 11, 3, HAIR)
body.rect(23, 21, 11, 1, HAIR_S)
body.poly([(23, 24), (26, 24), (24, 25)], HAIR)
body.poly([(27, 24), (30, 24), (28, 26)], HAIR)
body.poly([(31, 24), (34, 24), (33, 25)], HAIR)

# eyes: lash row, amber iris, highlight
body.rect(24, 25, 3, 1, EYE)
body.rect(24, 26, 3, 2, IRIS)
body.set(24, 26, WHITE)
body.set(26, 27, EYE)
body.rect(30, 25, 3, 1, EYE)
body.rect(30, 26, 3, 2, IRIS)
body.set(30, 26, WHITE)
body.set(32, 27, EYE)

# mouth + blush
body.set(28, 29, MOUTH)
body.rect(24, 28, 2, 1, BLUSH)
body.rect(31, 28, 2, 1, BLUSH)

# neck
body.rect(27, 32, 3, 2, SKIN_D)

# --- witch hat -----------------------------------------------------
body.poly([(28, 3), (36, 18), (20, 18)], CLOAK)
body.poly([(29, 5), (36, 18), (29, 18)], CLOAK_D)
body.poly([(27, 6), (24, 18), (22, 18)], CLOAK_L)
body.rect(22, 15, 13, 3, TRIM)
body.rect(22, 17, 13, 1, "#b8822a")
body.set(28, 16, CLOAK_D)
body.ellipse(28, 19, 12, 2, CLOAK)
body.ellipse(28, 20, 12, 1, CLOAK_D)

# --- cloak ---------------------------------------------------------
body.poly([(23, 33), (33, 33), (36, 37), (38, 46), (39, 54),
           (17, 54), (18, 46), (20, 37)], CLOAK)
body.poly([(33, 34), (36, 37), (38, 46), (39, 54), (33, 54)], CLOAK_D)
body.poly([(23, 33), (33, 33), (34, 36), (22, 36)], CLOAK_L)
body.line(23, 46, 22, 54, CLOAK_D)
body.line(33, 46, 34, 54, CLOAK_D)

# front robe + gold trim
body.poly([(26, 37), (30, 37), (32, 54), (24, 54)], ROBE)
body.poly([(29, 37), (30, 37), (32, 54), (30, 54)], ROBE_D)
body.line(26, 37, 24, 54, TRIM)
body.line(30, 37, 32, 54, TRIM)
body.rect(24, 43, 9, 2, TRIM)
body.set(28, 43, CLOAK_D)
body.rect(27, 34, 3, 1, TRIM)
body.set(28, 35, TRIM)

# --- arms ----------------------------------------------------------
# viewer-right arm raised to grip the staff
body.poly([(33, 35), (36, 36), (41, 38), (41, 42), (36, 40), (32, 38)], CLOAK)
body.line(33, 36, 37, 38, CLOAK_L)
body.rect(39, 38, 2, 4, TRIM)
body.rect(41, 38, 4, 3, SKIN)
body.rect(41, 40, 4, 1, SKIN_D)
body.set(44, 38, SKIN_D)

# viewer-left arm hanging relaxed
body.poly([(23, 35), (20, 37), (19, 46), (23, 48), (23, 40)], CLOAK)
body.line(23, 36, 22, 45, CLOAK_D)
body.rect(19, 44, 4, 2, TRIM)
body.rect(19, 46, 4, 3, SKIN)
body.rect(19, 48, 4, 1, SKIN_D)
body.set(22, 46, SKIN_D)

# cloak hem shading
body.rect(18, 53, 21, 1, CLOAK_D)

# --- boots ---------------------------------------------------------
body.rect(23, 55, 5, 5, BOOT)
body.rect(29, 55, 5, 5, BOOT)
body.rect(22, 58, 6, 2, BOOT)
body.rect(29, 58, 6, 2, BOOT)
body.rect(23, 55, 5, 1, ROBE_D)
body.rect(29, 55, 5, 1, ROBE_D)
body.rect(22, 59, 6, 1, BOOT_D)
body.rect(29, 59, 6, 1, BOOT_D)
body.set(24, 57, BOOT_D)
body.set(33, 57, BOOT_D)

# ---------------------------------------------------------------- staff
staff = new_canvas(W, H, name="staff")
staff.rect(42, 15, 3, 45, WOOD)
staff.rect(44, 15, 1, 45, WOOD_D)
staff.rect(42, 59, 3, 1, WOOD_D)
staff.rect(42, 16, 3, 2, TRIM)
staff.circle(43, 11, 4, ORB3)
staff.circle(43, 11, 3, ORB2)
staff.circle(42, 10, 1, ORB1)
staff.set(43, 11, ORB1)

# ---------------------------------------------------------------- glow
glow = new_canvas(W, H, name="glow")
for gx, gy in [(43, 4), (37, 9), (49, 12), (38, 15), (48, 6), (45, 18)]:
    glow.set(gx, gy, GLOW)
glow.circle(43, 11, 6, "#ffd97a55", fill=False)

# ---------------------------------------------------------------- compose
art = flatten([staff, body], name="art")
ink = outline_layer(art)
result = flatten([ink, art, glow], name="output")

print(result.stats_text())
view(result)
save("blue-cloak-girl-mage", result)
finish(result)
