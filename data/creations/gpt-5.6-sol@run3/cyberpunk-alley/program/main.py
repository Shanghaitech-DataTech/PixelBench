from pixelbench_api import *

c = new_canvas(128, 128, background="#070914", name="cyberpunk_alley")

# Palette
sky = "#0a0d1b"; deep = "#050711"; wall = "#111426"; wall2 = "#18182c"
edge = "#252642"; ink = "#03050b"; steel = "#30334b"; mist = "#39405a"
cyan = "#16f2e8"; cyan2 = "#087f91"; blue = "#2370ff"; pink = "#ff2da6"
magenta = "#9b176f"; violet = "#5b2b99"; red = "#ff405c"; orange = "#ff9d36"
yellow = "#ffe66b"; white = "#dffcff"; rain = "#77a9c4"; skin = "#b97a8b"

# Distant alley and converging architecture
c.poly([(0,0),(46,0),(53,73),(36,91),(0,102)], wall, True)
c.poly([(128,0),(83,0),(74,72),(92,91),(128,103)], "#101224", True)
c.poly([(45,0),(84,0),(75,73),(53,73)], sky, True)
c.rect(54,8,21,64,"#0b1020")
c.rect(58,16,14,55,"#10172a")
c.rect(61,24,8,45,"#172038")
# distant lit doorway
c.rect(61,47,8,24,cyan2)
c.rect(63,49,4,22,"#5cd6cd")
c.rect(64,52,3,19,"#d9fbcd")

