from pixelbench_api import *

W = 32

def mdist(a, b):
    d = (a - b) % W
    if d > W // 2:
        d -= W
    return d

def draw_carpet():
    c = new_canvas(W, W, name="carpet")

    def S(x, y, col):
        c.set(x % W, y % W, col)

    def diamond(cx, cy, r, col):
        for dy in range(-r, r + 1):
            w = r - abs(dy)
            for dx in range(-w, w + 1):
                c.set((cx + dx) % W, (cy + dy) % W, col)

    BG      = (236, 222, 194)
    BG_D    = (210, 190, 158)
    RED     = (130, 37, 51)
    RED_D   = (98, 24, 38)
    GOLD    = (223, 181, 97)
    GOLD_D  = (186, 146, 68)
    GOLD_L  = (246, 216, 158)
    ORANGE  = (203, 95, 53)

    A = [(0, 0), (16, 0), (0, 16), (16, 16)]
    B = [(8, 8), (24, 8), (8, 24), (24, 24)]

    def in_diamonds(x, y, centers, r):
        for (cx, cy) in centers:
            if abs(mdist(x, cx)) + abs(mdist(y, cy)) <= r:
                return True
        return False

    c.rect(0, 0, W, W, BG, fill=True)
    for y in range(W):
        for x in range(W):
            if (x + y) % 4 == 1:
                c.set(x, y, BG_D)

    for (cx, cy) in A:
        diamond(cx, cy, 7, RED)
    for (cx, cy) in B:
        diamond(cx, cy, 7, GOLD)

    for y in range(W):
        for x in range(W):
            if (x + y) % 4 == 1:
                if in_diamonds(x, y, A, 7):
                    c.set(x, y, RED_D)
                elif in_diamonds(x, y, B, 7):
                    c.set(x, y, GOLD_D)

    for (cx, cy) in A:
        diamond(cx, cy, 5, RED_D)
    for (cx, cy) in B:
        diamond(cx, cy, 5, GOLD_D)

    for (cx, cy) in A:
        diamond(cx, cy, 2, GOLD_L)
        S(cx, cy, RED)

    for (cx, cy) in B:
        for dx, dy in ((3, 0), (-3, 0), (0, 3), (0, -3)):
            S(cx + dx, cy + dy, RED)
        for dx, dy in ((2, 2), (-2, 2), (2, -2), (-2, -2)):
            S(cx + dx, cy + dy, ORANGE)
        for dx, dy in ((4, 0), (-4, 0), (0, 4), (0, -4)):
            S(cx + dx, cy + dy, GOLD_L)
        S(cx, cy, GOLD_L)

    for (cx, cy) in A:
        for (vx, vy) in ((cx, cy - 8), (cx + 8, cy), (cx, cy + 8), (cx - 8, cy)):
            S(vx, vy, ORANGE)

    return c

if __name__ == "__main__":
    c = draw_carpet()
    print(c.stats_text())
    finish(c)
