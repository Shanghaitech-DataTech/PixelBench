from pixelbench_api import *

def main():
    c = new_canvas(32, 32)
    c.color("#1A3B1A", "outline")
    c.color("#4A7C3C", "shadow")
    c.color("#7CB342", "base")
    c.color("#AED581", "light")
    c.color("#E8F5E9", "high")
    c.color("#795548", "stem")

    pear_bounds = {
        6: (14, 18),
        7: (13, 19),
        8: (13, 19),
        9: (13, 19),
        10: (12, 20),
        11: (12, 20),
        12: (12, 20),
        13: (11, 21),
        14: (11, 21),
        15: (10, 22),
        16: (9, 23),
        17: (8, 24),
        18: (7, 25),
        19: (6, 26),
        20: (5, 27),
        21: (5, 27),
        22: (4, 28),
        23: (4, 28),
        24: (4, 28),
        25: (4, 28),
        26: (5, 27),
        27: (6, 26),
        28: (8, 24),
        29: (10, 22),
        30: (13, 19)
    }

    for y, (x0, x1) in pear_bounds.items():
        c.line(x0, y, x1, y, "base")

    # Shadow
    for y, (x0, x1) in pear_bounds.items():
        if y >= 29:
            c.line(x0, y, x1, y, "shadow")
        elif y >= 27:
            c.line(x0, y, x0+1, y, "shadow")
            c.line(x1-5, y, x1, y, "shadow")
        elif y >= 25:
            c.line(x0, y, x0+1, y, "shadow")
            c.line(x1-4, y, x1, y, "shadow")
        elif y >= 20:
            c.line(x1-4, y, x1, y, "shadow")
        elif y >= 15:
            c.line(x1-3, y, x1, y, "shadow")
        elif y >= 10:
            c.line(x1-2, y, x1, y, "shadow")
        else:
            c.line(x1-1, y, x1, y, "shadow")

    # Light
    for y, (x0, x1) in pear_bounds.items():
        if 7 <= y <= 9:
            c.line(x0, y, x0+2, y, "light")
        elif 10 <= y <= 12:
            c.line(x0, y, x0+3, y, "light")
        elif 13 <= y <= 16:
            c.line(x0, y, x0+4, y, "light")
        elif 17 <= y <= 21:
            c.line(x0, y, x0+5, y, "light")
        elif 22 <= y <= 25:
            c.line(x0+1, y, x0+6, y, "light")
        elif 26 <= y <= 27:
            c.line(x0+2, y, x0+7, y, "light")

    # Highlight
    c.set(14, 8, "high")
    c.set(14, 9, "high")
    c.line(13, 10, 14, 10, "high")
    c.line(13, 11, 14, 11, "high")
    
    c.line(8, 17, 9, 17, "high")
    c.line(7, 18, 10, 18, "high")
    c.line(7, 19, 10, 19, "high")
    c.line(6, 20, 10, 20, "high")
    c.line(6, 21, 10, 21, "high")
    c.line(6, 22, 9, 22, "high")
    c.line(7, 23, 8, 23, "high")

    # Dimple
    c.line(15, 7, 17, 7, "shadow")
    c.set(16, 8, "shadow")

    c.outline("outline")

    # Stem
    c_stem = new_canvas(32, 32)
    for dx, dy in [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]:
        c_stem.line(15+dx, 8+dy, 18+dx, 2+dy, "outline")
        c_stem.line(16+dx, 8+dy, 19+dx, 2+dy, "outline")
    c_stem.line(15, 8, 18, 2, "stem")
    c_stem.line(16, 8, 19, 2, "stem")

    # Leaf
    c_leaf = new_canvas(32, 32)
    c_leaf.poly([(17, 6), (20, 3), (25, 3), (30, 8), (26, 11), (21, 11)], "base")
    c_leaf.poly([(17, 6), (20, 3), (25, 3), (30, 8), (24, 7), (20, 7)], "light")
    c_leaf.line(17, 6, 29, 8, "shadow") # vein
    c_leaf.outline("outline")

    final = flatten([c_stem, c, c_leaf])
    
    finish(final)

if __name__ == "__main__":
    main()
