# bottle-potion: turn the water in the bottle into a bubbling purple magic potion.

c = input_canvas.copy(name="output")

# ---- potion palette ----
P_MAIN   = c.color("#7b2fbe", name="potion")          # was dark water blue  #2f7598
P_LIGHT  = c.color("#b06ee8", name="potion_light")    # was light water blues
P_DEEP   = c.color("#3a1168", name="potion_deep")     # was dark maroon band #31121d
P_SHADOW = c.color("#3c1a5c", name="potion_shadow")   # was dark navy detail #282735
BUBBLE   = c.color("#e9d6ff", name="bubble")
SHINE    = c.color("#f7f0ff", name="bubble_shine")    # distinct from bg white

REMAP = {4: P_SHADOW, 5: P_MAIN, 6: P_LIGHT, 7: P_LIGHT, 8: P_LIGHT,
         9: P_DEEP, 10: P_LIGHT}

# ---- recolour every water pixel, preserving the original shading structure ----
for y in range(64):
    for x in range(64):
        tgt = REMAP.get(input_canvas.get(x, y))
        if tgt is not None:
            c.set(x, y, tgt)

# ---- bubbles rising through the potion ----
for bx, by, br in [
    (27, 27, 1), (24, 31, 2), (38, 29, 1), (13, 35, 1), (45, 34, 2),
    (30, 36, 1), (21, 39, 1), (33, 41, 1), (16, 47, 1), (42, 49, 2),
    (30, 53, 1), (35, 55, 1), (22, 57, 1), (28, 59, 1),
]:
    c.circle(bx, by, br, BUBBLE, fill=True)

for tx, ty in [(17, 30), (31, 28), (47, 31), (18, 33), (43, 39),
               (26, 44), (25, 50), (38, 51), (34, 47)]:
    c.set(tx, ty, BUBBLE)

# tiny specular dots on the three largest bubbles
for hx, hy in [(23, 30), (44, 33), (41, 48)]:
    c.set(hx, hy, SHINE)

# ---- verification ----
LEG = {1: ".", 2: "#", 11: "P", 12: "L", 13: "D", 14: "S", 15: "o", 16: "*"}
for (bx, by, br) in [(24, 31, 2), (45, 34, 2), (42, 49, 2), (13, 35, 1), (28, 59, 1)]:
    print(f"--- bubble ({bx},{by},r={br}) ---")
    for y in range(by - 3, by + 4):
        print(f"y={y:2d} " + "".join(LEG.get(c.get(x, y), "?") for x in range(bx - 4, bx + 5)))

# shine dots must NOT be background white (index 1)
print("shine pixels:", [(x, y, c.get(x, y)) for x, y in [(23, 30), (44, 33), (41, 48)]])

# no background-coloured pixel strictly inside the liquid body
inner_bad = [(x, y) for y in range(27, 60) for x in range(5, 50) if c.get(x, y) == 1]
print("white pixels inside liquid body:", inner_bad)

print(c.stats_text())
finish(c)
