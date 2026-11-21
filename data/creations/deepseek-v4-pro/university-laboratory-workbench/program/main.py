# University laboratory workbench - 64x64 pixel art

# Palette (tuples are auto-registered on first use)
WALL        = (190, 202, 220)
WALL_DARK   = (166, 178, 198)
WINDOW_GLASS = (168, 210, 232)
WINDOW_FRAME = (70, 84, 102)

BENCH_TOP   = (172, 122, 76)
BENCH_TOP_HI = (196, 148, 96)
BENCH_FRONT = (126, 86, 52)
BENCH_DARK  = (82, 56, 34)
BENCH_LINE  = (60, 40, 24)

OUTLINE     = (36, 40, 50)

MIC_BODY    = (86, 112, 152)
MIC_DARK    = (52, 74, 108)
METAL       = (172, 180, 188)
METAL_DARK  = (106, 114, 122)
GLASS       = (206, 228, 238)
GLASS_DARK  = (152, 184, 200)

RACK_WOOD   = (152, 98, 56)
RACK_DARK   = (106, 68, 40)

LABEL_RED   = (214, 76, 76)
LABEL_BLUE  = (76, 132, 200)
LABEL_YELLOW = (236, 192, 76)
LIQ_BLUE    = (88, 156, 224)
LIQ_GREEN   = (112, 208, 120)
LIQ_RED     = (220, 92, 92)
LIQ_YELLOW  = (240, 202, 74)

PAPER       = (244, 238, 218)
PAPER_SHADOW = (220, 208, 180)
BOOK_COVER  = (120, 70, 50)

BULB        = (186, 64, 64)
AMBER       = (176, 118, 54)
AMBER_HI    = (204, 148, 78)
AMBER_DARK  = (140, 90, 40)
WHITE       = (244, 244, 240)


def draw_background(c):
    c.rect(0, 0, 64, 64, WALL)
    # baseboard just above the bench
    c.rect(0, 34, 64, 2, WALL_DARK)

    # window on the right, above where the test-tube rack sits
    c.rect(47, 6, 16, 15, WINDOW_FRAME)          # outer frame y6..20
    c.rect(48, 7, 14, 13, WINDOW_GLASS)          # glass y7..19
    c.rect(54, 7, 2, 13, WINDOW_FRAME)           # vertical mullion
    c.rect(48, 13, 14, 2, WINDOW_FRAME)          # horizontal mullion

    # bench
    c.rect(0, 36, 64, 7, BENCH_TOP)              # top surface y36..42
    c.rect(0, 36, 64, 1, BENCH_TOP_HI)           # highlight
    c.rect(0, 43, 64, 5, BENCH_FRONT)            # front apron y43..47
    c.rect(0, 43, 64, 1, BENCH_DARK)             # shadow under top edge
    c.rect(0, 48, 64, 16, BENCH_DARK)            # cabinet body y48..63

    # cabinet panel seams and handles
    c.rect(20, 48, 2, 16, BENCH_LINE)
    c.rect(42, 48, 2, 16, BENCH_LINE)
    c.rect(9, 54, 9, 2, METAL_DARK)
    c.rect(30, 54, 9, 2, METAL_DARK)
    c.rect(51, 54, 9, 2, METAL_DARK)


def draw_microscope(c):
    # base and foot
    c.rect(4, 33, 21, 8, MIC_BODY)      # x4..24, y33..40
    c.rect(3, 40, 23, 2, MIC_DARK)      # x3..25, y40..41

    # arm (left vertical) and head
    c.rect(7, 12, 5, 22, MIC_BODY)      # x7..11, y12..33
    c.rect(7, 10, 12, 4, MIC_BODY)      # x7..18, y10..13

    # eyepiece
    c.rect(11, 4, 5, 7, METAL_DARK)     # x11..15, y4..10
    c.rect(12, 3, 3, 1, OUTLINE)        # eyepiece lens

    # body tube down to the objective
    c.rect(13, 13, 5, 9, MIC_BODY)      # x13..17, y13..21
    c.rect(13, 13, 5, 1, MIC_DARK)      # tube shading

    # objective and tip
    c.rect(12, 21, 7, 5, MIC_DARK)      # x12..18, y21..25
    c.rect(13, 25, 5, 1, METAL)

    # stage and slide
    c.rect(12, 28, 14, 3, METAL)        # x12..25, y28..30
    c.rect(14, 27, 6, 1, GLASS)         # glass slide

    # substage condenser
    c.rect(14, 30, 5, 3, METAL_DARK)    # x14..18, y30..32

    # focus knobs on the arm
    c.circle(12, 24, 1, METAL_DARK)
    c.circle(12, 27, 1, METAL_DARK)


