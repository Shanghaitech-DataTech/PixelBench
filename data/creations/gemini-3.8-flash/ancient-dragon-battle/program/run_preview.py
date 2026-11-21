import time
from generate_epic_art import generate, PALETTE

print("Rendering scene with generate_epic_art...")
t0 = time.time()
g = generate()
t1 = time.time()
print(f"Grid render time: {t1 - t0:.4f}s")

c = new_canvas(256, 256)
for y in range(256):
    row = g.grid[y]
    for x in range(256):
        c.set(x, y, row[x])
t2 = time.time()
print(f"Canvas transfer time: {t2 - t1:.4f}s")

print("Stats:", c.stats_text())
p = view(c)
print("Preview rendered:", p)
