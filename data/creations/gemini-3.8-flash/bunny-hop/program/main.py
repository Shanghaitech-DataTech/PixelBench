W, H = 38, 28

f1 = new_canvas(W, H, name="frame1")
f1.blit(input_canvas, 2, 0)

f2 = new_canvas(W, H, name="frame2")

# Palette indices matching input_canvas:
# a = 1 (#3a3737ff) dark outline / eye
# b = 2 (#b7b3b2ff) light grey shadow
# c = 3 (#827c7cff) medium grey shadow
# d = 4 (#efe9e7ff) white fur
# e = 5 (#d6b39dff) peach inner ear
# f = 6 (#bc8b6dff) dark peach ear shadow
# g = 7 (#cdae67ff) yellow nose

f2_art = [
#01234567890123456789012345678901234567
"......................................", # 0
"......................................", # 1
"....................aaa...............", # 2  far ear tip
"..................aaddba.aaa..........", # 3  far ear + near ear tip
"................aadeedbaaddda.........", # 4  near ear + far ear
"...............adeeedbaaddddda........", # 5  near ear + top of head
"..............afeedcbddddddddba.......", # 6  near ear + forehead
".............aafeecdddadbbddddba......", # 7  ear base + eye top
"............aaddfcdddddaaddddddba.....", # 8  eye bottom + muzzle
"...........aaddddddddddddddddddddba...", # 9  back of neck + cheek
".....aaa..aadddddddddddddddddddddagga.", # 10 tail + back + nose
"....aaddbaaddddddddddddddddddddddddca.", # 11 tail + back + chin
"...aaddddbaaddddddddddddddddddddddcba.", # 12 tail + back + throat
"...aaddddbaaddddddddddddddddddddddba..", # 13 rump + chest
"....aaaddbddddddddddddddddddddddcba...", # 14 hip + chest
".....aaddcddddddddcbbbddddddddddba....", # 15 hip + belly + front arm
"..aaaaaddcddddddba...abbddddddddba....", # 16 hind leg + upper front leg
".addddddcbddddba......abbbddddddba....", # 17 hind foot + front leg
"..aaddddbbbaaa.........aabbddddcba....", # 18 hind toes + forearm
"...aaaaaaa..............aabbddcba.....", # 19 front wrist
".........................aaddba.......", # 20 front paw
"..........................aaaa........", # 21 front paw toes
"......................................", # 22
"......................................", # 23
"......................................", # 24
"......................................", # 25
"......................................", # 26
"......................................", # 27
]

cmap = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
}

for y, row in enumerate(f2_art):
    for x, ch in enumerate(row):
        if ch in cmap:
            f2.set(x, y, cmap[ch])

view(f1)
view(f2)

finish([f1, f2])
