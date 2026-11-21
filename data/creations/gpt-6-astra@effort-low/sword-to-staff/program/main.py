result = input_canvas.copy(name='output')
# Remove the sword guard, grip and blade against the white background.
result.rect(41,39,6,2,'c0')
result.rect(42,41,3,15,'c0')
result.set(43,38,'c1')
# A long wooden walking staff, with an angular, knotted crook.
result.poly([(42,35),(42,24),(43,22),(43,18),(45,16),(48,16),(50,18),(50,21),(48,23),(46,23),(46,21),(47,20),(47,19),(46,19),(46,22),(45,25),(45,54),(44,56),(42,55)],'c1')
result.rect(43,25,1,30,'c4')
result.line(44,24,44,39,'c2')
result.line(43,41,43,53,'c2')
result.poly([(43,24),(44,21),(44,18),(46,17),(48,17),(49,19),(49,21),(47,22),(47,21),(48,20),(48,18),(45,18),(45,22),(44,25)],'c4')
result.line(45,18,47,18,'c2')
result.line(44,19,44,22,'c2')
result.set(43,46,'c6')
result.set(44,30,'c6')
# The original hand closes over the staff.
input_canvas.select(40,35,5,4).copy_to(40,35,result)
view(result)
finish(result)
