from pixelbench_api import *

# --- colors (shared palette from input) ---
RUST  = (0x6c, 0x51, 0x3a)   # a
BRN   = (0x97, 0x76, 0x3d)   # b
WALL  = (0xbd, 0xa7, 0x59)   # c
DARK  = (0x16, 0x1c, 0x2e)   # d
DBRN  = (0x98, 0x69, 0x4e)   # e
GOLD  = (0xdc, 0xaa, 0x46)   # f
YEL   = (0xf9, 0xe2, 0x79)   # g
HYEL  = (0xe1, 0xd9, 0x68)   # h
PALE  = (0xbb, 0xae, 0x93)   # i
PYEL  = (0xe1, 0xdc, 0xa3)   # j
SHAD  = (0x16, 0x1c, 0x2e, 0x45)  # k (transparent shadow)

f1 = input_canvas.copy(name="frame1")

# ============ Frame 2: 90-degree view (right wall + window) ============
W, H = 112, 157
f2 = new_canvas(W, H, name="frame2")

# --- roof band above the wall (high-angle: modest roof above eave) ---
# roof slope plane, receding: dark base with diagonal b/a streaks
f2.rect(0, 0, W, 34, DARK)
# diagonal shingle streaks (receding roof, like input's right slope)
for yy in range(4, 34):
    f2.line(20 - yy, yy, 92 - yy, yy, BRN)
for yy in range(4, 34):
    f2.line(34 - yy, yy, 78 - yy, yy, RUST)
for yy in range(4, 34):
    f2.line(60 - yy, yy, 104 - yy, yy, BRN)

# eaves trim
f2.rect(0, 34, W, 4, BRN)
f2.rect(0, 38, W, 3, DARK)

# --- right wall face ---
f2.rect(20, 41, 72, 100, DARK)     # wall with dark border
f2.rect(22, 43, 68, 96, WALL)      # wall face
# subtle wall shading columns
f2.rect(22, 43, 3, 96, RUST)
f2.rect(87, 43, 3, 96, RUST)
# upper wall band under eave
f2.rect(25, 45, 62, 4, BRN)
# lower base
f2.rect(25, 131, 62, 5, BRN)
f2.rect(25, 136, 62, 3, DARK)

# --- the right wall's big arched window ---
wx0, wy0 = 38, 56
w_w, w_h = 36, 76   # overall window incl frame
# outer dark frame
f2.rect(wx0, wy0, w_w, w_h, DARK)
# stone frame
f2.rect(wx0+2, wy0+2, w_w-4, w_h-4, BRN)
# glass area
f2.rect(wx0+4, wy0+5, w_w-8, w_h-9, HYEL)   # h glass
# arched top (extra glass above)
for i in range(4):
    f2.rect(wx0+4+i, wy0+2+i, w_w-8-2*i, 2, HYEL)
# pale-yellow highlights (top arch)
f2.rect(wx0+4, wy0+2, w_w-8, 2, PYEL)
# mullions: verticals
mx1, mx2 = wx0+11, wx0+23
f2.rect(mx1, wy0+4, 2, w_h-8, BRN)
f2.rect(mx2, wy0+4, 2, w_h-8, BRN)
# mullions: horizontals
f2.rect(wx0+4, wy0+30, w_w-8, 2, BRN)
f2.rect(wx0+4, wy0+56, w_w-8, 2, BRN)
# inner window shadow under arch
f2.rect(wx0+6, wy0+8, w_w-12, 4, DBRN)
# window sill
f2.rect(wx0-3, wy0+w_h-2, w_w+6, 3, DBRN)
f2.rect(wx0-2, wy0+w_h+1, w_w+4, 2, BRN)

# --- small accents on wall (left + right of window) like the input's style ---
# vertical wall seams
for yy in range(50, 132, 8):
    f2.rect(26, yy, 8, 2, RUST)
    f2.rect(78, yy, 8, 2, RUST)

# --- ground shadow ---
f2.rect(16, 139, 80, 2, SHAD)
f2.rect(12, 141, 88, 10, SHAD)
f2.rect(8, 151, 96, 6, SHAD)

print("frame2 built")
print(f2.stats_text())

finish([f1, f2])
