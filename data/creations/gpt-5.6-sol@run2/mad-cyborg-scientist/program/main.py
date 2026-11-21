# Mad cyborg scientist portrait, 64x64 pixel art.
C = {
    'bg': '#090d16', 'bg2': '#111a27', 'bg3': '#1b2935',
    'black': '#05070b', 'outline': '#17151a',
    'skin_d': '#6e3c32', 'skin': '#b56a52', 'skin_l': '#eead7e', 'skin_hi': '#ffd6a0',
    'lip': '#6d2732', 'mouth': '#260f18', 'tooth': '#f4e5c7',
    'hair_d': '#777b80', 'hair': '#c4c8c4', 'hair_hi': '#f5f2df',
    'steel_d': '#27323b', 'steel': '#526672', 'steel_l': '#8ba0a6', 'steel_hi': '#d0dedb',
    'rust': '#8b4931', 'copper': '#d1783d',
    'cyan_d': '#087b88', 'cyan': '#12d8df', 'cyan_hi': '#b9ffff',
    'red': '#e53d47', 'red_hi': '#ff8b68',
    'coat_d': '#6f7370', 'coat': '#b7b8aa', 'coat_l': '#e5e2cb',
    'leather_d': '#44291f', 'leather': '#71432a', 'leather_l': '#ad7040',
    'gold': '#d6a344', 'green': '#4c9b69'
}

result = new_canvas(64, 64, C['bg'], name='mad-cyborg-scientist')

# Workshop gloom, hard rim shapes and scattered machinery.
result.rect(2, 4, 13, 50, C['bg2'])
result.rect(4, 7, 3, 40, C['bg3'])
result.rect(8, 3, 2, 7, C['steel_d'])
result.rect(5, 11, 8, 2, C['steel_d'])
result.rect(53, 5, 8, 48, C['bg2'])
result.rect(58, 8, 3, 37, C['bg3'])
result.line(1, 57, 62, 57, C['steel_d'])
result.set(6, 17, C['red']); result.set(6, 27, C['cyan_d']); result.set(59, 13, C['gold'])
result.rect(10, 45, 2, 8, C['rust'])

# Back hair mass and wild tufts.
result.poly([(18,9),(20,5),(24,7),(25,2),(29,7),(33,3),(35,8),(41,5),(40,11),(47,10),(44,16),(47,21),(42,24),(19,22),(14,17)], C['hair_d'])
result.poly([(18,12),(15,7),(21,9),(22,3),(25,9),(29,5),(30,11)], C['hair_hi'])
result.poly([(32,9),(36,2),(37,10),(44,6),(41,13),(49,11),(43,17)], C['hair'])
result.line(17, 13, 12, 10, C['hair_hi']); result.line(16, 16, 10, 16, C['hair'])
result.line(42, 15, 50, 13, C['hair_hi']); result.line(41, 11, 46, 5, C['hair_hi'])

# Neck behind head.
result.rect(25, 35, 18, 13, C['outline'])
result.rect(27, 35, 7, 12, C['skin_d'])
result.rect(34, 34, 8, 13, C['steel_d'])
result.rect(38, 36, 3, 10, C['steel_l'])
result.line(35, 38, 35, 45, C['cyan_d'])

# Head silhouette: human left and machine right.
result.poly([(19,13),(26,9),(33,10),(34,16),(34,34),(30,40),(23,37),(18,31),(16,22)], C['outline'])
result.poly([(20,14),(27,10),(32,11),(33,17),(32,34),(29,38),(23,35),(19,30),(18,21)], C['skin'])
result.poly([(20,15),(26,11),(28,12),(25,34),(22,32),(20,27)], C['skin_l'])
result.poly([(20,16),(23,13),(25,14),(21,25),(19,25)], C['skin_hi'])
# Wrinkles and cheek shadow.
result.line(20, 20, 25, 18, C['skin_d']); result.line(19, 22, 25, 21, C['skin_d'])
result.line(20, 28, 25, 26, C['skin_d']); result.set(24, 29, C['skin_hi'])

# Robotic skull plating.
result.poly([(33,10),(40,11),(45,16),(47,26),(44,35),(39,40),(32,35),(33,27)], C['steel_d'])
result.poly([(35,12),(40,13),(43,17),(44,23),(40,25),(34,23)], C['steel'])
result.poly([(41,14),(44,18),(45,25),(42,24)], C['steel_l'])
result.poly([(34,26),(40,25),(45,28),(42,35),(37,38),(32,34)], C['steel'])
result.line(34, 12, 34, 35, C['steel_hi'])
result.line(39, 13, 40, 18, C['steel_hi'])
result.line(41, 28, 44, 30, C['steel_hi'])
result.rect(43, 22, 4, 6, C['outline']); result.rect(44, 23, 2, 4, C['rust'])
result.set(41, 16, C['rust']); result.set(42, 17, C['copper']); result.set(39, 34, C['rust'])
# Plate rivets.
for x,y in [(36,13),(43,20),(35,29),(42,33),(37,37)]:
    result.set(x,y,C['steel_hi'])

# Human eye under severe brow.
result.line(20, 18, 28, 16, C['outline'])
result.rect(22, 19, 6, 3, C['tooth'])
result.rect(25, 19, 2, 3, C['black'])
result.set(26,19,C['skin_hi'])
# Glowing cybernetic eye and bloom pixels.
result.rect(34, 18, 9, 6, C['outline'])
result.rect(35, 19, 7, 4, C['cyan_d'])
result.rect(37, 18, 4, 6, C['cyan'])
result.rect(38, 19, 2, 3, C['cyan_hi'])
result.set(34,17,C['cyan_d']); result.set(43,21,C['cyan_d']); result.set(37,24,C['cyan_d'])

