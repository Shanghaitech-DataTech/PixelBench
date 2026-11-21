from pixelbench_api import new_canvas, view, finish

# 32x32 laboratory microscope, transparent background.
c = new_canvas(32, 32, background=None, name="laboratory-microscope-icon")

outline = "#172433"
deep = "#24374a"
shadow = "#38536a"
steel = "#7893a5"
light = "#b8cad2"
highlight = "#e4f1f2"
cyan = "#55c7d3"
cyan_dark = "#278895"
accent = "#e7ad45"
base_dark = "#1d303f"

# Rear support/arm in three-quarter view.
c.poly([(20,8),(23,9),(25,12),(26,16),(26,21),(24,25),(21,27),(17,27),(17,24),(20,23),(22,20),(22,16),(21,13),(18,11)], outline)
c.poly([(21,10),(23,11),(24,14),(24,20),(22,23),(19,25),(18,25),(21,21),(22,18),(22,15),(20,12)], shadow)
c.set(23,13,steel).set(24,16,steel).set(23,20,steel)

# Eyepiece, angled body tube, and glass rim.
c.poly([(8,2),(14,2),(16,4),(15,7),(9,7),(7,5)], outline)
c.poly([(9,3),(13,3),(14,4),(13,5),(9,5),(8,4)], steel)
c.rect(9,3,4,1,light)
c.set(8,5,deep).set(14,5,deep)

# Main optical tube, descending toward the objective.
c.poly([(14,4),(17,4),(22,9),(22,12),(19,15),(16,13),(18,10),(13,7)], outline)
c.poly([(15,5),(17,6),(20,9),(20,12),(18,13),(17,12),(19,10),(15,7)], steel)
c.poly([(16,5),(17,6),(20,9),(19,10),(15,6)], light)
c.set(20,11,cyan).set(19,12,cyan_dark)

# Nosepiece and two objective lenses.
c.poly([(17,12),(21,12),(22,14),(20,16),(16,15),(15,14)], outline)
c.poly([(17,13),(20,13),(20,14),(18,15),(16,14)], shadow)
c.poly([(16,15),(19,15),(18,19),(15,19)], outline)
c.poly([(17,16),(18,16),(17,18),(16,18)], light)
c.poly([(19,15),(21,15),(21,18),(19,18)], outline)
c.set(20,16,steel)
c.set(16,19,cyan).set(17,19,cyan_dark)

# Stage, front lip, slide, and focus knob.
c.poly([(7,17),(22,17),(24,19),(22,21),(7,21),(5,19)], outline)
c.poly([(8,18),(21,18),(22,19),(21,19),(7,19),(6,18)], steel)
c.rect(9,17,8,1,light)
c.rect(11,17,5,1,highlight)
c.rect(7,20,14,1,deep)
c.rect(21,14,4,3,outline)
c.rect(22,15,2,1,accent)

# Illuminator beneath stage.
c.poly([(11,21),(18,21),(20,25),(18,27),(10,27),(9,25)], outline)
c.poly([(12,22),(17,22),(18,25),(17,26),(11,26),(10,25)], deep)
c.poly([(12,22),(16,22),(17,24),(11,24)], cyan_dark)
c.rect(12,22,4,1,cyan)
c.set(13,22,highlight)

# Wide perspective base and front bevel.
c.poly([(8,25),(21,25),(24,27),(28,28),(28,30),(5,30),(4,28)], outline)
c.poly([(9,26),(20,26),(23,28),(26,28),(26,29),(6,29),(7,27)], shadow)
c.poly([(9,26),(20,26),(22,27),(7,27)], steel)
c.rect(8,27,13,1,deep)
c.rect(7,29,18,1,base_dark)
c.set(6,28,light).set(23,28,steel).set(26,29,outline)

# Small material glints sharpen the three-quarter form.
c.set(10,4,highlight)
c.set(16,6,highlight)
c.set(19,9,highlight)
c.set(23,11,light)

view(c, scale=16, margin=0)
finish(c)
