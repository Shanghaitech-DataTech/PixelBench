from pixelbench_api import *

src = input_canvas
W, H = 44, 44

# ----- Frame 1: original picture content, same canvas dimensions -----
f1 = new_canvas(W, H, name='frame1')
f1.blit(src, 0, 0)

# ----- Frame 2: character throws a light punch with the left fist
# (the arm that extends horizontally to the right of the image).
# Copy the original, then extend that arm outward to the right with a fist.
f2 = new_canvas(W, H, name='frame2')
f2.blit(src, 0, 0)

# arm: outline (dark blue), fill (blue) running right from the body
f2.rect(14, 21, 17, 4, '#3f3f74')    # x=14..30, y=21..24
f2.rect(15, 22, 15, 2, '#5b6ee1')    # arm fill x=15..29
# fist at the end of the arm
f2.rect(31, 20, 5, 5, '#3f3f74')     # fist outline x=31..35, y=20..24
f2.rect(32, 21, 3, 3, '#eec39a')      # fist face
# light motion marks in front of the fist
f2.set(36, 20, '#cbdbfc')
f2.set(37, 21, '#cbdbfc')
f2.set(36, 22, '#cbdbfc')

print("frame1:", f1.stats())
print(f2.matrix_text(region=(0, 18, 40, 28), indices=True))
print(f2.stats_text())

finish([f1, f2])
