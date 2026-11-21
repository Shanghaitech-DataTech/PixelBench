# 48x48 RPG magic staff sprite on transparency
result = new_canvas(48, 48, background=None, name="magic-staff")

# Palette
outline = result.color("#24152d", "outline")
deep_wood = result.color("#3b2030", "deep_wood")
wood_dark = result.color("#593327", "wood_dark")
wood = result.color("#875036", "wood")
wood_light = result.color("#b77845", "wood_light")
wood_glint = result.color("#d89a58", "wood_glint")
wrap_dark = result.color("#34233f", "wrap_dark")
wrap = result.color("#66506f", "wrap")
purple_deep = result.color("#522574", "purple_deep")
purple = result.color("#8745bd", "purple")
purple_bright = result.color("#bf6aff", "purple_bright")
lilac = result.color("#e0a5ff", "lilac")
white = result.color("#fff1ff", "white")

# Main staff silhouette: heavy shaft flowing into a hooked, curled head.
result.path(
    "M9 44 L11 47 L16 47 L19 41 L22 35 L25 29 L28 23 "
    "L31 18 C32 15 31 12 33 9 C35 5 39 3 43 5 "
    "C47 7 48 11 46 15 C45 18 43 20 41 22 "
    "L37 19 C40 16 42 14 42 11 C42 9 40 8 38 9 "
    "C35 11 36 16 34 20 L31 26 L28 32 L24 39 L19 47 "
    "L14 47 Z", outline)

# Wood body inset, preserving a dark pixel outline.
result.path(
    "M12 43 L14 45 L17 44 L21 37 L24 31 L27 25 L30 19 "
    "C32 15 31 12 34 9 C36 6 39 5 42 7 C45 8 46 11 44 15 "
    "C43 17 42 18 41 19 L39 18 C42 15 44 12 43 10 "
    "C42 7 38 7 36 9 C33 12 35 16 32 21 L29 27 L26 33 "
    "L23 39 L18 46 L15 46 Z", wood_dark)

# Warm central facets along the shaft.
result.poly([(15,43),(18,43),(23,35),(27,27),(31,19),(32,15),(34,15),
             (33,20),(29,28),(26,35),(21,43),(18,46),(15,46)], wood)
result.poly([(18,41),(20,40),(24,33),(27,26),(30,21),(31,18),(32,19),
             (30,25),(27,31),(24,38),(21,43),(18,45)], wood_light)

# Hook lighting and inner dark curl.
result.path("M35 9 C37 6 41 6 44 9 C45 11 45 13 44 15 L42 16 C44 12 44 10 42 9 C40 7 38 8 36 10 Z", wood)
result.set(37,8,wood_light).set(38,7,wood_glint).set(39,7,wood_light)
result.set(43,9,wood_light).set(44,10,wood_glint).set(44,11,wood_light)
result.set(43,15,deep_wood).set(42,17,deep_wood).set(40,18,deep_wood)

# Carved branch spur on the left of the head.
result.poly([(29,21),(26,19),(24,16),(25,14),(28,18),(31,18)], outline)
result.poly([(29,20),(27,18),(26,16),(26,15),(29,18),(31,18)], wood)
result.set(27,16,wood_light).set(28,18,wood_light)

# Metal/leather binding around the upper shaft.
result.poly([(27,25),(29,23),(32,25),(30,28),(27,28),(25,27)], wrap_dark)
result.poly([(27,24),(31,25),(30,27),(26,27)], wrap)
result.set(28,24,lilac).set(29,25,wrap).set(26,26,wrap)

# Lower grip wraps.
result.poly([(16,37),(19,36),(22,38),(21,40),(18,40),(15,39)], wrap_dark)
result.line(17,37,21,38,wrap)
result.line(16,39,20,40,wrap)
result.set(18,37,lilac)

# Wood grain and chipped end.
result.line(18,34,21,29,deep_wood)
result.set(19,33,wood_light).set(20,31,wood_light)
result.line(14,42,16,41,wood_glint)
result.set(13,44,wood_light).set(14,45,wood)
result.set(11,45,deep_wood).set(16,46,wood_light).set(17,45,wood_glint)

# Suspended magical crystal inside the crook, dark rim first.
result.poly([(37,11),(40,13),(40,17),(37,21),(34,17),(34,14)], outline)
result.poly([(37,12),(39,14),(39,17),(37,20),(35,17),(35,14)], purple_deep)
result.poly([(37,12),(38,14),(38,17),(37,19),(36,17),(36,14)], purple)
result.set(36,14,purple_bright).set(37,13,lilac).set(38,15,purple_bright)
result.set(37,14,white).set(36,15,lilac)

# Magic halo pixels where crystal energy touches the curl.
result.set(33,12,purple).set(33,13,purple_bright).set(34,11,lilac)
result.set(40,18,purple).set(39,20,purple_bright).set(38,21,lilac)

# Purple particles: crisp diamonds, sparks, and tiny motes.
def diamond(cx, cy, outer, inner=None):
    result.set(cx, cy-1, outer).set(cx-1, cy, outer).set(cx, cy, outer).set(cx+1, cy, outer).set(cx, cy+1, outer)
    if inner is not None:
        result.set(cx, cy, inner)

diamond(29,7,purple,purple_bright)
result.set(29,5,lilac).set(27,7,purple_deep).set(31,7,lilac)
diamond(44,22,purple_deep,purple_bright)
result.set(44,20,lilac).set(46,22,purple)
diamond(33,27,purple,purple_bright)
result.set(33,25,lilac).set(35,27,purple_deep)
result.set(24,10,purple_bright).set(23,9,lilac)
result.set(46,7,purple).set(47,6,lilac)
result.set(41,26,purple_bright)
result.set(28,31,purple_deep).set(29,30,purple)

# A few high-energy star cores.
result.set(29,6,white)
result.set(44,21,lilac)
result.set(33,26,white)

view(result, scale=10, margin=1, edges="all")
finish(result)
