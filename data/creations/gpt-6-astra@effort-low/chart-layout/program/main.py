result = new_canvas(128,64, '#141e30', name='fruit_chart')
c=result
# inset panel and faint shared scale
c.rect(2,2,124,60,'#1d2a40')
for x in [20,50,80,110]:
    c.line(x,5,x,58,'#29394e')
c.line(19,5,19,58,'#64758b')
# Six pixels per unit; each bar has an inset lit top edge.
rows=[(8,10,'#eb5261','#ff8690','#ac354c'),(19,5,'#f4cc51','#ffe88b','#b28c35'),(30,7,'#ef913e','#ffc16b','#b96432'),(41,14,'#ece35c','#fff79b','#aca33d'),(52,2,'#a679da','#d2a5f6','#715298')]
for y,value,base,light,shade in rows:
    c.rect(21,y,6*value,7,base)
    c.line(21,y,20+6*value,y,light)
    c.line(21,y+6,20+6*value,y+6,shade)
    c.text(108 if value == 14 else 24+6*value,y,str(value),'#eef1ef')
# apple
c.line(10,5,11,7,'#a17951')
c.line(12,5,14,5,'#83b86b')
c.rect(7,8,8,6,'#b6314b')
c.rect(6,9,10,4,'#e94e60')
c.rect(8,7,3,1,'#f26c75'); c.rect(12,7,2,1,'#f26c75')
c.rect(8,14,6,1,'#b6314b'); c.rect(7,9,2,3,'#ff9a9b')
# banana curved crescent
c.poly([(6,19),(8,20),(8,23),(10,25),(13,25),(16,22),(15,26),(13,28),(9,28),(6,25),(5,22)],'#e6b948')
c.path('M 6 20 L 7 23 L 9 26 L 12 27 L 15 25', '#ffe783',fill=False)
c.set(6,18,'#a57d4d'); c.set(16,21,'#a57d4d')
# orange
c.circle(11,33,5,'#b55e30'); c.circle(11,33,4,'#f3963d')
c.rect(8,31,2,2,'#ffd080');c.set(13,35,'#dd762c')
c.line(11,28,11,29,'#a07b44'); c.line(12,28,14,27,'#74ae63')
# lemon
c.poly([(5,44),(7,41),(11,40),(15,42),(17,44),(15,47),(10,49),(7,47)],'#aca43d')
c.poly([(5,44),(8,42),(12,41),(15,43),(16,44),(14,47),(10,48),(7,46)],'#eee360')
c.line(8,43,12,42,'#fff8ae');c.set(7,44,'#fff8ae')
# grapes
c.line(11,50,12,52,'#a58557');c.line(12,50,15,50,'#83b86b')
for x,y in [(8,53),(12,53),(15,54),(9,56),(13,57),(11,60)]:
    c.circle(x,y,2,'#765296');c.circle(x,y,1,'#ab7edb');c.set(x,y-1,'#d0a8ec')
view(result)
finish(result)
