# Two rotated views of the supplied cottage, rebuilt as editable pixel geometry.
W, H = 160, 160
INK = '#161c2e'
DARK = '#6c513a'
WOOD = '#97763d'
WOOD_HI = '#bda759'
PLASTER = '#e1dca3'
PLASTER_HI = '#f9e279'
ROOF = '#dcaA46'
ROOF_DARK = '#98694e'
GLASS = '#e1d968'
SHADOW = '#161c2e45'


def poly(c, pts, col, outline=INK):
    if outline:
        c.poly(pts, outline)
    # Caller supplies inset where a heavy border matters; this is for silhouettes.
    c.poly(pts, col)


def beam(c, a, b, width=3, col=DARK):
    # Pixel beams are parallel strokes with a dark central core.
    x0,y0=a; x1,y1=b
    for o in range(-(width//2), width//2+1):
        c.line(x0+o,y0,x1+o,y1,col)


def window_front(c, x, y, w, h):
    c.rect(x-3,y-3,w+6,h+6,INK)
    c.rect(x,y,w,h,WOOD)
    c.rect(x+3,y+3,w-6,h-6,GLASS)
    c.line(x+w//2,y+3,x+w//2,y+h-4,INK)
    c.line(x+3,y+h//2,x+w-4,y+h//2,INK)
    c.line(x+4,y+4,x+w//2-2,y+4,PLASTER_HI)


def window_iso(c, pts):
    c.poly(pts, INK)
    q=[(pts[0][0]+3,pts[0][1]+2),(pts[1][0]-3,pts[1][1]+2),
       (pts[2][0]-3,pts[2][1]-3),(pts[3][0]+3,pts[3][1]-3)]
    c.poly(q, WOOD)
    r=[(q[0][0]+3,q[0][1]+2),(q[1][0]-3,q[1][1]+1),
       (q[2][0]-3,q[2][1]-2),(q[3][0]+3,q[3][1]-1)]
    c.poly(r, GLASS)
    c.line((r[0][0]+r[1][0])//2,(r[0][1]+r[1][1])//2,
           (r[3][0]+r[2][0])//2,(r[3][1]+r[2][1])//2,INK)
    c.line(r[0][0],(r[0][1]+r[3][1])//2,r[1][0],(r[1][1]+r[2][1])//2,INK)


def frame45():
    c=new_canvas(W,H,name='house_45_degrees')
    # Ground contact and fixed elevated footprint.
    c.ellipse(81,145,67,9,SHADOW)
    # Front and right walls share one vertical corner.
    c.poly([(22,82),(76,66),(76,139),(22,151)],INK)
    c.poly([(27,86),(72,73),(72,135),(27,145)],PLASTER)
    c.poly([(76,66),(139,86),(139,146),(76,139)],INK)
    c.poly([(81,73),(134,90),(134,139),(81,133)],'#c7bd87')
    # Front gable infill remains visible beneath the roof.
    c.poly([(27,83),(52,45),(76,70),(76,91)],INK)
    c.poly([(32,82),(52,53),(71,73),(71,86)],PLASTER)
    # Far roof plane then near/front roof planes, keeping substantial top depth.
    c.poly([(52,34),(108,51),(147,87),(137,95),(76,74)],INK)
    c.poly([(54,40),(105,56),(138,86),(135,88),(78,69)],ROOF_DARK)
    c.poly([(52,34),(76,74),(24,94),(13,86)],INK)
    c.poly([(51,42),(70,71),(25,88),(20,85)],ROOF)
    c.poly([(52,34),(108,51),(76,102),(70,96),(76,74)],INK)
    c.poly([(55,42),(102,56),(75,94),(76,69)],ROOF)
    # Ridge and eave timbers.
    c.line(52,34,108,51,WOOD_HI); c.line(52,35,108,52,WOOD_HI)
    c.line(15,86,76,103,INK); c.line(24,91,76,100,WOOD)
    c.line(76,101,142,93,INK); c.line(79,98,137,91,WOOD)
    # Roof tile courses emphasize the matching projection.
    for x0,y0,x1,y1 in [(31,80,68,67),(37,72,63,58),(83,88,112,57),(94,90,124,63),(108,91,135,75)]:
        c.line(x0,y0,x1,y1,WOOD_HI)
    for x,y in [(30,82),(42,76),(85,84),(97,78),(110,73),(122,80)]:
        c.rect(x,y,5,2,PLASTER_HI)
    # Structural timber on front wall and door.
    beam(c,(27,88),(27,143),3); beam(c,(72,87),(72,135),3)
    beam(c,(27,111),(72,101),3); beam(c,(28,139),(72,128),3)
    beam(c,(31,86),(52,54),3); beam(c,(52,54),(71,76),3)
    beam(c,(52,55),(52,99),3)
    c.path('M38 143 V116 Q38 98 53 95 Q68 98 68 116 V135',INK,fill=False)
    c.path('M43 141 V116 Q43 104 53 101 Q63 104 63 116 V137 Z',WOOD,fill=True)
    c.rect(47,112,13,25,ROOF_DARK)
    c.line(47,121,60,121,PLASTER_HI); c.set(58,128,PLASTER_HI)
    # Right wall timbers and its single window.
    beam(c,(81,76),(81,132),3); beam(c,(134,92),(134,139),3)
    beam(c,(82,103),(134,118),3); beam(c,(82,130),(134,138),3)
    beam(c,(83,78),(105,111),3); beam(c,(132,93),(111,116),3)
    window_iso(c,[(98,88),(123,96),(123,119),(98,112)])
    # Small masonry and wood highlights.
    c.line(30,93,68,82,PLASTER_HI); c.line(31,135,37,133,WOOD_HI)
    c.line(84,126,95,129,PLASTER_HI); c.line(124,128,131,130,WOOD_HI)
    return c


def frame90():
    c=new_canvas(W,H,name='house_90_degrees')
    c.ellipse(80,145,68,9,SHADOW)
    # Broadside right wall: no front plane is exposed.
    c.poly([(23,79),(137,79),(137,145),(23,145)],INK)
    c.rect(29,85,102,54,'#c7bd87')
    # Same roof pitch: far slope remains visible above the ridge.
    c.poly([(42,38),(118,38),(148,67),(137,80),(23,80),(12,68)],INK)
    c.poly([(43,44),(117,44),(139,66),(133,72),(27,72),(20,67)],ROOF_DARK)
    c.poly([(42,38),(118,38),(137,80),(23,80)],INK)
    c.poly([(45,45),(115,45),(130,73),(30,73)],ROOF)
    c.line(42,38,118,38,WOOD_HI); c.line(43,40,117,40,WOOD_HI)
    c.line(22,79,138,79,INK); c.line(28,76,132,76,WOOD)
    # Roof courses and irregular highlights match frame one.
    for y,xa,xb in [(50,40,120),(58,35,125),(66,31,129)]:
        c.line(xa,y,xb,y,WOOD_HI)
    for x,y in [(49,48),(70,55),(93,47),(112,61),(39,63),(82,64)]:
        c.rect(x,y,8,2,PLASTER_HI)
    # Right-wall timber grid, viewed head-on after the rotation.
    beam(c,(29,84),(29,139),3); beam(c,(131,84),(131,139),3)
    beam(c,(55,84),(55,139),3); beam(c,(105,84),(105,139),3)
    beam(c,(29,108),(131,108),3); beam(c,(29,138),(131,138),3)
    beam(c,(30,86),(54,107),3); beam(c,(55,108),(31,137),3)
    beam(c,(130,86),(106,107),3); beam(c,(105,108),(130,137),3)
    # The one right-hand window is now the central subject.
    window_front(c,65,91,30,34)
    c.line(69,96,78,96,PLASTER_HI)
    # Plaster wear and foundation marks.
    c.rect(35,116,8,2,PLASTER_HI); c.rect(114,118,10,2,WOOD_HI)
    c.line(37,132,49,132,WOOD); c.line(111,132,124,132,WOOD)
    c.rect(25,141,110,4,INK)
    return c

f1=frame45()
f2=frame90()
view(f1,scale=3,margin=2,edges='all')
view(f2,scale=3,margin=2,edges='all')
finish([f1,f2])
