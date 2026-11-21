from pixelbench_api import *

c = new_canvas(48, 48, name="sewing_machine")

# Register colors
dark_iron = c.color((35, 35, 42))     # darkest body
black = c.color((15, 15, 18))         # near black
mid_iron = c.color((70, 70, 80))      # main body
light_iron = c.color((115, 115, 130)) # lighter face
highlight = c.color((160, 160, 175))  # highlight
steel = c.color((200, 200, 215))      # bright steel (needle bar)

# Gold
gold_dark = c.color((135, 105, 45))
gold_mid = c.color((185, 150, 75))
gold_light = c.color((225, 195, 120))

# Red fabric
red_dark = c.color((130, 20, 28))
red_mid = c.color((170, 35, 42))
red_light = c.color((215, 60, 70))
red_bright = c.color((240, 95, 100))

# Wood base
wood_dark = c.color((90, 50, 28))
wood_mid = c.color((130, 80, 42))
wood_light = c.color((170, 115, 65))
wood_table = c.color((150, 100, 55))

# ============================================================
# BASE / TABLE (wooden stand with the machine on top)
# ============================================================
# Table top surface
c.rect(1, 36, 46, 2, wood_table, fill=True)
# Table body
c.rect(1, 38, 46, 10, wood_mid, fill=True)
# Table legs
c.rect(2, 44, 3, 4, wood_dark, fill=True)
c.rect(43, 44, 3, 4, wood_dark, fill=True)
# Table front highlight
c.rect(1, 39, 46, 1, wood_light, fill=True)
# Wood grain on table body
c.set(6, 41, wood_dark)
c.set(14, 42, wood_dark)
c.set(22, 40, wood_dark)
c.set(30, 43, wood_dark)
c.set(38, 41, wood_dark)
c.set(33, 40, wood_light)
c.set(10, 43, wood_light)

# ============================================================
# METAL BED of the machine (flat base plate above wooden table)
# ============================================================
c.rect(3, 33, 42, 3, mid_iron, fill=True)
c.rect(3, 33, 42, 1, light_iron, fill=True)  # top face
c.rect(3, 34, 42, 1, dark_iron, fill=True)  # bed side

# ============================================================
# RED FABRIC on the bed (under the needle area, left-center)
# ============================================================
# Main fabric body draped on bed beneath presser foot
c.rect(5, 31, 15, 4, red_mid, fill=True)   # flat portion on bed
c.rect(6, 30, 13, 1, red_light, fill=True) # top edge/fold
# fabric folds on the bed
c.rect(8, 32, 1, 2, red_dark, fill=True)   # fold line 1
c.rect(13, 32, 1, 2, red_dark, fill=True)  # fold line 2
# fabric piling/folds in front, hanging over bed edge
c.rect(7, 34, 12, 2, red_mid, fill=True)
c.rect(6, 35, 13, 2, red_dark, fill=True)
# fabric hanging down over the bed front onto table
c.rect(7, 36, 12, 3, red_dark, fill=True)
c.rect(8, 39, 10, 2, red_dark, fill=True)
# fabric fold highlights
c.rect(8, 37, 2, 1, red_mid, fill=True)
c.rect(12, 38, 3, 1, red_mid, fill=True)
c.rect(9, 41, 2, 1, red_mid, fill=True)
c.rect(14, 40, 1, 1, red_light, fill=True)
c.rect(6, 35, 1, 1, red_light, fill=True)

# ============================================================
# MACHINE BODY
# ============================================================
# --- HEAD (left, holding needle) ---
# Main head box
c.rect(8, 10, 8, 24, dark_iron, fill=True)
c.rect(9, 11, 6, 22, mid_iron, fill=True)
# Head top highlight
c.rect(9, 11, 6, 1, highlight, fill=True)

# --- ARM (horizontal, connecting head to handwheel side) ---
# Arm top
c.rect(16, 12, 26, 3, dark_iron, fill=True)
c.rect(16, 12, 26, 1, highlight, fill=True)
# Arm front face (slanted slightly - angled view)
c.rect(16, 15, 26, 7, mid_iron, fill=True)
# Arm front bottom edge
c.rect(16, 21, 26, 1, dark_iron, fill=True)
# Decorative gold line on arm face
c.rect(17, 16, 24, 1, gold_mid, fill=True)

