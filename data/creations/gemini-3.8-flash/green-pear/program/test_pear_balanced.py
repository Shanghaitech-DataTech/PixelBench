# Balanced, classic pear composition

grid = [
#01234567890123456789012345678901
"................................", # 0
"............BBBB................", # 1  stem tip
"...........BTTBB.......DDDDD....", # 2  leaf tip
"..........BTTB.......DDLLLLLD...", # 3  leaf
".........BTTB......DDLLLLHLLD...", # 4  leaf with shine
"........BTB.......DDLLLLLLMDD...", # 5  leaf
".......BTB..DD.....DDLLMMDD.....", # 6  leaf stem / petiole
"......DBBD.DMMD......DDDD.......", # 7  stem in pear dip
".....DMMMMMMMMMMD...............", # 8  pear neck top
"....DMLLLLMMMMMMSD..............", # 9  pear neck
"....DMLLLLMMMMMMSD..............", # 10 pear neck
"...DMLLLLLMMMMMMMSD.............", # 11
"...DMHLLLLMMMMMMMSD.............", # 12 neck highlight
"...DMHHLLLMMMMMMMMSD............", # 13 neck highlight
"..DMLLLLLLMMMMMMMMMSD...........", # 14 waist
"..DMLLLLLLLMMMMMMMMMSD..........", # 15 waist expanding
".DMLLLLLLLLMMMMMMMMMMSD.........", # 16
".DMLLLLLLLLMMMMMMMMMMMSD........", # 17 belly expanding
"DMLLLLLLLLLLMMMMMMMMMMMSD.......", # 18 belly
"DMLLLLLLLLLLMMMMMMMMMMMMSD......", # 19 belly
"DMLLHHLLLLLLMMMMMMMSSMMMMSD.....", # 20 belly highlight
"DMHHHHLLLLLLMMMMMSSSSSSMMMSD....", # 21 belly highlight
"DMHHHHLLLLLLMMMMSSSSSSSSMMMSD...", # 22
"DMLLHHLLLLLLMMMSSSSSSSSSSMMMSD..", # 23
".DMLLLLLLLLLMMMSSSSSSSSSSSMMSD..", # 24
".DMLLLLLLLLLMMSSSSSSSSSSSSSMD...", # 25
"..DMMLLLLLLMMMSSSSSSSSSSSSMD....", # 26
"...DMMMLLLMMMMMSSSSSSSSSSMD.....", # 27
"....DDMMMMMMMMMMSSSSSSSSMD......", # 28
"......DDMMMMMMMMMSSSSMDD........", # 29
"........DDDDDDDDDDDDDD..........", # 30
"................................", # 31
]

print("Grid height:", len(grid))
for y, row in enumerate(grid):
    assert len(row) == 32, f"Row {y} len {len(row)}"
