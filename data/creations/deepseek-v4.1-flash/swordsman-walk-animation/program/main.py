from pixelbench_api import *

# ---------------------------------------------------------------
# 16-bit RPG style red-haired swordsman, side view facing right.
# Two 32x32 frames side by side on a 64x32 canvas.
#   frame A = contact pose (legs apart, body low, cape billowing)
#   frame B = passing pose (legs together, body up 1px, cape settled)
# ---------------------------------------------------------------

PAL = {
    # hair
    'R': '#d8322a', 'r': '#9c1c18', 'H': '#f46a48',
    # skin
    's': '#f2c492', 'S': '#c08a5c', 'e': '#241820',
    # tunic
    't': '#8a5a36', 'T': '#5c3820', 'u': '#ab7647',
    # leather strap / belt
    'o': '#3a2418',
    # cape
    'c': '#2a3468', 'C': '#1c2450', 'l': '#4a5ca8',
    # sword
    'g': '#d8a838', 'G': '#a07018',
    'b': '#b8c4d8', 'B': '#eef4ff',
    # legs / boots
    'p': '#4a3a40', 'q': '#332830',
    'P': '#5e4028', 'k': '#3e2a18', 'Q': '#7d5a38',
}

# coloured (darkened) outline per part -- classic 16-bit rim
OR = '#7e1814'   # hair
OS = '#a87048'   # skin
OT = '#2a1a10'   # leather / tunic / strap
OC = '#0e1230'   # cape
OP = '#241a20'   # trousers
OK = '#33220f'   # boots
OB = '#585f78'   # blade
OG = '#6a4a12'   # gold

OUT_OF = {
    'R': OR, 'r': OR, 'H': OR,
    's': OS, 'S': OS, 'e': OS,
    't': OT, 'u': OT, 'T': OT, 'o': OT,
    'c': OC, 'l': OC, 'C': OC,
    'p': OP, 'q': OP,
    'P': OK, 'Q': OK, 'k': OK,
    'b': OB, 'B': OB,
    'g': OG, 'G': OG,
}


def lum(h):
    h = h.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return 0.299 * r + 0.587 * g + 0.114 * b


def build(rows):
    px = {}
    for y, segs in rows:
        for x, s in segs:
            for i, ch in enumerate(s):
                if ch == '.':
                    continue
                px[(x + i, y)] = ch
    return px


def render(canvas, px, ox, oy):
    out = {}
    for (x, y), ch in px.items():
        col = OUT_OF[ch]
        l = lum(col)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                n = (x + dx, y + dy)
                if n in px:
                    continue
                if n not in out or l < out[n][0]:
                    out[n] = (l, col)
    for (x, y), (l, col) in sorted(out.items()):
        canvas.set(ox + x, oy + y, col)
    for (x, y), ch in px.items():
        canvas.set(ox + x, oy + y, PAL[ch])


# ------------------------------------------------------------------
# FRAME A : contact pose -- front leg forward, back leg trailing
# ------------------------------------------------------------------
A = [
    # ---- cape (behind everything) ----
    (12, [(11, "cll")]),
    (13, [(8, "CccCcl")]),
    (14, [(7, "CccCcl")]),
    (15, [(7, "CccCcl")]),
    (16, [(6, "CccCccc")]),
    (17, [(6, "CccCccl")]),
    (18, [(7, "CcCccl")]),
    (19, [(8, "CcCcl")]),
    (20, [(8, "Ccccl")]),
    (21, [(9, "Cccc")]),
    (22, [(9, "Cc")]),

    # ---- back leg (dark, trailing) ----
    (21, [(13, "qqq")]),
    (22, [(12, "qqq")]),
    (23, [(12, "qqq")]),
    (24, [(11, "qqq")]),
    (25, [(11, "qqq")]),
    (26, [(10, "qqq")]),
    (27, [(10, "kkk")]),
    (28, [(10, "kkkkk")]),
    (29, [(10, "kkkkk")]),

    # ---- front leg (forward) ----
    (21, [(16, "ppp")]),
    (22, [(17, "ppp")]),
    (23, [(18, "ppp")]),
    (24, [(18, "ppp")]),
    (25, [(19, "ppp")]),
    (26, [(19, "ppp")]),
    (27, [(19, "PPQ")]),
    (28, [(19, "PPPPP")]),
    (29, [(19, "PPPPP")]),

    # ---- torso ----
    (13, [(13, "Ttttttu")]),
    (14, [(13, "Ttttttu")]),
    (15, [(13, "Ttttttu")]),
    (16, [(13, "Ttttttu")]),
    (17, [(13, "Ttttttu")]),
    (18, [(13, "Ttttttu")]),
    (19, [(13, "ooogooo")]),
    (20, [(13, "ppppppp")]),

    # ---- head ----
    (3, [(12, "rHRRRRR")]),
    (4, [(11, "rRHHRRRRR")]),
    (5, [(11, "RHRRRRRrss")]),
    (6, [(11, "RHRRrsssss")]),
    (7, [(11, "rRRRsssess")]),
    (8, [(11, "RRRssssssss")]),
    (9, [(12, "Rrsssssss")]),
    (10, [(13, "rsssssS")]),
    (11, [(14, "SSSSS")]),
    (12, [(15, "sss")]),

    # ---- ponytail ----
    (5, [(9, "rR")]),
    (6, [(8, "rRR")]),
    (7, [(8, "rRR")]),
    (8, [(8, "rRR")]),
    (9, [(9, "rRR")]),
    (10, [(10, "rrR")]),
    (11, [(11, "rrR")]),

    # ---- sword arm (swung forward) ----
    (13, [(18, "Tuu")]),
    (14, [(19, "Tu")]),
    (15, [(20, "Tu")]),
    (16, [(20, "Ts")]),
    (17, [(21, "s")]),

    # ---- long sword ----
    (2, [(28, "b")]),
    (3, [(28, "bB")]),
    (4, [(27, "bB")]),
    (5, [(27, "bB")]),
    (6, [(26, "bB")]),
    (7, [(26, "bB")]),
    (8, [(25, "bB")]),
    (9, [(25, "bB")]),
    (10, [(25, "bB")]),
    (11, [(24, "bB")]),
    (12, [(24, "bB")]),
    (13, [(24, "bB")]),
    (14, [(23, "bB")]),
    (15, [(23, "bB")]),
    (16, [(22, "bB")]),
    (17, [(22, "bB")]),
    (18, [(20, "ggggg")]),
    (19, [(21, "ss")]),
    (20, [(21, "GG")]),
    (21, [(21, "g")]),
]

