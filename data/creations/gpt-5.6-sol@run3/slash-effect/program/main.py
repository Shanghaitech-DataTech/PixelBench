result = new_canvas(48, 48, name="slash_effect")
# Frame 1: a compact, tapered crescent.
result.poly([(3,29),(4,24),(7,20),(11,17),(16,16),(21,17),(16,18),(12,20),(9,23),(6,27),(3,32)], '#a7def0')
result.poly([(3,30),(5,24),(9,20),(13,18),(18,17),(21,17),(16,19),(12,21),(9,24),(6,28)], '#ffffff')
result.line(6,25,10,21,'#ffffff')
# Frame 2: an expanded sweep, its bright cutting edge facing upper-left.
result.poly([(25,37),(25,29),(27,21),(31,15),(36,11),(42,9),(47,10),(42,11),(37,14),(33,18),(30,23),(28,29),(26,36)], '#9cd6eb')
result.poly([(25,36),(26,27),(29,20),(33,15),(38,12),(43,10),(47,10),(42,12),(38,15),(34,19),(31,24),(28,31)], '#ffffff')
# A separated trailing ribbon follows the same curve.
result.poly([(29,39),(30,32),(33,26),(37,21),(42,18),(46,17),(42,20),(38,24),(34,29),(31,35)], '#84bedb')
result.poly([(30,37),(32,30),(36,25),(40,21),(46,17),(41,22),(37,27),(33,32)], '#d7f5ff')
result.set(29,40,'#84bedb')
view(result)
finish(result)
