# 32px microscope, hand placed clusters, transparent exterior.
result = new_canvas(32, 32, name='laboratory_microscope')
c = result
ink = '#172739'
shadow = '#344b61'
steel = '#657f93'
mid = '#95afbd'
light = '#d1e2e6'
white = '#f1f8ed'
teal = '#299ba9'
cyan = '#79d6d1'
darkteal = '#226375'
red = '#d87565'
gold = '#edc779'

# Broad cast base: separate top and two visible vertical faces.
c.poly([(4,25),(16,22),(26,25),(28,27),(27,29),(16,31),(5,29),(3,27)], ink)
c.poly([(4,26),(16,24),(27,27),(16,29),(5,27)], light)
c.poly([(5,27),(16,29),(16,30),(5,28)], steel)
c.poly([(16,29),(27,27),(26,29),(16,30)], shadow)
c.line(6,26,15,24,white)
c.line(7,27,15,29,mid)
c.line(18,28,25,27,mid)

# Rear curved support arm with front-lit face and darker right edge.
c.poly([(18,8),(22,8),(25,11),(27,17),(26,23),(23,26),(19,25),(18,23),(21,20),(22,16),(21,13),(18,12)], ink)
c.poly([(19,9),(22,9),(24,12),(25,17),(24,22),(22,24),(20,24),(20,23),(23,20),(24,16),(22,12),(19,11)], mid)
c.poly([(22,9),(24,12),(26,17),(25,22),(23,25),(21,25),(24,21),(25,16),(23,11)], steel)
c.line(20,9,22,10,white)
c.line(23,12,24,15,light)
c.line(23,22,21,24,light)

# Substage illuminator on the base.
c.rect(13,21,5,4,shadow)
c.ellipse(15,24,4,2,ink)
c.ellipse(15,23,3,1,mid)
c.line(13,23,16,23,gold)
c.set(14,23,white)

# Perspective stage, its top and thick lower edge.
c.poly([(6,17),(18,14),(25,17),(25,19),(13,22),(6,19)],ink)
c.poly([(7,17),(18,15),(24,17),(13,20)],steel)
c.poly([(7,18),(13,20),(24,18),(24,19),(13,21),(7,19)],shadow)
c.line(8,17,17,15,mid)
c.line(7,18,12,20,light)
c.line(14,20,23,18,teal)
# Glass specimen slide and its retaining clips.
c.poly([(10,17),(16,16),(20,17),(14,19)], light)
c.line(12,17,16,17,cyan)
c.set(15,17,red)
c.line(9,17,10,18,white)
c.line(19,16,20,17,white)

# Revolving nosepiece and two objective lenses.
c.poly([(14,10),(19,10),(22,12),(19,14),(14,13),(12,12)],ink)
c.poly([(14,11),(19,11),(20,12),(17,13),(14,12)],steel)
# Rear objective angled out to the right.
c.poly([(19,12),(21,12),(22,14),(20,16),(18,14)],ink)
c.line(20,13,21,14,mid)
c.set(20,15,teal)
# Main objective barrel and colored magnification band.
c.rect(14,12,4,4,ink)
c.rect(15,12,2,3,light)
c.line(15,14,17,14,red)
c.rect(15,15,2,2,ink)
c.set(15,15,mid)

# Monocular body tube, tilted toward the viewer's upper left.
c.poly([(11,5),(15,2),(21,8),(21,10),(17,13),(14,10)],ink)
c.poly([(12,5),(15,3),(20,8),(17,11)],light)
c.poly([(17,10),(20,8),(20,10),(17,12),(15,10)],steel)
c.line(13,5,17,9,white)
c.line(16,5,19,8,mid)
# Black eyepiece with an inset blue optical surface.
c.poly([(7,3),(10,0),(13,1),(16,5),(12,9),(8,5)],ink)
c.poly([(9,3),(12,2),(14,5),(12,7)],shadow)
c.line(9,4,12,7,steel)
c.line(12,2,14,4,mid)
c.line(8,3,10,1,teal)
c.line(9,3,11,1,cyan)
c.set(10,2,white)

# Coaxial focus wheel on the outside of the support.
c.circle(24,12,3,ink)
c.circle(24,12,2,steel)
c.line(23,10,25,10,light)
c.line(22,11,22,12,mid)
c.circle(24,12,1,shadow)
c.set(24,11,cyan)
c.set(24,12,teal)
c.set(25,13,darkteal)

view(result, scale=12, margin=0)
save('laboratory-microscope-icon', result)
finish(result)
