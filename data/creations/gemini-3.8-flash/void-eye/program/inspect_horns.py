from main import draw_void_eye_boss
from pixelbench_api import canvas

c = canvas(-1)
# Print horn area: y from 1 to 18, x from 10 to 54
for y in range(1, 18):
    row = []
    for x in range(10, 55):
        idx = c.get(x, y)
        if idx is None:
            row.append("..")
        else:
            name = c.color_name(idx)
            if "248" in str(idx) or "fff" in name.lower() or name == "#f8f2ff":
                row.append("WW")
            elif name == "#d2bee2" or "210" in name:
                row.append("PP")
            elif name == "#0a0412":
                row.append("##")
            else:
                row.append("oo")
    print(f"{y:02d}: " + "".join(row))