# Left building panels, pipes and masonry
c.rect(0,8,35,3,deep); c.rect(0,35,43,3,deep); c.rect(0,67,48,4,deep)
c.line(41,0,46,70,steel); c.line(36,0,43,69,ink)
for y in (15,22,29,44,51,58):
    c.line(0,y,38+(y//18),y,edge)
c.rect(3,40,4,27,"#25273d"); c.rect(4,40,1,27,mist)
c.rect(8,48,2,20,ink); c.rect(10,48,1,19,cyan2)
# upper left window
c.rect(4,13,24,18,ink); c.rect(6,15,20,14,"#1e2940")
c.rect(7,16,8,5,blue); c.rect(17,16,8,5,violet)
c.rect(7,23,18,5,"#14233c"); c.line(16,15,16,29,ink)

# Left projecting neon sign
c.rect(1,33,31,31,ink)
c.rect(3,35,27,27,magenta)
c.rect(5,37,23,23,"#241126")
c.rect(7,39,19,19,"#541344")
c.text(9,41,"夜",pink,font="12px")
c.text(8,52,"BAR",white,font="5x7",spacing=0)
c.rect(30,39,4,3,steel); c.rect(30,56,6,3,steel)
# neon edge highlights
c.line(3,35,29,35,pink); c.line(3,35,3,61,pink)

# Left shop awning and doorway
c.poly([(0,72),(46,72),(42,79),(0,79)], ink)
for x in range(0,46,8):
    c.poly([(x,72),(min(x+5,46),72),(min(x+2,43),78),(max(x-3,0),78)], red if (x//8)%2==0 else white)
c.rect(0,79,40,31,"#101321")
c.rect(3,81,22,26,"#171927"); c.rect(5,83,18,22,"#242238")
c.rect(7,86,14,2,pink); c.rect(7,92,11,1,cyan2); c.rect(7,98,15,1,orange)
c.rect(27,82,10,28,ink); c.rect(29,84,6,26,"#2c2637")
c.set(33,96,yellow)

# Right wall structure
c.line(87,0,79,73,steel); c.line(93,0,84,73,ink)
c.rect(92,7,36,4,deep); c.rect(86,39,42,4,deep); c.rect(81,69,47,4,deep)
for y in (17,27,50,59):
    c.line(90-(y//18),y,127,y,edge)
# right upper windows
c.rect(100,14,26,18,ink); c.rect(102,16,22,14,"#13182b")
c.rect(103,17,9,5,"#233052"); c.rect(114,17,9,5,blue)
c.rect(103,24,20,4,"#1c2440")
# vertical cyan sign
c.rect(89,25,13,39,ink); c.rect(91,27,9,35,cyan2); c.rect(93,29,5,31,"#052e3a")
c.text(91,29,"雨",cyan,font="8px")
c.text(91,41,"街",cyan,font="8px")
c.text(91,53,"店",cyan,font="8px")
c.rect(87,29,3,3,steel); c.rect(86,58,4,3,steel)
# small orange sign
c.rect(105,45,23,13,ink); c.rect(107,47,21,9,orange)
c.text(109,48,"OPEN",deep,font="5x7",spacing=0)

# Right shop facade
c.rect(83,73,45,38,"#0b0c16")
c.rect(86,76,42,4,violet)
c.rect(88,81,18,28,"#22243a"); c.rect(90,83,14,24,"#303149")
c.rect(92,85,10,6,"#2a6780"); c.rect(92,94,10,10,"#171f34")
c.line(88,92,105,92,ink)
# Vending machines
c.rect(108,74,17,37,ink); c.rect(110,76,13,34,"#24304c")
c.rect(112,78,9,9,cyan2); c.rect(113,79,7,7,"#b9ffff")
c.rect(112,89,9,12,"#15182a")
for yy,col in [(90,pink),(94,orange),(98,cyan)]:
    c.rect(113,yy,2,2,col); c.rect(117,yy,3,2,"#56647b")
c.rect(113,104,7,3,steel); c.rect(111,108,11,2,deep)

# Power boxes and cables
c.rect(70,16,8,10,steel); c.rect(72,18,4,6,"#171a2b"); c.set(73,20,red)
c.path("M 0 18 C 25 15, 42 23, 69 19 C 90 15, 105 5, 128 8", ink, fill=False)
c.path("M 0 21 C 26 18, 46 30, 73 23 C 97 17, 107 16, 128 20", steel, fill=False)
c.path("M 32 0 C 40 22, 59 29, 78 31 C 96 33, 109 25, 128 28", ink, fill=False)
c.path("M 76 25 C 83 45, 77 57, 81 72", steel, fill=False)
# cable ties and hanging wire
for x,y in [(18,19),(47,24),(72,23),(103,17)]: c.rect(x,y,1,3,mist)
c.path("M 116 20 C 115 35, 121 37, 120 47", ink, fill=False)
c.circle(120,48,1,red)

# Street ground perspective
c.poly([(0,109),(36,88),(53,72),(75,72),(92,90),(128,111),(128,128),(0,128)], "#0a0d17")
c.line(53,73,13,127,"#171a29"); c.line(75,73,114,127,"#171a29")
c.line(43,84,85,84,"#23263a"); c.line(26,101,103,101,"#1b1f31")
# curb edges
c.poly([(0,107),(36,88),(39,91),(4,113),(0,113)], steel)
c.poly([(128,109),(91,89),(88,92),(124,115),(128,115)], "#292d42")

# Reflections and puddles
c.poly([(28,112),(51,103),(89,106),(111,115),(95,122),(45,122)], "#11182b")
c.poly([(37,113),(55,107),(78,109),(70,113),(46,116)], cyan2)
c.poly([(14,119),(42,113),(62,116),(50,121),(21,123)], magenta)
c.poly([(72,117),(98,113),(119,119),(112,124),(83,123)], violet)
c.line(47,117,76,117,cyan); c.line(80,121,111,121,pink)
c.line(20,125,55,125,"#5b245c"); c.line(89,126,124,126,"#204a79")
c.rect(4,116,17,1,"#454c67"); c.rect(101,112,19,1,"#43506a")
# broken neon reflection streaks
for x,y,w,col in [(8,110,8,pink),(23,115,11,red),(54,111,5,cyan),(63,120,8,cyan),(92,116,6,orange),(110,124,8,blue)]:
    c.rect(x,y,w,1,col)

# Person silhouette behind umbrella
# legs
c.poly([(61,103),(66,103),(65,119),(62,127),(58,127),(61,117)], ink)
c.poly([(67,103),(71,104),(74,118),(78,125),(74,127),(69,120)], ink)
c.rect(58,126,7,2,"#15131f"); c.rect(74,126,7,2,"#15131f")
# coat/body and head
c.poly([(61,86),(70,85),(76,103),(71,112),(60,109),(57,102)], ink)
c.poly([(62,90),(69,88),(72,104),(67,108),(60,104)], "#10111d")
c.circle(65,82,4,ink); c.rect(64,84,4,4,ink)
# shoulder rim light
c.line(59,92,57,101,pink); c.line(72,91,75,101,cyan)

# Transparent umbrella canopy: dark translucent impression + bright rim
c.poly([(45,84),(49,78),(56,74),(65,72),(74,74),(81,78),(86,84)], "#13283a")
c.poly([(45,84),(55,81),(65,84),(75,81),(86,84),(80,78),(73,74),(64,72),(55,75),(49,78)], "#1e3850")
c.path("M 44 84 Q 50 74 64 72 Q 78 72 87 84", cyan, fill=False)
c.line(45,84,86,84,cyan2)
c.line(64,73,64,84,"#8fe7ed")
c.line(64,84,67,100,steel)
c.path("M 67 100 Q 68 104 71 102", mist, fill=False)
# canopy panel ribs and highlights
c.line(47,83,64,73,"#5fa4ba"); c.line(64,73,84,83,"#5fa4ba")
c.line(55,81,64,73,"#365f75"); c.line(75,81,64,73,"#365f75")
c.rect(51,77,4,1,white); c.rect(78,79,3,1,cyan)

# Rain streaks, mostly visible against walls
for x,y,l in [(2,2,4),(12,31,3),(20,2,5),(31,12,4),(39,43,5),(48,9,4),(52,35,3),(79,7,5),(86,18,3),(96,2,5),(108,34,4),(121,3,4),(125,63,5),(7,70,4),(47,62,3),(103,63,4),(24,74,3),(115,65,3)]:
    c.line(x,y,x-1,y+l,rain)
# foreground rain splashes
for x,y in [(8,118),(31,109),(49,124),(88,111),(117,117)]:
    c.set(x,y,white); c.set(x-2,y+1,rain); c.set(x+2,y+1,rain)

# Sharp foreground framing and tiny surface details
c.rect(0,103,2,25,deep); c.rect(126,98,2,30,deep)
c.rect(15,104,2,2,yellow); c.rect(119,107,2,2,red)
c.set(54,91,cyan); c.set(82,94,pink)

view(c, scale=4, margin=0)
finish(c)