# Nose bridge split by metal seam.
result.line(29, 20, 27, 27, C['skin_d'])
result.line(27, 27, 31, 28, C['outline'])
result.set(28,26,C['skin_hi']); result.rect(32,23,2,6,C['steel_l'])

# Maniacal asymmetric grin.
result.poly([(22,30),(28,31),(33,29),(41,30),(38,36),(31,38),(25,35)], C['mouth'])
result.poly([(24,31),(29,32),(33,31),(39,31),(37,34),(31,35),(26,34)], C['tooth'])
result.line(30, 32, 30, 35, C['skin_d']); result.line(34, 31, 34, 35, C['steel_d'])
result.set(38,34,C['steel_hi']); result.line(24,36,29,38,C['lip'])

# Ear and brain electrode plugs with wires.
result.rect(15, 21, 5, 9, C['skin_d']); result.rect(16, 23, 3, 5, C['skin_l'])
result.rect(19, 8, 5, 4, C['outline']); result.rect(20, 8, 3, 3, C['copper'])
result.rect(36, 7, 5, 4, C['outline']); result.rect(37, 7, 3, 3, C['steel_hi'])
result.line(21, 8, 17, 3, C['red']); result.line(17, 3, 12, 5, C['red_hi'])
result.line(39, 7, 43, 2, C['cyan']); result.line(43, 2, 48, 4, C['cyan_d'])
result.set(12,5,C['red_hi']); result.set(48,4,C['cyan_hi'])

# Torso silhouette and dirty lab coat.
result.poly([(17,40),(25,38),(32,45),(40,39),(50,42),(57,63),(6,63),(11,46)], C['outline'])
result.poly([(16,42),(24,39),(31,47),(25,63),(7,63),(12,47)], C['coat'])
result.poly([(16,43),(21,41),(18,61),(9,61),(12,48)], C['coat_l'])
result.poly([(41,40),(50,43),(56,63),(39,63),(34,47)], C['coat_d'])
result.poly([(42,42),(48,44),(53,61),(47,61)], C['coat'])
# Lapels.
result.poly([(24,39),(31,46),(26,52),(20,42)], C['coat_l'])
result.poly([(40,40),(34,47),(39,52),(46,42)], C['steel_l'])
result.line(31, 45, 31, 62, C['outline'])
# Dirt and singe marks.
result.rect(12,54,5,2,C['leather_d']); result.set(20,48,C['rust']); result.set(22,56,C['steel_d'])
result.line(47,51,51,52,C['rust']); result.set(10,60,C['leather'])

# Leather apron.
result.poly([(25,47),(32,51),(39,47),(43,63),(20,63)], C['leather_d'])
result.poly([(27,49),(32,52),(37,49),(39,63),(23,63)], C['leather'])
result.line(27,50,22,43,C['leather_l']); result.line(37,50,44,43,C['leather_l'])
result.rect(29,55,7,3,C['leather_l']); result.rect(30,56,5,2,C['gold'])

# Tool belt along bottom with visible implements.
result.rect(14,59,35,4,C['leather_d']); result.rect(16,59,31,2,C['leather_l'])
result.rect(19,57,3,7,C['steel']); result.set(20,56,C['steel_hi'])
result.rect(42,56,3,8,C['rust']); result.rect(43,54,2,4,C['copper'])
result.rect(46,59,5,4,C['leather']); result.set(48,60,C['gold'])

# Raised exposed robotic arm on right, behind the hand.
result.poly([(48,44),(51,31),(55,30),(59,35),(56,49),(52,55)], C['outline'])
result.poly([(50,44),(52,32),(55,32),(57,36),(54,49)], C['steel'])
result.rect(52,35,4,4,C['steel_l']); result.rect(51,40,4,3,C['rust'])
result.line(51, 33, 48, 46, C['cyan']); result.line(56, 35, 58, 46, C['red'])
result.set(52,39,C['steel_hi']); result.set(55,44,C['copper'])

# Prosthetic wrist and splayed hand at upper-right.
result.rect(50,25,9,8,C['outline']); result.rect(51,26,7,6,C['steel'])
result.rect(52,27,2,3,C['steel_hi']); result.set(56,28,C['cyan'])
# Palm and segmented fingers.
result.poly([(53,25),(51,20),(52,18),(54,19),(56,24),(58,25),(59,30),(56,32),(52,29)], C['steel_d'])
result.rect(52,19,3,7,C['steel_l']); result.set(53,19,C['steel_hi'])
result.line(55,24,56,16,C['outline']); result.line(56,23,57,16,C['steel_l']); result.set(57,15,C['steel_hi'])
result.line(58,25,61,19,C['outline']); result.line(59,25,62,20,C['steel']); result.set(62,19,C['steel_hi'])
result.line(59,28,63,25,C['steel']); result.set(63,24,C['steel_hi'])
# Articulations.
for x,y in [(53,23),(56,20),(60,22),(58,28)]:
    result.set(x,y,C['copper'])
# Loose prosthetic cables.
result.line(51, 29, 47, 31, C['red']); result.line(47,31,48,39,C['red_hi'])
result.line(57, 31, 60, 34, C['cyan_d']); result.line(60,34,59,42,C['cyan'])
result.set(48,39,C['red_hi']); result.set(59,42,C['cyan_hi'])

# Final crisp highlights and silhouette accents.
result.set(18,14,C['hair_hi']); result.set(23,10,C['hair_hi']); result.set(45,14,C['hair_hi'])
result.line(8, 62, 55, 62, C['black'])
result.set(14,47,C['coat_l']); result.set(50,47,C['coat_l'])

view(result, scale=8, margin=0)
finish(result)
