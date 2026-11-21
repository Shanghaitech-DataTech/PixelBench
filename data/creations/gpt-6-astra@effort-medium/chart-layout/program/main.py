result = new_canvas(128,64,'#141d30',name='fruit_chart')
c=result
# Quiet chart panel and shared scale: five pixels per fruit count.
c.rect(20,4,104,56,'#1b2840')
for x in (24,49,74,99):
    c.line(x,5,x,57,'#2b3950')
c.line(24,5,24,57,'#718099')
rows=[(10,10,'#ec5964','#ff9293'),(21,5,'#e9bc45','#ffe286'),(32,7,'#ed893d','#ffba65'),(43,14,'#e0d94e','#fcf59b'),(54,2,'#9570d5','#c3a2f0')]
for y,v,col,hi in rows:
    c.rect(25,y-3,v*5,7,col)
    c.line(25,y-3,24+v*5,y-3,hi)
    c.text(28+v*5,y-3,str(v),'#edf1ef')
# Small unobtrusive numeric scale.
digits={'0':['111','101','101','101','111'],'1':['010','110','010','010','111'],'5':['111','100','111','001','111']}
for x,s in [(23,'0'),(48,'5'),(71,'10'),(96,'15')]:
    for i,ch in enumerate(s):
        for yy,row in enumerate(digits[ch]):
            for xx,p in enumerate(row):
                if p=='1': c.set(x+i*4+xx,59+yy,'#8d9ab0')
# Apple: cleft, stem, leaf and a highlight.
c.line(11,5,12,3,'#ad8061')
c.line(13,4,16,3,'#76ba76')
c.poly([(6,7),(8,6),(11,7),(14,6),(16,8),(16,11),(14,14),(11,15),(8,14),(6,11)],'#ec5964')
c.line(8,8,8,10,'#ffadb0')
c.line(13,13,15,11,'#b63853')
# Banana crescent.
c.poly([(6,18),(8,19),(8,23),(10,25),(13,25),(16,23),(17,20),(17,24),(15,27),(11,28),(7,26),(5,23),(5,20)],'#e9bc45')
c.line(7,22,9,25,'#ffe286')
c.line(9,26,13,26,'#ffe286')
c.set(6,18,'#a57e50');c.set(17,20,'#a57e50')
# Orange.
c.circle(11,33,5,'#ed893d')
c.line(10,28,11,27,'#a57e50')
c.line(12,28,15,27,'#76ba76')
c.line(8,30,7,32,'#ffcf83')
c.set(14,35,'#bf6036');c.set(12,37,'#bf6036')
# Lemon with pointed ends.
c.poly([(4,43),(7,40),(12,39),(16,41),(18,43),(15,46),(10,47),(6,46)],'#e0d94e')
c.line(8,41,12,40,'#fcf59b')
c.line(7,42,7,43,'#fcf59b')
c.line(11,46,14,45,'#b5ad3b')
# Grapes: separate shaded berries and leaf.
c.line(11,51,12,49,'#ad8061')
c.poly([(12,50),(15,48),(17,49),(15,51)],'#76ba76')
for x,y in [(8,53),(13,53),(10,56),(14,56),(12,59)]:
    c.circle(x,y,2,'#68469d')
    c.circle(x,y-1,1,'#9570d5')
    c.set(x,y-2,'#c3a2f0')
view(c)
finish(result)
