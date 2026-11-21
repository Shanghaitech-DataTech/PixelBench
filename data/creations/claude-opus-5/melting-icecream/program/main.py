out = input_canvas.copy(name="output")

DARK = out.color('#4a2930', 'choc_dark')
BODY = out.color('#5e363e')   # scoop dark brown
MID  = out.color('#95524c')   # scoop lit brown
LITE = out.color('#c3715b')   # scoop highlight

# deepest row the cone silhouette reaches, per column
cone_bottom = {}
for x in range(19, 43):
    cone_bottom[x] = 36
for x in range(21, 41):
    cone_bottom[x] = 40
for x in range(23, 39):
    cone_bottom[x] = 43
for x in range(24, 37):
    cone_bottom[x] = 46
for x in range(25, 37):
    cone_bottom[x] = 50
for x in range(27, 35):
    cone_bottom[x] = 54
for x in range(29, 33):
    cone_bottom[x] = 58

# ---- shallow scalloped collar just over the cone rim ----------------------
collar = {
    19: 33, 20: 34, 21: 34, 22: 35, 23: 34, 24: 33,
    25: 33, 26: 34, 27: 34, 28: 33, 29: 34, 30: 35,
    31: 34, 32: 33, 33: 33, 34: 34, 35: 34, 36: 35,
    37: 34, 38: 33, 39: 34, 40: 34, 41: 33, 42: 33,
}
for x, ybot in collar.items():
    ybot = min(ybot, cone_bottom[x])
    out.rect(x, 33, 1, ybot - 33 + 1, BODY)
    out.set(x, ybot, DARK)

# ---- three narrow runs, with the cone left visible between them -----------
def drip(cx, ybot, shoulder=2):
    """cx is the left column of a 2px run; shoulder rows are 1px wider."""
    for y in range(33, ybot + 1):
        w = 3 if y - 33 < shoulder else 2
        out.rect(cx, y, w, 1, BODY)
        out.set(cx + w - 1, y, MID)
    out.set(cx, ybot, BODY)
    out.set(cx + 1, ybot, MID)
    out.set(cx, ybot - 1, DARK)
    out.set(cx + 1, ybot - 3, LITE)

drip(21, 39)
drip(28, 46, shoulder=3)
drip(35, 42)

# one short dribble to break the rhythm
out.rect(32, 33, 1, 5, BODY)
out.set(32, 37, DARK)

# ---- a drop broken loose from the left run, against clear background ----
out.set(22, 41, BODY)
out.rect(21, 42, 2, 2, BODY)
out.set(22, 42, MID)
out.set(21, 44, BODY)

# ---- wet gloss: softening scoop and glossy melt ------------------------
for x, y in [(23, 30), (24, 31), (34, 31), (39, 30)]:
    out.set(x, y, MID)
for x, y in [(20, 34), (26, 34), (33, 34), (40, 34), (22, 36), (29, 38), (36, 38)]:
    out.set(x, y, MID)

view(out)
print(out.stats_text())
finish(out)
