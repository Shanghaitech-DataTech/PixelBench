from pixelbench_api import *

# 64x64 pixel-art scene: offshore wind maintenance platform
c = new_canvas(64, 64, background="#0b1b32", name="offshore_wind_maintenance")

# Palette
sky0="#102744"; sky1="#1b3b5d"; sky2="#285579"; sky3="#407494"; sky4="#76a2ae"; haze="#aac1b9"
ocean0="#0b2943"; ocean1="#10415a"; ocean2="#17647a"; foam="#8fc5c1"
ink="#081522"; deep="#102536"; steel="#344b55"; steel2="#61767a"; steel_hi="#9aada6"
yellow="#f2c34f"; orange="#d8793b"; red="#ad4b3c"; skin="#d79a70"; helmet="#f4cf58"
white="#d6e3d5"; pale="#b9d0c9"; window="#79bbc0"; rust="#8e5a43"; cable="#1d3037"

# Sky: broad horizontal pixel bands
c.rect(0,0,64,9,sky0)
c.rect(0,9,64,8,sky1)
c.rect(0,17,64,8,sky2)
c.rect(0,25,64,8,sky3)
c.rect(0,33,64,7,sky4)
c.rect(0,40,64,4,haze)
# sparse cloud streaks
c.rect(2,13,12,2,"#315776"); c.rect(5,12,7,1,"#3d6680")
c.rect(49,8,11,2,"#244b6a"); c.rect(52,7,6,1,"#315776")
c.rect(17,29,9,2,"#6f9a9d"); c.rect(20,28,5,1,"#82a9a5")

# Far ocean bands and horizon
c.rect(0,44,64,20,ocean0)
c.rect(0,47,64,4,ocean1)
c.rect(0,54,64,10,ocean0)
c.line(0,44,63,44,"#294f62")
# distant wave pixels
for x,y,w in [(1,48,8),(13,46,7),(24,49,10),(39,46,8),(52,49,10),(4,57,11),(19,55,7),(31,59,12),(48,56,8),(57,61,7)]:
    c.rect(x,y,w,1,ocean2)
for x,y,w in [(0,52,5),(9,50,6),(17,53,5),(27,51,8),(42,52,7),(54,51,5),(5,60,7),(23,62,6),(39,57,6),(52,60,10)]:
    c.rect(x,y,w,1,foam)
# small broken highlights
for x,y in [(3,53),(12,52),(22,48),(34,53),(46,48),(61,54),(15,59),(28,60),(45,62)]: c.rect(x,y,2,1,"#4c8a93")

# Distant turbines, softened silhouettes
# left turbine tower
c.poly([(12,28),(14,28),(15,42),(11,42)],"#466b76")
c.rect(10,41,6,1,"#527983")
c.circle(13,26,1,"#b1c6b7")
c.line(13,26,13,19,"#b1c6b7"); c.line(13,26,7,23,"#b1c6b7"); c.line(13,26,18,30,"#b1c6b7")
# mid distant turbine
c.poly([(23,23),(25,23),(27,41),(21,41)],"#52727a")
c.circle(24,21,1,"#c0d0c2")
c.line(24,21,24,13,"#c0d0c2"); c.line(24,21,18,18,"#c0d0c2"); c.line(24,21,29,27,"#c0d0c2")
# tiny far turbine at right horizon
c.poly([(58,34),(59,34),(60,43),(57,43)],"#62848a")
c.circle(58,32,1,"#cfdbca"); c.line(58,32,58,27,"#cfdbca"); c.line(58,32,54,30,"#cfdbca"); c.line(58,32,61,35,"#cfdbca")

# Main turbine tower behind platform, dark outline and lit face
c.poly([(43,19),(48,19),(51,40),(40,40)],ink)
c.poly([(44,20),(47,20),(49,39),(42,39)],steel2)
c.poly([(45,21),(47,21),(48,39),(46,39)],steel_hi)
# tower shadow bands
c.rect(43,29,5,1,steel); c.rect(42,35,7,1,steel)
# nacelle and hub
c.rect(42,14,9,5,ink)
c.rect(43,13,7,4,steel2)
c.rect(45,13,5,2,steel_hi)
c.rect(50,15,3,2,ink)
c.rect(44,16,5,1,window)
c.rect(42,16,2,2,steel)
c.circle(43,17,2,ink); c.circle(43,17,1,steel_hi)
# main turbine blades, outlined then inner highlights
c.line(43,16,43,3,ink); c.line(43,16,34,10,ink); c.line(43,16,54,25,ink)
c.line(43,16,43,4,white); c.line(42,5,43,3,pale)
c.line(42,15,35,10,pale); c.line(36,10,33,9,white)
c.line(44,17,53,24,pale); c.line(52,24,55,26,white)
# blade tip pixels
c.rect(42,2,2,2,white); c.rect(32,8,3,2,white); c.rect(54,25,3,2,white)

