bg = new_canvas(64, 64, name="bg")
hc = new_canvas(64, 64, name="backhair")
gr = new_canvas(64, 64, name="gear")
s = new_canvas(64, 64, name="sprite")
fr = new_canvas(64, 64, name="front")

# ---------------- palette ----------------
BG1 = bg.color("#27384a", "bg1")
BG2 = bg.color("#35506a", "bg2")
BG3 = bg.color("#456e8a", "bg3")
OUT = bg.color("#17120f", "outline")

SKIN = bg.color("#f6d9b6", "skin")
SKIN_S = bg.color("#dcae87", "skin_s")
SKIN_D = bg.color("#b4825d", "skin_d")

HAIR_L = bg.color("#9ddc72", "hair_l")
HAIR = bg.color("#5fae44", "hair")
HAIR_D = bg.color("#3a7a2c", "hair_d")
HAIR_X = bg.color("#1e4717", "hair_x")

CL_L = bg.color("#e3f3c6", "cloth_l")
CL = bg.color("#bedf93", "cloth")
CL_D = bg.color("#90b566", "cloth_d")
CL_X = bg.color("#5f7f45", "cloth_x")

LEA = bg.color("#8c5c34", "leather")
LEA_D = bg.color("#4e3119", "leather_d")
LEA_L = bg.color("#bb8747", "leather_l")

MET = bg.color("#d3dae1", "metal")
MET_D = bg.color("#8b95a1", "metal_d")

EYE = bg.color("#2f7f52", "eye")
WHT = bg.color("#fbfbf4", "white")
MOUTH = bg.color("#b06464", "mouth")
STR = bg.color("#efe7cd", "string")

# ---------------- background ----------------
bg.rect(0, 0, 64, 64, BG1)
bg.ellipse(32, 36, 27, 31, BG2)
bg.ellipse(32, 42, 19, 22, BG3)

# ================= long hair behind the body =================
hc.path("M22 14 C17 27 17 41 20 52 L28 50 C24 38 24 24 26 15 Z", HAIR_D)
hc.path("M38 14 C43 27 44 42 41 53 L35 51 C38 38 38 24 36 15 Z", HAIR_D)
hc.rect(23, 14, 16, 24, HAIR_D)
hc.outline(HAIR_X)
# interior strand shading, after the edge pass
hc.path("M21 46 L26 49 L23 53 Z", HAIR_X)
hc.path("M42 47 L36 50 L40 54 Z", HAIR_X)
hc.line(24, 24, 22, 44, HAIR)
hc.line(40, 26, 42, 46, HAIR_D)
hc.line(23, 27, 22, 38, HAIR_L)
hc.set(23, 39, HAIR_L)
hc.line(26, 24, 25, 42, HAIR_X)
hc.line(37, 24, 38, 44, HAIR_X)

# ================= gear: bow and quiver =================
# bow: three offset arcs give a 3px limb with its own dark edges
gr.path("M18 13 C9 25 9 43 18 55", LEA_D, fill=False)
gr.path("M20 13 C11 25 11 43 20 55", LEA_D, fill=False)
gr.path("M19 13 C10 25 10 43 19 55", LEA, fill=False)
gr.path("M19 17 C12 26 12 41 19 51", LEA_L, fill=False)
gr.line(19, 12, 19, 56, STR)
gr.rect(18, 12, 3, 2, LEA_D)
gr.rect(18, 55, 3, 2, LEA_D)

# quiver, frame right
gr.path("M39 22 L47 25 L45 48 L38 45 Z", LEA_D)
gr.path("M40 24 L46 26 L44 46 L39 44 Z", LEA)
gr.path("M41 25 L43 26 L42 43 L40 42 Z", LEA_L)
gr.rect(39, 33, 7, 2, LEA_D)
gr.rect(39, 41, 7, 2, LEA_D)
# arrows in the quiver
for ax, ay in ((41, 24), (43, 24), (45, 25)):
    gr.line(ax, ay, ax + 1, ay - 11, LEA)
    gr.set(ax + 1, ay - 12, MET)
    gr.set(ax + 1, ay - 13, MET_D)
