# swordsman-walk-animation: 64x32 sheet, two 32x32 frames, side view facing right
# Red-haired swordsman, long sword, dark blue cape, 16-bit RPG style.

PAL = {
    'O': '#1a1420',  # outline
    'R': '#d84a30',  # hair red
    'r': '#ff8a5a',  # hair highlight
    'S': '#f2c49a',  # skin
    'E': '#182028',  # eye
    'C': '#24418f',  # cape dark blue
    'c': '#3a63bd',  # cape highlight
    'A': '#8a5a34',  # leather tunic
    'a': '#5f3a1e',  # belt
    'P': '#3d4452',  # trousers
    'B': '#3a2414',  # boots
    'H': '#e8b84a',  # hilt gold
    'M': '#d8dce8',  # blade
    'm': '#98a0b8',  # blade shade
}

# Frame 1: contact pose - legs spread in stride, cape trailing
F1 = [
    "........|........|........|........",  # 0
    "........|........|........|........",  # 1
    "........|........|........|........",  # 2
    "........|........|........|........",  # 3
    "........|........|........|........",  # 4
    "........|........|........|........",  # 5
    "........|........|..RR....|........",  # 6  hair spike
    "........|......OR|RRRO....|........",  # 7
    "........|.....ORr|RRRRO...|........",  # 8
    "........|.....ORr|RRSSO...|........",  # 9
    "........|.....ORR|SSESO...|........",  # 10 eye
    "........|.....OR.|SSSSO...|........",  # 11
    "........|......O.|SSSO....|........",  # 12 chin
    "........|........|..SS....|........",  # 13 neck
    "........|...CCCAA|AAAAAO..|........",  # 14 shoulders + cape
    "........|.CCCCCAA|AAAAAASS|O.......",  # 15 arm + hand
    "........|.CCCCCAA|AAAAAASS|O.......",  # 16
    "........|CCcCCCAA|AAAA..HH|HO......",  # 17 sword guard
    "........|CCcCCCAA|AAAA....|.MM.....",  # 18 blade
    "........|CCCCCCAA|AAAA....|.MMM....",  # 19
    "........|CCCCC.aa|aaaa....|..mMM...",  # 20 belt
    "........|.CCCC.AA|AAAA....|...mMM..",  # 21
    "........|......AA|AAAA....|....MMM.",  # 22
    "........|......PP|..PP....|.....MM.",  # 23 thighs + tip
    "........|.....PP.|...PP...|........",  # 24
    "........|....PP..|....PP..|........",  # 25
    "........|...PP...|....PP..|........",  # 26
    "........|...BBB..|.....BB.|........",  # 27 boots
    "........|.BBBB...|.....BBB|........",  # 28
    "........|BBBB....|......BB|BB......",  # 29 feet
    "........|........|........|........",  # 30
    "........|........|........|........",  # 31
]

# Frame 2: passing pose - legs drawn together, back heel lifted, cape bunched
F2 = [
    "........|........|........|........",  # 0
    "........|........|........|........",  # 1
    "........|........|........|........",  # 2
    "........|........|........|........",  # 3
    "........|........|........|........",  # 4
    "........|........|........|........",  # 5
    "........|........|........|........",  # 6  (head dips 1px)
    "........|........|..RR....|........",  # 7
    "........|......OR|RRRO....|........",  # 8
    "........|.....ORr|RRRRO...|........",  # 9
    "........|.....ORr|RRSSO...|........",  # 10
    "........|.....ORR|SSESO...|........",  # 11
    "........|.....OR.|SSSSO...|........",  # 12
    "........|......O.|SSSO....|........",  # 13
    "........|...CCCAA|AAAAO...|........",  # 14 shoulders + neck
    "........|..CCCCAA|AAAAAASS|O.......",  # 15
    "........|.CCCCCAA|AAAAAASS|O.......",  # 16
    "........|..CcCCCAA|AAAA.HH|HO......",  # 17
    "........|CCcCCCAA|AAAA....|.MM.....",  # 18
    "........|CCCCC.aa|aaaa....|.MMM....",  # 19
    "........|CCCCC.AA|AAAA....|..mMM...",  # 20
    "........|.CCCC.AA|AAAA....|...mMM..",  # 21
    "........|..CCC.AA|AAAA....|....MMM.",  # 22
    "........|.......P|P.PP....|........",  # 23 thighs together
    "........|......PP|...PP...|........",  # 24
    "........|.....PP.|...PP...|........",  # 25
    "........|....BBB.|...PP...|........",  # 26 back heel lifts
    "........|...BBB..|...BBB..|........",  # 27
    "........|..BBBB..|...BBBB.|........",  # 28
    "........|...BBB..|....BBBB|........",  # 29
    "........|........|........|........",  # 30
    "........|........|........|........",  # 31
]


def draw(frame_map, name):
    cv = new_canvas(32, 32, name=name)
    for y, row in enumerate(frame_map):
        row = row.replace('|', '')
        assert len(row) == 32, (name, y, len(row))
        for x, ch in enumerate(row):
            if ch != '.':
                cv.set(x, y, PAL[ch])
    return cv


f1 = draw(F1, 'walk_frame1')
f2 = draw(F2, 'walk_frame2')

result = new_canvas(64, 32, name='swordsman-walk')
result.blit(f1, 0, 0)
result.blit(f2, 32, 0)

print(result.stats_text())
print('--- frame 1 ---')
print(f1.matrix_text())
print('--- frame 2 ---')
print(f2.matrix_text())

finish(result)
