f1=new_canvas(88,68,name='original')
f1.blit(input_canvas,8,3)
f2=new_canvas(88,68,name='release')
# Repose the original pixel clusters, retaining their palette and shading.
for y in range(63):
    if y<34:
        lean=round(8*(34-y)/34)
        for x in range(47):
            col=input_canvas.get(x,y)
            if col==0 or col in (13,14,15): continue
            if x>=28 and 20<=y<=24: continue
            f2.set(x+8+lean,y+5,col)
    else:
        # Open the stance: the forward leg and boot travel to the right.
        stride=round(12*min(1,(y-34)/23))
        for xx in range(47+stride):
            if xx<=16: sx=xx
            elif xx<27+stride: sx=16+round((xx-16)*11/(11+stride))
            else: sx=xx-stride
            if sx>=47: continue
            col=input_canvas.get(sx,y)
            if col: f2.set(xx+8,y+3,col)
# Extended sleeve, with a bent upper arm joining the forward shoulder.
f2.poly([(34,24),(40,24),(44,26),(51,26),(51,31),(42,31),(36,28)],6)
f2.poly([(35,25),(40,25),(44,27),(50,27),(50,30),(42,29),(36,27)],8)
f2.line(37,25,40,26,4)
f2.line(42,29,49,30,7)
# Preserve the original outstretched glove, moved beyond the sleeve.
for y in range(21,25):
    for x in range(31,40):
        col=input_canvas.get(x,y)
        if col and col not in (13,14,15): f2.set(x+19,y+5,col)
f2.line(50,27,55,27,10)
f2.line(51,28,56,28,10)
f2.set(56,27,5)
# Fast, tapering fire trail and detached leading flame.
red='#bc3b19'
f2.poly([(55,27),(61,25),(65,25),(63,22),(68,24),(72,23),(70,19),(76,21),(79,18),(79,22),(82,24),(83,28),(81,32),(77,34),(71,33),(67,30),(62,30),(58,29)],red)
f2.poly([(56,27),(65,26),(69,27),(67,24),(72,25),(74,22),(73,20),(77,23),(79,21),(79,24),(82,26),(82,29),(79,32),(73,32),(68,29),(62,29)],13)
f2.poly([(60,27),(69,27),(73,28),(71,25),(75,26),(77,23),(78,26),(80,26),(81,28),(78,31),(74,31),(69,28)],14)
f2.poly([(68,27),(74,28),(76,26),(77,28),(79,27),(79,29),(76,30),(73,29)],15)
f2.line(58,25,62,24,13)
f2.line(63,32,67,33,13)
f2.set(69,20,13)
f2.line(76,16,77,17,13)
f2.set(84,22,14)
f2.set(84,31,13)
f2.set(60,31,14)
view(f1)
view(f2)
finish([f1,f2])