for fx, fy in ((42, 14), (44, 14), (46, 15)):
    gr.set(fx - 1, fy, HAIR)
    gr.set(fx, fy, HAIR_L)
    gr.set(fx, fy + 1, HAIR)
    gr.set(fx + 1, fy + 1, HAIR_D)

# ================= head =================
s.path("M24 9 L24 18 C24 22 27 25 31 25 C35 25 37 22 37 17 L37 9 Z", SKIN)
s.path("M24 9 L26 9 L26 18 C26 21 27 23 29 24 C26 23 24 21 24 18 Z", SKIN_S)
s.set(25, 21, SKIN_D)
s.rect(24, 9, 13, 2, SKIN_S)
s.line(29, 24, 33, 24, SKIN_S)
s.set(34, 23, SKIN_S)
s.set(36, 20, SKIN_S)

# neck and shoulders
s.rect(29, 24, 5, 4, SKIN_S)
s.rect(30, 24, 4, 3, SKIN)
s.rect(29, 24, 5, 1, SKIN_D)

# hair crown and fringe: fringe stops above the eye row
s.path("M23 13 C22 5 28 3 32 3 C37 3 39 7 39 13 L39 9 L23 10 Z", HAIR)
s.rect(23, 7, 17, 3, HAIR)
s.poly([(23, 10), (27, 10), (26, 14), (23, 14)], HAIR_D)
s.poly([(27, 10), (31, 10), (31, 13), (28, 13)], HAIR)
s.poly([(31, 10), (35, 10), (35, 13), (32, 14)], HAIR_D)
s.poly([(35, 10), (39, 10), (39, 14), (36, 13)], HAIR)
s.set(26, 15, HAIR_D)
s.set(36, 14, HAIR)
s.line(26, 6, 32, 5, HAIR_L)
s.line(33, 5, 37, 8, HAIR_L)
s.set(24, 9, HAIR_L)
s.set(38, 9, HAIR_L)
s.set(28, 12, HAIR_X)
s.set(34, 12, HAIR_X)
s.set(31, 11, HAIR_L)

# pointed ears, over the hair so they read clearly
s.poly([(37, 15), (41, 9), (41, 17), (37, 18)], SKIN)
s.line(40, 11, 40, 15, SKIN_S)
s.set(41, 10, SKIN_S)
s.set(38, 17, SKIN_D)
s.set(39, 16, SKIN_S)
s.poly([(24, 14), (21, 10), (21, 17), (24, 17)], SKIN_S)
s.line(22, 12, 22, 16, SKIN_D)
s.set(23, 15, SKIN)

# features: pushed right of centre, far eye narrowed, for the three-quarter turn
s.line(26, 15, 28, 15, HAIR_D)
s.line(32, 15, 34, 15, HAIR_D)
s.rect(26, 17, 2, 2, WHT)      # far eye
s.rect(31, 17, 3, 2, WHT)      # near eye
s.rect(27, 17, 1, 2, EYE)
s.rect(32, 17, 1, 2, EYE)
s.set(27, 17, HAIR_X)
s.set(32, 17, HAIR_X)
s.set(26, 17, SKIN_D)
s.set(34, 17, SKIN_D)
s.set(33, 18, EYE)
# nose and mouth sit off-centre toward the near side
s.set(30, 20, SKIN_S)
s.set(30, 21, SKIN_D)
s.line(30, 23, 31, 23, MOUTH)
s.set(34, 21, SKIN_S)
s.set(27, 21, SKIN_S)

# ================= body =================
s.path("M27 27 L34 27 L38 30 L38 40 L24 40 L24 30 Z", CL)
s.path("M27 27 L31 27 L31 40 L24 40 L24 30 Z", CL_L)
s.rect(34, 30, 4, 10, CL_D)
s.line(28, 27, 31, 30, CL_L)
s.line(34, 27, 31, 30, CL_L)
s.set(31, 31, CL_D)

