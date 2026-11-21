result = new_canvas(48, 48, name="slash_effect")
# Two successive poses, arranged left to right on the required single sheet.
edge = '#b9dfef'
light = '#e4f5fc'
white = '#ffffff'
# Frame 1: a compact, tapered crescent sweeping upward.
result.poly([(4,32),(5,27),(7,23),(10,19),(14,16),(19,14),(16,17),(13,20),(10,24),(7,29)], edge)
result.poly([(5,30),(7,24),(11,19),(16,16),(14,19),(11,22),(8,27)], white)
result.set(18,14,white)
# Frame 2: a broader, longer crescent with a narrow trailing sweep.
result.poly([(24,37),(26,30),(28,24),(31,19),(35,15),(40,12),(46,10),(42,13),(38,17),(35,21),(32,26),(29,31)], edge)
result.poly([(25,35),(28,26),(31,20),(36,15),(43,12),(40,15),(36,19),(33,24),(30,29)], light)
result.poly([(27,31),(29,24),(32,19),(37,15),(43,12),(39,16),(35,21),(32,26)], white)
# Detached streak follows the outer curve and dwindles to a pixel.
result.poly([(28,37),(32,31),(35,26),(37,23),(36,28),(33,33),(29,37)], light)
result.line(29,36,33,31,white)
result.set(26,39,edge)
view(result)
save('slash_effect', result)
finish(result)
