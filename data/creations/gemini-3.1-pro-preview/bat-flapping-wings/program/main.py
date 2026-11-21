from pixelbench_api import *

# Frame 1: Original picture on a 40x30 canvas
f1 = new_canvas(40, 30, name="frame1")
f1.blit(input_canvas, 6, 4)

# Frame 2: Bat with raised wings
f2 = new_canvas(40, 30, name="frame2")

cmap = {
    'a': '#1d181eff',
    'b': '#7784a2ff',
    'c': '#b572b1ff',
    'd': '#432f53ff',
    'e': '#5f5f7bff',
    'f': '#ae0000ff',
    'g': '#fff9d6ff',
    'h': '#5c436fff',
}

body_pixels = [
    "          a     a          ", # 0
    "         aba   aba         ", # 1
    "         acdaaadca         ", # 2
    "         acbdbdeca         ", # 3
    "         daaebbaad         ", # 4
    "         dafabafad         ", # 5
    "          adcbeda          ", # 6
    "          aagagaa          ", # 7
    "         aehahahha         ", # 8
    "         aeehhhhea         ", # 9
    "         abeeheeba         ", # 10
    "        a.abbbbba.a        ", # 11
    "          abbabba          ", # 12
    "          aha.aha          ", # 13
    "          aha.aha          ", # 14
    "           a   a           ", # 15
]

for y, row in enumerate(body_pixels):
    for x, char in enumerate(row):
        if char != ' ' and char != '.':
            f2.set(x + 6, y + 4, cmap[char])

left_wing = [
    #0123456789012345
    "   dddd         ", # 2
    "  ddccccd       ", # 3
    " ddcceeeccd     ", # 4
    " dcceeeeeecdd   ", # 5
    " dceeeeeeeehcd  ", # 6
    "dceeeeeeeeehhcd ", # 7
    "dceeeeeeeeehhcd ", # 8
    "dceeeeeeeehhhcd ", # 9
    " dceeeeeeehhhcdd", # 10
    " dceeeeehhhhhcdd", # 11
    "  dceeeehhhhhcd ", # 12
    "  dceehhhhhhhcd ", # 13
    "   dcehhhhhhhcd ", # 14
    "    dchhhhhhcd  ", # 15
    "    dchhhhhcdd  ", # 16
    "     dhhhhcdd   ", # 17
    "     dhhhcdd    ", # 18
    "      dhhcd     ", # 19
    "      dhdd      ", # 20
    "       add      ", # 21
]

for y, row in enumerate(left_wing):
    for x, char in enumerate(row):
        if char != ' ':
            f2.set(x, y + 2, cmap[char])
            f2.set(38 - x, y + 2, cmap[char])

finish([f1, f2])
