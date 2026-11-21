# Let's design the pear silhouette and shading carefully.

# Canvas 32x32.
# Stem:
# (15, 1) to (18, 1) top cap
# curves down to (13, 7)
# Leaf:
# attached at stem (14, 4), spreads to (17-23, 2-6)
# Pear body:
# Top dent: centered at x=13, y=7
# Neck:
# y=8:  x=10..16 (width 7)
# y=9:  x=9..17  (width 9)
# y=10: x=9..17  (width 9)
# y=11: x=9..18  (width 10)
# y=12: x=9..18  (width 10)
# y=13: x=8..19  (width 12)
# Waist / expanding:
# y=14: x=8..20  (width 13)
# y=15: x=7..21  (width 15)
# y=16: x=6..22  (width 17)
# y=17: x=6..23  (width 18)
# Bulbous belly:
# y=18: x=5..24  (width 20)
# y=19: x=5..25  (width 21)
# y=20: x=4..25  (width 22)
# y=21: x=4..25  (width 22)
# y=22: x=4..25  (width 22)
# y=23: x=5..25  (width 21)
# y=24: x=5..24  (width 20)
# Round bottom:
# y=25: x=6..23  (width 18)
# y=26: x=7..22  (width 16)
# y=27: x=9..20  (width 12)
# y=28: x=11..18 (width 8)

grid = [
#01234567890123456789012345678901
"................................", # 0
"................BBBB............", # 1  stem top
"..............BBTTB...DDDDD.....", # 2  leaf
".............BBTTB..DDLLLLLD....", # 3  leaf
"............BBTTB..DLLLLLLLLD...", # 4  leaf
"............BTTB...DLLLMMMMMD...", # 5  leaf
"...........BBTB.....DDMMMDDD....", # 6  leaf base
"..........DBBBD.................", # 7  stem in dent
".........DMMMMMMSD..............", # 8  pear neck
"........DMLLLLLMMSD.............", # 9
"........DMLLLLLLMMSD............", # 10
"........DMLLLLLLLMMSD...........", # 11
"........DMHLLLLLLLMMSD..........", # 12
".......DMHHHLLLLLLLMMSD.........", # 13
".......DMHHHLLLLLLLLMMSD........", # 14
"......DMLLHHLLLLLLLLLMMSD.......", # 15
"......DMLLLLLLLLLLLLLLMMSD......", # 16
".....DMLLLLLLLLLLLLLLLLMMSD.....", # 17
".....DMLLLLLLLLLLLLLLLLLMMD.....", # 18
"....DMLLLLLLLLLLLLLLMMMMMMMD....", # 19
"....DMLLLLLLLLLLLMMMMMMMSSMMD...", # 20
"...DMMLLLLLLLLMMMMMMMMSSSSSMD...", # 21
"...DMMMLLLLMMMMMMMMMSSSSSSSSMD..", # 22
"...DMMMMMMMMMMMMMMSSSSSSSSSSMD..", # 23
"....DMMMMMMMMMMMMSSSSSSSSSSSMD..", # 24
"....DMMMMMMMMMMMSSSSSSSSSSSSMD..", # 25
".....DMMMMMMMMMSSSSSSSSSSSSMD...", # 26
"......DMMMMMMMMSSSSSSSSSSSMD....", # 27
".......DDMMMMMMSSSSSSSSSSMD.....", # 28
".........DDMMMMMSSSSSMD.........", # 29
"............DDDDDDDDD...........", # 30
"................................", # 31
]

with open("grid_test.py", "w") as f:
    f.write(f"grid = {grid}\n")
