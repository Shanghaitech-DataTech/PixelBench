result = new_canvas(64,64,background='#172f41',name='transit_icons')
bg='#172f41'
edge='#365363'
cream='#e6eee4'
ink='#203e4b'
teal='#398e91'
light='#8ac4bb'
window='#b9dcd0'
gold='#efb653'
white='#fff2cf'
# Four identical stepped-corner enamel panels.
for x,y in [(2,2),(34,2),(2,34),(34,34)]:
    result.rect(x+2,y,24,28,edge)
    result.rect(x,y+2,28,24,edge)
    result.rect(x+2,y+1,24,26,cream)
    result.rect(x+1,y+2,26,24,cream)
# Bus: broad windshield, route display, mirrors and wheels.
result.rect(10,24,4,3,ink)
result.rect(20,24,4,3,ink)
result.rect(7,12,2,6,ink)
result.rect(25,12,2,6,ink)
result.rect(11,6,12,2,ink)
result.rect(9,8,16,17,ink)
result.rect(11,8,12,15,teal)
result.rect(13,8,8,2,gold)
result.rect(11,11,12,8,ink)
result.rect(12,12,10,5,window)
result.rect(12,12,3,2,white)
result.rect(16,12,2,5,ink)
result.rect(11,20,3,2,white)
result.rect(20,20,3,2,white)
result.rect(15,21,4,2,ink)
# Subway: vaulted car silhouette and rails distinguish it from bus.
result.line(44,23,40,27,ink)
result.line(45,23,41,27,ink)
result.line(52,23,56,27,ink)
result.line(51,23,55,27,ink)
result.rect(43,26,11,1,teal)
result.poly([(44,6),(52,6),(56,10),(56,21),(53,25),(43,25),(40,21),(40,10)],ink)
result.poly([(45,8),(51,8),(54,11),(54,20),(51,23),(45,23),(42,20),(42,11)],teal)
result.rect(46,8,4,2,gold)
result.rect(43,11,10,8,ink)
result.rect(44,12,8,5,window)
result.rect(44,12,3,2,white)
result.rect(47,12,2,5,ink)
result.rect(43,20,3,2,white)
result.rect(50,20,3,2,white)
# Bicycle: two matched wheels and a diamond frame.
def thickline(x0,y0,x1,y1,col):
    result.line(x0,y0,x1,y1,col)
    result.line(x0,y0+1,x1,y1+1,col)
for x in [9,23]:
    result.circle(x,53,5,ink)
    result.circle(x,53,3,cream)
thickline(9,53,13,45,teal)
thickline(13,45,18,53,teal)
thickline(9,53,18,53,teal)
thickline(13,45,21,45,teal)
thickline(18,53,21,45,teal)
thickline(21,43,23,53,teal)
result.rect(10,42,6,2,ink)
result.rect(12,44,2,2,ink)
result.rect(19,41,5,2,ink)
result.rect(19,42,2,3,ink)
result.rect(8,52,2,2,gold)
result.rect(22,52,2,2,gold)
result.rect(16,52,3,3,ink)
result.rect(18,54,3,2,ink)
# Pedestrian: circular head, forward lean, swinging arms and stride.
result.rect(48,38,4,1,ink)
result.rect(47,39,6,4,ink)
result.rect(48,43,4,1,ink)
result.rect(49,39,3,3,gold)
result.poly([(47,44),(51,44),(51,48),(55,50),(55,52),(52,52),(49,50),(48,52),(52,56),(54,58),(52,60),(49,58),(45,54),(43,59),(40,59),(43,52),(45,48),(42,50),(40,50),(40,48),(43,46)],ink)
result.poly([(47,45),(49,45),(49,48),(47,52),(45,51)],teal)
result.rect(41,58,3,2,ink)
result.rect(52,58,4,2,ink)
view(result,scale=8,margin=0)
save('public-transportation-icon-set',result)
finish(result)
