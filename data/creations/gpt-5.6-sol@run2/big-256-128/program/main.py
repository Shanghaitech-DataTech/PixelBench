base = input_canvas.copy(name="original")

# Global night tint: preserve the source's detailed clouds, mountains, and masonry.
mood = new_canvas(256, 128, name="crimson night")
mood.rect(0, 0, 256, 128, "#170611a8")
mood.rect(0, 0, 256, 58, "#28081770")
mood.dither(0, 55, 256, 38, ["#34091455", "#08071266"], pattern="bayer4")
scene = flatten([base, mood], name="demon realm")

# Red storm rents and ember-lit cloud undersides.
storm = new_canvas(256, 128, name="blood storm")
for pts in [
    [(0,20),(35,27),(57,25),(83,31),(57,33),(23,29)],
    [(174,17),(205,14),(255,21),(255,27),(217,22),(187,24)],
    [(4,49),(43,45),(76,50),(104,48),(83,54),(35,53)],
    [(153,48),(187,43),(230,47),(255,42),(255,51),(214,53),(178,50)],
    [(0,73),(34,69),(59,73),(89,70),(64,77),(20,78)],
    [(174,70),(211,65),(255,68),(255,77),(223,73),(194,77)]
]: storm.poly(pts, "#6e1426aa")
storm.line(0, 57, 70, 62, "#c6323d66")
storm.line(186, 57, 255, 53, "#c6323d66")
# Falling sparks.
for x,y in [(13,38),(28,62),(45,17),(61,44),(83,11),(96,67),(108,29),(149,15),(159,62),(178,34),(193,8),(212,40),(231,60),(246,31),(18,88),(239,87)]:
    storm.set(x,y,"#ff7548").set(x,y+1,"#a91f2f")
scene = flatten([scene, storm], name="storm composited")

# Replace the pale moon with a pixel-edged blood moon.
moon = new_canvas(256, 128, name="hanging blood moon")
moon.circle(128, 25, 23, "#2a0710")
moon.circle(128, 25, 21, "#8f1725")
moon.circle(128, 25, 18, "#d43a39")
moon.dither(111, 9, 34, 32, ["#e65445", "#b92331"], pattern="bayer4")
# Lunar scars and shadow craters.
moon.rect(116,13,5,3,"#7b1023").rect(137,17,4,5,"#861326")
moon.rect(121,29,7,4,"#97172a").rect(132,35,5,3,"#7d1022")
moon.rect(112,24,3,6,"#a51c2c").rect(136,9,3,3,"#ff7654")
moon.line(119,8,116,18,"#ff7654")
moon.line(143,25,138,32,"#73101f")
# Heavy chain suspending the moon from the unseen ceiling of the sky.
moon.line(127,0,127,7,"#15060b")
moon.line(129,0,129,7,"#60101d")
for y in range(0,8,4):
    moon.rect(126,y,4,2,"#2b0910")
# Side chains, sagging toward the moon's iron hooks.
moon.path("M73 0 Q91 8 110 17", "#250810", fill=False)
moon.path("M183 0 Q164 8 146 17", "#250810", fill=False)
moon.path("M74 1 Q92 9 110 18", "#8a1823", fill=False)
moon.path("M182 1 Q163 9 146 18", "#8a1823", fill=False)
moon.rect(108,16,4,4,"#19060b").rect(145,16,4,4,"#19060b")
scene = flatten([scene, moon], name="moon composited")

# Reinforce the citadel as a black, many-spired Demon King's castle.
castle = new_canvas(256, 128, name="demon castle")
# Dark mass follows the original hill and fortress while allowing old stone highlights through.
castle.poly([(57,112),(68,93),(81,88),(86,75),(99,78),(105,65),(115,69),(123,53),(132,59),(139,67),(148,65),(156,78),(168,81),(177,102),(190,110),(190,128),(55,128)], "#100812d8")
# Central keep and horned crown.
castle.poly([(111,88),(111,57),(117,57),(117,48),(121,48),(121,38),(125,45),(128,36),(131,45),(135,38),(135,49),(140,49),(140,58),(146,58),(146,91)], "#160914")
castle.poly([(118,48),(123,43),(128,47),(133,43),(139,49),(136,54),(120,54)], "#310b18")
# Left and right towers with irregular battlements.
castle.poly([(87,96),(87,67),(91,67),(91,62),(95,66),(99,60),(102,67),(106,67),(106,98)], "#120812")
castle.poly([(148,99),(148,68),(152,68),(152,62),(156,67),(160,59),(163,67),(168,67),(168,101)], "#110711")
castle.rect(88,66,19,4,"#2b0c19").rect(148,67,21,4,"#2b0c19")
for x in [89,96,103,149,156,164]: castle.rect(x,62 if x<110 else 63,4,7,"#130711")
# Outer needle towers and hooked horns.
castle.poly([(72,108),(75,79),(78,87),(81,74),(84,87),(86,108)], "#110710")
castle.poly([(170,109),(172,82),(176,88),(179,73),(181,91),(184,109)], "#110710")
castle.line(81,75,76,68,"#2c0b17").line(179,74,185,66,"#2c0b17")
castle.line(76,68,73,72,"#6d1424").line(185,66,188,70,"#6d1424")
# Razor spires and finials.
for x,y0,y1 in [(75,79,69),(84,87,75),(94,62,52),(100,65,54),(115,57,43),(128,36,25),(140,58,45),(154,62,51),(161,61,47),(176,82,67)]:
    castle.line(x,y0,x,y1,"#09050b")
    castle.set(x,y1,"#a31d2b")
