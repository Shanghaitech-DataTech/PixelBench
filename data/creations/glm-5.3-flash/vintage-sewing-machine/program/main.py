# vintage-sewing-machine -- 48x48 pixel art, transparent background
# slightly angled side view: needle head left, handwheel right, red fabric on the bed

c = new_canvas(48, 48, background=None, name="vintage-sewing-machine")

# ---------------- palette ----------------
OUT    = c.color('#17131f', 'outline')
BODY   = c.color('#3a3449', 'body')
BODYHI = c.color('#5a5270', 'body_hi')
BODYLO = c.color('#262133', 'body_lo')
GOLD   = c.color('#e3b356', 'gold')
GOLDD  = c.color('#ad7f30', 'gold_dk')
MET    = c.color('#b6bec8', 'metal')
METL   = c.color('#e9eff6', 'metal_lt')
METD   = c.color('#7b8493', 'metal_dk')
RED    = c.color('#c93038', 'red')
REDL   = c.color('#f0686c', 'red_lt')
REDD   = c.color('#901f27', 'red_dk')
CREAM  = c.color('#f3e9d1', 'thread')

# ---------------- thread spool on the arm top ----------------
c.rect(17, 2, 6, 5, OUT)          # x17..22, y2..6
c.rect(17, 2, 1, 5, GOLDD)        # wooden left flange
c.rect(22, 2, 1, 5, GOLDD)        # wooden right flange
c.rect(18, 3, 4, 3, CREAM)        # thread wind x18..21, y3..5

# ---------------- bobbin winder ----------------
c.ellipse(27, 4, 2, 2, OUT, fill=True)
c.ellipse(27, 4, 1, 1, MET, fill=True)
c.set(27, 4, METD)
c.set(27, 2, METL)                # spindle tip

# ---------------- pillar ----------------
c.rect(30, 7, 11, 30, OUT)        # x30..40, y7..36
c.rect(31, 8, 9, 28, BODY)        # x31..39, y8..35

# ---------------- arm ----------------
c.rect(5, 7, 26, 10, OUT)         # x5..30, y7..16
c.rect(6, 8, 24, 8, BODY)         # x6..29, y8..15

# ---------------- head ----------------
c.rect(5, 7, 12, 20, OUT)         # x5..16, y7..26
c.rect(6, 8, 10, 18, BODY)        # x6..15, y8..25
c.rect(16, 8, 1, 8, BODY)         # head and arm share this edge

# ---------------- light and shade ----------------
c.rect(6, 8, 34, 1, BODYHI)       # top highlight along head + arm + pillar
c.rect(17, 15, 13, 1, BODYLO)     # arm belly shade x17..29
c.rect(31, 17, 1, 19, BODYHI)     # pillar left light
c.rect(39, 20, 1, 16, BODYLO)     # pillar right shade

# ---------------- face plate ----------------
c.rect(6, 17, 7, 9, BODYHI)       # panel x6..12, y17..25
c.rect(6, 17, 1, 9, BODYLO)       # left border
c.rect(8, 18, 3, 4, BODYLO)       # take-up slot x8..10, y18..21
c.rect(8, 19, 3, 1, METL)         # take-up lever
c.set(10, 18, METL)               # lever tip
c.ellipse(9, 23, 1, 1, OUT, fill=True)   # tension disc
c.set(9, 23, MET)
c.ellipse(9, 12, 2, 1, GOLD, fill=True)  # gold medallion
c.set(9, 12, GOLDD)

# ---------------- handwheel (ellipse = the slight angle) ----------------
c.ellipse(41, 14, 4, 5, OUT, fill=True)
c.ellipse(41, 14, 3, 4, MET, fill=True)
c.ellipse(41, 14, 2, 3, METD, fill=True)
c.ellipse(41, 14, 1, 1, METL, fill=True)
c.set(41, 14, METD)
c.set(38, 13, METL)               # rim highlight
c.set(38, 14, METL)

# ---------------- stitch length dial + pillar decal ----------------
c.ellipse(35, 25, 2, 2, OUT, fill=True)
c.ellipse(35, 25, 1, 1, GOLD, fill=True)
c.set(35, 25, METL)
c.ellipse(34, 21, 2, 1, GOLD, fill=True)
c.set(34, 21, GOLDD)

# ---------------- gold decal along the arm ----------------
c.rect(19, 11, 11, 1, GOLD)       # x19..29
c.set(19, 11, GOLDD)
c.set(29, 11, GOLDD)

