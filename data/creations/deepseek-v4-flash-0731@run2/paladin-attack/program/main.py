from pixelbench_api import *

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO"
COL = {ch: i + 1 for i, ch in enumerate(letters)}  # c0..c40 -> indices 1..41
W = input_canvas.color("#ffffffff")
WM = input_canvas.color("#ffffffcc")
WF = input_canvas.color("#ffffff88")

f1 = input_canvas.copy(name="frame1")
f2 = input_canvas.copy(name="frame2")

# ---------- Frame 2 : heavy downward swing + left foot steps forward ----------
# remove the old raised sword (cols 26-42 rows 0-30) and old body/legs (rows 22-47)
f2.clear(26, 0, 17, 31)
f2.clear(1, 22, 42, 26)

# --- white motion trail streaming out behind the swing (right arc) ---
trail = [
    (1, 38, "RR"),
    (2, 40, "R"),
    (3, 36, "RR"),
    (4, 38, "Q"),
    (5, 34, "QQ"),
    (6, 36, "Q"),
    (7, 32, "EQ"),
    (8, 34, "Q"),
    (9, 31, "EQ"),
    (10, 33, "Q"),
    (11, 30, "EQ"),
    (12, 32, "Q"),
    (13, 29, "EQ"),
    (14, 31, "Q"),
    (15, 29, "EQ"),
    (16, 31, "Q"),
    (17, 30, "EQ"),
    (18, 32, "Q"),
    (19, 31, "EQ"),
    (20, 33, "Q"),
    (22, 34, "Q"),
    (24, 35, "Q"),
    (26, 37, "EQ"),
    (28, 39, "EQ"),
    (30, 40, "Q"),
    (32, 41, "E"),
    (34, 42, "Q"),
    (36, 42, "Q"),
    (38, 42, "Q"),
    (40, 41, "Q"),
]
# --- torso (leaning forward into the blow) ---
torso = [
    (22, 11, "auuniqna"),
    (23, 11, "aueeeena"),
    (24, 10, "aeeuuuea"),
    (25, 10, "aeuuuuaa"),
    (26, 10, "auuuuuaaa"),
    (27,  9, "auuuuuaaa"),
    (28,  9, "auuuuuaaa"),
    (29,  9, "auuuaaa"),
    (30,  8, "auuuaaa"),
    (31,  8, "auuuaaa"),
    (32,  8, "auuuaaa"),
    (33,  9, "auuuaaa"),
    (34,  9, "auuuaaa"),
    (35, 10, "auuuaaa"),
    (36, 10, "auuuaaa"),
    (37, 10, "auuuaaa"),
]
# --- right arm (from right shoulder) swinging the sword down ---
rightarm = [
    (23, 17, "aeea"),
    (24, 18, "aeda"),
    (25, 19, "aeea"),
    (26, 21, "aeda"),
    (27, 23, "aMMa"),
    (28, 26, "aMMa"),
    (29, 28, "akk"),
    (30, 29, "ak"),
]
# --- left arm reaching across to grip the sword with both hands ---
leftarm = [
    (23, 12, "aeea"),
    (24, 13, "aeea"),
    (25, 15, "aeea"),
    (26, 17, "aMMa"),
    (27, 20, "aMMa"),
    (28, 23, "aMMa"),
    (29, 26, "akk"),
    (30, 28, "ak"),
]
# --- guard (gold crossguard) ---
guard = [
    (31, 27, "aajjjja"),
    (32, 28, "ajjjja"),
]
# --- blade driven DOWN (tip low, struck to the ground) ---
blade = [
    (33, 31, "aabca"),
    (34, 32, "aabc"),
    (35, 33, "aabc"),
    (36, 34, "aabc"),
    (37, 35, "aabc"),
    (38, 36, "aabc"),
    (39, 37, "aabc"),
    (40, 38, "aabc"),
    (41, 39, "aabc"),
    (42, 40, "aab"),
    (43, 41, "aab"),
    (44, 42, "ab"),
]
# --- legs: back (right) leg trailing on the left, left leg stepped forward ---
back_leg = [
    (38,  8, "aMMa"),
    (39,  6, "aMMa"),
    (40,  4, "aMMa"),
    (41,  3, "aMMa"),
    (42,  2, "aMMa"),
    (43,  1, "akka"),
    (44,  1, "akka"),
    (45,  1, "ak"),
]
front_leg = [
    (38, 14, "aMMa"),
    (39, 15, "aMMa"),
    (40, 17, "aMMa"),
    (41, 18, "aMMa"),
    (42, 20, "aMMa"),
    (43, 21, "akka"),
    (44, 23, "akka"),
    (45, 24, "akka"),
    (46, 26, "akka"),
    (47, 27, "akk"),
    (48, 29, "akk"),
    (49, 30, "ak"),
]
# --- ground kicked up at the struck point + foot shadows ---
shadow = [
    (46, 2, 41), (47, 2, 41), (48, 2, 41),
    (48, 30, 41), (49, 31, 41), (50, 32, 41),
    (50, 41, 41), (51, 42, 41), (52, 41, 41),
    (49, 40, 41), (50, 39, 41), (52, 40, 41), (53, 39, 41),
]
sparks = [(43, 42, W), (42, 43, W), (41, 44, WM), (40, 45, WM), (42, 46, WF), (39, 47, WF)]

for y, x0, s in trail:
    for i, ch in enumerate(s):
        v = {"E": W, "Q": WM, "R": WF}[ch]
        f2.set(x0 + i, y, v)
for y, x0, s in torso + rightarm + leftarm + guard + blade + back_leg + front_leg:
    for i, ch in enumerate(s):
        f2.set(x0 + i, y, COL[ch])
for (x, y, col) in shadow:
    f2.set(x, y, col)
for (x, y, col) in sparks:
    f2.set(x, y, col)

print(f2.matrix_text())
finish([f1, f2])
