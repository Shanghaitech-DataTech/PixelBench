result = new_canvas(32, 32, name='factory')
c = result
# Compact industrial palette.
ink='#202733'
edge='#35404b'
brick='#ad6550'
light='#d68b65'
shade='#794640'
mortar='#824c43'
roof='#74858a'
rooflight='#a6b5ad'
roofdark='#4c606b'
# Foundation and shallow three-quarter building silhouette.
c.poly([(3,17),(9,13),(28,16),(28,26),(23,29),(3,26)],ink)
c.poly([(4,18),(23,20),(23,27),(4,25)],brick)
c.poly([(24,20),(27,18),(27,25),(24,27)],shade)
# Brick courses, staggered joints.
c.line(4,21,22,23,mortar)
c.line(4,24,22,26,mortar)
for x,y in [(7,19),(14,20),(20,21),(10,22),(18,23),(6,25)]:
    c.line(x,y,x,y+1,mortar)
c.line(5,19,10,19,light)
c.line(15,20,20,20,light)
c.line(5,22,8,22,light)
c.set(19,24,light)
c.line(25,22,27,21,'#5c3e3d')
c.line(25,25,27,24,'#5c3e3d')
# Flat roof with a raised perimeter lip.
c.poly([(2,16),(9,12),(29,15),(23,20),(2,18)],ink)
c.poly([(4,16),(10,13),(27,15),(22,18)],roof)
c.line(4,16,22,18,rooflight)
c.line(22,18,27,15,rooflight)
c.line(3,18,22,20,roofdark)
c.line(24,19,28,16,edge)
# Tall brick smokestack, inset behind the front roof edge.
c.poly([(7,5),(10,3),(14,4),(14,14),(11,16),(7,15)],ink)
c.poly([(8,6),(11,7),(11,14),(8,14)],brick)
c.poly([(12,6),(13,5),(13,13),(12,14)],shade)
c.line(8,8,10,8,mortar)
c.line(8,11,10,11,mortar)
c.set(9,7,light)
c.set(8,10,light)
c.set(10,13,light)
# Wide cap and dark flue opening.
c.poly([(6,4),(10,2),(15,3),(15,6),(11,8),(6,6)],ink)
c.poly([(7,4),(10,3),(14,4),(11,6)],light)
c.line(7,5,10,6,brick)
c.line(11,6,14,5,shade)
c.line(9,4,11,4,ink)
# Rooftop extractor: boxed housing and slatted grille.
c.poly([(17,12),(20,10),(25,11),(25,14),(22,16),(17,15)],edge)
c.poly([(18,12),(20,11),(24,12),(22,13)],rooflight)
c.rect(18,13,4,2,roofdark)
c.line(23,13,24,12,roof)
c.set(19,13,ink)
c.set(21,13,ink)
c.set(19,14,ink)
c.set(21,14,ink)
# Small circular duct on the remaining roof area.
c.rect(14,15,2,2,edge)
c.line(14,14,15,14,rooflight)
# Recessed roller door and two lit industrial windows.
c.rect(12,21,6,6,ink)
c.rect(13,22,4,4,roofdark)
c.line(13,23,16,23,roof)
c.line(13,25,16,25,roof)
c.line(12,27,18,27,rooflight)
c.rect(5,20,5,3,ink)
c.line(6,21,8,21,'#dfc786')
c.set(7,21,edge)
c.rect(20,22,3,3,ink)
c.set(21,23,'#dfc786')
# Foundation rim and side-wall ventilation slot.
c.line(4,26,10,27,edge)
c.line(19,28,23,28,edge)
c.line(25,19,26,18,ink)
c.line(25,20,26,19,roofdark)
view(result, scale=12, margin=0)
finish(result)
