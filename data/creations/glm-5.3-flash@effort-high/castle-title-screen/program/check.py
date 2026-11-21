exec(open("main.py").read())
import numpy as np
w, h, rgba = c.to_rgba()
arr = np.frombuffer(bytes(rgba), dtype=np.uint8).reshape(h, w, 4)
small = arr[::4, ::4, :3]
# map to chars by luminance/hue
def ch(px):
    r, g, b = int(px[0]), int(px[1]), int(px[2])
    lum = (r * 3 + g * 6 + b) // 10
    if r > 200 and g > 150: return "S"   # sun/bright
    if r > 150 and g > 100: return "s"   # warm bright
    if r > 100 and g < 90:  return "w"   # warm mid
    if r > 60 and g < 70:   return "m"   # purple mid
    if lum > 25: return "p"              # dark purple
    return "#"                            # near black
for row in small:
    print("".join(ch(p) for p in row))
