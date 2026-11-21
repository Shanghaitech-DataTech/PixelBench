from pixelbench_api import new_canvas, finish

c = new_canvas(16, 16, name="planks")

# ---- palette ----
GROOVE = "#1e1207"   # dark seam grooves
CAP_L   = "#c08444"  # light board end cap
CAP_L2  = "#aa7135"
CAP_D   = "#7d4e1f"  # dark board end cap
CAP_D2  = "#6f431b"
SHAD    = "#4a2d10"  # shadow line under a board end
A_LT,  A_BASE, A_DK,  A_DEEP = "#b47a40", "#a26b35", "#8e5c2a", "#7a4c1f"
B_LT,  B_BASE, B_DK,  B_DEEP = "#9a6432", "#8a5827", "#77491d", "#653d16"
K_RING = "#5b3a16"
K_CORE = "#36200a"

# Three vertical boards: A light (x0-4), B dark (x6-9), C light (x11-14),
# with 1px grooves at x=5, x=10, x=15 (x15 wraps to x0 -> seamless horizontally).
boards = [
    (0,  4, [A_LT, A_BASE, A_DK, A_BASE, A_LT], A_DEEP),
    (6,  9, [B_LT, B_BASE, B_DK, B_BASE],       B_DEEP),
    (11, 14,[A_LT, A_BASE, A_DK, A_BASE, A_LT], A_DEEP),
]
# per-row wiggle so the grain is gently wavy; wig[0] == wig[15] == 0 keeps the
# vertical wrap continuous.
wig = [0,0,0,1,1,2,1,0,-1,-1,-2,-1,0,1,1,0]

for x0, x1, tones, deep in boards:
    for y in range(16):
        s = wig[y]
        for x in range(x0, x1 + 1):
            c.set(x, y, tones[(x - x0 - s) % len(tones)])
        c.set(x1, y, deep)          # shaded edge beside each groove

# dark seam grooves (x=15 wraps to x=0)
for y in range(16):
    for gx in (5, 10, 15):
        c.set(gx, y, GROOVE)

# board ends: alternating light/dark caps with staggered shadow seams
for x in list(range(0, 5)) + list(range(11, 15)):
    c.set(x, 0, CAP_L)
    c.set(x, 1, CAP_L2)
    c.set(x, 2, CAP_L2)
    c.set(x, 3, SHAD)
for x in range(6, 10):
    c.set(x, 0, CAP_D)
    c.set(x, 1, CAP_D2)
    c.set(x, 2, CAP_D2)
    c.set(x, 4, SHAD)

# knot 1 (board A), slanted along the grain wiggle
for x, y in [(1,6),(2,6),(1,7),(2,7),(3,7),(1,8),(3,8),(1,9),(2,9),(3,9),(2,10)]:
    c.set(x + wig[y], y, K_RING)
c.set(2, 8, K_CORE)
c.set(2, 9, K_CORE)

# knot 2 (board C), small, lower on the board
for x, y in [(12,12),(13,12),(14,12),(12,13),(14,13),(12,14),(13,14),(14,14)]:
    c.set(x, y, K_RING)
c.set(13, 13, K_CORE)

# short dark grain dashes for texture
for x, y in [(0,11),(1,11),(0,13),(7,12),(8,12)]:
    c.set(x, y, A_DK if x < 5 else B_DK)

print(c.stats_text())
finish(c)
