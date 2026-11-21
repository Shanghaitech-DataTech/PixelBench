from pixelbench_api import *

# 64x64 RPG enemy: young western dragon hatchling, facing left, growling
c = new_canvas(64, 64, background=None, name="dragon")

OUT   = "#1d2f16"  # dark outline
GD    = "#2c6626"  # green dark
GM    = "#4f9c3e"  # green mid
GL    = "#82c95f"  # green light
BL    = "#f2e6bb"  # belly light
BS    = "#d3bd85"  # belly shade
MEM   = "#c9763f"  # wing membrane
MEMD  = "#9d5228"  # membrane dark
MEML  = "#e89a5f"  # membrane light
HORN  = "#efe4c8"
HORND = "#c3ac7d"
EYE   = "#f6b93c"
PUP   = "#191410"
MTH   = "#5b2030"
TNG   = "#a8434f"
TTH   = "#f7f2e2"

# ---------------- tail (behind body) ----------------
c.poly([(43,40),(50,42),(55,46),(60,51),(62,55),(58,57),(51,54),(44,52),(37,46)], GM)
c.line(50,53,57,56, GD)

# ---------------- wing (half-spread, behind body) ----------------
mem = [(32,28),(36,17),(42,9),(49,5),(58,4),
       (54,11),(60,15),
       (53,19),(57,24),
       (50,25),(45,32),
       (38,32)]
c.poly(mem, MEM)
# membrane shading between fingers
c.poly([(46,14),(54,11),(57,14),(52,17)], MEMD)
c.poly([(45,20),(52,19),(54,23),(48,24)], MEMD)
# bones from elbow to fingertips
c.line(42,10,60,15, MEMD)
c.line(42,10,57,24, MEMD)
# leading edge arm (thick)
c.line(32,28,36,17, OUT)
c.line(33,29,37,18, OUT)
c.line(36,17,42,9, OUT)
c.line(37,18,43,10, OUT)
c.line(42,9,58,4, OUT)
c.line(43,10,58,5, OUT)
# trailing scallop edges dark
c.line(58,4,54,11, OUT)
c.line(54,11,60,15, OUT)
c.line(60,15,53,19, OUT)
c.line(53,19,57,24, OUT)
c.line(57,24,50,25, OUT)
c.line(50,25,45,32, OUT)

# ---------------- far legs (darker, behind) ----------------
c.rect(34,46,4,8, GD)
c.rect(46,47,5,8, GD)

# ---------------- body ----------------
c.ellipse(40,36,10,9, GM)
# lower/back shading
c.poly([(36,42),(50,40),(50,45),(38,46)], GD)

# ---------------- neck & head ----------------
c.ellipse(31,27,6,6, GM)                      # neck
c.ellipse(22,19,8,7, GM)                      # skull
c.poly([(14,13),(8,16),(6,19),(8,22),(20,23),(27,21),(27,15)], GM)  # upper snout
c.poly([(8,23),(12,30),(20,31),(26,27),(26,23)], GM)                # lower jaw
# open mouth interior
c.poly([(9,22),(25,22),(24,28),(12,28)], MTH)
# tongue
c.poly([(14,26),(22,26),(21,28),(14,28)], TNG)
# upper teeth (hanging)
for tx in (11,15,19,23):
    c.poly([(tx,22),(tx+2,22),(tx+1,25)], TTH)
# lower teeth (pointing up)
c.poly([(13,28),(15,28),(14,26)], TTH)
c.poly([(18,28),(20,28),(19,26)], TTH)

# brow + eye
c.line(19,12,26,14, GD)
c.set(22,16,EYE); c.set(23,16,EYE)
c.set(22,17,EYE); c.set(23,17,PUP)
# nostril
c.set(9,18,OUT); c.set(10,19,OUT)

# horns (small, swept back, hugging the skull)
c.poly([(23,12),(27,5),(28,13)], HORN)
c.poly([(27,13),(32,8),(31,16)], HORN)
c.line(24,12,27,12, HORND)
c.line(28,14,30,15, HORND)

# ---------------- belly ----------------
c.poly([(26,26),(33,30),(36,37),(36,45),(41,47),(45,43),(45,35),(41,29),(33,25)], BL)
c.line(33,33,42,33, BS)
c.line(34,38,44,38, BS)
c.line(34,43,43,43, BS)

# ---------------- near legs ----------------
# front leg
c.ellipse(30,44,4,5, GM)
c.rect(28,46,4,8, GM)
c.rect(25,54,8,3, GM)
# hind leg
c.ellipse(44,45,6,6, GM)
c.rect(42,49,5,6, GM)
c.rect(39,54,10,3, GM)
# leg shading
c.line(31,48,31,53, GD)
c.line(47,50,47,53, GD)

# ---------------- back & tail spikes ----------------
for sx,sy in [(29,20),(33,23)]:
    c.poly([(sx,sy),(sx+2,sy-4),(sx+4,sy)], HORN)
    c.set(sx+2,sy-1,HORND)
for sx,sy in [(49,41),(54,46),(58,50)]:
    c.poly([(sx,sy),(sx+2,sy-4),(sx+4,sy)], HORN)
# spade tip on tail (kept inside canvas)
c.poly([(60,49),(63,52),(59,53)], GD)

# ---------------- highlights ----------------
c.line(8,17,15,14, GL)          # snout ridge
c.line(17,12,24,12, GL)         # head top
c.set(33,28,GL); c.set(34,28,GL); c.set(35,29,GL)  # shoulder
c.set(42,42,GL); c.set(43,42,GL)  # thigh top
c.line(45,7,54,5, MEML)         # wing leading light

# ---------------- outline pass ----------------
c.outline(OUT)

# ---------------- claws (after outline, stay bright) ----------------
for fy in (54,55,56):
    c.set(23,fy,TTH); c.set(24,fy,TTH)
    c.set(37,fy,TTH); c.set(38,fy,TTH)

view(c)
finish(c)
