from pixelbench_api import new_canvas, finish

W, H = 64, 64
c = new_canvas(W, H, name="explosion")  # transparent background

# ---- Colour palette ----
# Frame 1: bright yellow fireball
Y_DIM    = c.color("#FFD200")   # outer fireball
Y_OUTER  = c.color("#FFE600")   # bright mid
Y_CORE   = c.color("#FFF9A0")   # hot core
O_DEEP   = c.color("#FF8A00")   # orange rim accent

# Frame 2: expanding orange-red blast with sparks
R_OUT    = c.color("#FF3A00")   # red outer shock
R_DRK    = c.color("#D61F00")   # dark red mid
O_BLAST  = c.color("#FF9B00")   # orange mid
Y_HOT    = c.color("#FFD21E")   # hot yellow center
SPK_A    = c.color("#FFE24A")   # bright spark
SPK_B    = c.color("#FF7A1E")   # orange spark
SPK_C    = c.color("#FFF6C8")   # white spark

# ---------------- Frame 1 : bright yellow fireball (left half) ----------------
fx, fy = 16, 32
c.ellipse(fx, fy, 9, 7, Y_DIM, fill=True)          # outer blob
c.ellipse(fx, fy, 7, 5, Y_OUTER, fill=True)        # bright mid
c.ellipse(fx, fy - 1, 5, 3, Y_CORE, fill=True)     # hot core
# accent flames licking outward
c.ellipse(fx - 6, fy, 2, 3, O_DEEP, fill=True)
c.ellipse(fx + 6, fy + 1, 2, 3, O_DEEP, fill=True)

# ---------------- Frame 2 : expanding orange-red blast (right half) -----------
bx, by = 48, 32
c.circle(bx, by, 11, R_OUT, fill=True)                     # red shock front
c.circle(bx, by, 8, R_DRK, fill=True)                      # dark red mid
c.circle(bx, by, 5, O_BLAST, fill=True)                    # orange mid
c.circle(bx, by, 3, Y_HOT, fill=True)                      # hot yellow center
c.circle(bx, by - 1, 2, SPK_C, fill=True)                  # blazing core

# lobe puffs (peripheral, still within right half)
c.circle(bx - 11, by - 3, 3, R_OUT, fill=True)
c.circle(bx + 11, by + 2, 3, R_OUT, fill=True)
c.circle(bx - 2, by - 11, 3, R_DRK, fill=True)
c.circle(bx + 3, by + 11, 3, R_DRK, fill=True)

# sparks scattered around the blast (within right half 32..63)
sparks = [
    (34, 18, SPK_A), (46, 16, SPK_B), (59, 22, SPK_A),
    (62, 32, SPK_C), (60, 44, SPK_A), (44, 50, SPK_B),
    (33, 46, SPK_A), (36, 26, SPK_C), (56, 28, SPK_B),
    (52, 52, SPK_A), (40, 20, SPK_C), (58, 38, SPK_B),
]
for sx, sy, sc in sparks:
    c.set(sx, sy, sc)

print(c.stats_text())
finish(c)
