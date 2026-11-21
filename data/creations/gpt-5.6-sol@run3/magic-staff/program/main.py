# 48x48 RPG wooden magic staff with purple magic particles
result = new_canvas(48, 48, background=None, name="magic_staff")

# Palette
outline = "#24162b"
deep_wood = "#4b2530"
wood_dark = "#6b342b"
wood = "#9a5634"
wood_light = "#c37a43"
wood_glint = "#e1a05b"
purple_dark = "#4d267d"
purple = "#7a3fc2"
purple_bright = "#b65cff"
lilac = "#df9cff"
spark = "#f4d8ff"

# Faint magical motes behind the staff
result.set(34, 3, purple_bright).set(35, 3, purple_bright)
result.set(33, 4, purple_bright).set(34, 4, lilac).set(35, 4, purple_bright).set(36, 4, purple_bright)
result.set(34, 5, purple_bright).set(35, 5, purple_bright)
result.set(42, 9, purple).set(43, 9, purple)
result.set(41, 10, purple).set(42, 10, lilac).set(43, 10, purple).set(44, 10, purple_dark)
result.set(42, 11, purple).set(43, 11, purple)
result.set(38, 16, purple_bright).set(39, 16, purple_bright)
result.set(37, 17, purple_bright).set(38, 17, lilac).set(39, 17, purple_bright).set(40, 17, purple)
result.set(38, 18, purple_bright).set(39, 18, purple)
result.set(43, 22, purple_dark).set(44, 22, purple)
result.set(42, 23, purple).set(43, 23, purple_bright).set(44, 23, purple)
result.set(43, 24, purple)

# Shaft outer silhouette, tapered and slightly irregular
result.poly([(6,44),(5,42),(7,38),(9,34),(11,30),(13,26),(15,22),(17,18),(19,14),(22,11),(25,10),(28,11),(29,13),(28,16),(26,18),(24,18),(23,16),(24,14),(22,15),(20,19),(18,23),(16,27),(14,31),(12,35),(10,39),(9,43)], outline)
# Main wood inset
result.poly([(7,42),(8,38),(10,34),(12,30),(14,26),(16,22),(18,18),(20,15),(22,13),(24,12),(26,13),(27,14),(26,16),(25,17),(24,17),(24,15),(22,16),(20,20),(18,24),(16,28),(14,32),(12,36),(10,40),(9,43)], wood_dark)
# Warm central grain
result.poly([(9,40),(11,35),(13,31),(15,27),(17,23),(19,19),(21,16),(23,14),(24,14),(22,18),(20,21),(18,25),(16,29),(14,33),(12,37),(10,42)], wood)
# Shaft highlight broken into carved sections
result.line(11,36,14,30,wood_light)
result.line(15,28,18,22,wood_light)
result.line(19,20,21,17,wood_light)
result.set(12,34,wood_glint).set(16,26,wood_glint).set(20,18,wood_glint)
# Bark notches / grain shadows
result.set(9,38,deep_wood).set(10,38,deep_wood)
result.set(12,32,deep_wood).set(13,32,deep_wood)
result.set(15,25,deep_wood).set(16,25,deep_wood)
result.set(18,21,deep_wood)
result.set(8,42,wood_light).set(7,43,deep_wood)

# Curved crown: heavy wooden hook rising and curling clockwise
result.poly([(20,15),(19,12),(20,8),(22,5),(25,3),(29,2),(33,3),(36,5),(38,8),(38,12),(36,15),(33,17),(30,18),(27,18),(26,16),(28,14),(31,14),(33,13),(34,11),(34,9),(32,7),(29,6),(26,7),(24,9),(24,12),(23,15)], outline)
result.poly([(21,14),(21,11),(22,8),(25,5),(29,4),(32,5),(35,7),(36,9),(36,12),(34,14),(31,16),(28,16),(28,15),(31,14),(33,12),(34,10),(33,8),(31,7),(28,7),(26,8),(24,10),(23,14)], wood_dark)
result.poly([(23,12),(24,9),(26,7),(29,5),(32,6),(34,8),(34,10),(33,11),(32,9),(30,8),(27,9),(25,11),(24,14)], wood)
result.set(25,8,wood_light).set(26,7,wood_light).set(27,6,wood_glint)
result.set(28,5,wood_light).set(29,5,wood_light).set(32,7,wood_light)
result.set(34,12,deep_wood).set(33,13,deep_wood).set(31,15,deep_wood)

# Suspended arcane crystal inside the crook
result.poly([(29,9),(32,11),(32,14),(29,17),(26,14),(26,11)], purple_dark)
result.poly([(29,9),(31,11),(31,14),(29,16),(27,14),(27,11)], purple)
result.poly([(29,10),(30,12),(30,14),(29,15),(28,13),(28,11)], purple_bright)
result.set(28,11,lilac).set(29,11,spark).set(28,12,lilac)

# Crown runes and small violet energy traces
result.set(22,9,purple_dark).set(23,8,purple)
result.set(24,6,purple_bright).set(25,5,lilac)
result.set(35,6,purple_dark).set(36,7,purple)
result.set(36,14,purple).set(35,15,purple_bright)

# Foreground particles: varied diamond/cross silhouettes
result.set(18,7,purple).set(19,7,purple)
result.set(17,8,purple).set(18,8,lilac).set(19,8,purple_bright).set(20,8,purple)
result.set(18,9,purple).set(19,9,purple)
result.set(40,4,purple)
result.set(39,5,purple).set(40,5,lilac).set(41,5,purple)
result.set(40,6,purple)
result.set(39,12,purple_bright).set(40,12,purple_bright)
result.set(38,13,purple_bright).set(39,13,spark).set(40,13,lilac).set(41,13,purple)
result.set(39,14,purple_bright).set(40,14,purple)
result.set(23,3,purple).set(24,3,purple_bright).set(24,2,lilac)
result.set(14,13,purple_dark).set(15,13,purple)
result.set(13,14,purple).set(14,14,purple_bright).set(15,14,lilac).set(16,14,purple)
result.set(14,15,purple).set(15,15,purple)

# Tiny high-energy pinpoints
for x, y, col in [(37,1,purple),(44,15,lilac),(41,19,purple_bright),(17,4,lilac),(11,19,purple),(21,1,purple_bright),(45,7,purple),(34,20,purple_dark)]:
    result.set(x,y,col)

# Reinforce the pointed butt cap
result.poly([(5,42),(7,42),(9,43),(8,46),(6,47),(5,45)], outline)
result.poly([(7,43),(8,44),(7,46),(6,45)], wood)
result.set(7,43,wood_light)

view(result, scale=10, margin=1, edges="all")
finish(result)
