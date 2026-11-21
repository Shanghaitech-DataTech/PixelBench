BIG = {
    "P": ["#########", "#       #", "#       #", "#       #", "#########",
          "#       #", "#       #", "#       #", "#       #", "#       #", "#       #"],
    "I": ["  #####  ", "    #    ", "    #    ", "    #    ", "    #    ",
          "    #    ", "    #    ", "    #    ", "    #    ", "    #    ", "  #####  "],
    "X": ["#       #", " #     # ", "  #   #  ", "   # #   ", "    #    ",
          "   # #   ", "  #   #  ", " #     # ", "#       #", "#       #", "#       #"],
    "E": ["#########", "#       #", "#       #", "#       #", "#########",
          "#       #", "#       #", "#       #", "#########", "#       #", "#########"],
    "L": ["#      ", "#      ", "#      ", "#      ", "#      ",
          "#      ", "#      ", "#      ", "#      ", "#      ", "#######"],
}
print("P len", len(BIG["P"][0]))
print("L lens", sorted({len(r) for r in BIG["L"]}))

def pts(g):
    return [(i, j) for j, r in enumerate(g) for i, ch in enumerate(r) if ch == "#"]

x = 5
fw = len(BIG["P"][0])
adv = fw + 2
mx = 0
for k, ch in enumerate("PIXEL"):
    gx = x + k * adv
    for (i, j) in pts(BIG[ch]):
        mx = max(mx, gx + i)
print("fw", fw, "adv", adv, "max abs fill", mx)
