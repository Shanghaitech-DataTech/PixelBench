# Perfectly symmetrical, beautifully shaded pear with connected leaf

C_DARK = "#1a320f"        # deep outline / crease / shadow rim
C_SHADOW = "#355e16"      # rich shaded green
C_MID = "#6ba525"         # vibrant pear green midtone
C_LIGHT = "#a6dc38"       # bright warm yellow-green
C_SPEC = "#e8fa8e"        # pale creamy yellow-lime highlight
C_STEM_DARK = "#3a2010"   # dark stem brown
C_STEM_LIGHT = "#7d4820"  # light stem brown

color_map = {
    '.': None,
    'D': C_DARK,
    'S': C_SHADOW,
    'M': C_MID,
    'L': C_LIGHT,
    'H': C_SPEC,
    'B': C_STEM_DARK,
    'T': C_STEM_LIGHT,
}

# 32x32 pixel art grid
grid = [
#01234567890123456789012345678901
"................................", # 0
"................................", # 1
"............BBBB................", # 2  stem tip
"...........BTTBB.......DDDDD....", # 3  stem & leaf tip
"..........BTTB.......DDLLLLLD...", # 4  stem & leaf
".........BTTB..DD...DLLLLHLLMD..", # 5  stem connects to leaf!
"........BTB...DMD..DLLLLLLMMD...", # 6  leaf body
".......DBBD..DMD....DDMMMMDD....", # 7  leaf bottom & stem base
"......DMMMDDDMD.......DDDD......", # 8  top indentation of pear
".....DMMLLMMMMMMSD..............", # 9  pear neck
"....DMLLLLMMMMMMMSD.............", # 10 pear neck
"....DMLLLLMMMMMMMSD.............", # 11 pear neck
"....DMHLLLMMMMMMMMSD............", # 12 neck highlight
"...DMHHLLMMMMMMMMMMSD...........", # 13 neck highlight
"...DMLLHLLMMMMMMMMMMSD..........", # 14 waist
"...DMLLLLMMMMMMMMMMMMSD.........", # 15 waist expanding
"..DMLLLLMMMMMMMMMMMMMMSD........", # 16 expanding
"..DMLLLLMMMMMMMMSSSSSSMDD.......", # 17 expanding
".DMLLLLMMMMMMMMSSSSSSSSMDD......", # 18 belly
".DMLLLLMMMMMMMSSSSSSSSSSMD......", # 19 belly
".DMHLLMMMMMMMSSSSSSSSSSSMD......", # 20 belly highlight
".DHHLLMMMMMMSSSSSSSSSSSSMD......", # 21 belly highlight
".DMHLLMMMMMMSSSSSSSSSSSSMD......", # 22
".DMLLLLMMMMMMSSSSSSSSSSSMD......", # 23
"..DMLLLLMMMMMSSSSSSSSSSSMD......", # 24
"..DMLLLLMMMMMSSSSSSSSSSMD.......", # 25
"...DMMLLMMMMMMSSSSSSSSMD........", # 26
"....DMMMMMMMMMSSSSSSSMD.........", # 27
".....DDMMMMMMMMSSSSMDD..........", # 28
".......DDDDMMMMMDDDD............", # 29
"...........DDDDD................", # 30
"................................", # 31
]

# Wait, let's check symmetry!
# In row 20: left is x=1, right is x=25. Center = 13.
# In row 9: left is x=5, right is x=17. Center = 11.
# Notice the center is shifting from 11 at top to 13 at bottom.
# That is a gentle organic lean, but let's make sure it's smooth.
# Let's inspect!
