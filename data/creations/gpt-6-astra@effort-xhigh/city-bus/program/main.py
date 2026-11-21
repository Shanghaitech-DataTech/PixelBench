# Modern low-floor city bus. All pixels are opaque or fully transparent.
result = new_canvas(64, 32, name="city_bus")
c = result
P = {
    'ink':'#182c38', 'tire':'#17212c', 'rubber':'#2c3a46',
    'rim':'#8298a3', 'steel':'#c5d4d2', 'hub':'#4b6574',
    'cream':'#e5eadd', 'roof':'#f7f3de', 'shade':'#a9c2bc',
    'teal':'#198f8f', 'light':'#45b9ab', 'deep':'#126470',
    'glass':'#284b60', 'blue':'#42778a', 'glint':'#91bfc4',
    'display':'#202f32', 'amber':'#ffd16a', 'orange':'#d98b43',
    'red':'#db6052', 'white':'#fff4ce'
}
# Low rooftop air-conditioning enclosure.
c.poly([(18,4),(20,3),(35,3),(37,5),(37,6),(18,6)],P['ink'])
c.rect(20,4,15,2,P['shade'])
c.line(21,4,33,4,P['cream'])
c.line(24,5,33,5,P['hub'])
# Stepped, gently rounded silhouette, with the nose on the right.
c.poly([(5,6),(56,6),(59,7),(61,10),(61,22),(62,23),(61,25),(4,25),(2,23),(2,9),(3,7)],P['ink'])
c.rect(4,8,54,16,P['cream'])
c.rect(3,10,2,12,P['cream'])
c.poly([(57,8),(59,9),(60,11),(60,23),(57,24)],P['cream'])
c.line(5,7,55,7,P['roof'])
c.line(4,8,58,8,P['roof'])
# A continuous dark window band, broken into distinct panes below.
c.rect(4,9,54,9,P['ink'])
c.rect(5,10,7,7,P['glass'])
c.rect(14,10,8,7,P['glass'])
c.rect(33,10,7,7,P['glass'])
c.rect(42,13,7,4,P['glass'])
for x,w in [(5,7),(14,8),(33,7)]:
    c.rect(x,10,w,2,P['blue'])
    c.line(x,10,x+w-1,10,P['glint'])
    c.line(x+1,12,x+3,14,P['blue'])
c.line(42,13,48,13,P['blue'])
c.line(43,14,45,16,P['blue'])
# A compact, unbranded amber LED route display, with a dark bezel.
c.rect(40,9,10,7,P['display'])
for x, glyph in [(41,['111','001','111','100','111']),
                 (45,['101','101','111','001','001'])]:
    for dy,row in enumerate(glyph):
        for dx,pixel in enumerate(row):
            if pixel == '1':
                c.set(x+dx,10+dy,P['amber'])
# Front windscreen follows the upright curved nose.
c.poly([(58,10),(59,11),(60,13),(60,17),(58,17)],P['glass'])
c.line(59,12,59,15,P['glint'])
c.line(58,17,60,17,P['ink'])
# Teal lower panels, pale belt rail, and a darker lower skirt.
c.rect(3,19,57,5,P['teal'])
c.line(4,18,59,18,P['roof'])
c.line(4,19,59,19,P['light'])
c.line(4,24,60,24,P['deep'])
c.line(5,25,59,25,P['ink'])
# Passenger doors: rear door near the middle, front door ahead of the axle.
for left,right,top in [(24,31,9),(51,57,10)]:
    c.rect(left,top,right-left+1,25-top,P['ink'])
    mid=(left+right)//2
    for a,b in [(left+1,mid),(mid+2,right-1)]:
        c.rect(a,top+1,b-a+1,12,P['glass'])
        c.rect(a,top+1,b-a+1,2,P['blue'])
        c.line(a,top+1,b,top+1,P['glint'])
        c.line(a,top+7,b,top+7,P['blue'])
        c.line(a,22,b,22,P['shade'])
        c.line(a,23,b,23,P['deep'])
    c.line(left+1,24,right-1,24,P['steel'])
    c.set(mid,19,P['steel'])
    c.set(mid+2,19,P['steel'])
# Rear engine panel, discreet seams, and lamps.
c.line(5,20,5,23,P['deep'])
c.line(7,21,10,21,P['deep'])
c.line(7,23,9,23,P['deep'])
c.line(34,20,38,20,P['light'])
c.line(35,22,38,22,P['deep'])
c.set(4,17,P['orange'])
c.rect(2,19,2,3,P['red'])
c.set(3,19,P['amber'])
c.rect(59,19,2,2,P['white'])
c.set(60,21,P['orange'])
c.rect(59,23,3,1,P['hub'])
c.rect(2,23,3,1,P['hub'])
# Wheel wells and two tyres. Upper arch edges are inset into the body.
for cx in (13,44):
    c.rect(cx-3,19,7,1,P['deep'])
    c.rect(cx-4,20,9,2,P['ink'])
    c.rect(cx-5,22,11,4,P['ink'])
    c.circle(cx,24,4,P['tire'])
    c.line(cx-2,21,cx+2,21,P['rubber'])
    c.set(cx-3,22,P['rubber'])
    c.ellipse(cx,24,2,2,P['rim'])
    c.line(cx-1,22,cx+1,22,P['steel'])
    c.set(cx-2,23,P['steel'])
    c.set(cx,24,P['hub'])
    c.set(cx+1,25,P['hub'])
    c.line(cx-1,27,cx+1,27,P['rubber'])
# Door-side mirror, articulated from the front pillar.
c.line(58,9,62,9,P['ink'])
c.rect(61,10,2,3,P['ink'])
c.set(62,10,P['shade'])
assert tuple(result.stats()['size']) == (64, 32)
assert result.stats()['colors_used'] <= 86
print(result.stats_text())
view(result, scale=8, margin=0)
save('city_bus', result)
finish(result)
