from pixelbench_api import *

out = input_canvas.copy(name="output")

blue = out.color((0, 151, 224))      # body blue (already in palette)
light = out.color((46, 205, 245))    # light blue detail
yellow = out.color((255, 215, 0))    # yellow body
lyellow = out.color((255, 238, 88))  # light yellow detail

n_body = n_light = 0
for y in range(64):
    for x in range(33, 64):  # right-hand parrot only
        idx = out.get(x, y)
        if idx == blue:
            out.set(x, y, yellow)
            n_body += 1
        elif idx == light:
            out.set(x, y, lyellow)
            n_light += 1

print("recolored body px:", n_body, "light px:", n_light)
print(out.stats_text())

# Verify: left parrot still has its blue, right side has none left
left_blue = sum(1 for y in range(64) for x in range(0, 33) if out.get(x, y) == blue)
right_blue = sum(1 for y in range(64) for x in range(33, 64) if out.get(x, y) == blue)
right_yellow = sum(1 for y in range(64) for x in range(33, 64) if out.get(x, y) in (yellow, lyellow))
print("left blue px:", left_blue, "| right blue px:", right_blue, "| right yellow px:", right_yellow)

print(out.matrix_text(region=(32, 14, 63, 48)))
finish(out)
