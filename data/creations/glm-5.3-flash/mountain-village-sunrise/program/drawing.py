# -*- coding: utf-8 -*-
"""mountain-village-sunrise -- 128x128 pixel art (drawing module)"""
import random

from pixelbench_api import new_canvas

W = H = 128
HORIZON = 90

PAL = {
    "sky0": "#191a38", "sky1": "#2c2650", "sky2": "#453062", "sky3": "#66396c",
    "sky4": "#8f476c", "sky5": "#b85a64", "sky6": "#dc7757", "sky7": "#f29b5a",
    "sky8": "#fbc27c", "sky9": "#ffe6ab",
    "star": "#9a90c0", "bird": "#3a2c50",
    "sun_edge": "#ffb45e", "sun_mid": "#ffdf96", "sun_core": "#fff6cf",
    "mtn_far": "#9d7fa4", "mtn_mid": "#6f5b8e", "mtn_near": "#4a4470",
    "alpen": "#eeb0ac",
    "mist": "#ecc9a0", "mist_hi": "#f9e4bb",
    "grass_lit": "#55703f", "grass": "#3d5638", "grass_dk": "#2a3d2b",
    "grass_vdk": "#1d2d20", "tuft_hi": "#6d8a4c", "tuft_dk": "#243826",
    "warm_gnd": "#6b7a45",
    "wall": "#7d5638", "wall_dk": "#5a3c28", "wall_lit": "#96683f",
    "timber": "#3a2718",
    "roof": "#8a4038", "roof_dk": "#632c2a", "roof_lit": "#b0603f",
    "door": "#2e1e14",
    "win": "#ffd98a", "win_glow": "#ffb85e",
    "chim": "#5c4034", "chim_top": "#7a564a",
    "smoke_lo": "#8f88a8", "smoke_md": "#a9a2bd", "smoke_hi": "#c5bfd4",
    "path_base": "#7a6a52", "path_edge": "#4a3c2c",
    "stone_hi": "#c9bfae", "stone_md": "#a2988a", "stone_dk": "#7a7168",
    "stone_warm": "#e0cfa8",
    "pine_dk": "#1c352c", "pine_md": "#2b4f38", "pine_lit": "#3f6b44",
    "fpine_dk": "#0e1f1a", "fpine_md": "#16302a", "fpine_lit": "#22453a",
    "trunk": "#3a2a1e",
    "rock": "#6b6558", "rock_hi": "#8a8272",
}
P = PAL


