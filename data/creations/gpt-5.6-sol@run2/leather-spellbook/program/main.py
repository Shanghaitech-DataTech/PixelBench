from pixelbench_api import new_canvas, view, finish

# Eight-colour RPG spellbook sprite on transparency.
result = new_canvas(32, 32, background=None, name="leather-spellbook")

OUT = "#211820"
LEATHER_DARK = "#4a2424"
LEATHER = "#7b3d2b"
LEATHER_LIGHT = "#a85b36"
GOLD_DARK = "#9a6128"
GOLD = "#e1ad46"
PAGE_DARK = "#9b7650"
PAGE = "#e2c58b"

# Closed book silhouette and lower page block, shown in slight perspective.
result.poly([(7,4),(24,5),(27,8),(27,24),(23,28),(7,27),(4,24),(4,8)], OUT)

# Page block visible along fore-edge and bottom.
result.poly([(8,22),(26,20),(26,24),(22,27),(8,26)], PAGE_DARK)
result.poly([(9,22),(25,21),(25,23),(22,26),(9,25)], PAGE)
result.line(10,24,22,24,PAGE_DARK)
result.line(21,25,24,23,PAGE_DARK)

# Leather cover body.
result.poly([(7,5),(23,6),(26,9),(26,20),(23,23),(7,22),(5,20),(5,8)], LEATHER_DARK)
result.poly([(9,6),(22,7),(25,9),(25,19),(22,22),(9,21)], LEATHER)
result.poly([(10,7),(21,8),(24,10),(24,18),(21,21),(10,20)], LEATHER_LIGHT)
# Broad leather shadow gives the cover depth and worn, uneven tone.
result.poly([(10,16),(24,14),(24,18),(21,21),(10,20)], LEATHER)
result.line(11,8,21,9,LEATHER)
result.line(11,19,20,20,LEATHER_DARK)

# Heavy spine with raised leather bands.
result.poly([(6,7),(10,6),(10,21),(7,23),(5,20),(5,8)], LEATHER_DARK)
result.line(8,7,8,21,LEATHER)
for y in (9,15,20):
    result.rect(5,y,5,2,OUT)
    result.line(6,y,9,y,LEATHER_LIGHT)

# Brass corner protectors.
result.poly([(21,6),(24,7),(26,9),(26,12),(24,12),(23,9),(21,8)], GOLD_DARK)
result.poly([(22,7),(24,8),(25,9),(25,11),(24,10),(23,8)], GOLD)
result.poly([(23,18),(26,18),(26,21),(23,24),(20,23),(20,21),(22,21)], GOLD_DARK)
result.poly([(24,19),(25,19),(25,21),(23,23),(21,22),(22,21)], GOLD)
result.poly([(7,21),(10,21),(10,23),(8,24),(6,22)], GOLD_DARK)
result.line(7,22,9,22,GOLD)

# Central arcane clasp / stamped gem-like ornament.
result.poly([(17,10),(20,13),(19,17),(16,19),(13,16),(14,12)], GOLD_DARK)
result.poly([(17,11),(19,13),(18,16),(16,18),(14,16),(15,13)], GOLD)
result.poly([(17,13),(18,14),(17,16),(15,15),(15,14)], LEATHER_DARK)
result.set(16,14,LEATHER_LIGHT)

# Reassert a few silhouette pixels for a strong dark RPG-item outline.
result.line(7,4,24,5,OUT)
result.line(27,8,27,24,OUT)
result.line(23,28,7,27,OUT)
result.line(4,24,4,8,OUT)

view(result, scale=16, margin=0)
finish(result)
