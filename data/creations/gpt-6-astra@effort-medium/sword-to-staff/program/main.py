output = input_canvas.copy(name='output')
# Remove the guard, grip remnant and steel blade below the fist.
output.rect(40,38,7,3,1)
output.rect(42,41,3,15,1)
# A long wooden walking staff with a naturally bent, knotted crown.
output.poly([(43,58),(43,24),(44,21),(44,17),(46,15),(49,16),(50,19),(49,22),(47,23),(46,26),(46,58)],2)
output.poly([(44,57),(44,25),(45,21),(45,18),(46,16),(48,17),(49,19),(48,21),(46,22),(45,26),(45,57)],5)
output.line(44,27,44,56,3)
output.line(45,18,46,17,8)
output.line(46,17,48,18,3)
output.line(45,22,46,20,3)
output.set(47,19,7)
output.line(44,46,45,45,7)
output.set(44,47,4)
output.line(44,30,45,29,7)
# The existing arm and fingers sit in front of the staff.
for y in range(28,38):
    for x in range(40,45):
        p=input_canvas.get(x,y)
        if p != 1:
            output.set(x,y,p)
view(output)
finish(output)
