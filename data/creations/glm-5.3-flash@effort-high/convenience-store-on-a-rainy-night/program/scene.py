import random
from pixelbench_api import *

def build():
    c = new_canvas(64, 64, background="#101426", name="store")

    # ---------- night sky (rows 0..6) ----------
    c.rect(0, 0, 64, 3, "#0c1020")
    c.ellipse(10, 2, 12, 3, "#0c1020")
    c.ellipse(48, 1, 14, 3, "#0c1020")

    # ---------- building wall ----------
    c.rect(2, 7, 60, 38, "#343a52")          # wall y7..44
    c.line(2, 7, 61, 7, "#454c6a")           # top highlight
    c.line(3, 22, 3, 44, "#2c3048")          # drain pipe left

    # ---------- sign band ----------
    c.rect(2, 7, 60, 8, "#232840")
    c.line(2, 14, 61, 14, "#454c6a")
    c.text(18, 7, "STORE", "#ffd98a", font="5x7")

    # ---------- awning (striped, scalloped) ----------
    for i in range(10):
        x0 = 2 + i * 6
        col = "#2f5a52" if i % 2 == 0 else "#3f7568"
        c.rect(x0, 15, 6, 5, col)
        c.rect(x0 + 1, 20, 4, 1, col)
        c.rect(x0 + 2, 21, 2, 1, col)

    # ---------- big glass window (x5..33) ----------
    c.rect(5, 22, 29, 21, "#4a5068")         # frame y22..42
    c.rect(6, 23, 27, 19, "#f2dfa8")         # glass y23..41
    c.rect(6, 23, 27, 3, "#fdf3cf")          # brighter top glow
    c.rect(19, 23, 1, 19, "#4a5068")         # mullion

    # interior shelves + goods
    c.rect(7, 34, 25, 1, "#a87c3c")
    c.rect(7, 39, 25, 1, "#a87c3c")
    c.rect(7, 41, 25, 1, "#a87c3c")
    goods_top = ["#b05a4a", "#4a7a5a", "#5a6fa0", "#8a6230"]
    gt = 0
    for gx in [8, 11, 14, 23, 26, 29]:
        c.rect(gx, 32, 2, 2, goods_top[gt % 4]); gt += 1
    for gx in [7, 10, 13, 16, 22, 25, 28, 31]:
        c.rect(gx, 37, 2, 2, goods_top[gt % 4]); gt += 1

    # OPEN sign hanging in the window
    c.text(8, 25, "OPEN", "#e0e8ff", font="5x7")

    # ---------- door (x40..50) ----------
    c.rect(40, 22, 11, 22, "#4a5068")        # frame y22..43
    c.rect(41, 25, 9, 16, "#f2dfa8")         # glass y25..40
    c.rect(41, 25, 9, 2, "#fdf3cf")
    c.rect(48, 32, 1, 5, "#6a7086")          # metal handle (right side)

    # ---------- poster on right wall ----------
    c.rect(54, 27, 6, 9, "#262b42")
    c.rect(55, 29, 4, 1, "#4a5070")
    c.rect(55, 31, 4, 1, "#4a5070")
    c.rect(55, 33, 3, 1, "#4a5070")

    # ---------- umbrella rack between window and door ----------
    c.rect(35, 42, 5, 4, "#4a3a2c")
    c.rect(35, 42, 5, 1, "#241c14")
    c.line(36, 28, 36, 42, "#6a5a3a")        # red umbrella pole
    c.poly([(34, 31), (36, 27), (38, 31)], "#c04545")
    c.set(36, 26, "#c04545")
    c.line(38, 34, 38, 42, "#6a5a3a")        # blue umbrella pole
    c.poly([(36, 37), (38, 33), (40, 37)], "#3f6fa8")
    c.set(38, 32, "#3f6fa8")

    # ---------- ground ----------
    c.rect(0, 45, 64, 5, "#4c5164")          # sidewalk y45..49
    for sx in range(0, 64, 8):
        c.line(sx, 45, sx, 48, "#41465a")    # slab joints
    c.line(0, 49, 63, 49, "#6a7086")         # curb
    c.rect(0, 50, 64, 14, "#262a38")         # road
    for sx in [6, 18, 30, 44, 57]:
        c.set(sx, 52 + (sx % 5), "#1e2230")
        c.set(sx + 3, 55 + (sx % 4), "#1e2230")

    # warm light spill on the sidewalk
    c.rect(6, 45, 27, 1, "#6b5a3c")
    c.rect(6, 46, 27, 2, "#57492f")
    c.rect(40, 45, 11, 1, "#6b5a3c")
    c.rect(40, 46, 11, 2, "#57492f")

    # ---------- puddles ----------
    c.ellipse(14, 57, 11, 3, "#3a4158")
    c.ellipse(14, 57, 10, 2, "#2c3244")
    c.ellipse(40, 59, 12, 3, "#3a4158")
    c.ellipse(40, 59, 11, 2, "#2c3244")
    c.ellipse(56, 53, 5, 2, "#3a4158")
    c.ellipse(56, 53, 4, 1, "#2c3244")

    # window reflections in the puddles
    for x in range(9, 25):
        if (x // 2) % 2 == 0:
            col = "#f2dfa0" if x % 3 else "#d8b060"
            for y in range(55, 60, 2):
                c.set(x, y, col)
    for x in range(31, 47):
        if (x // 2) % 2 == 0:
            col = "#f2dfa0" if x % 3 else "#d8b060"
            for y in range(57, 62, 2):
                c.set(x, y, col)
    # person's reflection
    c.rect(44, 58, 2, 2, "#c79a30")
    # wet sheen streaks on road
    c.line(4, 54, 20, 54, "#333a50")
    c.line(34, 56, 52, 56, "#333a50")
    c.line(10, 61, 26, 61, "#333a50")

    # ---------- parked bicycle, left, against the lit window ----------
    c.circle(11, 42, 3, "#1c202b", fill=False)
    c.circle(21, 42, 3, "#1c202b", fill=False)
    c.set(11, 42, "#6a7086"); c.set(21, 42, "#6a7086")
    c.line(11, 42, 16, 42, "#2f5a52")        # chainstay
    c.line(16, 42, 15, 38, "#2f5a52")        # seat tube
    c.line(16, 42, 20, 39, "#2f5a52")        # down tube
    c.line(15, 38, 20, 39, "#2f5a52")        # top tube
    c.line(20, 39, 21, 42, "#2f5a52")        # fork
    c.rect(13, 37, 3, 1, "#1c202b")          # saddle
    c.line(20, 39, 22, 37, "#2f5a52")        # stem
    c.set(23, 37, "#2f5a52")                 # handlebar

    # ---------- person in yellow raincoat at the door ----------
    c.ellipse(45, 33, 2, 2, "#f0c040")       # hood
    c.set(44, 33, "#5a3a20"); c.set(44, 34, "#5a3a20")  # face shadow
    c.poly([(42, 36), (48, 36), (49, 44), (41, 44)], "#f0c040")   # coat
    c.poly([(46, 36), (48, 36), (49, 44), (46, 44)], "#d09a28")   # shade
    c.line(47, 38, 48, 36, "#d09a28")        # arm reaching for handle
    c.rect(42, 45, 3, 1, "#1a1c26")          # shoes on sidewalk
    c.rect(46, 45, 3, 1, "#1a1c26")

    # ---------- rain ----------
    random.seed(11)
    for i in range(42):
        x = random.randint(1, 65)
        y = random.randint(0, 58)
        col = "#6d7ca6" if i % 3 else "#9fb0d6"
        c.line(x, y, x - 1, y + 4, col)
    # drips off the awning edge
    for dx in [5, 12, 19, 26, 33, 44, 51, 58]:
        c.line(dx, 21, dx, 23, "#8fa0c8")
    # splash flecks near the ground
    for (sx, sy) in [(10, 51), (22, 53), (36, 51), (50, 52), (60, 56), (16, 62), (44, 63)]:
        c.set(sx, sy, "#8fa0c8")

    return c

if __name__ == "__main__":
    from pixelbench_api import save, finish
    c = build()
    save("store", c)
    print(c.stats_text())
    finish(c)
