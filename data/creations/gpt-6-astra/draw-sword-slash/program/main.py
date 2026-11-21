# Preserve the original pixels on an expanded, shared frame.
W,H=144,120
OX,OY=30,40
f1=new_canvas(W,H,name='01_original')
f1.blit(input_canvas,OX,OY)
# The left arm is the far arm, at the image's right, holding the hilt.
body=input_canvas.copy(name='body_for_finish')
# Remove the old far sleeve, gripping left hand and the sheathed hilt.
body.poly([(49,26),(54,27),(57,30),(57,36),(61,36),(61,43),(49,43),(47,40),(47,35),(49,32)],None)
# Preserve the near right hand and the scabbard mouth. Restore torso edge.
body.poly([(47,27),(50,28),(49,33),(47,36),(48,39),(46,40),(45,35)],'c1')
body.poly([(47,28),(49,29),(47,33),(46,35),(47,38),(45,38),(45,30)],'c3')
trail=new_canvas(W,H,name='black_slash')
# One continuous rising sweep: thin at its lower-left origin, wide in motion,
# and tapering into the blade's upper-right finishing point.
trail.path('M 8 109 C 53 105 108 79 133 9 C 147 53 112 109 62 115 C 40 118 20 114 8 109 Z','#020202')
# Cut the inner crescent back to a sharp clean swoop.
trail.path('M 8 109 C 44 110 96 91 118 52 C 104 82 59 111 8 109 Z',None)
# Sparse trailing ink fragments.
trail.line(13,112,22,114,'c0')
trail.line(24,117,31,118,'c0')
trail.poly([(2,108),(7,107),(11,108),(6,110)],'c0')
f2=new_canvas(W,H,name='02_completed_slash')
f2.blit(trail,0,0)
f2.blit(body,OX,OY)
# Draw the raised arm and weapon separately to tune their proportions.
base=f2
f2=new_canvas(W,H,name='raised_left_arm')
# Raised left sleeve, shoulder to elbow to wrist. Near right arm is untouched.
f2.poly([(79,67),(85,65),(94,62),(100,55),(105,46),(110,46),(115,52),(109,64),(102,72),(90,78),(81,77)],'c1')
f2.poly([(81,68),(86,67),(95,64),(102,56),(106,49),(109,49),(112,53),(106,63),(99,70),(89,75),(82,74)],'c3')
f2.poly([(83,68),(87,67),(96,64),(102,57),(105,53),(107,54),(101,65),(94,70),(85,72)],'c2')
f2.poly([(83,74),(91,72),(100,68),(106,61),(111,53),(112,55),(108,64),(101,72),(90,77),(82,76)],'c4')
f2.line(99,65,104,66,'c1')
f2.line(101,62,106,63,'c4')
# Cuff.
f2.poly([(104,47),(109,44),(115,49),(113,54),(110,56),(103,51)],'c0')
f2.poly([(105,47),(109,46),(113,49),(112,52),(110,53),(105,50)],'c2')
# Drawn sword: outlined steel blade travels up and right from the guard.
f2.poly([(114,40),(111,37),(128,10),(134,4),(133,15),(119,41)],'c0')
f2.poly([(113,37),(128,12),(132,8),(131,16),(118,39)],'c13')
f2.poly([(113,37),(129,12),(132,8),(129,16),(115,38)],'c11')
f2.line(117,36,130,16,'c12')
# Grip continues down-left, in the raised LEFT fist only.
f2.line(114,40,107,51,'c0')
f2.line(115,40,108,51,'c0')
f2.line(114,40,108,49,'c8')
f2.set(112,43,'c6')
f2.set(110,46,'c6')
# Warm skin clusters around the hilt.
f2.poly([(108,42),(111,41),(114,43),(114,46),(111,51),(108,51),(105,48),(106,45)],'c5')
f2.poly([(108,43),(111,42),(113,44),(112,46),(110,46),(110,49),(108,50),(106,47)],'c10')
f2.line(110,43,112,44,'c6')
f2.set(111,47,'c8')
f2.set(107,49,'c6')
# Steel crossguard, clearly separating blade from fist.
f2.poly([(109,35),(112,35),(120,41),(119,44),(116,43),(109,38)],'c0')
f2.line(110,36,119,42,'c13')
f2.line(110,37,118,43,'c12')
f2.set(111,36,'c11')
# Compress the reach horizontally while keeping its shoulder anchored.
arm=f2
f2=new_canvas(W,H,name='02_completed_slash_final')
trail.select(0,0,W,H).resize(122,H).copy_to(12,0,f2,mode='over')
f2.blit(body,OX,OY)
arm.select(0,0,W,H).resize(122,H).copy_to(12,0,f2,mode='over')
view(f1,scale=4,margin=0)
view(f2,scale=4,margin=0)
# Neutral preview only, not an output frame.
bg=new_canvas(W,H,background='#aaa3b2',name='preview_background')
check=flatten([bg,f2],name='pose_check')
view(check,scale=4,margin=0)
finish([f1,f2])
