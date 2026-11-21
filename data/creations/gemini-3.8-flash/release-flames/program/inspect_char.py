# Let's inspect the palette and dump text of parts
for idx, entry in enumerate(input_canvas.palette()):
    print(f"{idx}: {entry['name']} - {entry['rgba']}")

# Let's see color usage per region or print matrix_text of head, torso, legs
print("Character overview:")
print(input_canvas.matrix_text((0, 0, 46, 62)))
