result = new_canvas(16, 16, name="magnifying_glass")
# Diagonal walnut handle, capped in brass.
ink = '#252333'
result.poly([(9,8),(15,13),(15,14),(14,15),(13,15),(8,10)], ink)
result.line(10,10,14,14,'#704634')
result.line(11,10,14,13,'#b77b47')
result.set(13,13,'#98603c')
result.set(14,14,'#704634')
# Pixel-stepped circular frame.
rows = {0:(4,7),1:(2,9),2:(1,10),3:(1,10),4:(0,11),5:(0,11),6:(0,11),7:(0,11),8:(1,10),9:(1,10),10:(2,9),11:(4,7)}
for y,(a,b) in rows.items():
    result.line(a,y,b,y,ink)
rows_inner = {1:(4,7),2:(2,9),3:(2,9),4:(1,10),5:(1,10),6:(1,10),7:(1,10),8:(2,9),9:(2,9),10:(4,7)}
for y,(a,b) in rows_inner.items():
    result.line(a,y,b,y,'#be884b')
result.line(4,1,7,1,'#ffe2a0')
result.line(2,2,4,2,'#ffe2a0')
result.line(2,3,2,4,'#edbd71')
result.line(1,4,1,7,'#edbd71')
result.line(4,10,7,10,'#805137')
result.line(9,8,9,9,'#805137')
result.line(10,5,10,7,'#956039')
# Inset lens and its lower shadow.
lens = {2:(4,7),3:(3,8),4:(2,9),5:(2,9),6:(2,9),7:(2,9),8:(3,8),9:(4,7)}
for y,(a,b) in lens.items():
    result.line(a,y,b,y,'#35536c')
for y,a,b in [(3,4,7),(4,3,8),(5,3,8),(6,3,8),(7,3,7),(8,4,6)]:
    result.line(a,y,b,y,'#72b6c2')
result.line(4,3,6,3,'#c8f0e3')
result.line(3,4,4,4,'#e9fff0')
result.set(3,5,'#e9fff0')
result.line(5,7,7,5,'#98d3d3')
result.set(7,8,'#518897')
# Small metal ferrule at the transition to the grip.
result.set(10,10,'#e6b66b')
result.set(11,11,'#be884b')
view(result, scale=24)
finish(result)
