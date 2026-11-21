# Two-frame bat wing-flap animation.
# Both frames use a larger transparent stage so the raised pose has room.
W, H = 31, 26
OX, OY = 2, 4

frame1 = new_canvas(W, H, name="bat_frame_1")
frame1.blit(input_canvas, OX, OY)

# Preserve the original head, torso, and feet while removing the drooped wings.
body = new_canvas(W, H, name="raised_body")
body.blit(input_canvas, OX, OY)
body.clear(0, 0, OX + 9, H)
body.clear(OX + 18, 0, W - (OX + 18), H)

wings = new_canvas(W, H, name="raised_wings")
outline = 1   # near-black plum
base = 4      # deep purple
shade = 8     # medium purple
rib = 5       # muted lavender
highlight = 3 # bright mauve

left_outline = [
    (11, 13), (10, 11), (8, 9), (7, 7), (5, 6), (4, 4), (1, 1),
    (0, 1), (1, 11), (3, 10), (4, 14), (6, 12), (7, 16),
    (9, 13), (11, 16)
]
left_inner = [
    (10, 13), (9, 11), (7, 10), (6, 8), (4, 7), (3, 5), (2, 3),
    (2, 9), (4, 8), (5, 12), (6, 10), (7, 14), (9, 11), (10, 14)
]
right_outline = [(30 - x, y) for x, y in left_outline]
right_inner = [(30 - x, y) for x, y in left_inner]

wings.poly(left_outline, outline)
wings.poly(right_outline, outline)
wings.poly(left_inner, base)
wings.poly(right_inner, base)

# Membrane facets and wing fingers, mirrored around the body.
left_facets = [
    [(2, 3), (4, 6), (4, 8), (2, 9)],
    [(4, 7), (7, 9), (6, 11), (5, 12)],
    [(7, 10), (10, 12), (9, 13), (7, 14)],
]
for pts in left_facets:
    wings.poly(pts, shade)
    wings.poly([(30 - x, y) for x, y in pts], shade)

# Mauve light catches the lifted leading edges.
wings.line(2, 2, 5, 6, highlight)
wings.line(28, 2, 25, 6, highlight)
wings.line(4, 6, 7, 8, highlight)
wings.line(26, 6, 23, 8, highlight)

# Dark structural ribs separate the membrane panels.
for x, y in [(2, 3), (4, 6), (7, 9)]:
    wings.line(10, 12, x, y, rib)
    wings.line(20, 12, 30 - x, y, rib)
wings.line(10, 13, 7, 14, rib)
wings.line(20, 13, 23, 14, rib)

frame2 = flatten([wings, body], name="bat_frame_2")

print(frame1.stats_text())
print(frame2.stats_text())
view(frame1, scale=16, margin=1, edges="all")
view(frame2, scale=16, margin=1, edges="all")
finish([frame1, frame2])
