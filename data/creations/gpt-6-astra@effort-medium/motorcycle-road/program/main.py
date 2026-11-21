# Remove only the white backdrop connected to the image boundary.
bike=input_canvas.copy(name='motorcycle')
bike.fill_at(0,0,None)
result=new_canvas(64,64,'#91cbd3',name='country_road')
# Small stepped clouds.
result.rect(5,7,15,3,'#e7f0db').rect(8,5,7,2,'#e7f0db').rect(17,8,7,2,'#e7f0db')
result.rect(43,4,12,3,'#e7f0db').rect(46,3,5,1,'#e7f0db')
# Layers of low hills and sunlit pasture.
result.poly([(0,24),(0,20),(9,17),(17,18),(28,23),(40,18),(50,16),(63,19),(63,30)],'#6b9c7c')
result.poly([(0,26),(12,22),(23,23),(36,27),(49,23),(63,25),(63,40),(0,40)],'#8ca95c')
result.poly([(0,30),(16,28),(34,31),(50,28),(63,29),(63,42),(0,42)],'#b5bc69')
result.line(0,34,63,31,'#d1cb82')
# Distant roadside trees.
for x,y in [(3,24),(58,22),(62,24)]:
 result.rect(x,y,1,7,'#6e6c43')
 result.ellipse(x,y-2,3,4,'#477656')
 result.rect(x-1,y-5,2,3,'#628c59')
# Field fence.
result.line(0,36,63,34,'#8b8259')
result.line(0,39,63,37,'#8b8259')
for x in [2,12,23,35,47,59]:
 y=35-x//30
 result.rect(x,y,2,7,'#766c50')
 result.set(x,y,'#d4c493')
# Paved lane, gravel verges, foreground grass.
result.poly([(0,42),(63,39),(63,60),(0,62)],'#cfbd8b')
result.poly([(0,44),(63,41),(63,57),(0,60)],'#75777c')
result.line(0,45,63,42,'#b6b6a5')
result.line(0,58,63,55,'#b6b6a5')
for x in [0,23,46]:
 result.line(x,54-x//24,x+11,54-x//24,'#e3d9a5')
result.poly([(0,62),(18,61),(38,60),(63,60),(63,64),(0,64)],'#788f4c')
for x,y in [(3,62),(11,63),(28,62),(41,61),(54,62),(60,60)]:
 result.line(x,y,x+2,y-1,'#aabb69')
result.ellipse(32,48,24,1,'#585b60')
result.blit(bike,0,0)
view(result)
finish(result)
