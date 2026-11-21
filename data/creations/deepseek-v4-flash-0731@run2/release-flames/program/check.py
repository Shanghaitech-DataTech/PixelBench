from pixelbench_api import input_canvas, new_canvas, finish

c0 = input_canvas.color((106, 108, 107))
c1 = input_canvas.color((36, 11, 12))
c2 = input_canvas.color((11, 1, 2))
c3 = input_canvas.color((68, 61, 69))
c4 = input_canvas.color((125, 66, 58))
c5 = input_canvas.color((1, 2, 2))
c6 = input_canvas.color((33, 29, 44))
c7 = input_canvas.color((69, 83, 99))
c8 = input_canvas.color((11, 11, 19))
c9 = input_canvas.color((74, 34, 45))
c10 = input_canvas.color((130, 134, 132))
c11 = input_canvas.color((223, 178, 172))
c12 = input_canvas.color((242, 114, 25))
c13 = input_canvas.color((244, 163, 12))
c14 = input_canvas.color((254, 211, 44))

def grab(src, x0, y0, x1, y1):
    g = new_canvas(x1 - x0 + 1, y1 - y0 + 1)
    for yy in range(y0, y1 + 1):
        for xx in range(x0, x1 + 1):
            g.set(xx - x0, yy - y0, src.get(xx, yy))
    return g

def put(cv, pts):
    for (x, y, cl) in pts:
        cv.set(x, y, cl)

f1 = new_canvas(100, 72)
f1.blit(input_canvas, 0, 0)

f2 = new_canvas(100, 72)
# legs
f2.rect(13, 40, 7, 11, c7)
f2.rect(9, 50, 9, 4, c2)
put(f2, [(15, 43, c6), (14, 46, c6), (11, 51, c8), (12, 52, c8)])
f2.set(10, 53, c8)
f2.rect(27, 38, 8, 7, c7)
f2.rect(29, 44, 7, 9, c7)
f2.rect(33, 52, 11, 4, c2)
f2.rect(43, 53, 3, 3, c2)
put(f2, [(27, 39, c8), (30, 41, c6), (30, 45, c6), (31, 47, c6),
        (30, 49, c6), (35, 53, c8), (37, 54, c8)])
f2.outline(c5)
# coat
f2.poly([(18, 17), (31, 23), (35, 44), (16, 40)], c4, fill=True)
f2.line(18, 17, 16, 40, c2)
f2.line(16, 40, 35, 44, c2)
f2.line(31, 23, 35, 44, c2)
f2.line(16, 41, 35, 45, c9)
put(f2, [(29, 25, c9), (30, 28, c9), (31, 31, c9), (32, 34, c9), (33, 37, c9),
        (33, 40, c9), (34, 42, c9), (30, 24, c9)])
f2.line(27, 25, 31, 36, c2)
f2.line(18, 34, 33, 37, c2)
f2.line(18, 35, 33, 38, c2)
f2.rect(24, 35, 3, 2, c10)
# left arm
f2.line(20, 20, 12, 29, c2)
f2.line(20, 21, 12, 30, c4)
f2.line(20, 22, 12, 31, c4)
f2.line(20, 23, 12, 32, c9)
f2.rect(10, 30, 5, 4, c2, fill=False)
f2.rect(11, 31, 3, 2, c11)
put(f2, [(11, 31, c1), (12, 31, c1), (10, 30, c1)])
# head
f2.blit(grab(input_canvas, 10, 0, 32, 18), 17, 1)
# right arm
f2.line(29, 23, 45, 27, c2)
f2.line(29, 24, 45, 28, c4)
f2.line(29, 25, 45, 29, c4)
f2.line(29, 26, 45, 30, c9)
f2.rect(45, 26, 5, 5, c2, fill=False)
f2.rect(46, 28, 3, 3, c11)
put(f2, [(46, 27, c1), (47, 27, c1), (49, 27, c1), (45, 28, c1), (48, 31, c1)])
# fireball
f2.circle(54, 21, 5, c12)
f2.circle(54, 21, 4, c13)
f2.circle(54, 21, 3, c14)
put(f2, [(55, 16, c12), (54, 15, c13), (53, 16, c13), (56, 17, c14),
        (60, 18, c12), (61, 19, c13), (60, 21, c13), (59, 16, c12), (58, 15, c13)])
put(f2, [(50, 24, c14), (51, 23, c13), (50, 22, c12), (48, 25, c14), (49, 26, c13)])
put(f2, [(48, 22, c12), (46, 21, c12), (44, 20, c13), (42, 19, c13), (40, 18, c14),
        (38, 17, c13), (36, 16, c12), (34, 15, c12), (32, 14, c13), (30, 13, c13),
        (28, 12, c14), (26, 11, c13), (24, 10, c12),
        (47, 24, c13), (45, 25, c12), (43, 26, c13), (41, 27, c14), (39, 28, c12),
        (37, 19, c12), (33, 18, c12), (31, 17, c13), (27, 15, c12)])
put(f2, [(46, 19, c13), (43, 17, c12), (39, 20, c13), (35, 18, c14), (29, 16, c13),
        (25, 13, c12), (44, 24, c14), (40, 26, c13)])
put(f2, [(63, 14, c13), (66, 17, c12), (69, 11, c14), (72, 15, c13), (75, 9, c14),
        (78, 13, c12), (81, 7, c13), (84, 11, c14), (87, 6, c14), (90, 10, c13),
        (93, 5, c12), (96, 8, c14), (99, 6, c13), (62, 20, c12), (65, 22, c13),
        (68, 16, c14), (71, 13, c12), (74, 12, c13), (77, 10, c14), (80, 9, c12),
        (83, 8, c13), (86, 12, c14), (89, 9, c13), (92, 11, c12), (95, 10, c14),
        (98, 13, c13)])

print("A: torso+legs (8,34)-(58,62):")
print(f2.matrix_text(region=(8, 34, 58, 62)))
print()
print("B: arm+ball (24,6)-(68,34):")
print(f2.matrix_text(region=(24, 6, 68, 34)))