# ---------------- bed ----------------
c.rect(2, 36, 44, 8, OUT)         # x2..45, y36..43
c.rect(3, 37, 42, 2, BODYHI)      # bed top surface
c.rect(32, 37, 8, 2, BODYLO)      # shadow under the pillar
c.rect(6, 37, 18, 2, METD)        # needle plate x6..23
c.rect(6, 37, 18, 1, MET)
c.rect(12, 37, 1, 2, BODYLO)      # needle slot
c.rect(25, 37, 7, 2, METD)        # slide plate x25..31
c.rect(25, 37, 7, 1, MET)
c.rect(3, 39, 42, 3, BODY)        # front face
c.rect(5, 40, 38, 1, GOLD)        # gold pinstripe
c.rect(3, 42, 42, 1, BODYLO)      # bottom shade
c.rect(4, 44, 6, 2, OUT)          # feet
c.rect(5, 44, 4, 1, BODYLO)
c.rect(38, 44, 6, 2, OUT)
c.rect(39, 44, 4, 1, BODYLO)

# ---------------- red fabric ----------------
c.rect(5, 32, 14, 1, REDL)        # x5..18  top highlight
c.rect(4, 33, 16, 1, RED)         # x4..19
c.rect(4, 34, 16, 1, RED)         # x4..19
c.rect(5, 35, 15, 1, RED)         # x5..19
c.rect(6, 36, 13, 1, REDD)        # x6..18  near edge on the bed rim
c.rect(16, 33, 1, 3, REDD)        # fold crease
c.set(6, 34, CREAM)               # stitches already sewn
c.set(8, 34, CREAM)
c.set(10, 34, CREAM)

# ---------------- presser bar / foot / needle bar / needle ----------------
c.rect(8, 26, 2, 4, METD)         # presser bar x8..9, y26..29
c.rect(8, 26, 1, 4, MET)
c.rect(11, 26, 2, 3, MET)         # needle bar x11..12, y26..28
c.rect(11, 26, 1, 3, METL)
c.rect(11, 29, 2, 1, METD)        # needle clamp
c.rect(5, 30, 7, 1, METL)         # foot top x5..11
c.rect(4, 31, 8, 1, MET)          # foot sole x4..11
c.rect(12, 30, 1, 3, METL)        # needle above the fabric
c.rect(12, 33, 1, 3, MET)         # needle buried in the fabric

# ---------------- thread path ----------------
for x, y in [(16, 3), (15, 4), (14, 5), (14, 6),
             (14, 7), (14, 8), (14, 9), (14, 10), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15),
             (13, 16), (12, 17), (11, 18), (10, 18), (9, 19), (8, 20), (8, 21), (9, 22),
             (9, 25), (10, 26), (10, 27), (10, 28), (11, 29)]:
    c.set(x, y, CREAM)

# ---------------- rounded corners ----------------
c.clear(5, 7, 1, 1)               # head top-left
c.clear(40, 7, 1, 1)              # pillar top-right
c.clear(5, 26, 1, 1)              # head bottom-left
c.clear(16, 26, 1, 1)             # head bottom-right
c.clear(2, 36, 1, 1)              # bed corners
c.clear(45, 36, 1, 1)
c.clear(2, 43, 1, 1)
c.clear(45, 43, 1, 1)

# ---------------- inspection ----------------
CODES = {'outline': 'o', 'body': 'b', 'body_hi': 'H', 'body_lo': 'L', 'gold': 'G',
         'gold_dk': 'g', 'metal': 'm', 'metal_lt': 'W', 'metal_dk': 'd', 'red': 'r',
         'red_lt': 'R', 'red_dk': 'D', 'thread': 't'}

def dump(x0, y0, x1, y1, chunk=16):
    idx = {d['index']: CODES.get(d['name'], '?') for d in c.palette()}
    for cx in range(x0, x1 + 1, chunk):
        ce = min(cx + chunk - 1, x1)
        print(f"--- x {cx}..{ce} ---")
        print("     " + "".join(str(x % 10) for x in range(cx, ce + 1)))
        for y in range(y0, y1 + 1):
            row = ""
            for x in range(cx, ce + 1):
                i = c.get(x, y)
                row += "." if i == 0 else idx.get(i, '?')
            print(f"{y:3d}  {row}")

print(c.stats_text())
dump(0, 24, 47, 40)
finish(c)