# hair over the shoulders, inside the silhouette
s.path("M26 20 C24 26 24 32 25 37 L28 36 C26 30 26 25 28 20 Z", HAIR)
s.path("M35 20 C38 26 38 32 37 36 L34 35 C36 30 36 25 35 20 Z", HAIR_D)
s.line(25, 29, 25, 35, HAIR_L)
s.line(37, 28, 37, 33, HAIR)
s.set(28, 36, HAIR_X)
s.set(34, 35, HAIR_X)

# quiver strap across the chest
s.line(29, 30, 37, 38, LEA_D)
s.line(30, 30, 38, 37, LEA)
s.set(33, 34, MET_D)
s.set(34, 35, MET)

# belt
s.rect(24, 40, 14, 3, LEA)
s.rect(29, 40, 4, 3, MET_D)
s.rect(30, 41, 2, 1, MET)
s.rect(24, 40, 3, 1, LEA_L)
s.rect(35, 40, 3, 1, LEA_D)

# skirt
s.path("M24 43 L38 43 L40 51 L22 51 Z", CL)
s.path("M24 43 L31 43 L30 51 L22 51 Z", CL_L)
s.rect(33, 43, 7, 8, CL_D)
s.line(22, 51, 40, 51, CL_X)
s.line(27, 44, 26, 50, CL_D)
s.line(35, 44, 36, 50, CL_X)

# legs and boots
s.rect(26, 51, 5, 5, CL_X)
s.rect(33, 51, 5, 5, CL_X)
s.rect(26, 54, 5, 7, LEA_D)
s.rect(33, 54, 5, 7, LEA_D)
s.rect(26, 54, 3, 7, LEA)
s.rect(33, 54, 3, 7, LEA)
s.rect(26, 53, 5, 1, LEA_L)
s.rect(33, 53, 5, 1, LEA_L)
s.rect(25, 59, 7, 3, LEA)
s.rect(33, 59, 7, 3, LEA)
s.rect(25, 61, 7, 1, LEA_D)
s.rect(33, 61, 7, 1, LEA_D)

# ================= arms =================
# her right arm, frame left, hanging
s.path("M24 29 L21 33 L21 41 L25 41 L25 34 Z", CL_L)
s.rect(21, 36, 2, 5, CL_D)
s.rect(21, 41, 4, 3, LEA)
s.rect(21, 41, 4, 1, LEA_L)
s.rect(21, 44, 4, 4, SKIN_S)
s.rect(21, 44, 3, 3, SKIN)
s.set(21, 47, SKIN_D)

# her left arm, frame right, bent to hold an arrow
s.path("M38 29 L41 33 L43 40 L39 41 L38 34 Z", CL_D)
s.rect(41, 35, 2, 5, CL_X)
s.rect(40, 41, 4, 3, LEA)
s.rect(40, 41, 4, 1, LEA_L)
s.rect(40, 44, 4, 4, SKIN_S)
s.rect(40, 44, 3, 3, SKIN)
s.set(43, 47, SKIN_D)

s.outline(OUT)

# front layer: the held arrow, nocked and clear of the body
fr.line(43, 55, 43, 36, LEA)
fr.set(43, 35, LEA_L)
fr.set(43, 34, MET)
fr.set(43, 33, MET_D)
fr.set(43, 45, LEA_L)
fr.set(42, 52, HAIR)
fr.set(43, 51, HAIR_L)
fr.set(44, 53, HAIR_D)
fr.set(43, 53, HAIR)
fr.set(43, 54, HAIR_D)

# outfit trim: a few light stitches so the tunic reads as cloth, not a block
fr.line(25, 31, 25, 38, CL_L)
fr.set(31, 28, CL_L)
fr.set(32, 29, CL_D)
fr.line(23, 44, 23, 50, CL_L)

result = flatten([bg, hc, gr, s, fr], name="output")
view(result)
save("female-elf-archer", result)
print(result.stats_text())
finish(result)
