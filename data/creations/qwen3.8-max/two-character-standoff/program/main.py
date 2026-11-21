from pixelbench_api import *
from art import C, background, knight, knight_rim, rogue, rogue_rim, fx

bg = new_canvas(128, 128, name="bg")
background(bg)

kc = new_canvas(128, 128, name="knightlayer")
knight(kc)
kc.outline(C['ink'])
knight_rim(kc)

gc = new_canvas(128, 128, name="roguelayer")
rogue(gc)
gc.outline(C['ink'])
rogue_rim(gc)

fxl = new_canvas(128, 128, name="fxlayer")
fx(fxl)

result = flatten([bg, kc, gc, fxl], name="output")
print(result.stats_text())
print(len(result.palette()), "palette entries")
view(result)
view(result.select(0, 8, 52, 112).preview("knightcrop"), scale=5, margin=1)
view(result.select(74, 24, 54, 96).preview("roguecrop"), scale=5, margin=1)
save("standoff", result, indexed=True)
finish(result)
