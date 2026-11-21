from pixelbench_api import *

COL = {
    'a': '#3a3737',  # outline
    'b': '#b7b3b2',  # mid grey shade
    'c': '#827c7c',  # dark grey (far limbs)
    'd': '#efe9e7',  # white body
    'e': '#d6b39d',  # inner ear light
    'f': '#bc8b6d',  # inner ear dark
    'g': '#cdae67',  # nose
}

ROWS = [["."] * 26 for _ in range(28)]

def put(y, x, s):
    for i, ch in enumerate(s):
        ROWS[y][x + i] = ch

# --- ears swept back (two, 4px wide, leaning left as they rise) ---
put(1, 10, "aa");  put(1, 15, "aa")
put(2, 10, "aeea"); put(2, 15, "adda")
put(3, 11, "aeea"); put(3, 16, "adda")
put(4, 12, "aeea"); put(4, 17, "adda")
put(5, 13, "afea"); put(5, 18, "adda")
put(6, 14, "aeea"); put(6, 19, "adda")
# --- head ---
put(7, 15, "aaaaaaa")
put(8, 14, "a"); put(8, 15, "dddd"); put(8, 19, "a"); put(8, 20, "dd"); put(8, 22, "a")
put(9, 14, "a"); put(9, 15, "dddddddd"); put(9, 23, "a")
put(10, 14, "a"); put(10, 15, "dddddddd"); put(10, 23, "gg"); put(10, 25, "a")
# --- stretched body, back rising to the neck ---
put(11, 7, "a"); put(11, 8, "d" * 13); put(11, 21, "bbb"); put(11, 24, "a")
put(12, 5, "a"); put(12, 6, "d" * 14); put(12, 20, "bbb"); put(12, 23, "a")
put(13, 4, "a"); put(13, 5, "d" * 17); put(13, 22, "a")
put(14, 3, "a"); put(14, 4, "d" * 17); put(14, 21, "a")
put(15, 2, "a"); put(15, 3, "d" * 17); put(15, 20, "a")
put(16, 2, "a"); put(16, 3, "d" * 17); put(16, 20, "a")
put(17, 2, "a"); put(17, 3, "b" * 16); put(17, 19, "a")
put(18, 3, "a"); put(18, 4, "b" * 15); put(18, 19, "a")
# --- tail bump at the rear ---
put(13, 2, "aa")
put(14, 1, "a"); put(14, 2, "dd")
put(15, 0, "a"); put(15, 1, "dd")
put(16, 0, "a"); put(16, 1, "dd")
put(17, 0, "aa")
put(18, 1, "aaa")
# --- legs: hind stretched back, front tucked ---
put(19, 2, "addda"); put(19, 8, "accca"); put(19, 14, "adda"); put(19, 19, "acca")
put(20, 1, "addda"); put(20, 7, "accca"); put(20, 14, "adda"); put(20, 19, "aaaa")
put(21, 0, "adddda"); put(21, 7, "accca"); put(21, 13, "aaaaa")
put(22, 0, "aaaaaa"); put(22, 7, "aaaaa")

for r in ROWS:
    assert len(r) == 26

f1 = input_canvas.copy(name="frame1")

f2 = new_canvas(26, 28, name="frame2")
for y, row in enumerate(ROWS):
    for x, ch in enumerate(row):
        if ch != '.':
            f2.set(x, y, COL[ch])

view(f1, scale=8, margin=2, edges="all")
view(f2, scale=8, margin=2, edges="all")

save("bunny_hop_f1", f1)
save("bunny_hop_f2", f2)

finish([f1, f2])
