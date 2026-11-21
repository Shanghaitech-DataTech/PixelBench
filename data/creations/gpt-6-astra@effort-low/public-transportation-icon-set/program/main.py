result = new_canvas(64,64,'#102b36',name='transport')
c=result
bg='#193e49'; edge='#35606a'; ink='#ecedcf'; shade='#a8c9bb'; accent='#f3b85b'; dark='#102b36'
for x,y in [(2,2),(33,2),(2,33),(33,33)]:
 c.rect(x+2,y,25,29,edge); c.rect(x,y+2,29,25,edge)
 c.rect(x+2,y+1,25,27,bg); c.rect(x+1,y+2,27,25,bg)
# bus front, mirrors and wheels
c.rect(8,13,2,5,shade); c.rect(23,13,2,5,shade)
c.rect(11,23,4,3,ink); c.rect(19,23,4,3,ink)
c.rect(11,7,12,17,ink); c.rect(10,9,14,13,ink)
c.rect(13,8,8,2,accent)
c.rect(12,12,10,6,dark); c.rect(12,12,4,5,shade); c.rect(18,12,4,5,shade)
c.rect(12,20,3,2,accent); c.rect(19,20,3,2,accent)
c.rect(16,21,2,1,dark)
# subway front and rails
c.line(42,27,46,21,shade); c.line(54,27,50,21,shade)
c.line(44,25,52,25,shade)
c.rect(44,6,9,2,ink); c.rect(42,8,13,14,ink); c.rect(43,22,11,2,ink)
c.rect(46,8,5,2,accent)
c.rect(44,12,9,6,dark); c.rect(44,12,4,5,shade); c.rect(49,12,4,5,shade)
c.rect(44,20,2,2,accent); c.rect(51,20,2,2,accent)
c.rect(47,22,3,2,dark)
# bicycle wheels: consistent two pixel rims
for x in [9,23]:
 c.circle(x,53,5,ink); c.circle(x,53,3,bg)
# frame
c.line(9,53,14,45,accent); c.line(10,53,15,45,accent)
c.line(9,53,18,53,accent); c.line(10,52,18,52,accent)
c.line(14,45,18,53,accent); c.line(15,45,19,53,accent)
c.line(14,45,21,45,accent); c.line(14,46,21,46,accent)
c.line(18,53,21,45,accent); c.line(19,53,22,45,accent)
c.line(23,53,20,42,shade); c.line(24,53,21,42,shade)
c.rect(20,41,5,2,ink); c.rect(11,42,6,2,ink); c.rect(14,44,2,2,ink)
# walking pedestrian
c.rect(48,38,4,5,ink); c.rect(47,39,6,3,ink)
c.poly([(47,44),(51,44),(52,49),(56,51),(55,53),(50,51),(49,48),(48,51),(52,57),(52,60),(49,60),(49,58),(45,53),(42,59),(39,59),(43,51),(45,46),(42,48),(41,52),(38,51),(40,46)],ink)
c.rect(47,45,3,6,accent)
view(c)
finish(result)
