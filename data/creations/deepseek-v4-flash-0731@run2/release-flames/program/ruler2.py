from pixelbench_api import new_canvas

def show(cv, x0, y0, x1, y1, legend=None):
    hdr1 = "     " + "".join(str((xx // 10) % 10) for xx in range(x0, x1 + 1))
    hdr2 = "     " + "".join(str(xx % 10) for xx in range(x0, x1 + 1))
    print(hdr1)
    print(hdr2)
    for yy in range(y0, y1 + 1):
        row = []
        for xx in range(x0, x1 + 1):
            idx = cv.get(xx, yy)
            if idx == 0:
                row.append(".")
            elif legend:
                row.append(legend[idx] if idx in legend else "?")
            else:
                row.append("#")
        print(f"{yy:3d} " + "".join(row))

# rebuild frame2-only legs and coat to view with legend
from pixelbench_api import input_canvas
c2 = input_canvas.color((11, 1, 2))
c4 = input_canvas.color((125, 66, 58))
c5 = input_canvas.color((1, 2, 2))
c6 = input_canvas.color((33, 29, 44))
c7 = input_canvas.color((69, 83, 99))
c8 = input_canvas.color((11, 11, 19))
c9 = input_canvas.color((74, 34, 45))
c10 = input_canvas.color((130, 134, 132))

f2 = new_canvas(100, 72)
f2.rect(13, 40, 7, 11, c7)
f2.rect(9, 50, 9, 4, c2)
f2.rect(27, 38, 8, 7, c7)
f2.rect(29, 44, 7, 9, c7)
f2.rect(33, 52, 11, 4, c2)
f2.rect(43, 53, 3, 3, c2)
f2.outline(c5)
f2.poly([(18, 17), (31, 23), (35, 44), (16, 40)], c4, fill=True)
f2.line(16, 41, 35, 45, c9)

leg = {c2: "b", c5: "x", c7: "H", c4: "R", c9: "j", c6: "g", c8: "i"}
show(f2, 4, 36, 50, 58, leg)
