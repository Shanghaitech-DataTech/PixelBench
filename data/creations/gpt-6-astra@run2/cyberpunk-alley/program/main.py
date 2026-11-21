# 128x128 cyberpunk alley
c = new_canvas(128, 128, '#101728', name='Neon Rain')
# palette
night='#101728'; deep='#171d32'; shadow='#20243a'; wall='#30334a'; wall2='#45415a'; concrete='#666076'
black='#090e1b'; blue='#253b59'; cyan='#45e6df'; ice='#a3fff1'; pink='#ff3d9a'; red='#f04468'; orange='#ffab56'; yellow='#ffe78a'; purple='#944bd2'; violet='#55368a'; green='#52d39b'; rain='#6689a8'; puddle='#1c5366'; white='#d7f9ed'
# distant sky and alley depth
c.rect(35, 24, 58, 54, '#18283d')
c.poly([(40,31),(88,31),(78,72),(50,72)], '#213650')
c.rect(48,37,32,28,'#29415a')
c.rect(57,43,14,22,'#344e65')
# distant window glow
c.rect(58,45,12,12,'#f04468'); c.rect(60,47,8,8,'#ffab56'); c.rect(63,47,2,7,'#ffe78a')
# left building mass
c.poly([(0,0),(47,0),(55,29),(51,68),(66,82),(69,128),(0,128)], '#29283c')
c.poly([(0,0),(34,0),(45,26),(45,54),(57,70),(58,128),(0,128)], '#38334a')
# left facade panels
c.rect(0,0,17,68,'#454052'); c.rect(17,0,15,62,'#39374a'); c.rect(32,0,15,47,'#302f44')
c.rect(0,68,54,4,'#201f32'); c.rect(2,7,12,25,'#20283c'); c.rect(5,10,6,18,'#4d3557')
c.rect(20,6,9,20,'#20283c'); c.rect(22,9,5,14,'#67c5c2'); c.rect(35,4,8,19,'#20283c'); c.rect(37,7,4,13,'#f04468')
# left window frames / lit panes
for x,y,w,h,col in [(3,38,12,19,'#224456'),(21,33,10,20,'#60405c'),(36,29,10,15,'#294c5b'),(3,82,13,15,'#a34373'),(22,78,15,19,'#285268')]:
    c.rect(x-2,y-2,w+4,h+4,'#171d30'); c.rect(x,y,w,h,col)
    c.line(x+w//2,y,x+w//2,y+h-1,'#171d30'); c.line(x,y+h//2,x+w-1,y+h//2,'#171d30')
# brick / pipes left
for y in range(4,67,9):
    c.line(0,y,46,y,'#333247')
for x in [16,32]: c.line(x,0,x,65,'#51475a')
c.rect(46,0,3,72,'#777084'); c.rect(49,0,2,72,'#201f32')
c.line(4,70,4,119,'#778096'); c.line(7,70,7,119,'#191e30')
# right building mass
c.poly([(81,0),(128,0),(128,128),(61,128),(63,83),(79,66),(76,30)], '#25293e')
c.poly([(91,0),(128,0),(128,128),(70,128),(70,81),(84,63),(83,27)], '#34354b')
c.rect(84,0,15,55,'#414055'); c.rect(100,0,14,62,'#35374d'); c.rect(115,0,13,70,'#2b3046')
# right windows
for x,y,w,h,col in [(88,8,10,24,'#1b4b5c'),(104,8,11,30,'#662d5b'),(119,12,7,24,'#244f63'),(88,39,12,16,'#634064'),(105,45,11,18,'#1b4955'),(119,44,7,20,'#6b3e5e'),(87,75,14,18,'#27485f')]:
    c.rect(x-2,y-2,w+4,h+4,'#171c2e'); c.rect(x,y,w,h,col)
    c.line(x+w//2,y,x+w//2,y+h-1,'#171d30'); c.line(x,y+h//2,x+w-1,y+h//2,'#171d30')
for y in range(6,69,10): c.line(84,y,128,y,'#4a465b')
c.rect(80,0,3,77,'#7b7184'); c.rect(78,3,2,72,'#1a2032')
# signs and neon shop fascia
c.rect(0,60,39,5,'#151b2c'); c.rect(1,56,37,3,'#a92d75'); c.rect(2,57,35,1,'#ff70ba')
c.rect(6,44,25,12,'#141a2b'); c.rect(7,45,23,10,'#c52f80'); c.rect(8,46,21,1,'#ff88cb')
c.text(9,48,'RAMEN','#fff0c5',font='5x7')
c.rect(82,59,39,7,'#171b30'); c.rect(85,54,33,5,'#147d91'); c.rect(87,55,29,2,'#55fff0')
c.text(89,56,'NIGHT','#dffff7',font='5x7')
c.rect(94,26,26,12,'#161a2c'); c.rect(96,28,22,8,'#a43786'); c.text(99,29,'HOTEL','#fff0ce',font='5x7')
# sign hanger brackets
c.line(8,55,8,62,'#9290a0'); c.line(30,55,30,61,'#9290a0'); c.line(87,53,87,62,'#9290a0'); c.line(116,53,116,63,'#9290a0')
# awning over shop, alternating panels
c.rect(0,65,43,3,'#191e30')
for x in range(2,43,8):
    c.poly([(x,68),(x+7,68),(x+5,73),(x+1,73)], pink if x%16 else '#44dce0')
# shop door left
c.rect(9,74,23,37,'#111a2a'); c.rect(11,76,19,31,'#205060'); c.rect(13,78,15,27,'#2f7280'); c.rect(14,79,13,21,'#1b2b40')
c.rect(13,79,4,20,'#f4a45c'); c.rect(18,79,8,20,'#337f91'); c.rect(27,93,1,3,'#fff4c0')
c.rect(8,106,27,3,'#111827')
# right vending machine two units
c.rect(99,70,22,43,'#101827'); c.rect(101,72,18,39,'#384052'); c.rect(103,74,14,23,'#16283b')
# lit drink rows
for i,col in enumerate(['#ff4c92','#4fe1de','#ffbe59','#9658db']):
    x=104+(i%2)*6; y=76+(i//2)*8
    c.rect(x,y,4,6,col); c.rect(x+1,y,2,2,'#fff0c8')
c.rect(103,100,14,7,'#1c2638'); c.rect(105,102,10,2,'#51e6db'); c.rect(115,78,2,17,'#d5e6df'); c.rect(103,109,14,2,'#ff3d9a')
# second vending / utility panel
c.rect(83,84,13,28,'#111a28'); c.rect(85,86,9,16,'#4a3158'); c.rect(86,87,7,12,'#f04f8b'); c.rect(87,88,5,3,'#ffe78a'); c.rect(85,104,9,5,'#25263b')
# utility boxes and pipes
c.rect(38,81,12,22,'#23273a'); c.rect(40,83,8,17,'#4c485b'); c.rect(42,85,4,2,'#ff587e'); c.line(41,90,47,90,'#171b2c'); c.rect(45,95,2,3,'#63e0d4')
c.line(54,72,54,116,'#777688'); c.line(57,72,57,115,'#292c40'); c.rect(51,83,8,3,'#55576a')
# ground plane, perspective cobbles
c.poly([(0,110),(42,92),(63,79),(79,79),(102,94),(128,108),(128,128),(0,128)], '#171f32')
c.poly([(0,116),(49,97),(64,84),(78,84),(101,99),(128,116),(128,128),(0,128)], '#202b40')
# pavement seams converge
for x in [0,18,39,55,64,75,92,111,128]: c.line(64,83,x,128,'#30394c')
for y in [96,104,113,122]: c.line(0,y,128,y,'#303247')
# puddles reflective
c.ellipse(23,117,18,4,'#174554'); c.ellipse(23,116,14,2,'#277b88'); c.line(10,116,18,115,'#61d9d5'); c.line(28,118,37,117,'#e54f91')
c.ellipse(91,119,24,5,'#153e52'); c.ellipse(91,118,18,3,'#216c80'); c.line(77,117,88,116,'#47dfd3'); c.line(96,120,108,119,'#ec4c90'); c.line(112,117,119,117,'#6ec9d0')
c.ellipse(56,106,9,2,'#1a5364'); c.line(49,105,57,104,'#ff5291'); c.line(61,107,66,107,'#72eee1')
# reflections streak down from neon signs
for x,y,w,col in [(10,74,2,'#e84b9c'),(15,74,1,'#ffab56'),(26,74,2,'#42dcd8'),(91,68,2,'#37d9d7'),(98,68,1,'#ff58a1'),(113,69,2,'#38c8d0')]:
    c.rect(x,y,w,random.randint(5,12),col)
# power cables across sky, anchored on facades
c.path('M 0 20 C 24 13 40 30 58 23 S 98 12 128 21', '#080e1b', fill=False)
c.path('M 0 25 C 28 20 48 36 69 28 S 103 17 128 27', '#101322', fill=False)
c.path('M 5 18 C 28 12 43 28 58 22 S 99 11 124 19', '#697080', fill=False)
c.line(19,17,19,23,'#111321'); c.line(100,16,100,21,'#171a2a')
# cables down walls
c.path('M 47 0 C 48 18 45 35 52 50 L 55 70', '#111522', fill=False); c.path('M 48 0 C 49 18 46 35 53 50', '#817888', fill=False)
c.path('M 79 0 C 76 19 81 32 77 46 L 79 61', '#111522', fill=False); c.path('M 80 0 C 77 19 82 32 78 46', '#77758a', fill=False)
# rain slashes, sparse contrasting
for x,y in [(5,4),(13,29),(38,17),(62,8),(74,35),(95,5),(122,32),(7,72),(70,54),(126,82),(37,47),(67,70),(3,101),(116,98),(80,7),(32,111),(124,52),(60,32),(20,66),(73,93)]:
    c.line(x,y,x-2,y+5,'#52718c')
# Person with transparent umbrella, silhouette in foreground at lower center
# umbrella canopy bright-edged transparent aqua shape
c.path('M 48 91 Q 49 81 57 78 Q 65 73 74 78 Q 82 81 84 91 Q 80 89 77 92 Q 74 89 71 92 Q 67 89 64 92 Q 60 89 57 92 Q 53 89 48 91 Z', '#267c91')
c.path('M 48 90 Q 51 81 58 78 Q 66 75 74 78 Q 81 81 84 90', '#a1fff1', fill=False)
c.line(49,90,64,92,'#66e8df'); c.line(64,92,84,90,'#66e8df'); c.line(64,77,64,92,'#d4fff1'); c.line(56,80,64,92,'#75e4e7'); c.line(73,80,64,92,'#75e4e7')
# umbrella hook and head
c.line(64,92,64,96,'#d8fff2'); c.path('M 64 95 Q 68 95 67 98', '#d8fff2', fill=False)
c.circle(64,98,3,'#d8a47b'); c.rect(61,97,7,2,'#d8a47b'); c.rect(62,97,5,1,'#101725')
# coat torso and arms
c.poly([(61,101),(67,101),(70,109),(72,118),(65,120),(56,118),(59,108)], '#121a29')
c.poly([(61,102),(64,104),(67,102),(69,110),(67,117),(61,117),(58,111)], '#202e43')
c.rect(62,104,4,2,'#ff3d9a'); c.line(64,104,64,116,'#57627a')
c.poly([(59,105),(57,108),(54,113),(56,115),(61,110)], '#151d2b'); c.poly([(68,105),(71,108),(73,113),(71,115),(67,110)], '#151d2b')
c.rect(54,113,3,3,'#d8a47b'); c.rect(71,113,3,3,'#d8a47b')
# legs and boots
c.poly([(60,117),(64,117),(63,124),(60,126),(57,125)], '#101522'); c.poly([(65,117),(69,117),(70,124),(74,126),(72,128),(64,127)], '#101522')
c.rect(57,124,6,3,'#080d18'); c.rect(69,125,6,3,'#080d18'); c.line(60,119,61,123,'#4d6075'); c.line(67,119,68,123,'#4d6075')
# foreground rain-lit edge accents
c.line(47,92,45,96,'#7ee8e6'); c.line(83,92,85,97,'#ff6aaa')
# subtle foreground debris
c.rect(5,125,9,1,'#667384'); c.rect(39,122,4,1,'#7e7c8c'); c.line(110,126,119,125,'#637b8a')
# Reduce to an 80-colour palette while preserving the important neon accents.
from collections import Counter
w, h, rgba = c.to_rgba()
pixels = [tuple(rgba[i:i+4]) for i in range(0, len(rgba), 4)]
counts = Counter(pixels)
pinned_hex = [cyan, ice, pink, red, orange, yellow, purple, violet, green, white, rain, puddle, night, black, '#267c91', '#a1fff1', '#d8a47b']
def rgba_of(hx):
    v = hx.lstrip('#')
    return tuple(int(v[i:i+2], 16) for i in (0, 2, 4)) + (255,)
chosen = [rgba_of(v) for v in pinned_hex if rgba_of(v) in counts]
for col, _ in counts.most_common():
    if col not in chosen and len(chosen) < 80:
        chosen.append(col)
def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2 + 2*(a[3]-b[3])**2
result = new_canvas(128, 128, name='Neon Rain')
for i, col in enumerate(pixels):
    if col[3] == 0:
        continue
    target = col if col in chosen else min(chosen, key=lambda p: dist(col, p))
    result.set(i % w, i // w, target)
view(result)
finish(result)
