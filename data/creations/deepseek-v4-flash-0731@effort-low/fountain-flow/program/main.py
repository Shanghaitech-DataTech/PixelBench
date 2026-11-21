from pixelbench_api import *

out = input_canvas.copy(name='output')

# ---- 1. Top water spray plume bursting from the nozzle (rows 0-8) ----
for row in range(0, 9):
    for x in range(31, 35):
        out.set(x, row, 7)          # light-blue jet core
out.rect(27, 1, 11, 1, 7)            # expanding spray fan
out.rect(24, 2, 17, 1, 7)
out.rect(22, 3, 21, 1, 7)
out.rect(20, 4, 25, 1, 7)
out.rect(19, 5, 27, 1, 7)
for x in (20, 21, 44): out.set(x, 4, 6)      # darker blue spray edges
out.set(18, 3, 6); out.set(47, 3, 6)
out.set(19, 6, 6); out.set(46, 6, 6)
out.set(17, 2, 6); out.set(48, 2, 6)
for (fx, fy) in [(30,0),(35,0),(27,1),(38,1),(25,2),(40,2),(28,3),(37,3)]:
    out.set(fx, fy, 4)               # white foam at plume top

# upper-bowl water highlights / overflow droplets
for (x,y) in [(15,10),(13,12),(48,10),(50,12),(12,15),(17,17),(46,15),(49,17)]:
    out.set(x, y, 6)
for (x,y) in [(16,11),(47,11),(15,16),(48,16),(20,25),(45,25),(19,29),(46,29)]:
    out.set(x, y, 7)
# flowing water streaks across upper bowl interior
for row in (14, 18, 21, 25, 29):
    for x in range(18, 46):
        if (x + row) % 3 != 0:
            out.set(x, row, 7)
for (x,y) in [(22,24),(43,24),(21,28),(44,28)]:
    out.set(x, y, 4)

# ---- 2. Cascades running down both sides into the lower basin ----
for row in range(30, 45):
    out.set(9, row, 7); out.set(10, row, 7)    # left cascade
    out.set(54, row, 7); out.set(53, row, 7)   # right cascade
out.set(8,39,6);out.set(9,40,6);out.set(10,41,6);out.set(9,42,6);out.set(8,43,6)
out.set(55,39,6);out.set(54,40,6);out.set(53,41,6);out.set(54,42,6);out.set(55,43,6)

# ---- 3. Splash foam where cascades land + bubbling lower basin ----
for (x,y) in [(6,40),(7,41),(8,42),(6,43),(12,41),(12,44),(11,38),
              (57,40),(56,41),(55,42),(57,43),(51,41),(51,44),(52,38)]:
    out.set(x, y, 4)
for (x,y) in [(28,44),(31,46),(35,45),(29,48),(33,47),(36,49),(30,50),(24,46),(40,46)]:
    out.set(x, y, 4)

print(out.stats_text())
finish(out)
