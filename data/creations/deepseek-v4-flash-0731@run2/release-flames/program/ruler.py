from pixelbench_api import input_canvas, new_canvas

c7 = input_canvas.color((69, 83, 99))

def show(cv, x0, y0, x1, y1):
    # ruler with tens row and units row
    w = x1 - x0 + 1
    hdr1 = "     " + "".join(str((xx // 10) % 10) for xx in range(x0, x1 + 1))
    hdr2 = "     " + "".join(str(xx % 10) for xx in range(x0, x1 + 1))
    print(hdr1)
    print(hdr2)
    for yy in range(y0, y1 + 1):
        row = []
        for xx in range(x0, x1 + 1):
            idx = cv.get(xx, yy)
            row.append("." if idx == 0 else "#")
        print(f"{yy:3d} " + "".join(row))

f2 = new_canvas(100, 72)
f2.rect(13, 40, 7, 11, c7)
f2.rect(9, 50, 9, 4, c7)
show(f2, 4, 36, 40, 60)
