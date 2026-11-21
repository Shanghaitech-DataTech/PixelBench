from pixelbench_api import *

PAL = {
    '.': None,               # Transparent

    # Bone tones
    'W': '#faf7ee',          # Bright bone highlight / patella / cranium crest
    'w': '#dcd1b6',          # Ancient cream bone
    'b': '#a59475',          # Bone midtone
    's': '#6e5d44',          # Bone shadow
    'S': '#453826',          # Bone deep shadow
    'J': '#22150e',          # Dark joint shading / cartilage / deep cavity
    'D': '#0c0503',          # Deepest outline / abyss / pitch black

    # Glowing eye
    'e': '#ff2222',          # Glowing red eye ember

    # Shield - Weathered Wood
    'y': '#c57a36',          # Wood highlight
    'x': '#8f4f20',          # Wood midtone
    'u': '#5c2d0f',          # Wood shadow
    'U': '#2a1104',          # Wood plank seam

    # Metal - Iron / Steel (Shield rim/boss & Short sword)
    'H': '#f0f5fa',          # Steel gleam / highlight
    'm': '#a3b7ce',          # Steel light
    'i': '#62748c',          # Steel midtone
    'I': '#384352',          # Steel shadow
    'k': '#171d24',          # Steel dark outline

    # Bronze / Brass (Sword crossguard & pommel)
    'G': '#dbaa3e',          # Bronze highlight
    'g': '#946e22',          # Bronze midtone
    'q': '#47330d',          # Bronze shadow

    # Rags / Tattered loincloth
    'r': '#822f39',          # Cloth light
    'R': '#501920',          # Cloth midtone
    'p': '#24070c',          # Cloth deep shadow
}

GRID = [
#01234567890123456789012345678901
"................................", # 0
"................................", # 1
"................................", # 2
"................................", # 3
"................................", # 4
"............DDDDD...............", # 5  Top of skull dome
"...........DWwwwbDD.........k...", # 6  Cranium & short sword tip (28,6)
"..........DWwwWwwsbD.......kHk..", # 7  Cranium highlight & blade edge
"..........DwwbwswssD......kHmk..", # 8  Brow ridge & blade
"..........DebDDbDsDD.....kHmk...", # 9  Glowing red eye (col 10), nose bridge, right socket
"..........DwbDwDwbsD....kHmk....", # 10 Cheekbone (col 11), nasal hole (col 12), blade
"..........DDwbwbwsD...kkHmk.....", # 11 Upper teeth & jaw, blade & guard tip
".....kkk...DDDwbDD...kGGqkk.....", # 12 Chin & hunched neck, sword crossguard
"....kmmk....DbJssbDD.kGqWqk.....", # 13 Left shoulder, hunched spine, grip & bony fingers
"...kmyuyik..DwDJJsbDD.kgqk......", # 14 Shield rim, left arm, ribs, bronze pommel
"..kmyxUxuik.DJwDJsbDJbD.........", # 15 Shield planks, elbow, ribs, right elbow
".kmyxiHmxukDDwDJssDDJsbD........", # 16 Shield iron boss, ribs & spine, right elbow joint
".kmyxmHixukDDJDJbDD..DDD........", # 17 Shield iron boss (gleam), bottom ribs
".kmyxIiIxukD.DJssJD.............", # 18 Shield iron boss bottom, spine to pelvis
"..kmyuuik..DbRRRbD..............", # 19 Shield bottom, pelvis & loincloth
"...kmmk...DJpRRRpD..............", # 20 Shield rim, tattered loincloth
"....kk...DWJDppDJwD.............", # 21 Pelvis crest, dark hip joints!
"........DWwD....DwJD............", # 22 Left femur forward, right femur back
".......DWwD......DwJD...........", # 23 Femurs reaching to knees
".......DWJD......DWJD...........", # 24 Left knee juts out (W/J), Right knee bent (W/J)
".......DwJD......DwJD...........", # 25 Left shin drops (w/J), Right shin drops (w/J)
".......DwJD......DwJD...........", # 26 Tibia bones
"......DJwJD......DJwJD..........", # 27 Ankle joints with dark shading
".....DwWbD........DbWwD.........", # 28 Skeletal clawed feet
".....D.DDD........DD.DD.........", # 29 Ground contact with distinct toes
"................................", # 30
"................................", # 31
]

c = new_canvas(32, 32)
for y, row in enumerate(GRID):
    for x, ch in enumerate(row):
        col = PAL.get(ch)
        if col:
            c.set(x, y, col)

print("Canvas stats:", c.stats())
finish(c)