# Platform upper deck, rear rail and maintenance cabin
# rear railing
c.line(27,34,60,34,ink); c.line(27,35,60,35,steel2)
for x in [28,34,40,47,54,59]: c.line(x,34,x,39,steel)
c.rect(27,38,34,4,ink)
c.rect(28,38,32,2,steel_hi)
c.rect(29,40,30,2,steel)
c.rect(31,39,11,1,"#b2b9a3")
# cabin/tool shed on deck
c.rect(49,28,9,10,ink); c.rect(50,29,7,9,steel)
c.rect(51,30,5,3,window); c.rect(52,30,4,1,"#b8d8cf")
c.rect(50,34,7,3,steel2); c.rect(53,34,1,3,ink)
c.rect(48,27,10,2,ink); c.rect(50,26,6,2,steel2)
# orange safety case and equipment
c.rect(28,35,5,4,ink); c.rect(29,35,3,3,orange); c.rect(29,36,3,1,yellow)
c.rect(58,35,3,3,red); c.rect(59,34,1,1,yellow)

# Structural legs and cross bracing, foreground
# four main legs
c.line(30,41,26,62,ink); c.line(32,41,29,62,ink)
c.line(55,41,59,62,ink); c.line(57,41,62,62,ink)
c.line(31,42,28,62,steel2); c.line(56,42,60,62,steel2)
# lower beams
c.line(25,61,63,61,ink); c.line(26,59,61,59,steel)
# diagonal lattice
for seg in [(31,43,55,59),(55,43,31,59),(30,47,58,55),(57,47,28,55)]: c.line(*seg,ink)
for seg in [(32,44,53,58),(53,44,33,58),(31,48,56,54),(56,48,30,54)]: c.line(*seg,steel2)
# foreground braces highlights
c.line(27,61,31,43,steel_hi); c.line(60,61,56,43,steel_hi)
# footings and splash shadows
c.rect(23,61,9,2,ink); c.rect(57,61,7,2,ink)
c.rect(22,63,12,1,ocean2); c.rect(56,63,8,1,ocean2)

# Access ladder at front, clearly separate from bracing
c.rect(35,35,4,27,ink)
c.rect(36,36,1,25,steel_hi); c.rect(38,36,1,25,steel)
for y in range(38,61,4): c.rect(35,y,5,1,ink); c.rect(36,y,3,1,steel_hi)
# ladder cage hoops
for y in [42,50,58]: c.line(34,y,40,y,steel)

# Technician climbing ladder: boots, legs, torso, arms, helmet
# back leg and boot
c.rect(35,34,2,6,ink); c.rect(36,34,2,5,orange); c.rect(35,39,3,2,ink)
# front leg bent toward rung
c.line(38,34,40,38,ink); c.line(38,34,40,38,orange); c.rect(39,38,3,2,ink)
# body outline and orange hi-vis vest
c.rect(33,27,7,9,ink); c.rect(34,28,5,7,orange); c.rect(35,28,3,6,yellow)
# vest reflective bands
c.rect(34,30,5,1,white); c.rect(35,33,4,1,white)
# harness and belt
c.line(34,28,39,34,red); c.line(39,28,35,34,red); c.rect(34,34,6,1,ink)
# arms reaching ladder
c.line(34,29,31,33,ink); c.line(34,29,32,33,skin); c.rect(30,32,3,2,ink); c.rect(31,32,2,1,skin)
c.line(39,29,41,33,ink); c.line(39,29,40,32,skin); c.rect(40,32,2,2,ink); c.rect(40,32,1,1,skin)
# neck and face
c.rect(35,25,4,3,ink); c.rect(36,25,2,3,skin)
c.rect(34,22,7,5,ink); c.rect(35,23,5,4,skin); c.rect(39,24,2,1,ink)
# helmet, chin strap
c.rect(34,21,7,3,ink); c.rect(35,20,5,3,helmet); c.rect(34,22,7,2,helmet); c.rect(34,23,3,1,ink); c.rect(39,24,2,1,ink)
c.rect(36,24,1,1,"#f1b078")
# safety lanyard from harness to rail
c.line(39,29,43,35,cable); c.rect(42,34,2,2,yellow)

# foreground wave occlusion adds depth at feet
c.rect(0,63,20,1,ocean1); c.rect(34,63,18,1,ocean1)
c.rect(3,62,8,1,foam); c.rect(46,62,9,1,foam)

# crisp small glints and bolts
for x,y in [(29,41),(42,41),(55,41),(31,46),(56,46),(28,53),(59,53)]: c.set(x,y,"#c1c7b2")

view(c, size=512, margin=0)
finish(c)
