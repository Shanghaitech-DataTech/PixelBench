# Source colours and the original logical pixel grid.
chars='.abcdefghijklmnopqrstuvw'
small=new_canvas(28,50,name='source_grid')
for y in range(50):
 for x in range(28): small.set(x,y,input_canvas.get(int((x+.5)*66/28),int((y+.5)*119/50)))
colors={ch:i for i,ch in enumerate(chars)}
def grid(rows,name):
 c=new_canvas(28,50,name=name)
 for y,row in enumerate(rows):
  assert len(row)<=28,(y,len(row),row)
  for x,ch in enumerate(row): c.set(x,y,colors[ch])
 return c
def patch(c,rows,y0):
 for y,row in enumerate(rows,y0):
  assert len(row)<=28,(y,len(row),row)
  c.rect(0,y,28,1,None)
  for x,ch in enumerate(row): c.set(x,y,colors[ch])
# A turn toward the character's left: the face projects to image right.
head=[
'.......aaaaa...aaaa.........',
'......abcabbaaaabacba.......',
'.....abcabccccbccbacba......',
'....aacdaccddccddcadcaa.....',
'...abadedbccddcdcbdedaba....',
'...acaddedcdddddcddeddaca...',
'..abdbcefeddcccdddefecbda...',
'..acdeccbddcabbacdbccedca...',
'..bdcfdaedeabccbadeadfcda...',
'..cdbdacfeeaaaaaaeefcadca...',
'..cfacafccfaagggggafccfca...',
'...dfaadabcagggggggcbadfa...',
'...bdcaabaaaagggggggaacda...',
'....cdagaaccgggggggghadca...',
'....iaaachhghggggggghccaa...',
'....iggahaajhgggggggghaa...',
'.....igaaaakiighgggkiiga...',
'.....ihjhhlimlggggglmilhi...',
'......iijgnnlgggggglnngji...',
'........ihgggggggggggggi...',
'........ijohgggggggghoji...',
'......ppppjjohgggghojja....',
'.....pqqqqqpjjjjjjjjpa.....',
]
left=grid(head,'left_grid')
body=[
'....pqrrsqsqphooooohap......',
'...ptrsrsqsqqthoohtqqtp.....',
'...pqsqssqsssqthhtssqtp.....',
'....pqsstqsssstggtssqpa.....',
'...ijpppqqsrsssttsssapa.....',
'...iohopqqsrrssssssqppai....',
'...ighjppqqssssssssqpphgi...',
'..iouojipptttqssqtttpjouoi..',
'..iuujivipqtqssssqtppijuui..',
'.iougojwvptqtsssstqtpjoguoi.',
'.iguggowptpqtqssqtqpoggugi..',
'.igggjvpttpptqqqqtppgjgggi..',
'.ijggjpttqpqptqqtpqpjggji...',
'..ioghptqpqqtqqqqtqphgoi...',
'...iiptqtqstqssssqtsqpii....',
]
patch(left,body,23)
# Keep the original full, pleated skirt with perspective compression.
for y in range(38,50):
 for x in range(28):
  sx=round((x-14)/.89+13.5)
  if 0<=sx<28: left.set(x,y,small.get(sx,y))
# Far braid glimpsed beyond the shoulder.
braidfar=[
'aa','bca','cda','afca','dbaba','cdbca','adcaa','cdbaa','abca','aaa'
]
for j,row in enumerate(braidfar):
 for k,ch in enumerate(row): left.set(23+k if 23+k<28 else 27,21+j,colors[ch])
# Opposite turn; retain anatomical placement of the shoulder braid.
right=left.copy(name='right_grid').mirror('h')
# Remove mirrored far braid, restoring the far arm/shoulder silhouette.
for y in range(21,31):
 for x in range(0,5): right.set(x,y,None)
# Source braid comes forward on the near shoulder in this turn.
braid=[
'...abca','..abbd a'.replace(' ',''),'..accfcaa','..acdbabafa',
'..aefdababca','..afdabcdaba','..aacdadfaa','..afeedabap',
'..adcaacdaja','...adbaaaaai','....acapjhg','.....aapijou','.......a',
]
for j,row in enumerate(braid):
 for k,ch in enumerate(row):
  if ch!='.': right.set(16+k,19+j,colors[ch])
