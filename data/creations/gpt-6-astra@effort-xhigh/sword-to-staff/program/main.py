output = input_canvas.copy(name='output')
# Remove the sword's guard and blade, retaining the surrounding sprite.
output.rect(40, 38, 7, 3, 'c0')
output.rect(42, 41, 3, 15, 'c0')
# A carved wooden walking staff, using the sprite's warm brown palette.
# The slightly crooked, knotted head gives the long shaft a natural silhouette.
output.poly([(44,14),(47,14),(48,15),(48,18),(46,21),(46,54),(45,56),(43,55),(43,22),(42,19),(42,17)], 'c1')
output.poly([(44,15),(46,15),(47,16),(47,18),(45,21),(45,54),(44,54),(44,21),(43,19),(43,17)], 'c4')
output.line(44,21,44,53,'c2')
output.line(45,22,45,53,'c4')
output.line(44,16,46,16,'c2')
output.line(43,17,43,19,'c2')
output.set(44,20,'c2')
# Small knots and a worn foot, at the same level of detail as the outfit.
output.set(44,27,'c4')
output.set(45,28,'c6')
output.set(44,46,'c4')
output.set(45,47,'c6')
output.line(44,53,45,53,'c6')
# Fingers wrap in front of the staff at the original hand position.
output.rect(40,35,5,3,'c8')
output.set(45,35,'c1')
output.set(45,36,'c7')
output.line(43,37,45,37,'c7')
output.line(40,38,45,38,'c1')
view(output, scale=8, margin=0)
finish(output)
