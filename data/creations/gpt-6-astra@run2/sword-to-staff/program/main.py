output = input_canvas.copy(name='output')
# Remove the sword guard and blade, preserving the adventurer's arm.
output.rect(40,39,7,2,'#ffffff')
output.rect(42,41,3,15,'#ffffff')
# A carved wooden staff, with a bent, knotted crown.
dark='#2e1f12'
wood='#7a4a26'
light='#96613a'
output.poly([(44,56),(44,23),(43,21),(43,17),(45,14),(48,14),(50,16),(50,20),(48,23),(47,26),(47,56)],dark)
output.rect(45,24,1,31,wood)
output.line(45,25,45,53,light)
output.poly([(44,18),(46,15),(48,15),(49,17),(49,20),(47,22),(46,26),(45,26),(45,22),(44,20)],wood)
output.line(45,18,46,16,light)
output.line(46,16,48,16,light)
output.line(44,19,45,21,light)
output.set(47,18,dark)
output.set(47,19,dark)
output.line(46,21,46,24,light)
# Restore the fingers in front of the shaft to show a firm grip.
output.rect(43,35,3,3,'#f2c49b')
output.rect(44,37,2,1,'#d89b6a')
output.rect(43,38,3,1,dark)
output.set(46,35,dark)
output.set(46,36,dark)
output.set(46,37,dark)
view(output,scale=8)
finish(output)
