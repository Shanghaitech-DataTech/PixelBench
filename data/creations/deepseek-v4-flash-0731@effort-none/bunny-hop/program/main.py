from pixelbench_api import *

A = '#3a3737'
B = '#b7b3b2'
D = '#efe9e7'
E = '#d6b39d'
G = '#cdae67'

CW, CH = 48, 34

# Frame 1: original content preserved
f1 = new_canvas(CW, CH, name="frame1")
f1.blit(input_canvas, 11, 3)

# Frame 2: rabbit caught in a mid-leap bunny-hop to the right
f2 = new_canvas(CW, CH, name="frame2")

# === MID-LEAP BUNNY-HOP POSE ===

# Body — stretched horizontally for the leap
f2.ellipse(23, 16, 13, 5, D)
f2.ellipse(32, 13, 5, 4, D)
f2.ellipse(37, 10, 4, 3, D)

# The connection to bridge body and ears
f2.rect(10, 9, 30, 14, D)

# Ears — two vertical rabbit ears
f2.ellipse(34, 6, 3, 4, D)
f2.ellipse(30, 7, 2, 4, D)

# Hind legs (trailing behind, left)
f2.ellipse(11, 22, 4, 3, D)
f2.ellipse(8, 24, 3, 2, D)

# Front legs (reaching forward, right)
f2.ellipse(41, 18, 4, 3, D)
f2.ellipse(45, 21, 2, 2, D)

# Tail
f2.circle(9, 17, 2, D)

# Inner ear tan color
f2.set(33, 5, E)
f2.set(37, 5, E)

# Eye
f2.set(38, 10, G)

# Body shading
f2.set(16, 18, B)
f2.set(26, 18, B)

# Unified outline around the full rabbit
f2.outline(A)

finish([f1, f2])
