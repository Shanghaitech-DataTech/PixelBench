output = input_canvas.copy(name='output')

# Remove the sword guard and blade without disturbing the hand or sleeve.
output.rect(41, 39, 6, 2, 1)
output.rect(42, 41, 3, 13, 1)
output.rect(43, 54, 2, 1, 1)
output.set(43, 55, 1)

# A dark-outlined wooden staff with a green gem finial.
dark, wood, light_wood = 2, 16, 5
green, light_green = 13, 14
output.rect(43, 9, 3, 48, dark)
output.rect(44, 9, 1, 47, wood)
output.set(44, 11, light_wood)
output.set(44, 19, light_wood)
output.set(44, 28, light_wood)
output.set(44, 45, light_wood)
output.rect(43, 56, 3, 2, dark)
output.set(44, 56, wood)

# Faceted magical stone at the staff's crown.
output.rect(43, 3, 3, 1, dark)
output.rect(41, 4, 7, 1, dark)
output.rect(40, 5, 9, 3, dark)
output.rect(41, 8, 7, 1, dark)
output.rect(43, 9, 3, 1, dark)
output.rect(42, 5, 5, 3, green)
output.rect(43, 4, 3, 1, green)
output.rect(43, 8, 3, 1, green)
output.set(42, 5, light_green)
output.set(43, 5, light_green)
output.set(42, 6, light_green)

# Restore the original fist over the shaft so it visibly grips the staff.
input_canvas.select(40, 35, 6, 4).copy_to(40, 35, output, mode='replace')

view(output, scale=8, margin=0)
finish(output)
