# Preserve the complete original sprite and give the punch room to extend.
f1 = new_canvas(35,44,name='frame_1_original')
f1.blit(input_canvas,0,0)
f2 = f1.copy(name='frame_2_left_jab')
ink='#222034'
skin='#eec39a'
mid='#df7126'
shade='#8f563b'
# Remove the bent left forearm and fist, keeping the body and other arm intact.
f2.clear(13,8,9,6)
f2.clear(16,14,5,1)
# Preserve the neck and fill the torso behind the moving shoulder.
for x in range(13,17):
    f2.set(x,8,input_canvas.get(x,8))
f2.set(13,13,skin)
# Join the shoulder and ribcage below the new outstretched arm.
f2.line(13,12,15,14,skin)
f2.line(15,13,16,15,shade)
f2.set(16,14,ink)
# Silhouette: shoulder, level forearm, and a small closed fist.
f2.poly([(12,9),(16,9),(18,10),(25,10),(26,8),(29,8),(31,10),(31,13),(29,15),(26,15),(24,14),(18,14),(16,15),(14,13),(12,11)],ink)
# Broad lit top plane and warm underside, matching the source palette.
f2.poly([(13,10),(16,10),(18,11),(26,11),(26,13),(18,13),(16,14),(14,12),(13,12)],mid)
f2.line(14,10,16,10,skin)
f2.line(16,11,25,11,skin)
f2.line(18,12,24,12,skin)
f2.line(17,13,24,13,shade)
f2.set(16,13,mid)
# Fist: light knuckles, thumb fold, and a shaded heel.
f2.poly([(27,9),(29,9),(30,10),(30,12),(29,14),(27,14),(25,13),(26,11)],mid)
f2.line(27,9,29,9,skin)
f2.line(27,10,30,10,skin)
f2.line(28,11,30,11,skin)
f2.set(26,11,skin)
f2.set(27,12,shade)
f2.line(28,13,29,13,shade)
f2.set(26,13,skin)
print(f1.stats_text())
print(f2.stats_text())
print(f2.matrix_text(region=(6,6,33,17)))
save('frame_1',f1)
save('frame_2',f2)
finish([f1,f2])
