from pixelbench_api import *

c = input_canvas
W, H = 112, 157
hdr = "    " + "".join(str(i%10) for i in range(57))
lines = [hdr]
for gy in range(105):
    row = ""
    for gx in range(57):
        xs = gx*2-1; xe = min(gx*2+1, W)
        ys = gy*2-1; ye = min(gy*2+1, H)
        cnt = {}
        for y in range(max(0, ys), ye):
            for x in range(xs, xe):
                if x < 0: continue
                i = c.get(x, y)
                cnt[i] = cnt.get(i, 0) + 1
        top = max(cnt, key=cnt.get)
        row += "0123456789abc"[top]
    lines.append(f"{gy:3d} {row}")
print("\n".join(lines))
