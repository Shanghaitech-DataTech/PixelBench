from pixelbench_api import *

c = new_canvas(32, 32, name="steamer")

BAM = '#c08a45'      # body bamboo
BAM_MID = '#9c6b2e'
BAM_DARK = '#7a5222'
BAM_LIGHT = '#d9a962'
BAM_TOP = '#b07d3a'
INNER = '#6b4a1e'     # interior shadow
WRAP = '#f5ead0'      # dumpling wrapper
SH1 = '#e0d0aa'
SH2 = '#d6c49a'
STEAM = '#ffffff'

# --- basket body ---
c.rect(4, 20, 25, 8, BAM)          # x4..28, y20..27
c.line(4, 20, 4, 27, BAM_DARK)
c.line(28, 20, 28, 27, BAM_DARK)
for yy in (22, 24, 26):
    c.line(5, yy, 27, yy, BAM_MID)

# interior dark strip behind dumplings
c.rect(5, 18, 23, 2, INNER)        # y18..19

# --- dumplings (3, clearly shaped, on left-open side) ---
def dumpling(cx):
    c.ellipse(cx, 14, 2, 3, WRAP)      # rounded body, rows 11..17
    c.line(cx - 2, 15, cx + 2, 15, SH1)
    c.line(cx - 2, 16, cx + 2, 16, SH2)
    # crimped top
    c.line(cx - 2, 11, cx, 12, SH1)
    c.line(cx + 2, 11, cx, 12, SH1)
    c.set(cx, 10, WRAP)
    # dark crease between folds
    c.set(cx, 14, SH1)

dumpling(7)
dumpling(13)
dumpling(19)

# front rim band
c.rect(4, 19, 25, 2, BAM_DARK)     # y19..20
c.rect(4, 19, 25, 1, BAM_TOP)

# --- lid (partially open, tilted onto right side) ---
c.ellipse(26, 13, 5, 6, BAM_LIGHT) # rows 7..19, x21..29
c.line(21, 11, 21, 18, BAM_MID)
c.line(22, 18, 28, 18, BAM_MID)
# lid top highlight
c.line(23, 8, 29, 8, BAM_TOP)
# handle
c.rect(25, 4, 3, 3, BAM_TOP)
c.rect(25, 3, 3, 1, BAM_LIGHT)

# --- steam (small rising puffs) ---
for (sx, sy) in [(7, 9), (9, 7), (8, 5), (11, 6), (13, 9), (6, 11), (10, 8), (6, 4)]:
    c.set(sx, sy, STEAM)

print(c.stats_text())
print(c.matrix_text())
finish(c)
