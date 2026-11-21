from pixelbench_api import *

c = input_canvas.copy(name="output")

BLUE = c.color("#0097e0")
CYAN = c.color("#2ecdf5")
YELLOW = c.color("#ffd400", name="yellow_body")

for y in range(64):
    for x in range(64):
        idx = c.get(x, y)
        if x >= 32 and (idx == BLUE or idx == CYAN):
            c.set(x, y, YELLOW)

# Verify: no blue/cyan remains in right half; left parrot (x<32) still blue.
left_blue = sum(1 for y in range(64) for x in range(32) if c.get(x, y) == BLUE)
right_blue = sum(1 for y in range(64) for x in range(32, 64) if c.get(x, y) == BLUE)
right_cyan = sum(1 for y in range(64) for x in range(32, 64) if c.get(x, y) == CYAN)
print("left blue:", left_blue, "| right blue:", right_blue, "| right cyan:", right_cyan)
print(c.matrix_text(region=(0, 14, 31, 48)))
finish(c)