# --- HPEADWHEEL (right end) ---
cx, cy = 41, 17
c.circle(cx, cy, 7, black, fill=True)
c.circle(cx, cy, 6, dark_iron, fill=True)
c.circle(cx, cy, 5, gold_dark, fill=True)
c.circle(cx, cy, 3, gold_mid, fill=True)
c.circle(cx, cy, 2, gold_light, fill=True)
# spokes
c.line(cx-5, cy, cx+5, cy, gold_dark)
c.line(cx, cy-5, cx, cy+5, gold_dark)
c.line(cx-4, cy-4, cx+4, cy+4, gold_dark)
c.line(cx-4, cy+4, cx+4, cy-4, gold_mid)
# hub
c.circle(cx, cy, 1, gold_light, fill=True)

# --- bobbin / tension area near handwheel ---
c.circle(34, 20, 2, dark_iron, fill=True)
c.circle(34, 20, 1, gold_mid, fill=True)

# handwheel crank handle (small lever projecting up from wheel hub)
c.rect(41, 8, 1, 2, gold_dark, fill=True)
c.rect(40, 6, 3, 2, black, fill=True)
c.rect(41, 7, 1, 1, gold_mid, fill=True)

# --- TENSION DISC on arm face ---
c.circle(22, 18, 3, gold_dark, fill=True)
c.circle(22, 18, 2, gold_mid, fill=True)
c.circle(22, 18, 1, gold_light, fill=True)

# --- THREAD SPOOL on top of arm ---
c.rect(19, 6, 5, 6, red_dark, fill=True)  # spool
c.rect(20, 7, 3, 4, red_mid, fill=True)
c.rect(20, 7, 3, 1, red_light, fill=True)
# spool pin
c.rect(21, 4, 1, 2, gold_mid, fill=True)

# ============================================================
# NEEDLE HEAD DETAILS (left side below head)
# ============================================================
# Faceplate detail on head
c.rect(10, 15, 4, 8, light_iron, fill=True)
c.rect(11, 16, 2, 6, highlight, fill=True)

# Needle clamp / screw
c.rect(11, 26, 2, 1, gold_light, fill=True)

# NEEDLE BAR - descends from head to presser foot / fabric
c.rect(12, 27, 2, 6, steel, fill=True)
# Needle (thin, bright) - through presser foot into fabric
c.rect(13, 33, 1, 4, steel, fill=True)

# PRESSER FOOT
# presser foot arm (from head down, in front)
c.rect(10, 29, 1, 5, light_iron, fill=True)
# presser foot plate resting on fabric (dark metal, reads against red)
c.rect(9, 33, 6, 2, dark_iron, fill=True)  # main plate
c.rect(10, 32, 4, 1, mid_iron, fill=True)  # connecting piece
c.rect(9, 35, 6, 1, black, fill=True)     # foot underside shadow

# ============================================================
# DETAILS / DECORATION
# ============================================================
# Scrollwork on arm (gold leaf pattern)
c.set(18, 19, gold_dark)
c.set(28, 14, gold_mid)
c.set(29, 13, gold_mid)
# brand circle decal on arm
c.circle(26, 18, 2, black, fill=True)
c.circle(26, 18, 1, gold_mid, fill=True)

# Needle plate (small metal plate with stitching hole on bed under needle)
c.rect(8, 35, 5, 1, light_iron, fill=True)
c.set(10, 35, black)  # needle hole slot

# Stitch line marks on the fabric top (dark dashes)
c.rect(16, 31, 1, 1, red_dark, fill=True)
c.rect(18, 31, 1, 1, red_dark, fill=True)
c.rect(20, 31, 1, 1, red_dark, fill=True)
c.rect(22, 31, 1, 1, red_dark, fill=True)

print(c.stats_text())
print(c.matrix_text(region=(0,0,47,47), indices=False))
view(c)
save("sewing_machine", c)
finish(c)
