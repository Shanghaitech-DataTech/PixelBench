from pixelbench_api import *

s = input_canvas.select(0, 0, 93, 128)
s1 = s.rotate(135)

c_knife = new_canvas(s1.size[0], s1.size[1])
s1.copy_to(0, 0, c_knife)

c_after1 = new_canvas(s1.size[0], s1.size[1])
c_after2 = new_canvas(s1.size[0], s1.size[1])
for y in range(s1.size[1]):
    for x in range(s1.size[0]):
        idx = c_knife.get(x, y)
        rgba = c_knife.palette()[idx]['rgba']
        if rgba[3] > 0:
            c_after1.set(x, y, (rgba[0], rgba[1], rgba[2], int(rgba[3] * 0.25)))
            c_after2.set(x, y, (rgba[0], rgba[1], rgba[2], int(rgba[3] * 0.5)))

c_main = new_canvas(320, 160)
c_main.blit(c_after1, 0, 0)
c_main.blit(c_after2, 40, 0)
c_main.blit(c_knife, 80, 0)

# White slash effect
c_main.path("M 233 91 L 270 90 L 310 91 L 270 92 Z", "#ffffff")
c_main.path("M 190 82 L 230 81 L 260 82 L 230 83 Z", "#ffffff")
c_main.path("M 180 100 L 220 99 L 250 100 L 220 101 Z", "#ffffff")

c_main.line(260, 85, 275, 85, "#ffffff")
c_main.line(255, 96, 280, 96, "#ffffff")
c_main.line(240, 75, 250, 75, "#ffffff")
c_main.line(230, 105, 245, 105, "#ffffff")

finish(c_main)
