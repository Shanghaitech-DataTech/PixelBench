from main import build_void_eye
from pixelbench_api import canvas

# Let's inspect canvas after build_void_eye
c = canvas(-1)
print("Palette size:", len(c.palette()))
for y in range(52, 64):
    row = []
    for x in range(26, 38):
        idx = c.get(x, y)
        val = c.color_name(idx) if idx is not None else "None"
        row.append(f"{val[:7]}")
    print(f"y={y:02d}: " + " ".join(row))
