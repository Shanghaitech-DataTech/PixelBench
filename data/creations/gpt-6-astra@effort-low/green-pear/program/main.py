result = new_canvas(32,32)
outline='#304529'
dark='#528337'
mid='#7eae3e'
light='#acd34f'
shine='#d5e880'
brown='#765039'
# curved wooden stem
result.poly([(15,9),(15,5),(17,2),(19,2),(18,4),(17,6),(17,9)],brown)
result.line(15,6,15,8,outline)
# pointed leaf
result.poly([(17,5),(19,2),(23,2),(25,3),(22,6),(19,6)],outline)
result.poly([(18,5),(21,3),(24,3),(21,5)],dark)
result.line(19,4,22,3,light)
# pear silhouette: narrow neck to broad base
result.poly([(14,7),(17,7),(19,9),(19,12),(20,15),(23,18),(25,22),(25,25),(23,28),(20,29),(11,29),(7,27),(5,24),(5,21),(7,17),(10,14),(11,10)],outline)
result.poly([(14,8),(17,8),(18,10),(18,13),(19,16),(22,19),(24,22),(24,25),(22,27),(19,28),(11,28),(8,26),(6,23),(6,21),(8,18),(11,15),(12,11)],mid)
# shaded right and bottom
result.poly([(17,9),(18,11),(18,14),(20,18),(23,21),(24,23),(23,26),(20,28),(11,28),(8,26),(7,24),(10,26),(17,26),(20,24),(21,21),(19,18),(17,14)],dark)
# broad light face
result.poly([(13,10),(15,9),(16,10),(16,14),(18,18),(19,21),(18,24),(15,25),(11,25),(8,23),(8,21),(10,18),(12,15)],light)
# compact highlight clusters
result.line(13,11,13,14,shine)
result.line(12,14,12,16,shine)
result.poly([(10,19),(12,18),(12,20),(10,22),(9,22),(9,20)],shine)
# restrained skin texture
result.set(15,23,mid)
result.set(17,21,mid)
result.set(10,24,mid)
result.set(20,23,mid)
result.set(21,25,mid)
result.line(14,28,16,28,outline)
view(result)
finish(result)
