from pixelbench_api import *
import random

output = input_canvas.copy(name="output")

# Hardcoded bounding box for the character's body
output.clear(x=70, y=55, w=45, h=90)

# Redraw background
for y in range(55, 145):
    for x in range(70, 115):
        if output.get(x, y) == 0: # Transparent
            if y < 76:
                output.set(x, y, 12)
            elif y < 96:
                output.set(x, y, 37)
            elif y < 105:
                output.set(x, y, 53)
            else:
                output.set(x, y, 11)

# Redraw vending machine
# Inside glowing background
output.rect(86, 59, 30, 57, 253)
# Left casing
output.rect(82, 55, 4, 92, 36)
# Top casing
output.rect(82, 55, 54, 4, 36)
# Shelves
output.rect(86, 73, 30, 2, 36)
output.rect(86, 87, 30, 2, 36)
output.rect(86, 101, 30, 2, 36)
# Lower part of vending machine
output.rect(86, 116, 30, 31, 36)

# Redraw motorcycle parts
output.rect(70, 105, 10, 15, 122) # Tank
output.rect(75, 105, 25, 10, 48) # Seat
output.rect(78, 102, 20, 3, 48)

# Add Lightning
output.color((255, 255, 255, 255), "lightning")
output.color((200, 200, 255, 255), "lightning_glow")

# Lightning 1
output.line(30, 0, 40, 30, "lightning")
output.line(29, 0, 39, 30, "lightning_glow")
output.line(40, 30, 35, 40, "lightning")
output.line(39, 30, 34, 40, "lightning_glow")
output.line(35, 40, 50, 70, "lightning")
output.line(34, 40, 49, 70, "lightning_glow")
output.line(40, 30, 50, 45, "lightning")

# Lightning 2
output.line(130, 0, 120, 40, "lightning")
output.line(120, 40, 135, 60, "lightning")

# Wet ground with clinging water droplets
output.color((150, 200, 255, 180), "puddle")
output.color((200, 220, 255, 200), "droplet")

random.seed(42)
for y in range(130, 170):
    for x in range(0, 170):
        # Ground area
        c = output.get(x, y)
        if c in [10, 11, 12, 13, 14, 15]:
            if random.random() < 0.15:
                output.set(x, y, "puddle")
            if random.random() < 0.03:
                output.set(x, y, "droplet")

# Rain with semi-transparent droplets
output.color((200, 220, 255, 100), "rain")
for i in range(400):
    x = random.randint(0, 170)
    y = random.randint(0, 170)
    length = random.randint(4, 10)
    output.line(x, y, x - length//3, y + length, "rain")

finish(output)
