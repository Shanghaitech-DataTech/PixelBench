from pixelbench_api import *

src = input_canvas
f1 = src.copy(name="f1")            # frame 1: original picture content
f2 = src.copy(name="f2")            # frame 2: completed drawn-sword slash

BLACK  = src.color((2, 2, 2))
SKIN   = src.color((232, 160, 110))
SILVER = src.color((235, 235, 242))
HANDLE = src.color((88, 78, 142))
GUARD  = src.color((110, 106, 130))
GRAY   = src.color((150, 146, 160))
ROBE   = src.color((69, 68, 99))
DARK   = src.color((35, 28, 44))
CREASE = src.color((27, 2, 2))
CROWN  = src.color((105, 101, 125))

G_OLD = src.color((146, 110, 107))
H_OLD = src.color((138, 131, 133))

# ---------- frame 2 ----------
# 1) erase the old sword, hilt, claw and top-right clutter
f2.clear(38, 4, 24, 34)                     # x38..61, y4..37
for y in range(26, 38):
    for x in range(32, 39):                  # blade sliver beside the face
        if f2.get(x, y) == G_OLD:
            f2.set(x, y, None)
for y in range(38, 53):
    for x in range(27, 41):                  # old grip / hand marring the robe
        if f2.get(x, y) in (G_OLD, H_OLD):
            f2.set(x, y, None)

# head crown beside the face (restored, the trail passes in front of it)
f2.rect(38, 4, 6, 7, CROWN)
f2.rect(39, 10, 4, 3, DARK)

# robe patch bridging the cleaned side of the torso
f2.poly([(30, 37), (41, 37), (41, 52), (39, 54), (30, 53)], ROBE)
f2.poly([(30, 37), (41, 37), (41, 52), (39, 54), (30, 53)], BLACK, fill=False)

# cape strip and legs restored from the source
cape = src.select(24, 46, 7, 16).preview("cape")
f2.blit(cape, 24, 46)
legs = src.select(28, 53, 34, 19).preview("legs")
f2.blit(legs, 28, 53)

# 2) black slash trail sweeping from the lower left up to the upper right
f2.poly([(0, 63), (7, 57), (27, 39), (35, 31), (43, 23), (48, 17),
         (43, 14), (37, 21), (23, 34), (4, 55), (0, 59)], BLACK)
f2.poly([(47, 14), (54, 6), (49, 4), (42, 12)], BLACK)
f2.line(24, 45, 38, 31, GRAY)                # ghost echoes inside the trail
f2.line(25, 46, 39, 32, GRAY)

# 3) left arm raised from the shoulder toward the new grip
f2.line(29, 44, 34, 38, SKIN)
f2.line(30, 45, 35, 39, SKIN)
f2.line(30, 46, 35, 40, DARK)

# 4) handle, guard, completed bright blade, pointing up-right
f2.line(36, 36, 33, 39, HANDLE)
f2.line(37, 37, 34, 40, HANDLE)
f2.line(38, 31, 44, 37, GUARD)
f2.line(37, 27, 60, 4, SILVER)
f2.line(38, 28, 61, 5, SILVER)
f2.set(60, 3, SILVER)
f2.set(61, 4, SILVER)

# 5) left hand gripping the handle (the hand that gripped the blade in the image)
f2.rect(32, 28, 11, 11, BLACK)
f2.rect(33, 29, 9, 9, SKIN)
f2.line(33, 31, 41, 31, CREASE)
f2.line(33, 34, 41, 34, CREASE)
f2.line(33, 37, 41, 37, CREASE)

finish([f1, f2])
print("done", f1.stats()["size"], f2.stats()["size"])
