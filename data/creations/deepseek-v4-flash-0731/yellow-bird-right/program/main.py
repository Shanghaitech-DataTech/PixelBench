from pixelbench_api import *

out = input_canvas.copy(name="output")
pal = out.palette()
def rgba_of(i):
    return tuple(pal[i]['rgba'])

BLUE = (0, 151, 224, 255)
LIGHTBLUE = (46, 205, 245, 255)
Y = out.color("#ffd21a", name="body_yellow")
LY = out.color("#fff59b", name="light_yellow")

# Two parrots face each other, separated by a white gap around columns 29-34.
# The right parrot occupies x >= 33.  Recolour its blue body to yellow and its
# light-blue accents to a lighter yellow, leaving the left parrot untouched.
for y in range(64):
    for x in range(64):
        if x >= 33:
            r = rgba_of(out.get(x, y))
            if r == BLUE:
                out.set(x, y, Y)
            elif r == LIGHTBLUE:
                out.set(x, y, LY)

print(out.stats_text())
print(out.matrix_text(region=(30, 14, 63, 47), indices=False))

finish(out)
