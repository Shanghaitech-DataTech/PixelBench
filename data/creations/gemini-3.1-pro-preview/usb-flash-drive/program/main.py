from pixelbench_api import *

c = new_canvas(32, 32)

C_OUTLINE = "#1a1a24"
C_CONN_BASE = "#d0d5e0"
C_CONN_HIGH = "#ffffff"
C_CONN_SHAD = "#a0a5b4"
C_CONN_DARK = "#707888"
C_CONN_INSIDE = "#2a2a35"
C_CONN_PIN = "#e5c05c"

C_CASE_BASE = "#808896"
C_CASE_HIGH = "#b4bac4"
C_CASE_SHAD = "#525866"
C_CASE_DARK = "#363a45"
C_CASE_ACCENT = "#00e5ff"

C_LOOP_BASE = "#525866"
C_LOOP_SHAD = "#363a45"
C_STRAP = "#2a2a35"

# 1. Connector
c.poly([(23,12), (20,9), (20,12), (23,15)], C_CONN_DARK)
c.poly([(28,7), (23,12), (23,15), (28,10)], C_CONN_SHAD)
c.poly([(25,4), (28,7), (23,12), (20,9)], C_CONN_BASE)

c.poly([(25,4), (21,10), (22,11), (26,5)], C_CONN_HIGH)
c.poly([(25,5), (27,7), (23,11), (21,9)], C_CONN_INSIDE)
c.line(24, 7, 22, 9, C_CONN_PIN)
c.line(25, 8, 23, 10, C_CONN_PIN)

# 2. Casing
c.poly([(14,23), (9,18), (9,22), (14,27)], C_CASE_DARK)
c.poly([(24,13), (14,23), (14,27), (24,17)], C_CASE_SHAD)
c.poly([(19,8), (24,13), (14,23), (9,18)], C_CASE_BASE)

c.poly([(19,8), (21,10), (11,20), (9,18)], C_CASE_HIGH)
c.line(17, 14, 13, 18, C_CASE_DARK)
c.poly([(16,14), (17,15), (15,17), (14,16)], C_CASE_ACCENT)
c.set(20, 11, C_CASE_ACCENT)
c.set(21, 12, C_CASE_ACCENT)

# Grip lines
c.line(12, 19, 10, 21, C_CASE_SHAD)
c.line(13, 20, 11, 22, C_CASE_SHAD)

# 3. Loop
c.poly([(10,27), (8,25), (8,27), (10,29)], C_LOOP_SHAD)
c.poly([(14,23), (10,27), (10,29), (14,25)], C_LOOP_SHAD)
c.poly([(12,21), (14,23), (10,27), (8,25)], C_LOOP_BASE)

c.set(11, 24, "transparent")
c.set(10, 25, "transparent")

# 4. Outlines
c.outline(C_OUTLINE)

# 5. Internal Edges
c.line(19,8, 24,13, C_OUTLINE)
c.line(24,13, 14,23, C_OUTLINE)
c.line(14,23, 9,18, C_OUTLINE)
c.line(14,23, 14,27, C_OUTLINE)

c.line(28,7, 23,12, C_OUTLINE)

c.line(14,23, 10,27, C_OUTLINE)
c.line(10,27, 8,25, C_OUTLINE)
c.line(10,27, 10,29, C_OUTLINE)

# 6. Strap String
c.path("M 11 24 Q 6 28 4 26 Q 6 23 11 24", C_STRAP, fill=False)
c.path("M 10 25 Q 5 29 3 27 Q 5 24 10 25", C_OUTLINE, fill=False)

finish(c)
