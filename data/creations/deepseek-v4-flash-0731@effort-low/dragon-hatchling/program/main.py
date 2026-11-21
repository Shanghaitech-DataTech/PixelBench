from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64, name="dragon")

OUT   = "#0a2414"
DARK  = "#1e4a26"
MID   = "#2e6b34"
LIGHT = "#3f8a45"
MEM   = "#1f5a2e"
MEML  = "#2f7440"
BELLY = "#f3e6b8"
BELD  = "#d3bd82"
HORN  = "#e9dfc0"
HORND = "#a8914c"
EYE   = "#ffe34a"
EYER  = "#e2761a"
PUPIL = "#2a0f14"
MOUTH = "#5e1016"
TONG  = "#a83234"
TEETH = "#fffaf0"
CLAW  = "#d6c9a4"

# ---------- Tail ----------
c.poly([(28,33),(19,37),(11,41),(6,46),(7,55),(13,52),(22,47),(30,42),(32,38)], MID)
# tail spikes (horn edges on outer side)
c.line(11,41,10,37,HORN).line(10,37,13,40,HORN)
c.line(8,45,7,41,HORN).line(7,41,10,44,HORN)
c.line(6,50,5,46,HORN).line(5,46,8,49,HORN)
# tail tip
c.circle(7,53,2,HORN)

# ---------- Wings ----------
c.poly([(24,27),(4,8),(0,23),(3,40),(14,47),(25,47),(30,37),(29,29)], MEM)
c.poly([(40,27),(60,8),(63,23),(61,40),(50,47),(39,47),(34,37),(35,29)], MEM)
# finger bones
c.line(26,32,7,11,DARK).line(26,32,7,26,DARK).line(25,36,16,45,DARK)
c.line(38,32,57,11,DARK).line(38,32,57,26,DARK).line(39,36,48,45,DARK)
# membrane sheen
c.circle(7,20,2,MEML).circle(57,20,2,MEML)
c.circle(5,13,1,MEML).circle(59,13,1,MEML)
c.circle(12,43,1,MEML).circle(52,43,1,MEML)

# ---------- Legs ----------
c.ellipse(21,45,5,4,DARK).ellipse(43,45,5,4,DARK)
for cx in (21,43):
    for tx in (cx-2,cx,cx+2):
        c.line(tx,48,tx+(1 if cx==21 else -1),52,CLAW)

# ---------- Body ----------
c.ellipse(32,31,13,11,MID)
# scale rows
for (sx,sy) in [(27,28),(36,28),(24,32),(40,32),(31,35),(29,27),(35,27)]:
    c.set(sx,sy,LIGHT); c.set(sx+1,sy,LIGHT)
# belly
c.ellipse(32,33,7,8,BELLY)
c.ellipse(32,32,4,2,BELD)
# arm nubs
c.circle(19,38,3,MID).circle(45,38,3,MID)

# ---------- Head ----------
c.ellipse(32,14,13,10,MID)
# brow scutes
c.poly([(22,8),(27,5),(32,7)],DARK).poly([(42,8),(37,5),(32,7)],DARK)
# horns
c.poly([(27,6),(23,0),(31,5)],HORN).poly([(37,6),(41,0),(33,5)],HORN)
c.poly([(25,1),(22,0),(27,3)],HORND).poly([(39,1),(42,0),(37,3)],HORND)
# nostrils
c.set(28,18,DARK); c.set(36,18,DARK)

# eyes
c.circle(25,11,3,EYE).circle(39,11,3,EYE)
c.circle(24,11,1,EYER).circle(40,11,1,EYER)
c.set(25,11,PUPIL); c.set(24,11,PUPIL)
c.set(39,11,PUPIL); c.set(40,11,PUPIL)
c.line(21,7,28,9,OUT).line(43,7,36,9,OUT)

# ---------- open mouth ----------
c.ellipse(32,24,7,5,MOUTH)
c.ellipse(32,26,4,2,TONG)
# upper teeth
for tx in (27,31,35,39):
    c.poly([(tx,20),(tx+1,20),(tx+3,23),(tx,22)],TEETH)
# lower teeth
for tx in (29,33,37):
    c.poly([(tx,25),(tx+1,25),(tx+3,22),(tx,23)],TEETH)

# cheek scales
for (sx,sy) in [(20,16),(44,16),(20,20),(44,20)]:
    c.set(sx,sy,LIGHT)

c.outline(OUT)
print(c.stats_text())
finish(c)
