# Polar researcher sprite, 48x48, transparent background.
# Character on one layer (so outline() only hits the character),
# wind streaks on a second layer behind, flattened at the end.

OUT      = '#171320'   # outline
PARKA    = '#d95b29'
PARKA_D  = '#a63f18'
PARKA_L  = '#f08246'
FUR      = '#f2e7d0'
FUR_D    = '#c9b894'
SKIN     = '#e0a878'
SKIN_D   = '#b97e52'
STRAP    = '#3a2f28'
GOGGLE   = '#bfe6f2'
GOGGLE_D = '#6fa9c4'
WHITE    = '#ffffff'
PANT     = '#33415e'
PANT_D   = '#232c42'
BOOT     = '#1c2230'
BOOT_L   = '#2e3a52'
CASE     = '#c9ced6'
CASE_D   = '#8a929e'
CASE_HI  = '#eef1f5'
STICKER  = '#4fa8d8'
SCARF    = '#b9372f'
SCARF_D  = '#7c231d'
WIND1    = (210, 238, 248, 120)
WIND2    = (210, 238, 248, 70)
SNOW     = (255, 255, 255, 170)

char = new_canvas(48, 48, name="researcher")
wind = new_canvas(48, 48, name="wind")

# ---------------- wind layer ----------------
wind.line(0, 9, 12, 9, WIND1)
wind.line(3, 10, 10, 10, WIND2)
wind.line(1, 17, 15, 17, WIND1)
wind.line(0, 18, 8, 18, WIND2)
wind.line(2, 25, 10, 25, WIND1)
wind.line(1, 29, 6, 29, WIND1)
wind.line(0, 30, 4, 30, WIND2)
wind.line(0, 33, 7, 33, WIND2)
wind.line(38, 6, 47, 6, WIND1)
wind.line(42, 7, 47, 7, WIND2)
wind.line(41, 24, 47, 24, WIND1)
wind.line(44, 37, 47, 37, WIND2)
for (sx, sy) in [(14, 5), (6, 22), (18, 30), (40, 14), (45, 30), (10, 40), (36, 42)]:
    wind.set(sx, sy, SNOW)

# ---------------- character ----------------
# rear (trailing) leg + boot, stretched back
char.poly([(19, 32), (24, 34), (18, 40), (13, 38)], PANT)
char.poly([(13, 38), (18, 40), (13, 44), (9, 44)], PANT_D)
char.poly([(6, 43), (13, 42), (14, 45), (6, 45)], BOOT)

# rear arm reaching back with the sample case
char.poly([(23, 18), (26, 21), (18, 28), (15, 25)], PARKA)
char.poly([(15, 25), (18, 28), (12, 32), (9, 30)], PARKA)
char.circle(11, 31, 2, PARKA_D)                 # mitten
char.line(11, 32, 11, 35, OUT)                  # handle grip
char.rect(9, 33, 5, 1, OUT)                     # handle top
char.rect(5, 35, 11, 9, CASE)                   # case body
char.rect(5, 35, 11, 2, CASE_HI)                # lid highlight
char.rect(5, 42, 11, 2, CASE_D)                 # bottom shade
char.rect(9, 38, 4, 3, STICKER)                 # sample sticker
char.set(10, 38, WHITE)
char.set(7, 35, CASE_D); char.set(13, 35, CASE_D)   # latches

# torso (leaning forward, to the right)
char.poly([(23, 18), (33, 21), (29, 36), (19, 34), (21, 24)], PARKA)

# front leg, braced forward
char.poly([(25, 33), (30, 34), (33, 40), (28, 40)], PANT)
char.poly([(28, 39), (33, 39), (34, 44), (29, 44)], PANT_D)
char.poly([(29, 42), (35, 42), (38, 44), (38, 45), (28, 45)], BOOT)
char.set(30, 43, BOOT_L); char.set(31, 43, BOOT_L)

# front arm swinging forward
char.poly([(30, 21), (33, 23), (36, 29), (33, 30)], PARKA)
char.circle(35, 30, 2, PARKA_D)                 # mitten

# scarf: a thin ribbon whipping back in the wind
char.poly([(29, 17), (22, 15), (14, 16), (13, 18), (22, 19), (29, 19)], SCARF)
char.line(14, 16, 11, 14, SCARF)
char.line(14, 18, 11, 20, SCARF_D)

# hood (pushed forward of the shoulders: leaning into the wind)
char.circle(29, 12, 7, PARKA)
char.circle(29, 12, 4, FUR)
char.circle(32, 13, 3, SKIN)                    # face
char.rect(33, 17, 3, 2, PARKA)                  # collar into shoulder
# goggles
char.line(25, 11, 28, 11, STRAP)
char.rect(29, 10, 7, 3, STRAP)
char.rect(30, 10, 2, 1, GOGGLE)
char.rect(33, 10, 2, 1, GOGGLE)
char.rect(30, 11, 2, 1, GOGGLE_D)
char.rect(33, 11, 2, 1, GOGGLE_D)
char.set(30, 10, WHITE); char.set(33, 10, WHITE)
char.set(32, 15, SKIN_D)                        # mouth

# shading + highlight details
char.line(28, 21, 24, 34, PARKA_D)              # zipper
char.line(19, 34, 29, 36, PARKA_D)              # hem
char.line(26, 12, 26, 14, FUR_D)                # fur shade
char.set(25, 15, FUR_D)
char.rect(30, 21, 3, 2, PARKA_L)                # shoulder highlight
char.set(24, 8, PARKA_L); char.set(25, 7, PARKA_L)  # hood highlight
char.set(23, 9, PARKA_L)
char.set(31, 35, PANT_D)                        # crotch shade

char.outline(OUT)

result = flatten([wind, char], name="result")
print(result.stats())
view(result)
finish(result)
