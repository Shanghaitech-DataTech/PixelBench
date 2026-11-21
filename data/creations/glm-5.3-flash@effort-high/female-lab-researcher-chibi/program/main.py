from pixelbench_api import *

# 16x16 chibi female lab researcher
c = new_canvas(16, 16, name="result")

# Palette
K = c.color("#202028", name="hair_black")     # black hair
H = c.color("#3c3c4c", name="hair_shine")     # hair highlight
S = c.color("#f3c9a2", name="skin")
E = c.color("#5a3418", name="eye_brown")      # brown eyes
M = c.color("#c46a5a", name="mouth")
W = c.color("#f7f7fa", name="coat_white")
G = c.color("#d8d8e2", name="coat_shadow")
P = c.color("#e0798f", name="shirt_pink")
D = c.color("#3a3244", name="shoes")

# Pixel map: rows of 16 chars
rows = [
    "....KKKKKKKK....",  # 0  hair top
    "...KKHHHKKKKK...",  # 1  hair with shine
    "..KKKHHKKKKKKK..",  # 2  hair
    "..KKKKKKKKKKKK..",  # 3  full fringe
    "..KSSSSSSSSSSK..",  # 4  face
    "..KSSEESSSEESSK.",  # 5  brown eyes
    "..KSSSSSMMSSSSK.",  # 6  mouth (centered)
    "..KKSSSSSSSSKK..",  # 7  jaw
    "...KKSSSSSSKK...",  # 8  chin / hair sides
    "..KWWWPPPWWWWK..",  # 9  shoulders + collar
    "..KWWWWPPWWWWK..",  # 10 coat + pink shirt
    "...WWWWPPWWWW...",  # 11 coat
    "...SGWWPPWWWS...",  # 12 pocket + hands
    "..WGGWWPPWWGGW..",  # 13 coat hem shading
    ".....SS..SS.....",  # 14 legs
    ".....DD..DD.....",  # 15 shoes
]

key = {".": None, "K": K, "H": H, "S": S, "E": E, "M": M,
       "W": W, "G": G, "P": P, "D": D}

for y, row in enumerate(rows):
    assert len(row) == 16, (y, len(row), row)
    for x, ch in enumerate(row):
        if key[ch] is not None:
            c.set(x, y, key[ch])

print(c.stats_text())
print(c.matrix_text())

finish(c)
