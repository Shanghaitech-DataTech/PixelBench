# Let's write an interactive generator script in draft_pear.py
# that we can run and view to get the shape and shading absolutely gorgeous.

grid = [
#01234567890123456789012345678901
"................................", # 0
"................................", # 1
".................BBBB...........", # 2  stem tip
"................BTTB............", # 3  stem
"...............BTTB...DDDDD.....", # 4  stem & leaf top
"..............BTB...DDLLLLLD....", # 5  leaf
".............BTB...DLLLLHLLD....", # 6  leaf with highlight
"...........DDBBD..DDLLLLLLMD....", # 7  stem into pear dip, leaf base
"..........DMMMMMMSDDDDDDMDD.....", # 8  pear neck & leaf tip
".........DMLLLLLMMMMSDD.........", # 9  pear neck
"........DMLLLLLLLLMMMSD.........", # 10 pear neck
"........DMHLLLLLLLLLMMSD........", # 11 pear neck
".......DMHHLLLLLLLLLLMMSD.......", # 12 pear waist
".......DMHHLLLLLLLLLLLMMSD......", # 13
"......DMLLHLLLLLLLLLLLLMMSD.....", # 14 expanding
".....DMLLLLLLLLLLLLLLLLLMMSD....", # 15
"....DMLLLLLLLLLLLLLLLLLLLMMSD...", # 16 belly
"...DMLLLLLLLLLLLLLLLLLLLLLMSD...", # 17 belly
"...DMLLLLLLLLLLLLLLLLLLLLLMMSD..", # 18
"..DMLLLLLLLLLLLLLLLLLLLLLLLMMSD.", # 19
"..DMLLLLLLLLLLLLLLLLMMMMMMMMMSD.", # 20
"..DMMLLLLLLLLLLLLMMMMMMSSSSSMMSD", # 21
"..DMMMLLLLLLLLMMMMMMMSSSSSSSSMDD", # 22
"...DMMMMMMLLMMMMMMMSSSSSSSSSSMD.", # 23
"...DMMMMMMMMMMMMMSSSSSSSSSSSSMD.", # 24
"....DMMMMMMMMMMMSSSSSSSSSSSSMD..", # 25
".....DMMMMMMMMMSSSSSSSSSSSSMD...", # 26
"......DDMMMMMMSSSSSSSSSSSMDD....", # 27
"........DDMMMMSSSSSSSSMMDD......", # 28
"..........DDDDDDDDDDDD..........", # 29
"................................", # 30
"................................", # 31
]

print("Rows:", len(grid))
for r in grid:
    assert len(r) == 32
