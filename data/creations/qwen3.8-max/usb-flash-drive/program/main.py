# USB flash drive - 32x32 RPG item portrait
# metal casing, USB connector, keychain strap, dark outline, transparent bg

c = new_canvas(32, 32, name="usb_flash_drive")

COL = {
    'K': '#151729',   # dark outline
    'N': '#232a3d',   # deep hole shadow
    'A': '#f2f6fa',   # metal brightest
    'B': '#ccd8e3',   # metal light
    'C': '#9dabbc',   # metal mid
    'D': '#71808f',   # metal shadow
    'E': '#4e5a6a',   # metal deep shadow
    'H': '#7d6128',   # dim gold contacts
    'L': '#6bf7dc',   # LED bright
    'M': '#1f9e8c',   # LED mid
    'T': '#f08a63',   # strap highlight
    'R': '#d8483c',   # strap red
    'S': '#97302a',   # strap shadow
}


def put(x, y, ch):
    if ch in '. ':
        return
    c.set(x, y, COL[ch])


def rowstr(y, s, x0=0):
    for i, ch in enumerate(s):
        put(x0 + i, y, ch)


# ---------------- USB connector (top) ----------------
rowstr(1, 'KKKKKKKKKK', 11)
rowstr(2, 'K' + 'AABBCCDDED' + 'K', 10)
rowstr(3, 'K' + 'ABNNCCNNDE' + 'K', 10)
rowstr(4, 'K' + 'ABHHCCHHDE' + 'K', 10)
rowstr(5, 'K' + 'ABCCCCDDEE' + 'K', 10)
rowstr(6, 'K' + 'DDDEEEEEEE' + 'K', 10)

# ---------------- metal casing ----------------
rowstr(7,  'KKKKKKKKKKKKKK', 9)
rowstr(8,  'K' + 'AAABBBBBCCCDDC' + 'K', 8)
rowstr(9,  'K' + 'ABBBCCCCDDDEED' + 'K', 8)
rowstr(10, 'K' + 'ABBCBCCCDDDEED' + 'K', 8)          # sheen diagonal
rowstr(11, 'K' + 'ABBCCBCCDDDEED' + 'K', 8)
rowstr(12, 'K' + 'ABBCCCBCDDDEED' + 'K', 8)
rowstr(13, 'K' + 'DEEEEEEEEEEEED' + 'K', 8)          # cap seam groove
rowstr(14, 'K' + 'AAABBBBBCCCDDC' + 'K', 8)          # lit edge under seam
rowstr(15, 'K' + 'ABBCCBCCDDDEED' + 'K', 8)          # sheen continues
rowstr(16, 'K' + 'ALMCCCBCDDDEED' + 'K', 8)          # LED 2x2
rowstr(17, 'K' + 'AMMCCCCBDDDEED' + 'K', 8)
rowstr(18, 'K' + 'DEEEEEEEEEEEED' + 'K', 8)          # lower groove
rowstr(19, 'K' + 'BCCDDDDDEEEEEE' + 'K', 8)
rowstr(20, 'K' + 'CDDEEEEEEEEEEE' + 'K', 8)

# ---------------- bottom + lanyard tab ----------------
rowstr(21, 'KKKK' + 'CCDDEE' + 'KKKK', 9)
rowstr(22, 'K' + 'DD' + 'NN' + 'EE' + 'K', 12)
rowstr(23, 'KKKKKKKK', 12)

# ---------------- keychain strap ----------------
rowstr(24, 'KTRRSK', 13)
rowstr(25, 'KTRKKRSK', 12)
rowstr(26, 'KTRK..KRSK', 11)
rowstr(27, 'KTRK..KRSK', 11)
rowstr(28, 'KTRRRRRRSK', 11)
rowstr(29, 'KTRRRRSK', 12)
rowstr(30, 'KKKKKK', 13)

print(c.stats_text())
p = view(c)
print("view:", p)
save("usb_flash_drive", c)

finish(c)
