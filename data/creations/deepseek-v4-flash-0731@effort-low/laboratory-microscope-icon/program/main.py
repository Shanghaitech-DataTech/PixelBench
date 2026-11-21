from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

OUT  = (16, 20, 32)
BODY = (150, 163, 186)
BODYD= (110, 124, 146)
ARMD = (82, 94, 112)
STAGE= (58, 66, 84)
BASE = (46, 54, 72)
LENS = (26, 30, 42)
HIL  = (188, 201, 222)
ACC  = (196, 66, 66)
EO   = (64, 74, 92)
SLID = (148, 200, 182)

# ---------- Eyepiece (rows 2-5) ----------
c.rect(11, 2, 7, 4, OUT)
c.rect(12, 3, 5, 2, EO)
c.rect(12, 3, 5, 1, HIL)
c.rect(12, 4, 1, 1, HIL)
c.rect(12, 5, 5, 1, BODYD)

# ---------- Body tube (rows 6-12) ----------
c.rect(14, 6, 6, 7, OUT)
c.rect(15, 7, 4, 5, BODY)
c.rect(15, 7, 1, 5, HIL)

# ---------- Nosepiece/collar (rows 13-15) ----------
c.rect(13, 13, 8, 3, OUT)
c.rect(14, 14, 6, 2, BODYD)
c.rect(14, 14, 6, 1, BODY)

# ---------- Objective (rows 16-21) ----------
c.rect(12, 16, 5, 6, OUT)
c.rect(13, 17, 3, 2, BODYD)     # body
c.rect(13, 19, 3, 1, ACC)       # red band
c.rect(13, 20, 3, 1, LENS)      # lens tip

# ---------- Arm (rows 6-22) ----------
c.rect(20, 6, 4, 17, OUT)
c.rect(21, 7, 2, 15, ARMD)
c.rect(21, 7, 1, 5, HIL)
# focus knob
c.circle(21, 17, 2, OUT)
c.circle(21, 17, 1, EO)
c.set(21,16,EO)

# ---------- Stage (rows 22-25) ----------
c.rect(4, 22, 14, 3, OUT)
c.rect(5, 23, 12, 2, STAGE)
c.rect(5, 23, 12, 1, HIL)
# slide
c.rect(8, 21, 5, 2, OUT)
c.rect(9, 21, 3, 1, SLID)

# ---------- Pillar (rows 25-28) ----------
c.rect(6, 25, 4, 4, OUT)
c.rect(7, 25, 2, 3, BODYD)
c.rect(7, 25, 1, 3, HIL)
c.set(8,26,EO)

# ---------- Base (rows 28-31) ----------
c.rect(4, 28, 25, 4, OUT)
c.rect(5, 29, 23, 2, BASE)
c.rect(5, 29, 5, 1, EO)
c.rect(21, 29, 6, 1, EO)
c.rect(10, 29, 8, 1, HIL)

finish(c)
