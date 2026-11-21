# Both frames retain the original sprite at the same scale.
f1 = new_canvas(76, 68, name='frame1')
f1.blit(input_canvas, 10, 4)

# Separate the figure from the raised weapon for the follow-through.
figure = input_canvas.copy(name='figure')
figure.poly([(18,0),(29,0),(29,7),(27,9),(22,8),(18,8)], None)
figure.poly([(28,8),(35,9),(42,11),(42,22),(36,22),(32,19),(29,14)], None)
# Shift the forward boot out to the left, preserving its pixel texture.
boot = input_canvas.select(3,50,15,9).preview()
figure.poly([(3,51),(16,50),(17,57),(15,59),(3,59)], None)

f2 = new_canvas(76,68,name='frame2')
# Sweeping white arc behind the descending blade.
f2.path('M 40 5 Q 63 5 71 24 Q 74 31 73 38 L 70 35 Q 69 20 60 14 Q 52 8 40 8 Z', '#ffffff')
f2.path('M 47 10 Q 62 13 68 27 L 66 25 Q 59 15 47 12 Z', '#d6dbe0')
f2.line(68, 31, 70, 35, '#ffffff')
f2.blit(figure,10,4)
f2.blit(boot,5,57)
# Restore the leg-to-boot connection in the original armour colours.
f2.poly([(17,51),(22,52),(21,57),(18,61),(13,61),(13,58)], '#101010')
f2.poly([(17,52),(21,53),(20,57),(16,59),(14,58)], '#5a565a')
f2.line(16,55,19,56,'#a9a5ab')
f2.line(13,60,18,60,'#332d32')
# The forward hand grips a sword angled down and out from the body.
# Dark outline, silver blade planes, and gold crossguard use the sprite palette.
f2.poly([(39,27),(43,29),(46,32),(44,35),(40,33),(37,31)], '#101010')
f2.poly([(39,28),(42,29),(44,32),(42,33),(39,31)], '#858086')
f2.set(40,29,'#dccaca')
# Blade, with an emphatic point at the end of the swing.
f2.poly([(45,31),(68,49),(70,54),(65,53),(42,36)], '#101010')
f2.poly([(46,32),(67,49),(68,52),(65,51),(44,35)], '#858086')
f2.poly([(46,32),(67,49),(68,51),(47,36),(44,34)], '#dccaca')
f2.line(47,33,65,48,'#ffffff')
f2.line(48,37,64,50,'#5a565a')
# Crossguard and grip, positioned over the blade root.
f2.line(39,35,47,27,'#101010')
f2.line(40,35,47,28,'#c67b02')
f2.line(41,34,46,29,'#ffcc43')
f2.line(36,25,42,31,'#101010')
f2.line(37,25,42,30,'#512a13')
f2.line(37,26,41,30,'#af7a18')
f2.circle(36,24,1,'#101010')
f2.set(36,24,'#ffcc43')
print(f1.stats_text())
print(f2.stats_text())
finish([f1,f2])
