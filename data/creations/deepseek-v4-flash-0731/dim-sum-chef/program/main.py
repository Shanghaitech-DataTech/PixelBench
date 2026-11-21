from pixelbench_api import *

OUT = "#23262e"
SKIN = "#f0c39a"
HAIR = "#42302c"
WHITE = "#fdfdfd"
HAT_S = "#d8d8de"
UNI = "#3d7d8c"
APRON = "#f4f2ec"
DUST = "#d6d3cc"
BAMBOO = "#c98a4b"
BAMBOO_D = "#9c5f26"
INNER = "#4e3117"
BUN = "#fff6e0"
BUN_S = "#e6d5ae"
BLUSH = "#e99a88"
MOUTH = "#7c4038"
SHOE = "#1f2329"


def main():
    c = new_canvas(32, 32)

    # ---- arms (behind torso / steamer)
    c.rect(8, 13, 2, 9, UNI)
    c.rect(22, 13, 2, 9, UNI)

    # ---- torso / uniform
    c.rect(9, 13, 14, 16, UNI)      # x9-22, y13-28

    # ---- apron (white bib + lower flap, flour dust)
    c.rect(12, 14, 8, 6, APRON)     # bib y14-19
    c.rect(11, 27, 10, 2, APRON)    # lower apron y27-28
    for x, y in [(13, 15), (16, 16), (18, 15), (14, 17),
                 (17, 18), (15, 19), (13, 27), (18, 28)]:
        c.set(x, y, DUST)

    # ---- legs + shoes
    c.rect(11, 29, 4, 2, UNI)       # y29-30
    c.rect(17, 29, 4, 2, UNI)
    c.rect(10, 31, 5, 1, SHOE)
    c.rect(17, 31, 5, 1, SHOE)

    # ---- chef hat
    c.rect(13, 0, 6, 1, WHITE)
    c.rect(11, 1, 10, 2, WHITE)
    c.rect(10, 3, 12, 2, WHITE)
    c.rect(11, 5, 10, 1, HAT_S)     # band

    # ---- head
    c.ellipse(16, 9, 4, 3.5, SKIN)  # face
    c.rect(11, 8, 1, 3, SKIN)       # ears
    c.rect(20, 8, 1, 3, SKIN)
    c.rect(13, 6, 5, 1, SKIN)       # forehead right under the band
    c.set(12, 6, HAIR)
    c.set(19, 6, HAIR)
    c.set(13, 8, HAIR)
    c.set(18, 8, HAIR)
    c.set(13, 9, OUT)
    c.set(18, 9, OUT)
    c.set(14, 11, MOUTH)
    c.set(15, 11, MOUTH)
    c.set(16, 11, MOUTH)
    c.set(13, 10, BLUSH)
    c.set(18, 10, BLUSH)

    # ---- hat fold shading (inside the crown; drawn before the outline)
    c.set(12, 2, HAT_S)
    c.set(18, 2, HAT_S)
    c.set(15, 1, HAT_S)
    c.set(15, 3, HAT_S)

    # ---- bamboo steamer
    c.ellipse(16, 21, 7, 4.5, BAMBOO)
    c.ellipse(16, 21, 6, 3.4, BAMBOO_D)
    c.ellipse(16, 21, 5, 2.7, INNER)

    # ---- buns inside steamer
    c.ellipse(13, 21, 1.6, 1.7, BUN)
    c.ellipse(16, 20.8, 1.6, 1.7, BUN)
    c.ellipse(19, 21, 1.6, 1.7, BUN)
    c.set(13, 22, BUN_S)
    c.set(16, 22, BUN_S)
    c.set(19, 22, BUN_S)

    # ---- hands gripping the rim
    c.ellipse(9, 21, 1.8, 2.3, SKIN)    # left hand
    c.ellipse(23, 21, 1.8, 2.3, SKIN)   # right hand

    # ---- unified dark outline
    c.outline(OUT)

    print(c.stats_text())
    print(c.matrix_text())
    symbols = {9:'#', 5:'W', 6:'s', 7:'G', 8:'H', 10:'M', 11:'B',
               1:'U', 2:'A', 3:'d', 12:'L', 13:'l', 14:'n', 15:'o', 16:'p'}
    print("ROW MAP", symbols)
    for yy in range(32):
        row = ''
        for xx in range(32):
            idx = c.get(xx, yy)
            row += symbols.get(idx, '.')
        print(f"{yy:02d} {row}")
    finish(c)


main()
