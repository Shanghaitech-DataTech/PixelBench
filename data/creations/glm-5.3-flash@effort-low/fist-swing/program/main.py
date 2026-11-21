# fist-swing: frame1 = original, frame2 = left-fist punch (arm extending right)

W, H = 38, 44
OX = 4  # input placed at x=4

f1 = new_canvas(W, H, name="f1")
f1.blit(input_canvas, OX, 0)

f2 = f1.copy(name="f2")

a = "#222034ff"  # outline
e = "#df7126ff"  # sleeve (orange)
c = "#eec39aff"  # skin
f = "#8f563bff"  # brown detail

# remove the old bent arm (canvas coords: orig x+4)
f2.clear(OX + 15, 9, 12, 7)   # x19-30, y9-15

# new straight punching arm: rows 10-13, from shoulder x21 to fist x33
f2.rect(21, 10, 9, 4, e)          # sleeve
f2.rect(30, 10, 4, 4, c)          # fist
f2.line(31, 10, 31, 13, f)        # knuckle line
# outline
f2.line(21, 9, 33, 9, a)
f2.line(21, 14, 33, 14, a)
f2.line(34, 10, 34, 13, a)
f2.line(20, 10, 20, 13, a)
# bridge to shoulder
f2.set(19, 9, e)
f2.set(20, 9, e)
f2.set(19, 10, e)
# small speed lines behind the arm
f2.line(15, 10, 17, 10, a)
f2.line(14, 12, 17, 12, a)

print(f1.stats_text())
print(f2.stats_text())
print(f2.matrix_text(region=(10, 6, 36, 17)))

save("fist_frame1", f1)
save("fist_frame2", f2)
finish([f1, f2])
