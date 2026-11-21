from pixelbench_api import *

# rebuild frames exactly as in the real program
RUST  = (0x6c, 0x51, 0x3a)
BRN   = (0x97, 0x76, 0x3d)
WALL  = (0xbd, 0xa7, 0x59)
DARK  = (0x16, 0x1c, 0x2e)
DBRN  = (0x98, 0x69, 0x4e)
GOLD  = (0xdc, 0xaa, 0x46)
YEL   = (0xf9, 0xe2, 0x79)
HYEL  = (0xe1, 0xd9, 0x68)
PALE  = (0xbb, 0xae, 0x93)
PYEL  = (0xe1, 0xdc, 0xa3)
SHAD  = (0x16, 0x1c, 0x2e, 0x45)

f2 = new_canvas(112, 157, name="frame2")

f2.rect(0, 0, 112, 34, DARK)
for yy in range(4, 34):
    f2.line(20 - yy, yy, 92 - yy, yy, BRN)
for yy in range(4, 34):
    f2.line(34 - yy, yy, 78 - yy, yy, RUST)
for yy in range(4, 34):
    f2.line(60 - yy, yy, 104 - yy, yy, BRN)
f2.rect(0, 34, 112, 4, BRN)
f2.rect(0, 38, 112, 3, DARK)
f2.rect(20, 41, 72, 100, DARK)
f2.rect(22, 43, 68, 96, WALL)
f2.rect(22, 43, 3, 96, RUST)
f2.rect(87, 43, 3, 96, RUST)
f2.rect(25, 45, 62, 4, BRN)
f2.rect(25, 131, 62, 5, BRN)
f2.rect(25, 136, 62, 3, DARK)
wx0, wy0 = 38, 56
w_w, w_h = 36, 76
f2.rect(wx0, wy0, w_w, w_h, DARK)
f2.rect(wx0+2, wy0+2, w_w-4, w_h-4, BRN)
f2.rect(wx0+4, wy0+5, w_w-8, w_h-9, HYEL)
for i in range(4):
    f2.rect(wx0+4+i, wy0+2+i, w_w-8-2*i, 2, HYEL)
f2.rect(wx0+4, wy0+2, w_w-8, 2, PYEL)
mx1, mx2 = wx0+11, wx0+23
f2.rect(mx1, wy0+4, 2, w_h-8, BRN)
f2.rect(mx2, wy0+4, 2, w_h-8, BRN)
f2.rect(wx0+4, wy0+30, w_w-8, 2, BRN)
f2.rect(wx0+4, wy0+56, w_w-8, 2, BRN)
f2.rect(wx0+6, wy0+8, w_w-12, 4, DBRN)
f2.rect(wx0-3, wy0+w_h-2, w_w+6, 3, DBRN)
f2.rect(wx0-2, wy0+w_h+1, w_w+4, 2, BRN)
for yy in range(50, 132, 8):
    f2.rect(26, yy, 8, 2, RUST)
    f2.rect(78, yy, 8, 2, RUST)
f2.rect(16, 139, 80, 2, SHAD)
f2.rect(12, 141, 88, 10, SHAD)
f2.rect(8, 151, 96, 6, SHAD)

print(f2.matrix_text(region=(0, 0, 111, 156), indices=False))
