result = new_canvas(64,64, '#201923', name='tavern')
c=result
ink='#17151e'; dark='#30202a'; wood='#63392f'; mid='#8c5137'; light='#b97943'; gold='#e5ac57'; cream='#ffe6a0'
# wall and floor
c.rect(2,3,60,38,'#483035')
c.rect(4,8,56,30,'#593a36')
for y in [11,19,27,35]:
 c.line(3,y,61,y,'#493035')
for x in [5,31,59]:
 c.rect(x,3,3,38,dark); c.line(x,5,x,37,'#805039')
c.rect(0,0,64,5,ink); c.rect(1,1,62,2,wood)
c.rect(0,41,64,23,'#493035')
for y in [45,51,58,63]: c.line(0,y,63,y,'#271f28')
for x,y in [(12,42),(42,42),(25,46),(54,46),(8,52),(38,52),(22,59),(51,59)]: c.line(x,y,x,min(63,y+5),'#2d2229')
for x,y,w in [(4,48,9),(28,44,8),(43,55,14),(25,61,15),(3,56,8)]: c.line(x,y,x+w,y,'#684236')
# bottle shelves recessed
c.rect(20,9,36,23,ink); c.rect(22,10,32,20,'#34262c')
for y in [18,29]:
 c.rect(19,y,38,3,ink); c.rect(20,y,36,1,light); c.rect(21,y+1,35,1,wood)
def bottle(x,y,col):
 c.rect(x+1,y,2,2,ink);c.rect(x,y+2,4,6,ink)
 c.rect(x+1,y+2,2,5,col);c.set(x+1,y+2,'#b2bd83');c.rect(x+1,y+4,2,2,'#d1ac72')
for x,y,col in [(23,10,'#63856b'),(29,10,'#a85b42'),(36,10,'#5d8580'),(43,10,'#779052'),(49,10,'#a95f44'),(23,21,'#a47842'),(29,21,'#487a67'),(35,21,'#4f827e'),(45,21,'#82874f'),(51,21,'#944c41')]: bottle(x,y,col)
# wall sign
c.rect(9,13,9,12,ink);c.rect(10,14,7,10,mid)
c.rect(12,16,3,5,gold);c.rect(15,17,2,3,gold);c.set(13,15,cream)
# hanging lamps with stepped pools of warm wall light
for x,y in [(13,8),(45,6)]:
 c.rect(x-5,y+5,11,2,'#87583d');c.rect(x-4,y+7,9,1,'#754a38')
 c.line(x,4,x,y+2,ink)
 c.poly([(x-2,y+2),(x+2,y+2),(x+5,y+6),(x-5,y+6)],ink)
 c.poly([(x-1,y+3),(x+1,y+3),(x+3,y+5),(x-3,y+5)],light)
 c.line(x-4,y+6,x+4,y+6,gold);c.line(x-2,y+7,x+2,y+7,cream)
# counter shadow and panel front
c.rect(8,36,49,14,ink); c.rect(10,38,45,10,wood)
for x in [11,26,41]:
 c.rect(x,39,13,8,'#3d292b');c.rect(x+1,40,11,6,mid);c.line(x+2,41,x+10,41,light);c.line(x+11,41,x+11,46,wood)
c.rect(8,48,49,2,ink);c.line(10,48,55,48,light)
c.poly([(9,31),(54,31),(59,35),(58,38),(6,38),(6,35)],ink)
c.poly([(10,32),(53,32),(57,35),(8,35)],light)
c.line(8,36,57,36,'#d89a51');c.line(10,33,50,33,'#ca8a48')
# glasses and drinks on bar
def mug(x,y):
 c.rect(x,y,4,5,ink);c.rect(x+4,y+1,2,3,ink);c.set(x+4,y+2,gold)
 c.rect(x+1,y+1,2,3,'#d99b49');c.line(x,y,x+3,y,'#fff0bd');c.set(x+1,y+1,cream)
mug(15,29);mug(43,29)
c.rect(33,28,4,4,ink);c.rect(34,28,2,3,'#afc7b1');c.set(34,28,'#f1e4b1');c.line(35,31,35,33,cream);c.line(34,33,36,33,cream)
bottle(24,26,'#4c7960')
# floor shadows
for x in [18,36,51]: c.ellipse(x,57,7,2,'#2c222a')
# stools
for x,y in [(18,47),(36,49),(51,46)]:
 c.line(x-3,y+3,x-5,y+10,ink);c.line(x+3,y+3,x+5,y+10,ink)
 c.line(x-2,y+3,x-4,y+10,light);c.line(x+2,y+3,x+4,y+10,wood)
 c.line(x-3,y+8,x+3,y+8,ink);c.line(x-3,y+7,x+3,y+7,mid)
 c.ellipse(x,y+2,6,3,ink);c.ellipse(x,y,6,2,ink);c.ellipse(x,y,5,1,light);c.line(x-3,y-1,x+3,y-1,'#d0914b')
# foreground barrel
c.ellipse(6,55,6,7,ink);c.rect(1,49,11,11,ink);c.ellipse(6,54,5,7,mid)
for x in [3,6,9]: c.line(x,50,x,59,wood)
c.ellipse(6,48,6,3,ink);c.ellipse(6,48,5,2,light);c.ellipse(6,48,3,1,wood)
for y in [51,58]:
 c.line(1,y,11,y,'#282a30');c.line(2,y,10,y,'#6c6960');c.set(3,y,'#b3a17a')
c.line(3,61,9,61,ink)
# right barrel behind bar edge
c.rect(59,32,5,13,ink);c.rect(60,33,4,11,mid);c.line(62,33,62,44,wood)
for y in [35,42]: c.line(59,y,63,y,'#818070')
c.line(59,32,63,32,light)
# soft curls of smoke in restrained muted tones
c.path('M 7 30 Q 4 27 8 26 Q 12 24 9 22', '#80675b', fill=False)
c.path('M 39 28 Q 41 26 39 24 Q 37 22 41 21', '#796259', fill=False)
c.set(10,21,'#685248');c.set(42,20,'#685248')
# edge framing
c.rect(0,4,2,39,ink);c.rect(62,4,2,27,ink)
view(result)
finish(result)
