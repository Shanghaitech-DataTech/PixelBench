from pixelbench_api import *

W = 128
H = 128
c = new_canvas(W, H, name="castle_title")

# ---------------- sky gradient (top -> horizon) ----------------
SKY = [
    "#241150", "#34155f", "#4a1a6e", "#662270", "#873073", "#a83d6e",
    "#c85062", "#e06456", "#f07c40", "#f89a38", "#ffbc47", "#ffd97a",
]
for y in range(0, 84):
    idx = min(len(SKY) - 1, int(y * len(SKY) / 84))
    c.rect(0, y, W, 1, SKY[idx])

# birds
def bird(px, py):
    c.set(px, py, "#2a1240")
    c.set(px + 2, py - 1, "#2a1240")
    c.set(px + 4, py, "#2a1240")

bird(26, 30); bird(34, 25); bird(42, 30)
bird(84, 20); bird(91, 16); bird(98, 20)

# ---------------- layered clouds (upper) ----------------
def cloud_band(pts, col, hi=None):
    for (x, y, rx) in pts:
        c.ellipse(x, y, rx, 3, col)
        if hi is not None:
            c.ellipse(x, y - 1, max(2, rx - 2), 1, hi)

cloud_band([(10, 14, 10), (30, 13, 16), (52, 14, 20), (78, 12, 18), (100, 13, 16), (117, 14, 9)],
           "#5a2070", "#7a2a78")
cloud_band([(16, 30, 16), (40, 28, 18), (62, 30, 20), (86, 29, 16), (110, 31, 14)],
           "#7a2a78", "#a83d6e")

# ---------------- large orange sun ----------------
c.circle(64, 58, 21, "#e06456")
c.circle(64, 58, 17, "#f07c40")
c.circle(64, 58, 14, "#ff9a38")
c.circle(64, 58, 11, "#ffc04d")
c.circle(64, 58, 8, "#ffd97a")

# ---------------- lower cloud bank over the sun ----------------
cloud_band([(14, 74, 16), (38, 72, 18), (62, 73, 17), (86, 71, 18), (110, 73, 16), (119, 74, 8)],
           "#c85062", "#e06456")

# ---------------- sea ----------------
SEA = ["#3a1a4e", "#331648", "#2b1240", "#241038", "#1e0c30"]
for y in range(84, 116):
    idx = min(len(SEA) - 1, int((y - 84) * len(SEA) / (116 - 84)))
    c.rect(0, y, W, 1, SEA[idx])

c.rect(0, 84, W, 1, "#d85a50")          # bright horizon line
c.rect(30, 86, 68, 2, "#c85062")       # horizon glow wash

# sun reflection shimmer
c.rect(50, 88, 28, 3, "#ff9a38")
for y in range(92, 115):
    half = max(2, 15 - int((y - 92) * 0.35))
    if y % 4 == 0:
        c.rect(64 - half, y, half * 2, 1, "#ffd97a")
    elif y % 4 == 2:
        c.rect(64 - half, y, half * 2, 1, "#f89a38")

# water ripples
for (wx, wy) in [(8, 92), (24, 98), (40, 104), (18, 110), (44, 96), (30, 112),
                 (12, 100), (82, 94), (110, 100), (96, 108), (80, 96), (112, 104),
                 (70, 112), (100, 114)]:
    c.rect(wx, wy, 5, 1, "#4a2a5a")
for (gx, gy) in [(68, 92), (60, 98), (72, 104), (56, 110), (64, 112)]:
    c.rect(gx, gy, 3, 1, "#ffbc47")

# ---------------- cliff (right) ----------------
CLIFF = "#150a26"
c.poly([(66, 98), (74, 90), (82, 84), (92, 82), (104, 80), (118, 82), (127, 86),
        (127, 127), (66, 127)], CLIFF)
# rim light along cliff edge
c.line(66, 98, 74, 90, "#4a2a5a")
c.line(74, 90, 82, 84, "#7a3a5a")
c.line(82, 84, 104, 80, "#a83d6e")
c.line(104, 80, 118, 82, "#7a3a5a")
c.line(118, 82, 127, 86, "#4a2a5a")
c.set(88, 83, "#ff9a38"); c.set(96, 81, "#ff9a38"); c.set(104, 80, "#ff9a38")

# ---------------- castle ----------------
WALL = "#2b1240"
DARK = "#1e0c30"

# keep
c.rect(94, 46, 20, 33, WALL)
c.poly([(94, 46), (104, 35), (114, 46)], DARK)
# connecting wall on the cliff
c.rect(70, 74, 26, 5, WALL)
# left tower
c.rect(84, 40, 14, 35, WALL)
c.poly([(84, 40), (91, 25), (98, 40)], DARK)
c.line(84, 40, 91, 25, "#4a2a5a")
# right tower
c.rect(106, 42, 14, 33, WALL)
c.poly([(106, 42), (113, 27), (120, 42)], DARK)
c.line(106, 42, 113, 27, "#4a2a5a")

# flags
c.line(91, 16, 91, 25, DARK)
c.poly([(91, 16), (91, 24), (101, 20)], "#e0443c")
c.poly([(91, 17), (91, 21), (97, 19)], "#ff6a5a")
c.line(113, 18, 113, 27, DARK)
c.poly([(113, 18), (113, 26), (123, 22)], "#e0443c")
c.poly([(113, 19), (113, 23), (119, 21)], "#ff6a5a")

# lit windows
c.rect(98, 54, 4, 6, "#ff9a38"); c.rect(99, 55, 2, 4, "#ffd97a")
c.rect(104, 52, 4, 6, "#ff9a38"); c.rect(105, 53, 2, 4, "#ffd97a")
c.rect(110, 54, 4, 6, "#ff9a38"); c.rect(111, 55, 2, 4, "#ffd97a")
c.rect(89, 52, 3, 5, "#ff9a38")
c.rect(112, 54, 3, 5, "#ff9a38")
c.rect(102, 66, 4, 13, DARK)  # gate

# ---------------- dark foreground rocks ----------------
c.poly([(0, 127), (0, 110), (12, 102), (26, 108), (40, 116), (54, 126), (54, 127)], "#0d0718")
c.poly([(64, 127), (78, 119), (94, 114), (110, 117), (122, 122), (127, 125), (127, 127)], "#0d0718")
# rim highlights on the rocks
c.line(0, 109, 26, 107, "#241038")
c.line(78, 117, 110, 115, "#241038")
c.set(12, 101, "#7a3a5a"); c.set(94, 113, "#7a3a5a")

# ---------------- report ----------------
print(c.stats_text())
save("castle_title", c)
finish(c)