# ------------------------------------------------------------------
# FRAME B : passing pose
# ------------------------------------------------------------------
B = [
    # ---- cape (hangs closer, less billow) ----
    (11, [(11, "cll")]),
    (12, [(9, "Ccccl")]),
    (13, [(8, "CccCcl")]),
    (14, [(8, "CccCcl")]),
    (15, [(8, "CccCcl")]),
    (16, [(9, "CcCcl")]),
    (17, [(9, "CcCcl")]),
    (18, [(10, "Cccl")]),
    (19, [(10, "Ccl")]),
    (20, [(11, "cl")]),

    # ---- back leg (lifted off ground) ----
    (20, [(13, "qqq")]),
    (21, [(12, "qqq")]),
    (22, [(12, "qqq")]),
    (23, [(11, "qqq")]),
    (24, [(11, "qqq")]),
    (25, [(11, "qqq")]),
    (26, [(11, "kkk")]),
    (27, [(11, "kkkk")]),

    # ---- front leg (supporting) ----
    (20, [(16, "ppp")]),
    (21, [(17, "ppp")]),
    (22, [(17, "ppp")]),
    (23, [(18, "ppp")]),
    (24, [(18, "ppp")]),
    (25, [(18, "ppp")]),
    (26, [(18, "ppp")]),
    (27, [(18, "PPQ")]),
    (28, [(18, "PPPPP")]),
    (29, [(18, "PPPPP")]),

    # ---- torso ----
    (12, [(13, "Ttttttu")]),
    (13, [(13, "Ttttttu")]),
    (14, [(13, "Ttttttu")]),
    (15, [(13, "Ttttttu")]),
    (16, [(13, "Ttttttu")]),
    (17, [(13, "Ttttttu")]),
    (18, [(13, "ooogooo")]),
    (19, [(13, "ppppppp")]),

    # ---- head ----
    (2, [(12, "rHRRRRR")]),
    (3, [(11, "rRHHRRRRR")]),
    (4, [(11, "RHRRRRRrss")]),
    (5, [(11, "RHRRrsssss")]),
    (6, [(11, "rRRRsssess")]),
    (7, [(11, "RRRssssssss")]),
    (8, [(12, "Rrsssssss")]),
    (9, [(13, "rsssssS")]),
    (10, [(14, "SSSSS")]),
    (11, [(15, "sss")]),

    # ---- ponytail ----
    (4, [(9, "rR")]),
    (5, [(8, "rRR")]),
    (6, [(8, "rRR")]),
    (7, [(8, "rRR")]),
    (8, [(9, "rRR")]),
    (9, [(10, "rrR")]),
    (10, [(11, "rrR")]),

    # ---- sword arm (swung slightly back) ----
    (12, [(17, "Tuu")]),
    (13, [(18, "Tu")]),
    (14, [(19, "Tu")]),
    (15, [(19, "Ts")]),
    (16, [(20, "s")]),

    # ---- long sword ----
    (1, [(28, "b")]),
    (2, [(28, "bB")]),
    (3, [(27, "bB")]),
    (4, [(27, "bB")]),
    (5, [(26, "bB")]),
    (6, [(26, "bB")]),
    (7, [(25, "bB")]),
    (8, [(25, "bB")]),
    (9, [(25, "bB")]),
    (10, [(24, "bB")]),
    (11, [(24, "bB")]),
    (12, [(24, "bB")]),
    (13, [(23, "bB")]),
    (14, [(23, "bB")]),
    (15, [(22, "bB")]),
    (16, [(22, "bB")]),
    (17, [(19, "ggggg")]),
    (18, [(20, "ss")]),
    (19, [(20, "GG")]),
    (20, [(20, "g")]),
]

c = new_canvas(64, 32, name="result")

pa = build(A)
pb = build(B)

for name, px in (("A", pa), ("B", pb)):
    for (x, y) in px:
        if not (0 <= x < 32 and 0 <= y < 32):
            print("OUT OF FRAME", name, x, y)

render(c, pa, 0, 0)
render(c, pb, 32, 0)

print(c.stats_text())
print("--- FRAME A (0..31) ---")
print(c.matrix_text(region=(0, 0, 31, 31)))
print("--- FRAME B (32..63) ---")
print(c.matrix_text(region=(32, 0, 63, 31)))

save("swordsman_walk", c)
finish(c)
