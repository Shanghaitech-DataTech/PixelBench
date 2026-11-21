from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32, name="rts-factory-icon")

OUT    = c.color((38, 38, 44))     # clean dark silhouette outline
BRICK  = c.color((178, 76, 50))    # brick wall
ROOF   = c.color((126, 124, 132))  # flat roof
CHIM   = c.color((88, 86, 94))     # chimney body
CAP    = c.color((146, 144, 152))  # chimney cap band
WIN    = c.color((232, 168, 64))   # glowing window
DOOR   = c.color((26, 26, 32))     # loading door
VENT   = c.color((54, 54, 62))     # vent panel
SLAT   = c.color((140, 142, 150))  # vent slats
SMOKE  = c.color((170, 172, 180))
SMOKEL = c.color((206, 208, 216))

# --- smoke puffs above the right chimney ---
c.set(22, 1, SMOKEL).set(23, 1, SMOKE).set(24, 1, SMOKE)
c.set(23, 2, SMOKEL).set(24, 2, SMOKE)

# --- left chimney ---
c.rect(7, 4, 3, 6, CHIM)
c.rect(6, 3, 5, 2, CAP)
c.rect(7, 4, 3, 6, OUT, fill=False)
c.rect(6, 3, 5, 2, OUT, fill=False)

# --- right chimney ---
c.rect(22, 6, 3, 4, CHIM)
c.rect(21, 5, 5, 2, CAP)
c.rect(22, 6, 3, 4, OUT, fill=False)
c.rect(21, 5, 5, 2, OUT, fill=False)

# --- roof vent boxes ---
c.rect(12, 8, 3, 2, VENT).rect(12, 8, 3, 2, OUT, fill=False)
c.rect(17, 8, 3, 2, VENT).rect(17, 8, 3, 2, OUT, fill=False)

# --- flat roof ---
c.rect(2, 10, 28, 3, ROOF)
c.rect(2, 10, 28, 3, OUT, fill=False)

# --- brick wall ---
c.rect(5, 13, 22, 18, BRICK)
for yy in (16, 19, 22, 25, 28):
    c.line(5, yy, 26, yy, OUT)
mortar = [
    (13, 10), (13, 15), (13, 20),
    (16, 8), (16, 13), (16, 18), (16, 23),
    (19, 10), (19, 15), (19, 20),
    (22, 8), (22, 13), (22, 18), (22, 23),
    (25, 10), (25, 15), (25, 20),
    (28, 8), (28, 13), (28, 18), (28, 23),
]
for y0, x0 in mortar:
    c.line(x0, y0, x0, y0 + 2, OUT)

# --- wall vents ---
c.rect(20, 15, 4, 7, VENT)
for yy in (16, 18, 20):
    c.line(21, yy, 22, yy, SLAT)
c.rect(20, 15, 4, 7, OUT, fill=False)

# --- loading door ---
c.rect(13, 23, 6, 7, DOOR)
c.rect(13, 23, 6, 7, OUT, fill=False)

# --- silhouette: outline the entire brick wall once ---
c.rect(5, 13, 22, 18, OUT, fill=False)

print(c.stats_text())
print(c.matrix_text())

finish(c)
