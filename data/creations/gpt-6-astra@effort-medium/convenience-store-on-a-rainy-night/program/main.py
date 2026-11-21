result = new_canvas(64,64, '#111b30', name='rainy_corner')
c=result
# distant buildings
c.rect(0,8,13,33,'#19283e'); c.rect(3,4,8,5,'#19283e')
c.rect(52,3,12,39,'#18263b')
for x,y in [(3,13),(8,23),(56,9),(60,25)]: c.rect(x,y,2,4,'#304359')
c.rect(0,41,64,23,'#233448')
c.poly([(0,49),(63,43),(63,53),(0,60)],'#293d50')
# shop side and facade
c.rect(8,16,46,30,'#101a28')
c.rect(10,18,42,26,'#45616a')
c.rect(12,22,38,21,'#9b8466')
# bright glass panes
c.rect(13,23,22,17,'#f8ce7c')
c.rect(37,23,12,19,'#ffd98b')
c.rect(14,24,20,4,'#ffe9ac')
# shelves, merchandise silhouettes
for y in [31,37]:
 c.rect(14,y,20,1,'#947553')
for x,h,col in [(15,3,'#bd7759'),(18,4,'#718879'),(22,3,'#b9905a'),(26,4,'#b76c50'),(30,3,'#729187')]:
 c.rect(x,31-h,2,h,col)
for x,col in [(15,'#7d9b86'),(19,'#c87e55'),(23,'#d39a60'),(28,'#81978a'),(31,'#bb725b')]:
 c.rect(x,34,2,3,col)
c.rect(13,39,22,2,'#d9a860')
# glazing reflections and mullions
c.line(14,24,14,38,'#fff1bf'); c.line(16,24,22,30,'#ffe4a0')
c.line(26,24,33,31,'#ffe4a0')
c.rect(24,23,1,17,'#647873')
c.rect(35,22,2,21,'#253b47')
c.rect(49,22,2,22,'#253b47')
c.rect(12,40,24,3,'#314b55')
# open door angled outward
c.poly([(38,24),(43,26),(43,44),(38,41)],'#6c8a84')
c.poly([(39,25),(42,27),(42,39),(39,38)],'#b4c8a3')
c.line(41,32,41,34,'#ffe7a1')
c.rect(10,44,43,2,'#627778'); c.rect(9,46,45,2,'#334b57')
# header illuminated blank fascia with invented generic text
c.rect(9,14,44,8,'#172c3c'); c.rect(11,15,40,6,'#6bada9')
c.rect(12,14,38,7,'#b8e2c6')
c.text(18,14,'OPEN', '#284f59')
# awning top and edge
c.rect(8,12,46,2,'#608b91'); c.rect(7,21,48,2,'#213d4b')
c.line(8,21,54,21,'#769c9b')
# street reflections
for x,y,w,col in [(15,50,16,'#8e8465'),(28,52,16,'#b29b6b'),(19,54,13,'#736f60'),(35,49,13,'#d3b075'),(25,57,17,'#777a66'),(35,59,12,'#535f5d'),(8,58,10,'#3e6474'),(45,54,13,'#4c7280'),(3,51,7,'#3b596d'),(14,61,18,'#375465')]:
 c.rect(x,y,w,1,col)
c.line(25,49,32,49,'#c8b07a'); c.line(33,55,40,55,'#c8a675')
# umbrella rack on right
c.rect(51,38,9,1,'#8aabb0'); c.rect(51,39,1,7,'#263e50'); c.rect(59,39,1,7,'#263e50')
c.rect(51,43,9,2,'#537382'); c.set(52,45,'#a0b4b4'); c.set(59,45,'#a0b4b4')
for x,y,col in [(53,34,'#b76972'),(56,32,'#82a7af'),(58,35,'#7186a1')]:
 c.line(x,y-2,x,y+7,'#a3b9b8'); c.set(x-1,y-2,'#a3b9b8')
 c.poly([(x,y),(x-1,y+5),(x,y+8),(x+1,y+5)],col)
# bicycle foreground left, wheels and frame
for x in [8,23]:
 c.circle(x,48,5,'#101c2b'); c.circle(x,48,4,'#73909a',False)
 c.line(x-3,50,x+3,46,'#3e5769'); c.set(x,48,'#a4b5b6')
c.line(8,48,12,41,'#cf8c77'); c.line(12,41,17,48,'#cf8c77'); c.line(8,48,17,48,'#cf8c77')
c.line(12,41,20,41,'#e6ad8a'); c.line(20,41,17,48,'#cf8c77'); c.line(20,40,23,48,'#e6ad8a')
c.line(20,41,20,37,'#99b7bb'); c.line(20,37,23,37,'#99b7bb')
c.line(12,41,11,39,'#a1aeb2'); c.rect(9,38,5,2,'#162738')
c.line(17,48,19,50,'#91a4aa'); c.line(18,50,20,50,'#172b3a')
# entering figure: boots and coat, warmly lit right edge
c.rect(40,43,2,6,'#172537'); c.rect(44,43,2,4,'#172537')
c.rect(39,49,4,1,'#0f1e2d'); c.rect(44,47,4,1,'#0f1e2d')
c.poly([(40,33),(44,33),(46,38),(46,44),(38,44),(39,37)],'#dfac48')
c.poly([(40,34),(42,34),(41,42),(39,43)],'#bc8035')
c.line(45,36,47,39,'#ffcf6c'); c.line(47,39,48,35,'#ffcf6c'); c.set(48,34,'#f3c89a')
c.ellipse(42,31,3,4,'#e9b951'); c.poly([(43,28),(45,30),(45,34),(42,34),(42,30)],'#8c653e')
c.rect(44,30,2,3,'#f5cf99'); c.line(40,29,41,28,'#ffdc7a')
c.line(42,36,42,41,'#f9c65e')
# rain in controlled short streaks
for x,y in [(1,2),(16,2),(28,5),(42,1),(58,1),(6,8),(21,7),(36,9),(61,13),(3,29),(5,36),(58,22),(61,32),(1,44),(30,43),(60,48),(4,57),(51,58),(57,55),(22,59),(34,61)]:
 c.line(x,y,x-1 if x>0 else x,y+2,'#4c7189')
# roof droplets, puddle ripples
for x in [11,28,48]: c.set(x,11,'#9bb8bd')
for x,y in [(5,55),(53,51),(47,61)]:
 c.line(x,y,x+5,y,'#5a7c8d'); c.set(x+2,y-1,'#7f9ba5')
view(c)
finish(result)
