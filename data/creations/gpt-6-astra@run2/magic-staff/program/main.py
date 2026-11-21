result = new_canvas(48,48, name='magic_staff')
c=result
# Restrained, opaque sprite palette; all untouched pixels stay transparent.
ink='#291c32'
wooddark='#553047'
woodshadow='#794451'
wood='#a15d49'
light='#cf8c59'
gold='#efbd76'
# Hook and shaft: a single connected, stepped silhouette.
c.poly([(10,41),(24,20),(28,14),(29,11),(28,9),(27,8),(24,8),(22,10),(22,12),(24,14),(24,17),(22,18),(19,17),(17,14),(16,10),(17,7),(20,4),(24,2),(29,2),(32,4),(34,7),(35,11),(33,16),(30,21),(16,43),(13,46),(10,45)],ink)
c.poly([(11,42),(26,19),(30,13),(31,10),(29,7),(27,6),(23,6),(20,9),(20,13),(23,15),(23,16),(21,17),(18,14),(17,10),(18,7),(21,5),(25,3),(29,3),(31,5),(33,8),(34,11),(32,16),(29,21),(15,43),(13,45),(11,44)],woodshadow)
# Warm outer edge and flowing grain around the crook.
c.poly([(11,42),(25,21),(29,15),(31,11),(30,7),(27,5),(23,5),(19,8),(19,12),(21,15),(20,15),(18,12),(18,9),(20,6),(24,4),(28,4),(31,6),(33,10),(32,14),(29,20),(14,43),(12,44)],wood)
c.line(12,41,27,19,light)
c.line(27,19,31,12,light)
c.line(31,12,32,10,light)
c.line(32,9,30,6,light)
c.line(29,5,25,4,gold)
c.line(24,4,20,7,light)
c.line(19,8,18,10,gold)
c.line(19,12,21,15,light)
c.set(22,16,gold)
c.line(29,17,18,34,wooddark)
c.line(17,36,13,42,wooddark)
c.set(12,44,light)
# Two little branch scars / knots.
c.line(25,22,26,24,wooddark)
c.set(25,23,light)
c.line(16,37,17,38,woodshadow)
# Dark violet leather grip winds across the diagonal shaft.
c.poly([(20,27),(22,25),(26,28),(24,31),(21,35),(17,33)],ink)
c.poly([(20,28),(22,27),(24,29),(21,33),(19,32)],'#574267')
c.line(20,28,23,30,'#a18a9d')
c.line(19,30,22,32,'#8a6f8b')
c.line(18,32,20,34,'#b69b9e')
c.set(24,28,gold)
c.set(19,34,gold)
# Amethyst suspended in the hook, faceted with sharp pixel edges.
c.poly([(25,9),(28,11),(28,14),(25,17),(23,14),(23,12)],'#38204d')
c.poly([(25,10),(27,12),(27,14),(25,16),(24,14),(24,12)],'#9254d3')
c.line(25,11,25,14,'#e5b7ff')
c.set(26,12,'#fff0ff')
c.set(26,14,'#bd79f0')
c.set(25,15,'#6a38a5')
# Purple motes and small four-point spell sparks, kept clear of the silhouette.
def spark(x,y,col,core):
    c.line(x-2,y,x+2,y,col)
    c.line(x,y-2,x,y+2,col)
    c.set(x,y,core)
spark(39,8,'#a563dc','#f7d9ff')
spark(35,23,'#9254d3','#edc1ff')
spark(11,18,'#ae70e8','#ffe4ff')
c.set(13,6,'#cc94f3')
c.set(14,7,'#7446a1')
c.rect(37,16,2,2,'#bd80ee')
c.set(38,16,'#e6b6ff')
c.set(29,25,'#cb91ef')
c.set(31,28,'#704292')
c.set(10,29,'#a563dc')
c.set(8,31,'#653979')
c.set(39,28,'#704292')
c.set(16,21,'#8250aa')
view(result)
finish(result)
