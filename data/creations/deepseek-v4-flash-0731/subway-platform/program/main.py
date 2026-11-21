from pixelbench_api import new_canvas, finish

c = new_canvas(64, 64)

def mix(col, t, base=(0, 0, 0)):
    return tuple(round(base[i] + (col[i] - base[i]) * t) for i in range(3))

def overlay(c, x0, y0, x1, y1, rgb, t):
    pl = {e['index']: e['rgba'] for e in c.palette()}
    for y in range(y0, y1):
        for x in range(x0, x1):
            e = pl.get(c.get(x, y))
            base = e[:3] if e else (0, 0, 0)
            c.set(x, y, mix(rgb, t, base))

# ---------------- back wall & ceiling ----------------
c.rect(0, 0, 64, 4, (38, 38, 48))
c.rect(0, 4, 20, 9, (198, 200, 210))
c.rect(20, 4, 24, 9, (206, 208, 218))
c.rect(44, 4, 20, 9, (214, 216, 226))

# ceiling lights, receding to the right (depth)
c.rect(11, 0, 14, 2, (176, 176, 184))
c.rect(13, 1, 10, 1, (252, 250, 224))
overlay(c, 9, 0, 26, 4, (255, 250, 200), 0.30)
c.rect(35, 0, 9, 2, (176, 176, 184))
c.rect(37, 1, 6, 1, (250, 248, 220))
overlay(c, 33, 0, 44, 3, (255, 250, 200), 0.22)
c.rect(52, 0, 5, 2, (176, 176, 184))
c.rect(53, 1, 3, 1, (248, 246, 218))
overlay(c, 50, 0, 57, 3, (255, 250, 200), 0.16)

# ---------------- station signs (no brand names) ----------------
c.rect(2, 4, 45, 9, (20, 58, 152))
c.text(6, 5, "STATION", (250, 250, 250))
c.rect(50, 4, 12, 9, (190, 70, 60))
c.rect(53, 7, 6, 2, (250, 250, 250))
c.poly([(59, 6), (62, 8), (59, 10)], (250, 250, 250))

# ---------------- train arriving behind the doors ----------------
c.rect(0, 12, 64, 1, (112, 26, 22))            # roof edge
c.rect(0, 13, 64, 24, (190, 56, 46))           # train body
c.rect(0, 34, 64, 3, (104, 30, 26))            # dark skirt
for d in range(8):
    x = d * 8
    if d % 2 == 0:
        c.rect(x + 1, 15, 6, 12, (196, 224, 244))   # interior window
        c.rect(x + 2, 16, 4, 10, (222, 240, 252))
        c.rect(x + 2, 23, 4, 1, (168, 200, 226))
    else:
        c.rect(x + 1, 17, 6, 3, (206, 96, 86))      # motion streaks
        c.rect(x + 1, 26, 6, 2, (200, 88, 80))
        c.rect(x + 2, 18, 4, 1, (232, 142, 130))
        c.rect(x + 2, 27, 4, 1, (220, 122, 112))
c.circle(2, 30, 2, (255, 236, 170))            # headlight
c.set(2, 30, (255, 252, 235))
c.set(1, 29, (255, 240, 190))

# ---------------- platform screen doors ----------------
for f in (0, 8, 16, 24, 32, 40, 48, 56):
    c.rect(f, 13, 2, 26, (226, 229, 235))
for p in (2, 10, 18, 26, 34, 42, 50, 58):
    overlay(c, p, 14, p + 6, 38, (152, 206, 238), 0.40)
c.rect(0, 26, 64, 1, (214, 218, 224))          # door mid rail
overlay(c, 3, 17, 6, 21, (244, 250, 255), 0.22)
overlay(c, 18, 18, 21, 22, (244, 250, 255), 0.22)
overlay(c, 34, 18, 37, 22, (244, 250, 255), 0.22)
overlay(c, 42, 19, 45, 23, (244, 250, 255), 0.22)
overlay(c, 58, 16, 61, 20, (244, 250, 255), 0.16)
# headlight glow through the glass of the first door
c.set(4, 28, (255, 236, 170))
c.set(4, 29, (232, 190, 132))
c.set(5, 28, (240, 204, 150))

