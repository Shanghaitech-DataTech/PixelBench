result = new_canvas(64,64)
c=result
ink='#100f20'
dark='#21172f'
mid='#392440'
light='#62405a'
# diffuse hovering shadow
c.ellipse(32,57,18,4,'#130e2420')
c.ellipse(32,57,14,3,'#130e2430')
c.ellipse(32,57,10,2,'#130e2440')
# short muscular tendrils behind the orb
for d in ['M17 32 Q8 34 9 42 Q10 47 16 45 L18 42 Q12 43 13 39 L22 37 Z', 'M44 32 Q56 32 55 41 Q54 45 49 44 L47 41 Q52 42 51 38 L43 38 Z', 'M22 40 Q17 47 21 51 Q25 54 28 49 L28 45 Q24 50 23 47 L27 40 Z', 'M36 41 Q35 48 40 51 Q46 52 47 46 L45 43 Q45 48 41 47 L41 40 Z']:
 c.path(d,ink)
c.path('M17 34 Q10 36 11 42 Q12 45 16 43 L14 43 Q11 39 18 37 Z',light)
c.path('M46 34 Q54 34 53 41 L50 42 L52 39 L49 37 Z',mid)
c.path('M23 42 Q19 48 23 50 L26 48 Q21 50 24 44 Z',light)
c.path('M38 43 Q38 49 43 49 L45 47 L41 47 L40 42 Z',mid)
# orb outline
c.ellipse(32,27,23,21,ink)
c.ellipse(32,26,21,19,dark)
c.ellipse(30,24,19,17,mid)
c.path('M12 23 Q15 8 30 7 Q40 6 47 15 L41 12 L31 10 L22 13 L17 19 Z',light)
c.path('M14 31 Q19 42 34 43 L44 38 L50 30 Q51 43 36 46 Q20 46 14 36 Z','#171323')
# heavy angular eyelids framing pale sinister eye
c.path('M11 26 L17 19 L25 16 L36 15 L45 19 L53 26 L47 33 L38 38 L27 38 L17 33 Z',ink)
c.path('M13 26 L20 21 L28 19 L37 19 L45 22 L51 26 L45 31 L37 35 L27 35 L20 32 Z','#a49aaf')
c.path('M15 26 L23 22 L31 21 L40 21 L48 25 L49 27 L43 30 L35 32 L26 32 L20 30 Z','#ded4df')
c.path('M15 26 L21 23 L24 23 L20 27 L22 30 Z','#bfb1c8')
# iris dark outline and shading
c.ellipse(33,27,11,12,ink)
c.ellipse(33,27,9,11,'#30204f')
c.ellipse(33,26,8,10,'#49246d')
c.path('M26 23 L29 19 L35 18 L39 22 L36 21 L30 21 L28 26 L27 30 L25 27 Z','#64358c')
c.path('M27 31 L30 35 L36 35 L40 30 L38 31 L35 33 L31 32 Z','#7442a1')
# radial iris streaks
for a,b,x,y,col in [(27,23,29,25,'#8b53ad'),(30,19,31,22,'#8050a0'),(36,20,35,23,'#64358c'),(39,24,37,25,'#8b53ad'),(38,30,36,29,'#995bc2'),(34,35,34,32,'#a467ce'),(29,32,30,30,'#8b53ad')]: c.line(a,b,x,y,col)
# luminous small void pupil
c.ellipse(33,27,4,6,'#382052')
c.ellipse(33,27,2,5,'#a87ad0')
c.line(33,23,33,30,'#ddc2ed')
c.set(33,25,'#f4e2ff')
c.set(32,26,'#cda8e6')
# upper eyelid overhang
c.path('M11 25 L17 18 L26 14 L36 14 L45 18 L53 25 L49 23 L43 20 L36 17 L27 17 L19 21 Z',dark)
c.line(19,18,26,15,light)
c.line(27,14,35,14,light)
c.line(42,18,48,21,mid)
# lower lid reflected purple
c.line(19,34,26,38,light)
c.line(27,39,36,39,'#503451')
c.line(38,38,45,34,mid)
# sparse dermal ridges
c.line(19,12,22,11,'#91627a')
c.line(25,9,30,8,'#91627a')
c.line(13,28,14,32,light)
c.set(48,16,light)
c.line(46,39,43,42,mid)
view(c)
finish(result)
