output = input_canvas.copy(name="output")

# palette ids in the source
BLUE = 3      # c2 #0097e0  base plumage
BLUE_HI = 8   # c7 #2ecdf5  plumage highlight
BEAK = 4      # c3 #ffcf1a  beak upper half

# new colours
yellow = output.color("#ffdb1f", name="yellow")
yellow_hi = output.color("#fff07a", name="yellow_hi")
beak_orange = output.color("#f08a14", name="beak_orange")

SPLIT = 32  # right parrot is entirely at x >= 34; gap at 32-33

# sanity check: no left-parrot plumage crosses the split
left_blue = sum(
    1
    for y in range(64)
    for x in range(SPLIT)
    if output.get(x, y) in (BLUE, BLUE_HI)
)
right_blue = 0

for y in range(64):
    for x in range(SPLIT, 64):
        i = output.get(x, y)
        if i == BLUE:
            output.set(x, y, yellow)
            right_blue += 1
        elif i == BLUE_HI:
            output.set(x, y, yellow_hi)
            right_blue += 1
        elif i == BEAK:
            output.set(x, y, beak_orange)

print("left-half blue pixels (untouched):", left_blue)
print("right-half pixels recoloured:", right_blue)
print(output.stats_text())
print(view(output))

result = output
finish(result)
