c = input_canvas
output = c.copy(name="output")

blue = c.color("#0097e0ff")
yellow = c.color("#ffe600")

# Find the boundary between the two parrots by scanning a mid row.
# Left parrot is around x<32, right parrot around x>=32.
count = 0
for y in range(64):
    for x in range(64):
        if x >= 32 and output.get(x, y) == blue:
            output.set(x, y, yellow)
            count += 1

print("Changed pixels:", count)
finish(output)
