from pixelbench_api import *


def main():
    W = H = 48
    c = new_canvas(W, H)

    def col(spec):
        return c.color(spec)

    OUT = col((38, 22, 12))    # dark brown outline
    WD  = col((70, 44, 22))    # dark wood
    WM  = col((104, 66, 30))   # mid wood
    WL  = col((140, 90, 42))   # light wood
    WH  = col((178, 122, 64))  # bright wood
    WT  = col((210, 156, 98))  # sunlit wood
    PD  = col((84, 40, 150))   # deep purple
    PM  = col((136, 72, 208))  # mid purple
    PB  = col((192, 124, 250)) # bright purple
    PG  = col((232, 190, 255)) # pale glow
    PW  = col((250, 230, 255)) # white-hot core
    BD  = col((96, 50, 162))   # band dark
    BL  = col((156, 102, 220)) # band light

    # ---- wooden shaft ----
    for y in range(21, 44):
        x0, x1 = 21, 27
        c.set(x0, y, OUT)
        c.set(x1, y, OUT)
        for x in range(x0 + 1, x1):
            if y in (25, 26):
                cc = {22: BD, 23: PM, 24: BL, 25: PM, 26: BD}[x]
            else:
                cc = {22: WM, 23: WL, 24: WH, 25: WL, 26: WM}[x]
            c.set(x, y, cc)

    # bottom taper
    c.set(22, 44, OUT); c.set(26, 44, OUT)
    for x in range(23, 26):
        c.set(x, 44, WL if x == 24 else WM)
    c.set(23, 45, OUT); c.set(25, 45, OUT)
    c.set(24, 45, WM)
    c.set(24, 46, OUT)

    # ---- curved head (hook that bends right then curls) ----
    hook = [
        (20, 21, 27),
        (19, 22, 26),
        (18, 23, 28),
        (17, 24, 29),
        (16, 25, 30),
        (15, 26, 31),
        (14, 27, 31),
        (13, 28, 31),
        (12, 28, 31),
        (11, 27, 30),
        (10, 27, 29),
        (9,  28, 28),
    ]
    for y, x0, x1 in hook:
        c.set(x0, y, OUT)
        if x1 != x0:
            c.set(x1, y, OUT)
        mid = (x0 + x1) / 2.0
        for x in range(x0 + 1, x1):
            d = abs(x - mid)
            cc = WT if d < 0.55 else (WL if d < 1.1 else WM)
            c.set(x, y, cc)

    # ---- glowing purple orb capping the curled tip ----
    c.set(28, 5, PM)
    c.set(27, 6, PD); c.set(28, 6, PB); c.set(29, 6, PD)
    c.set(26, 7, PD); c.set(27, 7, PB); c.set(28, 7, PW); c.set(29, 7, PM); c.set(30, 7, PD)
    c.set(27, 8, PD); c.set(28, 8, PB); c.set(29, 8, PD)
    c.set(28, 9, PM)

    # soft halo around the orb
    glow = [(28, 4), (26, 5), (30, 5), (25, 6), (31, 6),
            (25, 8), (31, 8), (26, 9), (30, 9), (27, 10), (29, 10)]
    for (x, y) in glow:
        c.set(x, y, PG)

    # ---- purple particle effects ----
    parts = [
        (34, 6, PB), (36, 9, PG), (38, 13, PM), (35, 16, PD),
        (32, 19, PB), (35, 22, PG), (32, 25, PM), (29, 22, PG),
        (18, 9, PM), (16, 13, PG), (13, 17, PB), (16, 21, PD),
        (13, 25, PG), (16, 28, PM), (12, 31, PB), (34, 28, PM),
        (31, 31, PG), (35, 33, PD), (29, 31, PG), (19, 33, PM),
        (17, 36, PG), (14, 38, PD), (32, 37, PB), (28, 41, PM),
        (20, 39, PB), (17, 42, PG), (25, 30, PD),
    ]
    for (x, y, cc) in parts:
        c.set(x, y, cc)
    # sparkle cross near orb
    for (x, y) in [(36, 8), (36, 10), (35, 9), (37, 9)]:
        c.set(x, y, PG)

    # ---- subtle wood grain ----
    for (x, y, cc) in [(26, 30, WD), (22, 34, WD), (26, 37, WD), (23, 40, WD)]:
        c.set(x, y, cc)

    print(c.stats_text())
    print(c.matrix_text(region=(22, 2, 34, 12)))
    print(c.matrix_text(region=(8, 20, 40, 47)))
    return c


result = main()
finish(result)
