from pixelbench_api import *

c = input_canvas.copy(name="output")
pal = c.palette()
for p in pal[:30]:
    print(p)

hex4 = c.color("#5e363e")
hex17 = c.color("#95524c")
hex23 = c.color("#99544d")
print("index for #5e363e:", hex4)
print("index for #95524c:", hex23) if False else None
print("index for #95524c:", c.color("#95524c"))
print("index for #99544d:", c.color("#99544d"))
print("get(15,27):", c.get(15, 27), c.color_name(c.get(15, 27)))