# ---------------- platform floor ----------------
c.rect(0, 38, 64, 1, (204, 206, 214))
c.rect(0, 39, 64, 25, (152, 152, 162))
c.rect(0, 43, 64, 20, (148, 148, 158))
for x in range(8, 64, 8):
    c.rect(x, 43, 1, 18, (136, 136, 146))
c.rect(0, 52, 64, 1, (132, 132, 142))
c.rect(0, 62, 64, 2, (102, 102, 112))
c.rect(0, 40, 64, 3, (244, 202, 96))           # yellow safety strip
c.rect(1, 41, 3, 1, (246, 220, 136))
c.rect(34, 41, 8, 1, (246, 220, 136))

# ---------------- passenger 1: sitting, reading ----------------
c.circle(13, 26, 3, (46, 46, 60))       # head
c.rect(10, 29, 7, 14, (46, 46, 60))     # torso
c.rect(11, 41, 8, 5, (46, 46, 60))      # thigh (back of bench seat)
c.rect(13, 46, 3, 8, (46, 46, 60))      # shin
c.rect(12, 54, 6, 3, (34, 34, 44))      # foot
c.rect(15, 30, 2, 12, (40, 40, 52))     # arm to phone
c.rect(13, 40, 7, 3, (40, 40, 52))
c.rect(15, 41, 4, 3, (170, 232, 252))   # phone

# ---------------- bench ----------------
c.rect(6, 36, 12, 10, (132, 80, 44))          # back
c.rect(6, 36, 12, 1, (100, 58, 30))
c.rect(5, 46, 14, 4, (148, 92, 52))           # seat slat
c.rect(5, 49, 14, 1, (126, 76, 42))
c.rect(6, 52, 3, 8, (80, 46, 24))             # legs
c.rect(15, 52, 3, 8, (80, 46, 24))
c.rect(4, 55, 16, 1, (116, 70, 36))           # bench floor shadow
overlay(c, 5, 44, 19, 49, (255, 240, 200), 0.10)

# ---------------- passenger 2: standing, phone ----------------
c.circle(33, 24, 3, (50, 50, 64))       # head
c.rect(31, 27, 6, 14, (50, 50, 64))     # torso
c.rect(29, 28, 2, 11, (44, 44, 56))     # arm down
c.rect(37, 28, 2, 7, (44, 44, 56))      # upper arm
c.rect(35, 35, 4, 6, (44, 44, 56))
c.rect(36, 37, 4, 3, (170, 232, 252))   # phone
c.rect(31, 41, 3, 13, (50, 50, 64))     # legs
c.rect(30, 53, 4, 3, (38, 38, 48))
c.rect(34, 42, 2, 10, (46, 46, 58))
c.rect(33, 52, 3, 4, (38, 38, 48))

# ---------------- passenger 3: walking, far (depth) ----------------
c.rect(49, 38, 7, 7, (88, 88, 108))    # head
c.rect(51, 45, 5, 9, (88, 88, 108))     # body
c.rect(49, 46, 2, 5, (80, 80, 98))      # back arm
c.rect(55, 47, 2, 6, (80, 80, 98))      # front arm
c.rect(48, 54, 2, 7, (80, 80, 98))      # back leg, stride
c.rect(53, 53, 2, 7, (80, 80, 98))      # front leg, stride
c.rect(47, 60, 3, 2, (72, 72, 88))      # back shoe
c.rect(53, 59, 4, 2, (72, 72, 88))      # front shoe

# ---------------- soft shadows ----------------
overlay(c, 3, 60, 20, 63, (40, 40, 50), 0.25)
overlay(c, 26, 59, 41, 62, (40, 40, 50), 0.25)
overlay(c, 46, 61, 58, 63, (40, 40, 50), 0.25)

print(c.stats_text())
print(c.matrix_text(region=(0, 0, 63, 12)))
finish(c)
