from pixelbench_api import *

# One 48x48 sprite sheet: two 24x48 animation frames.
result = new_canvas(48, 48, background=None, name="teleport_portal_2frame")

# Palette: compact violet ramp plus energetic highlights.
shadow = "#180d3f"
deep = "#26105d"
indigo = "#37147a"
purple = "#551c9b"
mid = "#7730bc"
bright = "#a44de0"
hot = "#cf7cff"
pale = "#edc4ff"
white = "#fff4ff"
blue = "#765dff"

# Frame 1, centered at (11,24): a turbulent purple vortex.
# Sparse outer particles.
for x, y, c in [
    (10,3,bright),(5,6,mid),(17,7,hot),(2,13,purple),(20,14,bright),
    (1,24,mid),(21,27,hot),(3,35,bright),(18,39,mid),(9,44,purple),
    (15,43,hot),(22,21,purple),(2,29,indigo)
]:
    result.set(x,y,c)
result.rect(8,4,4,1,mid)
result.rect(4,8,3,1,bright)
result.rect(17,10,3,1,mid)
result.rect(1,18,2,1,bright)
result.rect(19,34,2,1,purple)
result.rect(6,41,3,1,mid)

# Jagged outer ring.
result.poly([(10,5),(14,6),(14,8),(18,9),(18,12),(21,14),(20,18),(22,21),(21,26),(22,30),(19,33),(19,37),(15,39),(14,42),(9,41),(7,39),(4,38),(4,34),(1,31),(3,27),(1,23),(3,19),(2,16),(5,13),(5,10),(8,9)], deep)
result.poly([(10,7),(14,8),(14,10),(18,12),(17,15),(20,18),(18,21),(20,25),(18,28),(19,32),(15,33),(15,37),(11,39),(8,37),(5,36),(6,32),(3,29),(5,25),(3,22),(6,19),(4,16),(8,14),(7,11)], purple)
# Inner swirl bands, broken into pixel arcs.
result.poly([(9,9),(14,10),(17,13),(16,16),(12,14),(8,15),(5,18),(5,15),(7,12)], bright)
result.poly([(17,17),(19,21),(18,25),(15,27),(14,24),(16,21),(13,19)], mid)
result.poly([(17,29),(15,34),(11,37),(7,35),(6,32),(10,33),(13,31)], bright)
result.poly([(5,29),(3,25),(5,20),(8,18),(10,20),(7,22),(7,26),(10,28),(9,31)], mid)
# Rotating inner eye and luminous core.
result.poly([(10,14),(14,15),(16,19),(14,22),(10,21),(7,23),(8,18)], hot)
result.poly([(10,21),(14,23),(15,27),(12,31),(8,29),(7,25)], bright)
result.poly([(10,18),(13,19),(12,22),(15,25),(12,28),(9,26),(8,22)], pale)
result.poly([(10,21),(12,22),(11,24),(13,25),(11,27),(9,25),(9,23)], white)
result.set(6,17,pale); result.set(17,27,hot); result.set(6,30,hot)

# Frame 2, centered at (36,24): rotated vortex with a glowing halo.
# Detached halo motes.
for x, y, c in [
    (35,2,hot),(29,5,bright),(42,6,pale),(25,12,bright),(46,15,hot),
    (24,24,pale),(47,27,bright),(26,36,hot),(43,41,pale),(35,45,bright),
    (29,43,mid),(46,33,mid)
]:
    result.set(x,y,c)
result.rect(33,3,4,1,bright)
result.rect(27,7,3,1,hot)
result.rect(42,9,3,1,bright)
result.rect(24,18,2,1,hot)
result.rect(45,21,2,1,pale)
result.rect(26,39,3,1,bright)
result.rect(40,43,3,1,hot)

# Bright, segmented halo silhouette.
result.poly([(34,5),(39,6),(39,8),(43,9),(42,12),(45,14),(44,18),(47,20),(45,24),(47,29),(44,31),(44,36),(40,37),(39,41),(34,42),(31,40),(27,39),(28,35),(25,33),(27,29),(24,26),(26,22),(24,19),(28,16),(27,12),(31,11),(31,7)], deep)
result.poly([(34,6),(39,7),(38,9),(43,11),(41,14),(45,17),(43,20),(46,23),(44,27),(46,30),(42,33),(43,36),(38,37),(38,40),(33,40),(31,38),(28,37),(30,33),(27,31),(29,27),(26,24),(29,20),(27,18),(31,15),(29,12),(34,11)], blue)
# Halo highlight segments.
result.poly([(31,8),(36,6),(40,8),(39,10),(35,9),(32,11)], pale)
result.poly([(42,12),(45,17),(43,20),(42,17),(39,14)], hot)
result.poly([(45,24),(46,29),(42,34),(41,31),(43,27)], pale)
result.poly([(39,38),(34,41),(29,38),(31,35),(35,38)], hot)
result.poly([(27,32),(25,26),(27,21),(30,23),(29,27)], pale)
result.poly([(27,18),(29,12),(33,10),(34,13),(31,16)], hot)
# Rotated internal spiral.
result.poly([(35,11),(40,12),(42,16),(39,17),(36,15),(33,17),(30,16),(31,13)], purple)
result.poly([(41,18),(43,22),(41,26),(38,24),(39,21),(36,19)], bright)
result.poly([(41,28),(39,34),(35,37),(32,34),(35,32),(37,29)], mid)
result.poly([(31,34),(28,31),(28,26),(31,27),(33,30),(36,29),(35,33)], bright)
result.poly([(29,24),(30,20),(34,18),(36,21),(33,23),(32,27),(29,27)], mid)
# Twisted central flare.
result.poly([(34,15),(38,17),(39,20),(36,22),(38,25),(36,29),(32,28),(31,25),(33,22),(31,19)], hot)
result.poly([(35,18),(37,20),(35,22),(37,24),(35,27),(33,25),(34,23),(32,21)], pale)
result.poly([(35,20),(36,21),(34,23),(36,24),(35,25),(33,24),(34,22)], white)
# Crisp glints on halo.
result.set(37,7,white); result.set(44,18,white); result.set(44,29,white)
result.set(39,37,white); result.set(27,27,white); result.set(30,13,pale)

view(result, scale=10, margin=0)
finish(result)
