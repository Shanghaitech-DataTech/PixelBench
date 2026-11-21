result = new_canvas(48,48,name='polar_researcher')
c=result
ink='#1a2639'; dark='#283b50'; mid='#466075'; light='#7895a3'
red='#b94e43'; shade='#763d42'; hi='#e77959'; bright='#f49a6b'
fur='#c2cbbc'; snow='#f0e7cb'; fs='#839e9e'
# scarf whipped behind the body
c.poly([(25,17),(30,17),(35,14),(39,15),(44,13),(42,17),(37,18),(33,18),(29,21),(25,20)],ink)
c.poly([(28,18),(35,15),(39,16),(42,15),(40,17),(34,17),(30,20)],red)
c.line(32,17,37,16,hi)
# legs spread for traction: far leg
c.poly([(26,28),(32,28),(32,33),(36,38),(37,40),(34,43),(30,41),(27,37),(23,33)],ink)
c.poly([(27,30),(30,30),(30,34),(34,39),(32,40),(28,36),(25,33)],dark)
c.line(29,32,32,37,mid)
# far boot
c.poly([(33,38),(37,38),(39,41),(41,42),(41,44),(33,44),(30,42)],ink)
c.line(33,40,36,40,mid)
c.line(34,43,40,43,light)
# near leg
c.poly([(20,28),(27,30),(25,35),(23,39),(22,42),(15,42),(16,38),(18,33)],ink)
c.poly([(20,32),(24,32),(22,36),(21,40),(17,40),(19,35)],dark)
c.line(20,33,18,37,mid)
# planted boot
c.poly([(16,39),(22,39),(23,43),(22,45),(11,45),(10,43),(12,41)],ink)
c.rect(13,42,8,2,dark)
c.line(12,44,21,44,light)
c.line(17,40,20,40,mid)
# rear pack
c.poly([(28,15),(33,18),(35,26),(32,30),(27,28),(25,20)],ink)
c.poly([(29,17),(32,19),(33,25),(30,27),(28,23)],dark)
c.line(31,19,32,23,mid)
c.rect(31,24,3,2,mid)
# parka torso angled forward
c.poly([(19,15),(26,15),(29,19),(31,27),(32,31),(27,34),(18,32),(17,28),(16,22)],ink)
c.poly([(20,17),(25,17),(27,20),(29,27),(29,31),(26,32),(19,30),(18,25),(18,21)],red)
c.poly([(25,18),(28,23),(29,29),(26,31),(23,30),(24,25)],shade)
c.poly([(19,19),(22,18),(23,21),(20,26),(18,26)],hi)
c.line(19,29,26,31,hi)
# fur hem
c.line(19,31,25,33,fs)
c.line(25,33,30,31,fur)
# hood silhouette leaning into wind (left)
c.poly([(15,4),(21,4),(25,6),(27,10),(26,15),(23,19),(17,19),(12,16),(10,12),(11,8)],ink)
c.poly([(16,5),(21,5),(24,7),(25,10),(24,15),(21,17),(17,17),(13,14),(12,10),(13,7)],red)
c.line(17,5,21,5,hi)
c.line(23,7,24,10,hi)
# thick irregular fur rim
c.poly([(13,6),(17,6),(20,8),(21,12),(19,16),(16,18),(12,16),(10,13),(10,9)],fs)
c.poly([(13,6),(16,6),(19,8),(20,11),(18,15),(15,17),(12,15),(10,12),(11,9)],fur)
c.line(12,8,14,7,snow)
c.line(10,10,10,12,snow)
c.line(12,15,14,16,snow)
c.set(18,8,snow)
# face mask and goggle inset
c.poly([(13,8),(16,8),(18,10),(18,13),(15,15),(12,13),(12,10)],ink)
c.poly([(12,12),(17,12),(17,14),(14,15),(12,14)],dark)
c.line(13,14,15,14,mid)
c.line(12,9,17,9,ink)
c.line(11,10,18,10,ink)
c.line(12,11,17,11,'#76c6df')
c.line(12,10,16,10,'#c2edee')
c.set(13,10,'#f4ffff'); c.set(16,11,'#e6fcf4')
c.set(18,10,mid)
# shoulder and arm hanging forward to case
c.poly([(21,18),(24,20),(23,24),(20,28),(17,30),(14,28),(15,24),(17,20)],ink)
c.poly([(20,19),(22,20),(21,24),(18,27),(15,26),(16,23),(18,20)],red)
c.line(18,20,20,19,bright)
c.line(17,22,16,24,hi)
c.line(17,27,19,25,shade)
# cuff and glove
c.poly([(15,26),(19,28),(17,31),(14,30),(13,28)],ink)
c.line(14,27,17,29,fur)
c.rect(14,29,3,3,dark)
c.set(14,29,light)
# case handle
c.rect(10,30,6,5,ink)
c.rect(11,31,4,3,light)
c.rect(12,32,2,2,None)
c.rect(14,30,2,2,dark)
# insulated sample case with metal corners
c.poly([(7,33),(18,33),(20,35),(20,41),(7,41),(5,39),(5,35)],ink)
c.rect(7,34,11,6,mid)
c.rect(6,35,2,4,dark)
c.rect(18,35,1,5,dark)
c.line(8,34,16,34,light)
c.line(8,36,17,36,dark)
c.rect(7,34,2,2,'#aec3c4')
c.rect(16,34,2,2,'#aec3c4')
c.rect(7,39,2,1,light)
c.rect(16,39,2,1,light)
c.rect(11,36,4,3,'#d7ddca')
c.rect(12,36,1,3,'#467b92')
c.set(13,37,'#467b92')
# small shoulder patch and seams
c.set(22,20,fur)
c.line(26,26,28,26,ink)
c.line(26,27,28,27,hi)
view(result)
finish(result)
