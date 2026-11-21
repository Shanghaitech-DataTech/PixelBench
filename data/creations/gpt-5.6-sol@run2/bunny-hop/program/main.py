# Build two editable animation frames on a shared, expanded stage.
print(input_canvas.palette())

W, H = 40, 32
f1 = new_canvas(W, H, name="frame_1_original")
f1.blit(input_canvas, 3, 4)

# Palette colours sampled from the source sprite.
pal = input_canvas.palette()
rgba = {entry["index"]: tuple(entry["rgba"]) for entry in pal}
# Source indices reported by matrix_text are one-based display labels; actual
# palette entries below are selected by their source order.
for entry in pal:
    print(entry)

f2 = new_canvas(W, H, name="frame_2_mid_leap")
# Start with the original sprite shifted forward and airborne, then reshape its
# lower half into a stretched hopping pose while retaining head/ear identity.
f2.blit(input_canvas, 11, 0)

# Erase the original grounded body/legs, retaining head, ears, and upper chest.
f2.clear(11, 12, 26, 16)

# Use exact source palette entries by index after palette inspection.
# Temporary body construction; indices are finalized after this preview.
outline = 1
shadow = 2
mid = 3
fur = 4
pink = 5
eye = 6
accent = 7

# Airborne body, elongated from rump to shoulder.
f2.poly([(8,14),(11,11),(18,10),(25,11),(30,15),(29,21),(24,24),(16,24),(10,21),(6,18)], outline)
f2.poly([(9,15),(12,12),(19,11),(25,12),(29,15),(28,20),(23,22),(15,22),(10,20),(8,18)], fur)
# Back shading and haunch definition.
f2.line(9,18,12,13,shadow)
f2.line(10,20,15,22,mid)
f2.rect(12,12,4,2,mid)
f2.rect(24,20,4,2,shadow)
f2.set(18,20,mid)
f2.set(19,19,mid)

# Hind legs kick backward (left), separated into two readable limbs.
f2.poly([(12,20),(9,21),(5,25),(1,25),(0,27),(7,27),(13,23)], outline)
f2.poly([(11,21),(8,22),(5,25),(2,25),(2,26),(7,26),(12,23)], fur)
f2.poly([(15,21),(12,24),(8,28),(4,29),(4,31),(11,31),(17,24)], outline)
f2.poly([(14,22),(12,25),(9,28),(6,29),(6,30),(10,30),(16,23)], fur)
f2.line(5,28,11,28,mid)

# Forelegs reach forward (right) during flight.
f2.poly([(25,20),(29,22),(34,25),(39,25),(39,28),(33,28),(27,24),(23,22)], outline)
f2.poly([(26,21),(29,23),(34,26),(38,26),(38,27),(34,27),(28,23),(24,22)], fur)
f2.poly([(23,21),(27,24),(31,28),(36,29),(36,31),(30,31),(25,27),(20,23)], outline)
f2.poly([(24,22),(27,25),(31,29),(35,30),(31,30),(25,26),(21,23)], fur)
f2.line(31,28,36,28,mid)

# Tail lifted behind the moving body.
f2.poly([(8,14),(5,12),(2,13),(1,16),(4,18),(8,17)], outline)
f2.poly([(7,14),(5,13),(3,14),(3,16),(5,17),(8,16)], fur)
f2.set(3,16,mid)

# Restore the complete original head and face (including eye and gold nose)
# over the new torso. Transparent source pixels are skipped.
head = input_canvas.select(14, 7, 12, 16)
head.copy_to(25, 5, f2, mode="over")
# A stepped neck bridge keeps the original head attached to the stretched body.
f2.line(25,16,27,19,outline)
f2.line(24,16,26,19,fur)
f2.set(25,17,mid)

# Side-by-side working preview; this canvas is intentionally not submitted.
preview = new_canvas(W * 2 + 2, H, name="animation_preview")
preview.blit(f1, 0, 0)
preview.blit(f2, W + 2, 0)
view(preview, scale=10, margin=1, edges="all")
finish([f1, f2])