# Hell-lit windows, narrow and uneven.
for x,y,h in [(94,73,6),(101,76,5),(116,62,8),(124,54,7),(132,56,6),(139,65,8),(154,74,6),(161,77,8),(78,91,5),(176,92,6)]:
    castle.rect(x,y,2,h,"#ff4b32")
    castle.set(x,y,"#ffd05a")
# Gate: a furnace mouth beneath the keep.
castle.path("M116 105 V94 Q128 83 140 94 V105 Z", "#350a16")
castle.path("M121 105 V96 Q128 89 135 96 V105 Z", "#a51c27")
castle.rect(125,96,6,9,"#f04a31")
castle.line(128,95,128,105,"#ffd05a")
# Stone-red edge highlights.
castle.line(88,95,88,69,"#671526").line(106,96,106,70,"#671526")
castle.line(148,98,148,70,"#671526").line(168,99,168,71,"#671526")
castle.line(112,87,112,59,"#721829").line(145,89,145,60,"#721829")
# Torn royal banners.
castle.line(105,65,105,81,"#5e1020")
castle.poly([(106,67),(116,70),(111,74),(116,78),(106,77)], "#9d1728")
castle.set(110,71,"#f05a3f")
castle.line(151,68,151,84,"#5e1020")
castle.poly([(152,70),(161,72),(157,76),(161,80),(152,79)], "#8d1426")
# Subtle masonry and roof rims keep the fortress dimensional.
for x0,y0,x1 in [(90,84,104),(114,73,125),(130,76,144),(150,87,165),(93,91,103),(116,84,127),(132,88,144)]:
    castle.line(x0,y0,x1,y0,"#3d1020")
for x,y in [(92,70),(99,70),(116,55),(123,51),(134,52),(151,71),(159,71)]:
    castle.rect(x,y,4,2,"#571426")
castle.line(87,99,107,99,"#761629").line(147,101,169,101,"#761629")
castle.line(110,90,147,90,"#611426")
# Iron gate bars and small arrow slits.
for x in [119,124,132,137]: castle.line(x,96,x,105,"#220913")
for x,y in [(96,85),(102,89),(117,78),(124,68),(136,70),(142,80),(154,88),(162,91)]:
    castle.set(x,y,"#c62830").set(x,y+1,"#651320")
scene = flatten([scene, castle], name="castle composited")

# Volcanic foreground, dead spikes, lava fissures, and circling bats.
front = new_canvas(256, 128, name="cursed foreground")
front.poly([(0,114),(18,111),(29,116),(45,109),(62,117),(79,111),(96,116),(111,108),(128,113),(143,106),(160,115),(176,110),(191,116),(207,107),(224,114),(239,106),(255,110),(255,127),(0,127)], "#09060dce")
for pts in [[(20,127),(31,119),(43,127)],[(65,128),(78,116),(89,128)],[(153,128),(164,117),(177,128)],[(209,128),(224,116),(239,128)]]:
    front.poly(pts,"#1d0913")
for x0,y0,x1,y1 in [(5,122,28,125),(48,120,69,124),(91,122,112,118),(145,120,168,125),(188,123,205,118),(225,121,252,117)]:
    front.line(x0,y0,x1,y1,"#8e1727")
    front.set(x1,y1,"#ff643d")
# Thorn silhouettes at the edges.
front.line(7,116,4,96,"#08050a").line(4,105,0,101,"#08050a").line(4,108,10,102,"#08050a")
front.line(244,111,249,91,"#08050a").line(248,99,255,94,"#08050a").line(247,103,240,98,"#08050a")
# Pixel bats.
for x,y,s in [(35,37,1),(67,54,1),(188,39,1),(214,61,1),(51,74,1),(200,80,1),(102,22,1),(160,28,1)]:
    front.line(x-4*s,y,x,y+2*s,"#07040a")
    front.line(x,y+2*s,x+4*s,y,"#07040a")
    front.set(x,y+1,"#b21e2b")
# Crown sigil over the gate.
front.poly([(123,88),(125,82),(128,87),(131,82),(133,88),(128,92)], "#f04a35", fill=False)

result = flatten([scene, front], name="demon_king_castle")
view(result, size=768, margin=0)
finish(result)
