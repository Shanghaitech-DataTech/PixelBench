result = new_canvas(64, 64, '#101c30', name='subway_platform')
c = result
# cool station shell and receding soffit
c.rect(0,0,64,5,'#1c2c43')
c.line(0,5,63,10,'#354960')
c.poly([(0,6),(64,11),(64,16),(0,12)],'#263c52')
c.line(0,8,26,10,'#819d9e')
c.line(0,9,25,11,'#dce6c5')
c.rect(0,13,64,28,'#142538')
c.rect(57,15,7,23,'#0b1426')
# overhead unbranded station signs
c.line(7,2,7,6,'#69818b')
c.rect(2,6,19,8,'#0c2435')
c.rect(2,6,2,8,'#eab96b')
c.text(6,7,'02','#e8d9ab')
c.line(45,4,45,7,'#69818b')
c.rect(30,7,31,9,'#0b2533')
c.text(32,8,'EAST','#d4e2cc',spacing=0)
c.line(55,11,59,11,'#eab96b')
c.set(57,9,'#eab96b'); c.set(58,10,'#eab96b'); c.set(58,12,'#eab96b'); c.set(57,13,'#eab96b')
# arriving train: long bands, lit windows and rounded leading cab
c.poly([(0,17),(46,17),(51,18),(55,22),(57,29),(57,35),(0,35)],'#819eaa')
c.line(0,17,45,17,'#cadbd5')
c.poly([(0,20),(46,20),(50,21),(53,25),(54,28),(0,28)],'#233c53')
for x in [-5,10,25]:
    c.rect(max(0,x),21, max(1,11+min(0,x)),6,'#d6d9aa')
    c.line(max(0,x),21,x+10,21,'#f3e7ba')
    c.line(max(0,x),26,x+10,26,'#8aa89f')
c.poly([(41,21),(47,21),(50,23),(52,27),(41,27)],'#72b8c5')
c.line(43,22,48,22,'#b5e2dd')
c.line(47,24,50,26,'#a6d6d5')
c.rect(0,29,55,3,'#d17c4d')
c.line(0,29,52,29,'#edba70')
c.line(0,34,56,34,'#455e72')
c.rect(52,30,3,2,'#fff0bb')
c.rect(1,19,17,1,'#4e7185')
c.rect(0,23,8,1,'#f4ebc9')
c.rect(16,24,10,1,'#a5c4ba')
c.rect(0,31,22,1,'#efb172')
c.rect(0,36,64,5,'#0c192a')
c.line(0,38,63,38,'#476070')
# platform and perspective tile seams
c.poly([(0,41),(64,39),(64,64),(0,64)],'#425969')
c.poly([(0,42),(64,40),(64,43),(0,46)],'#d3ad63')
c.line(0,46,63,43,'#233d50')
c.line(0,55,63,49,'#354b5c')
c.line(0,63,63,56,'#354b5c')
for x in [4,23,43,61]:
    c.line(x,46,x-3 if x>3 else 0,63,'#354b5c')
for x in range(1,64,4):
    y=44 if x<31 else 43
    c.set(x,y,'#8c784c')
# glass platform screen doors, frames and subdued reflections
c.line(0,27,63,27,'#8aa9af')
c.line(0,28,63,28,'#2c5265')
c.line(0,40,63,39,'#9cb7b5')
for x in [3,19,35,51,62]:
    c.rect(x,27,2,14,'#213b50')
    c.line(x,27,x,40,'#789aa7')
    c.set(x,26,'#d8b869')
for x in [11,27,43,58]:
    c.line(x,29,x,39,'#527c8e')
    c.rect(x-1,33,2,3,'#172f42')
for x in [6,22,38,54]:
    c.line(x,30,x+3,30,'#85afb6')
    c.line(x,31,x+2,31,'#527c8e')
