from pixelbench_api import new_canvas, finish, input_canvas

c = new_canvas(32, 32)

WO = (250, 244, 230)
WB = (240, 228, 204)
WS = (222, 204, 174)
GR = (202, 182, 154)
SK = (247, 207, 197)
SK2 = (236, 188, 178)
EA = (242, 178, 163)
DK = (72, 58, 52)

# ---- back legs ----
for x in (9, 14, 20, 26):
    c.rect(x, 25, 3, 5, WS)
    c.rect(x, 28, 3, 1, GR)

# ---- body wool ----
c.ellipse(18, 19, 9, 6, WB)          # main torso
c.circle(14, 12, 5, WB)
c.circle(20, 11, 5, WB)
c.circle(25, 14, 4, WB)
c.circle(27, 18, 4, WB)
c.circle(11, 18, 4, WB)
c.circle(17, 12, 4, WB)
c.circle(22, 13, 4, WB)
# shade + highlight
c.ellipse(18, 22, 8, 4, WS)
c.ellipse(17, 14, 6, 3, WO)

# ---- head (side facing left) ----
# wool bump connecting to body
c.circle(8, 12, 4, WB)
# head face (pink)
c.poly([(4,12),(10,10),(13,12),(13,17),(9,18),(5,16)], SK)
# wool cap on head
c.circle(10, 9, 3, WB)
c.circle(7, 10, 3, WB)
# ear (drooping pink)
c.ellipse(12, 9, 2, 2, EA)
c.ellipse(13, 11, 1, 2, EA)
# eye
c.set(6, 13, DK)
c.set(6, 14, DK)
# nose
c.set(4, 15, DK)
c.set(5, 16, DK)
c.set(4, 16, SK2)

# ---- tail ----
c.circle(27, 14, 3, WB)
c.circle(29, 16, 2, WB)

# soft ground shadow
c.ellipse(17, 29, 11, 2, (196, 176, 148))

print(c.stats_text())
finish(c)
print(c.matrix_text())