def build():
    c = new_canvas(W, H, background=PAL["sky0"], name="mountain-village-sunrise")
    for k, v in PAL.items():
        c.color(v, k)

    # ---------------- helpers ----------------
    def glow(cx, cy, r0, r1, col, step):
        for y in range(max(0, cy - r1), min(H, cy + r1 + 1)):
            for x in range(max(0, cx - r1), min(W, cx + r1 + 1)):
                d2 = (x - cx) ** 2 + (y - cy) ** 2
                if r0 * r0 <= d2 <= r1 * r1 and (x + y) % step == 0:
                    c.set(x, y, col)

    def dither_disc(cx, cy, r, col, step, ymin=0, ymax=H):
        for y in range(max(ymin, cy - r), min(ymax, cy + r + 1)):
            for x in range(max(0, cx - r), min(W, cx + r + 1)):
                if (x - cx) ** 2 + (y - cy) ** 2 <= r * r and (x + y) % step == 0:
                    c.set(x, y, col)

    def fill_ridge(pts, col, bottom=HORIZON + 3):
        c.poly(list(pts) + [(W - 1, bottom), (0, bottom)], col, True)

    def pine(cx, base, h, w, dk, md, lt, trunk=None):
        trunk_h = max(2, h // 8) if trunk else 0
        fh = h - trunk_h
        top = base - fh
        for i in range(fh):
            y = top + i
            half = int(w * (i + 1) / fh / 2)
            if i > 2 and (i % 4) == 0:
                half = max(0, half - 1)
            if half <= 0:
                c.set(cx, y, md)
            else:
                c.line(cx - half, y, cx + half, y, md)
                c.set(cx + half, y, lt)
                if half >= 2:
                    c.set(cx + half - 1, y, lt)
                c.set(cx - half, y, dk)
                if half >= 3:
                    c.set(cx - half + 1, y, dk)
        if trunk:
            c.rect(cx - 1, base - trunk_h, 2, trunk_h, trunk)

    def house(x, y_base, w, wall_h, roof_h, wins, door=None, chim=None):
        y0 = y_base - wall_h
        ax = x + w // 2
        ay = y0 - roof_h
        c.rect(x, y0, w, wall_h, P["wall"])
        c.rect(x, y0, 2, wall_h, P["wall_dk"])
        c.rect(x + w - 3, y0, 3, wall_h, P["wall_lit"])
        c.rect(x, y0, w, 1, P["timber"])
        c.rect(x, y_base - 1, w, 1, P["timber"])
        c.rect(x, y0, 1, wall_h, P["timber"])
        c.rect(x + w - 1, y0, 1, wall_h, P["timber"])
        c.poly([(x - 2, y0), (ax, ay), (x + w + 2, y0)], P["roof"])
        c.poly([(ax, ay), (x - 2, y0), (ax, y0)], P["roof_dk"])
        c.poly([(ax, ay), (x + w + 2, y0), (x + w - 1, y0)], P["roof_lit"])
        if chim:
            cxx, cw, chh = chim
            slope = (y0 - ay) / max(1.0, (ax - (x - 2)))
            ry = int(ay + (ax - cxx) * slope)
            top = ry - chh
            c.rect(cxx, top, cw, (ry + 2) - top, P["chim"])
            c.rect(cxx - 1, top - 1, cw + 2, 2, P["chim_top"])
        if door:
            dx, dw, dh = door
            c.rect(dx, y_base - dh, dw, dh, P["door"])
            c.rect(dx, y_base - dh, dw, 1, P["timber"])
            c.set(dx + dw - 2, y_base - dh // 2, P["win_glow"])
        for (wx, wy, ww, wh) in wins:
            c.rect(wx, wy, ww, wh, P["timber"])
            c.rect(wx + 1, wy + 1, ww - 2, wh - 2, P["win"])
            if ww >= 6 and wh >= 6:
                c.rect(wx + 1, wy + 1 + (wh - 2) // 2, ww - 2, 1, P["timber"])
                c.rect(wx + 1 + (ww - 2) // 2, wy + 1, 1, wh - 2, P["timber"])
            c.set(wx - 1, wy + wh - 1, P["win_glow"])
            c.set(wx + ww, wy + wh - 1, P["win_glow"])
        return ax, ay

    # ---------------- sky ----------------
    SX, SY = 96, 56
    bands = [("sky0", 0), ("sky1", 9), ("sky2", 18), ("sky3", 27), ("sky4", 36),
             ("sky5", 45), ("sky6", 54), ("sky7", 63), ("sky8", 72), ("sky9", 81)]
    for i, (nm, y0) in enumerate(bands):
        y1 = bands[i + 1][1] if i + 1 < len(bands) else HORIZON
        c.rect(0, y0, W, y1 - y0, P[nm])
        if i + 1 < len(bands):
            c.dither(0, y1 - 2, W, 2, [P[nm], P[bands[i + 1][0]]], pattern="checker")

    for (sx, sy) in [(14, 6), (30, 11), (52, 4), (70, 9), (62, 15), (40, 20),
                     (6, 12), (46, 9), (84, 5), (100, 8), (112, 14), (120, 6)]:
        if ((sx - SX) ** 2 + (sy - SY) ** 2) < 20 ** 2:
            continue
        c.set(sx, sy, P["star"])

    # ---------------- sun ----------------
    glow(SX, SY, 8, 14, P["sun_mid"], 2)
    glow(SX, SY, 14, 22, P["sky7"], 3)
    glow(SX, SY, 22, 32, P["sky6"], 5)
    c.circle(SX, SY, 8, P["sun_edge"])
    c.circle(SX, SY, 6, P["sun_mid"])
    c.circle(SX, SY, 4, P["sun_core"])

    # ---------------- mountains ----------------
    ridgeA = [(0, 78), (14, 64), (28, 72), (44, 56), (60, 68), (76, 60),
              (96, 61), (112, 66), (127, 58)]
    fill_ridge(ridgeA, P["mtn_far"])
    for (px, py) in [(14, 64), (44, 56), (76, 60)]:
        for t in range(4):
            c.set(px + t, py + t, P["alpen"])
            if t < 2:
                c.set(px + t, py + t + 1, P["alpen"])

    ridgeB = [(0, 88), (12, 76), (26, 84), (40, 74), (56, 82), (72, 76),
              (88, 84), (104, 74), (118, 82), (127, 78)]
    fill_ridge(ridgeB, P["mtn_mid"])

    ridgeC = [(0, 90), (14, 78), (30, 86), (46, 76), (62, 84), (78, 78),
              (94, 86), (110, 78), (127, 88)]
    fill_ridge(ridgeC, P["mtn_near"])

    # ---------------- ground ----------------
    c.rect(0, 90, W, H - 90, P["grass"])
    c.rect(0, 90, W, 10, P["grass_lit"])
    c.dither(0, 98, W, 3, [P["grass_lit"], P["grass"]], pattern="checker")
    c.rect(0, 114, W, H - 114, P["grass_dk"])
    c.dither(0, 112, W, 3, [P["grass"], P["grass_dk"]], pattern="checker")
    c.rect(0, 123, W, H - 123, P["grass_vdk"])
    c.dither(0, 121, W, 3, [P["grass_dk"], P["grass_vdk"]], pattern="checker")
    # sunrise rim light along the meadow's top edge
    for x in range(W):
        if (x % 2) == 0 and 62 <= x <= 118:
            c.set(x, 90, P["tuft_hi"])

    # ---------------- valley mist ----------------
    for x in range(W):
        if (x + 84) % 3 == 0:
            c.set(x, 84, P["mist"])
        if (x + 85) % 2 == 0:
            c.set(x, 85, P["mist"])
    c.rect(0, 86, W, 4, P["mist"])
    for y in range(86, 92):
        for x in range(80, 118):
            if (x + y) % 2 == 0 and abs(x - 99) < 17 - (y - 86):
                c.set(x, y, P["mist_hi"])
    c.dither(0, 90, W, 2, [P["mist_hi"], P["grass_lit"]], pattern="checker")

    dither_disc(98, 98, 18, P["warm_gnd"], 3, ymin=92, ymax=113)
    dither_disc(98, 96, 10, P["warm_gnd"], 2, ymin=92, ymax=110)

    # ---------------- mid pines ----------------
    pine(2, 93, 9, 7, P["pine_dk"], P["pine_md"], P["pine_lit"], P["trunk"])
    pine(12, 96, 20, 14, P["pine_dk"], P["pine_md"], P["pine_lit"], P["trunk"])
    pine(34, 94, 26, 16, P["pine_dk"], P["pine_md"], P["pine_lit"], P["trunk"])
    pine(43, 97, 15, 11, P["pine_dk"], P["pine_md"], P["pine_lit"], P["trunk"])
    pine(84, 98, 14, 10, P["pine_dk"], P["pine_md"], P["pine_lit"], P["trunk"])
    pine(114, 96, 22, 15, P["pine_dk"], P["pine_md"], P["pine_lit"], P["trunk"])
    pine(124, 98, 16, 12, P["pine_dk"], P["pine_md"], P["pine_lit"], P["trunk"])

    # low mist drifting in front of the treeline (houses drawn after cover it)
    c.dither(0, 91, W, 2, [P["mist_hi"], P["grass_lit"]], pattern="checker")
    c.dither(0, 93, W, 1, [P["mist"], P["grass_lit"]], pattern="checker")
    for (mx, my) in [(8, 92), (40, 93), (84, 92), (116, 92)]:
        dither_disc(mx, my, 3, P["mist_hi"], 2, ymin=88, ymax=96)

    # ---------------- houses ----------------
    house(18, 96, 22, 11, 10, [(21, 88, 4, 4), (32, 88, 4, 4)],
          door=(27, 4, 6), chim=(24, 3, 6))
    house(86, 98, 24, 13, 12, [(89, 88, 5, 5), (104, 88, 5, 5)],
          door=(95, 6, 10), chim=(91, 4, 7))
    house(46, 100, 36, 20, 15, [(51, 85, 6, 6), (72, 85, 6, 6)],
          door=(61, 7, 10), chim=(54, 5, 9))

    # ---------------- chimney smoke ----------------
    for (x, y, r, col) in [(56, 60, 2, "smoke_lo"), (53, 55, 2, "smoke_lo"),
                           (49, 49, 3, "smoke_md"), (44, 43, 3, "smoke_md"),
                           (38, 36, 4, "smoke_md"), (31, 28, 5, "smoke_hi"),
                           (23, 20, 6, "smoke_hi")]:
        c.circle(x, y, r, P[col])
    for (x, y, r, col) in [(92, 69, 1, "smoke_lo"), (89, 64, 2, "smoke_md"),
                           (85, 58, 2, "smoke_md"), (80, 51, 3, "smoke_hi")]:
        c.circle(x, y, r, P[col])
    c.circle(25, 69, 1, P["smoke_md"])
    c.circle(21, 65, 2, P["smoke_lo"])

    # ---------------- stone path ----------------
    L_ANCH = [(100, 59), (108, 56), (116, 52), (128, 46)]
    R_ANCH = [(100, 69), (108, 73), (116, 79), (128, 85)]

    def ipol(anch, y):
        if y <= anch[0][0]:
            return anch[0][1]
        for i in range(len(anch) - 1):
            (ya, va), (yb, vb) = anch[i], anch[i + 1]
            if ya <= y <= yb:
                t = (y - ya) / float(yb - ya)
                return va + (vb - va) * t
        return anch[-1][1]

    for y in range(100, 128):
        l = int(round(ipol(L_ANCH, y)))
        r = int(round(ipol(R_ANCH, y)))
        c.line(l, y, r, y, P["path_base"])
        c.set(l, y, P["path_edge"])
        c.set(r, y, P["path_edge"])

    rng = random.Random(11)
    for y in range(101, 127):
        l = int(round(ipol(L_ANCH, y)))
        r = int(round(ipol(R_ANCH, y)))
        if r - l < 5:
            continue
        for k in range(rng.choice([1, 2, 2, 3])):
            sw = rng.choice([2, 2, 3, 3, 4])
            sh = rng.choice([1, 1, 2])
            sx = rng.randint(l + 1, max(l + 1, r - sw - 1))
            col = rng.choices([P["stone_hi"], P["stone_md"], P["stone_dk"]],
                              [3, 4, 2])[0]
            c.rect(sx, y, sw, sh, col)
            if col == P["stone_hi"] and rng.random() < 0.5:
                c.set(sx + sw - 1, y, P["stone_warm"])

    dither_disc(64, 106, 14, P["stone_warm"], 3, ymin=100)
    dither_disc(64, 105, 9, P["stone_warm"], 2, ymin=100)
    dither_disc(64, 104, 5, P["win"], 2, ymin=100)

    # ---------------- ground detail ----------------
    rng2 = random.Random(5)
    for i in range(95):
        x = rng2.randrange(1, W - 1)
        y = rng2.randrange(93, H - 1)
        if y >= 100:
            l = ipol(L_ANCH, y)
            r = ipol(R_ANCH, y)
            if l - 3 <= x <= r + 3:
                continue
        if ((x - 64) ** 2) / 260.0 + ((y - 104) ** 2) / 40.0 < 1.3:
            continue
        h = 1 + (y - 93) // 14
        col = P["tuft_hi"] if y < 114 else P["tuft_dk"]
        for k in range(h):
            c.set(x, y - k, col)
        if rng2.random() < 0.35:
            c.set(x + 1, y - h, col)

    for (bx, by, rx, ry) in [(36, 103, 4, 2), (92, 105, 5, 3), (22, 107, 4, 2),
                             (112, 109, 4, 2), (78, 111, 3, 2)]:
        c.ellipse(bx, by, rx, ry, P["pine_md"])
        c.ellipse(bx + 1, by - 1, rx - 1, max(1, ry - 1), P["pine_lit"])

    c.ellipse(44, 113, 3, 2, P["rock"])
    c.set(45, 111, P["rock_hi"])
    c.ellipse(90, 119, 4, 2, P["rock"])
    c.set(91, 117, P["rock_hi"])
    c.ellipse(30, 122, 3, 2, P["rock"])

    # ---------------- birds ----------------
    for (bx, by) in [(66, 22), (74, 28), (58, 33)]:
        c.set(bx, by, P["bird"])
        c.set(bx + 1, by + 1, P["bird"])
        c.set(bx + 2, by, P["bird"])

    # ---------------- foreground framing pines ----------------
    pine(6, 129, 48, 26, P["fpine_dk"], P["fpine_md"], P["fpine_lit"], P["fpine_dk"])
    pine(123, 129, 40, 22, P["fpine_dk"], P["fpine_md"], P["fpine_lit"], P["fpine_dk"])

    return c