# foreground contact shadows
c.ellipse(11,54,7,2,'#2b4052')
c.ellipse(31,54,11,2,'#2b4052')
c.ellipse(50,55,9,2,'#2b4052')
# platform bench
c.rect(23,43,17,3,'#a77f62')
c.line(24,43,39,43,'#d1ac81')
c.rect(23,47,18,2,'#c29b75')
c.line(23,49,40,49,'#192d40')
c.rect(25,50,2,4,'#1b2f42'); c.rect(38,50,2,4,'#1b2f42')
c.rect(22,45,2,4,'#78929a'); c.rect(40,45,2,4,'#78929a')
# passenger one: standing with travel bag, warm long coat
c.rect(9,31,5,5,'#172335')
c.rect(10,33,4,4,'#d7a27c')
c.set(13,34,'#ebc49a')
c.rect(10,37,3,2,'#dfc592')
c.poly([(8,38),(13,38),(15,44),(14,48),(7,48),(7,41)],'#b66c4b')
c.line(8,39,8,45,'#e8a465')
c.line(13,40,14,44,'#824c41')
c.rect(9,48,2,5,'#15283b'); c.rect(12,48,2,5,'#1c3043')
c.rect(8,53,3,2,'#101d30'); c.rect(12,53,4,2,'#101d30')
c.rect(5,44,4,6,'#172d40'); c.line(6,44,7,43,'#b6a58a'); c.set(7,43,'#d7a27c')
c.line(5,45,5,48,'#5e7a87')
# passenger two: seated, leaning forward over book
c.rect(28,35,5,3,'#121e30')
c.rect(29,37,4,3,'#bd876c')
c.set(33,38,'#d9a582')
c.poly([(28,40),(32,40),(34,44),(36,45),(35,47),(28,46),(27,43)],'#6c9b98')
c.line(28,41,28,44,'#a7c2ac')
c.line(31,42,34,44,'#426e78')
c.rect(34,43,4,2,'#e4d7b0'); c.set(35,44,'#bd876c')
c.poly([(29,47),(35,47),(36,49),(34,53),(32,53),(33,49),(29,49)],'#192c41')
c.rect(28,48,2,5,'#263b50')
c.rect(27,53,4,2,'#111f30'); c.rect(32,53,5,2,'#111f30')
# passenger three: walking to the right, bent arm with phone
c.rect(47,31,5,3,'#101d30')
c.rect(48,33,4,4,'#d7aa86'); c.set(52,34,'#d7aa86')
c.rect(48,37,3,2,'#eee0b9')
c.poly([(47,38),(51,38),(53,43),(51,47),(46,47),(45,42)],'#5681ae')
c.line(47,39,47,44,'#85aec7')
c.poly([(45,39),(47,40),(47,45),(44,46),(43,44),(43,41)],'#172b40')
c.line(44,41,44,44,'#386071')
c.line(51,40,54,42,'#85aec7'); c.line(54,42,56,39,'#d7aa86')
c.rect(55,37,2,3,'#112034'); c.set(55,37,'#99d9d3')
c.poly([(47,47),(50,47),(49,50),(46,54),(44,54),(46,50)],'#15263b')
c.poly([(50,47),(52,47),(53,51),(56,54),(54,55),(50,51)],'#20374e')
c.rect(43,54,4,2,'#0d1c2d'); c.rect(54,54,4,2,'#0d1c2d')
# small foreground highlights
c.line(2,59,12,58,'#526b79')
c.line(38,60,46,59,'#526b79')
# Consolidate close shades into a compact final palette.
merge = {'#ebc49a':'#d7aa86', '#dfc592':'#eee0b9', '#d9a582':'#d7aa86', '#b6a58a':'#d3ad63', '#f4ebc9':'#f3e7ba', '#a6d6d5':'#b5e2dd', '#efb172':'#edba70', '#e8d9ab':'#e4d7b0'}
indices = {c.color(a): c.color(b) for a,b in merge.items()}
for y in range(64):
    for x in range(64):
        idx = c.get(x,y)
        if idx in indices:
            c.set(x,y,indices[idx])
view(result)
save('subway_platform',result)
finish(result)
