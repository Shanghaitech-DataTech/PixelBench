from pixelbench_api import *

output = input_canvas.copy(name='output')

# Remove background
output.fill_at(0, 0, 0)
output.fill_at(63, 0, 0)
output.fill_at(0, 63, 0)
output.fill_at(63, 63, 0)

# Remove trapped background
output.fill_at(32, 44, 0) # Under the bike
output.fill_at(18, 36, 0) # Above rear wheel
output.fill_at(42, 36, 0) # Above front wheel

bg = new_canvas(64, 64, name="bg")
# Sky
bg.rect(0, 0, 64, 32, "#87CEEB")
# Sun
bg.circle(10, 10, 5, "#FFD700")

# Clouds
bg.ellipse(45, 10, 8, 4, "#FFFFFF")
bg.ellipse(40, 8, 6, 3, "#FFFFFF")
bg.ellipse(50, 9, 5, 3, "#FFFFFF")

# Mountains
bg.poly([(0, 32), (15, 16), (35, 32)], "#808080")
bg.poly([(15, 16), (10, 21), (20, 21)], "#FFFFFF") # Snow cap 1

bg.poly([(25, 32), (45, 20), (64, 32)], "#A9A9A9")
bg.poly([(45, 20), (40, 24), (50, 24)], "#FFFFFF") # Snow cap 2

# Grass
bg.rect(0, 32, 64, 32, "#228B22")

# Trees
bg.rect(8, 30, 2, 4, "#5C4033")
bg.circle(9, 27, 4, "#006400")
bg.circle(9, 24, 3, "#006400")

bg.rect(54, 31, 2, 3, "#5C4033")
bg.circle(55, 28, 3, "#006400")

# Road
bg.poly([(24, 32), (40, 32), (64, 64), (0, 64)], "#444444")

# Road lines
bg.poly([(31, 34), (32, 34), (32, 38), (31, 38)], "#FFFFFF")
bg.poly([(31, 44), (33, 44), (33, 50), (31, 50)], "#FFFFFF")
bg.poly([(30, 58), (34, 58), (34, 64), (30, 64)], "#FFFFFF")

# Shadow
bg.ellipse(34, 50, 26, 3, (0, 0, 0, 100))

final = flatten([bg, output])
finish(final)