def draw_rack(c):
    # test tubes (drawn behind the wooden bars)
    tubes = [(52, LIQ_BLUE), (55, LIQ_GREEN), (58, LIQ_RED)]
    for tx, liq in tubes:
        c.rect(tx, 21, 2, 19, GLASS)     # glass tube y21..39
        c.rect(tx, 32, 2, 7, liq)        # liquid y32..38

    # wooden rack frame
    c.rect(49, 27, 15, 3, RACK_WOOD)     # top bar x49..63 y27..29
    c.rect(49, 36, 15, 3, RACK_WOOD)     # bottom bar y36..38
    c.rect(49, 27, 3, 14, RACK_WOOD)     # left side x49..51 y27..40
    c.rect(61, 27, 3, 14, RACK_WOOD)     # right side x61..63 y27..40

    # feet and handle
    c.rect(49, 40, 3, 2, RACK_DARK)
    c.rect(61, 40, 3, 2, RACK_DARK)
    c.rect(53, 24, 6, 2, RACK_DARK)      # carrying handle

    # frame outline for definition
    c.rect(49, 27, 15, 14, RACK_DARK, fill=False)


def draw_round_bottle(c):
    x = 27
    # cap and neck
    c.rect(x + 1, 25, 4, 3, OUTLINE)     # cap y25..27
    c.rect(x + 1, 28, 4, 2, GLASS)       # neck y28..29
    # sloped shoulders (flare from the neck to the body width)
    c.poly([(x + 1, 30), (x + 4, 30), (x + 6, 33), (x, 33)], GLASS)
    c.line(x + 1, 30, x, 33, GLASS_DARK)       # left shoulder slant
    c.line(x + 4, 30, x + 6, 33, GLASS_DARK)   # right shoulder slant
    # body
    c.rect(x, 33, 7, 8, GLASS)           # y33..40
    # red label with white stripe (kept above the notebook)
    c.rect(x, 32, 7, 3, LABEL_RED)       # y32..34
    c.rect(x, 33, 7, 1, WHITE)
    # yellow liquid
    c.rect(x, 35, 7, 5, LIQ_YELLOW)      # y35..39
    # glass shading and edge definition
    c.rect(x, 33, 1, 8, GLASS_DARK)            # left body edge
    c.rect(x + 6, 33, 1, 8, GLASS_DARK)        # right body edge
    c.rect(x, 40, 7, 1, GLASS_DARK)            # bottom edge


def draw_square_bottle(c):
    x = 35
    # cap and neck
    c.rect(x + 1, 27, 4, 2, OUTLINE)     # cap y27..28
    c.rect(x + 1, 29, 4, 2, GLASS)       # neck y29..30
    # rectangular body
    c.rect(x, 31, 7, 10, GLASS)          # y31..40
    # blue label with white stripe (kept above the notebook)
    c.rect(x, 31, 7, 3, LABEL_BLUE)      # y31..33
    c.rect(x, 32, 7, 1, WHITE)
    # green liquid
    c.rect(x, 34, 7, 5, LIQ_GREEN)       # y34..38
    # glass shading and edge definition
    c.rect(x, 31, 1, 10, GLASS_DARK)           # left body edge
    c.rect(x + 6, 31, 1, 10, GLASS_DARK)       # right body edge
    c.rect(x, 40, 7, 1, GLASS_DARK)            # bottom edge


def draw_dropper(c):
    x = 43
    # rubber bulb and glass dropper tube
    c.ellipse(x + 3, 26, 2, 3, BULB)     # x44..48, y23..29
    c.rect(x + 1, 29, 3, 4, GLASS)       # tube y29..32
    c.rect(x + 1, 32, 3, 2, METAL_DARK)  # cap y32..33
    # amber bottle body
    c.rect(x, 33, 6, 8, AMBER)           # y33..40
    c.rect(x + 1, 34, 1, 4, AMBER_HI)    # glass highlight
    # small white label with red stripe
    c.rect(x, 35, 6, 3, WHITE)           # y35..37
    c.rect(x, 36, 6, 1, LABEL_RED)
    # body outline
    c.rect(x, 33, 6, 8, AMBER_DARK, fill=False)


def draw_notebook(c):
    # open notebook lying on the bench, seen from above/front
    # cover shows as a border around the pages
    c.rect(23, 37, 19, 6, BOOK_COVER)      # x23..41, y37..42

    # two pages with a center gutter
    c.rect(24, 36, 7, 6, PAPER)            # left page x24..30, y36..41
    c.rect(34, 36, 7, 6, PAPER)            # right page x34..40, y36..41
    c.rect(31, 36, 3, 6, PAPER_SHADOW)     # gutter x31..33, y36..41

    # ruled lines
    for yy in range(38, 41):
        c.line(24, yy, 30, yy, PAPER_SHADOW)
        c.line(34, yy, 40, yy, PAPER_SHADOW)


def main():
    c = new_canvas(64, 64, name="workbench")
    draw_background(c)
    draw_microscope(c)
    draw_rack(c)
    draw_round_bottle(c)
    draw_square_bottle(c)
    draw_dropper(c)
    draw_notebook(c)

    finish(c)


main()