# Rear curls, broad back of the head, and plain back neckline.
backhead=[
'.......aaaaa....aaaaa.......',
'......abcabbaaaabbacba......',
'.....abcabccccbcccbacba.....',
'....aacdaccddccddccadcaa....',
'...abadedbccddcdccbdedaba...',
'...acaddedcddddddcdeddaca...',
'..abdbcefeddccccddefecbdba..',
'..acdeccbddcabbacddbccedca..',
'.abdcfdaedeabccbaedeadfcdba.',
'.acdbdacfeedcddcdeefcadbdca.',
'..cfacafccfeddcddefccfacafca',
'..adfaadabcddddddcbadaafda..',
'..abdcaabccdeffedccbaacdba..',
'...acdacddedefeddddcadca...',
'...aaaacdebcccccbedcaaaa...',
'...ibcddcdabccbadcddcbai...',
'....acdefdceffecdfedcai....',
'....iacdcabcddcbacdcai.....',
'.....iaabddcbbcddbaai......',
'......aacfedddefcaa........',
'......acdaacccaadca........',
'.....pacdbafedfabcapp......',
'....pqaedcadbcadceaqp......',
]
back=grid(backhead,'rear_grid')
backbody=[
'...pqqaaecdabceedaaqqp.....',
'..ptqssacadcbcdacaqsqtp....',
'..pqsqssaacddcaassssqsp....',
'...pqsstqaaccaaqssstqp.....',
'..ijpppqsaaddassqqpppji....',
'..iohopqqsaacassqqpphohi...',
'..ighjppqqsassssqqppjhgi...',
'.iouojipptttqqqqtttppijouoi.',
'.iuujivipqtqqqqqqtqpivijuui.',
'iougojwvptqtqqqqtqtpvwjoguoi',
'iguggowptpqtqqqqtqptpwoggugi',
'igggjvpttpptqqqqtppttpgjgggi',
'ijggjpttqpqptqqtpqpqttpjggji',
'.ioghptqpqqtqqqqtqqpqtphgoi.',
'..iiptqtqstqssssqtsqtqtpii..',
]
patch(back,backbody,23)
for y in range(38,50):
 for x in range(28): back.set(x,y,small.get(x,y))
# Back neckline and the braid falling over the character's left shoulder.
patch(back,[
'......aacfedddefcaa........',
'......acdaacccaadca........',
'.....pacdbaggggabcappp.....',
'....pqaedcahhhhaqqqqqp....',
'...pqqacfdaaqqaassssqqp...',
'..ptqsaedcaaqsssssssqqtp..',
'..pqsacfdaaqssssssssqsp...',
'...pqadcbaqsssssssstqp....',
'..ijpacfdaqsqqqqqqpppji...',
'..iohacdbasqqqqqqqpphohi..',
'..ighjaaaassssssqqppjhgi..',
],19)
# Reinstate the receding sleeve in the second turn.
for x,y,ch in [(4,23,'p'),(4,24,'q'),(3,25,'p'),(4,25,'s'),(4,26,'p'),(4,27,'j'),(4,28,'h'),(3,29,'i'),(4,29,'g')]:
 right.set(x,y,colors[ch])
# Fill the receding shoulder cap, keeping its silver sleeve continuous.
for y,row in [(23,'pqs'),(24,'pqs'),(25,'pqs'),(26,'pqq')]:
 for j,ch in enumerate(row): right.set(3+j,y,colors[ch])
# Hair overlaps the upper edge of the back collar.
back.set(15,21,colors['a'])
back.set(16,21,colors['c'])
back.set(15,22,colors['h'])
# The far eye narrows as it wraps away from the viewer.
for c,x in [(left,23),(right,4)]:
 for y in (16,17,18):
  c.set(x,y,colors['g'])
# Export at the source dimensions, retaining its original large pixel cadence.
def upscale(c,name):
 out=new_canvas(66,119,name=name)
 for y in range(119):
  for x in range(66): out.set(x,y,c.get(int(x*28/66),int(y*50/119)))
 return out
f1=upscale(left,'frame_1_left_45')
f2=upscale(right,'frame_2_right_45')
f3=upscale(back,'frame_3_rear')
view(f1,scale=4)
view(f2,scale=4)
view(f3,scale=4)
finish([f1,f2,f3])
