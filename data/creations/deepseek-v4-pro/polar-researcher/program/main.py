# Polar researcher sprite - 48x48, transparent background
c = new_canvas(48, 48, background=None, name="polar-researcher")

# ---------- palette ----------
OUT        = c.color('#1a2438', 'outline')      # dark navy outline
PARKA      = c.color('#d6553a', 'parka')        # orange-red parka
PARKA_LIT  = c.color('#f2845c', 'parka-lit')    # parka highlight
PARKA_DK   = c.color('#a03a26', 'parka-dark')   # parka shadow
FUR        = c.color('#f2ece0', 'fur')          # cream fur trim
FUR_DK     = c.color('#cfc4b0', 'fur-dark')     # fur shadow
SKIN       = c.color('#e8b48c', 'skin')
LENS       = c.color('#aedcf2', 'lens')         # pale blue goggle lens
LENS_HI    = c.color('#e8f6ff', 'lens-hi')      # goggle reflection
FRAME      = c.color('#35405c', 'frame')        # goggle frame
PANTS      = c.color('#2c3c58', 'pants')        # snow pants
BOOT       = c.color('#3a2f2c', 'boot')
BOOT_HI    = c.color('#5d4c46', 'boot-hi')
CASE       = c.color('#a3b2c0', 'case')         # sample case silver
CASE_DK    = c.color('#738294', 'case-dark')
HANDLE     = c.color('#3c4a5c', 'handle')
SCARF      = c.color('#e8c14a', 'scarf')
SCARF_DK   = c.color('#bf9a34', 'scarf-dark')
MITTEN     = c.color('#b0452c', 'mitten')
SNOW       = c.color('#f7fbff', 'snow')
WIND       = c.color('#cfe3f2', 'wind')

# ---------- helpers ----------
def poly(pts, col, outline=True):
    c.poly(pts, col, fill=True)
    if outline:
        c.poly(pts, OUT, fill=False)

# ---------- draw back-to-front ----------

# scarf tail (streams left, behind body)
poly([(21,13),(12,11),(5,12),(3,16),(8,17),(4,20),(11,19),(17,18),(21,16)], SCARF)
# a fold shadow on the tail
c.poly([(12,11),(5,12),(3,16),(8,17),(12,14)], SCARF_DK, fill=True)

# far (back) leg
poly([(20,28),(24,29),(23,41),(18,43)], PANTS)

# torso (leaning right: shoulder forward, hip back)
poly([(22,13),(31,14),(29,30),(20,29)], PARKA)

# near (front) leg
poly([(24,28),(29,29),(30,41),(24,43)], PANTS)

# boots
poly([(14,42),(21,41),(22,46),(13,47)], BOOT)
poly([(22,42),(31,41),(32,47),(21,47)], BOOT)
# boot highlights
c.line(17,44,19,44,BOOT_HI)
c.line(26,44,28,44,BOOT_HI)

# hood / head
c.circle(26,8,7,PARKA,fill=True)
c.circle(26,8,7,OUT,fill=False)
c.line(21,3,24,3,PARKA_LIT)

# face opening (skin)
c.ellipse(28,8,4,5,SKIN,fill=True)
c.ellipse(28,8,4,5,OUT,fill=False)

# goggles - strap, frame, pale reflective lens, highlight
c.rect(23,6,11,4,FRAME,fill=True)               # strap across hood
c.ellipse(29,8,5,4,FRAME,fill=True)             # goggle frame
c.ellipse(29,8,4,3,LENS,fill=True)              # pale blue lens
c.ellipse(27,7,2,1,LENS_HI,fill=True)           # reflection streak

# fur trim - thin cream rim along the front of the hood opening
c.poly([(32,4),(34,6),(34,11),(32,13),(31,11),(31,6)], FUR, fill=True)
c.poly([(32,7),(33,7),(33,10),(32,10)], FUR_DK, fill=True)

# near arm / sleeve reaching down to the case
poly([(25,14),(30,15),(33,24),(28,26)], PARKA_DK)

# scarf wrap around neck
poly([(21,12),(30,13),(30,16),(21,15)], SCARF)
c.poly([(21,13),(30,14),(30,15),(21,15)], SCARF_DK, fill=True)

# sample case
poly([(33,25),(42,25),(42,33),(33,33)], CASE)
# mitten gripping the handle (over the case)
poly([(33,23),(39,24),(39,27),(33,28)], MITTEN)
# handle above the mitten
c.rect(35,22,4,2,HANDLE,fill=True)
c.rect(34,29,8,2,CASE_DK,fill=True)
c.rect(34,31,3,2,CASE_DK,fill=True)
c.rect(37,29,3,2,LENS,fill=True)   # small sample window / label

# ---------- wind & snow ----------
# wind streaks (blowing from right toward left)
c.line(40,5,45,5,WIND)
c.line(42,9,46,9,WIND)
c.line(39,38,44,38,WIND)
c.line(2,26,7,26,WIND)
c.line(4,33,8,33,WIND)

# snow particles
for (sx,sy) in [(5,30),(10,37),(16,42),(7,17),(38,4),(41,15),(36,40),(12,5),(43,44)]:
    c.rect(sx,sy,1,1,SNOW,fill=True)

# ---------- report ----------
print(c.stats_text())
print(c.matrix_text(region=(0,0,47,47)))
finish(c)
