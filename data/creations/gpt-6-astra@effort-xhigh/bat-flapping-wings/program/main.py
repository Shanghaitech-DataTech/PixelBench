# Two equally sized frames; the original pixels are preserved in frame 1.
W, H = 41, 30
DX, DY = 7, 8
f1 = new_canvas(W, H, name='frame_1_wings_down')
f1.blit(input_canvas, DX, DY)

ink = '#1d181e'
edge = '#432f53'
pink = '#b572b1'
slate = '#5f5f7b'
web = '#5c436f'

# Raised left wing, with a swept leading edge and scalloped membrane.
wing = new_canvas(W, H, name='raised_wing')
shape = [(16,15),(15,12),(13,9),(11,6),(8,4),(5,2),(1,0),
         (2,4),(2,8),(3,11),(4,9),(6,9),(8,11),(10,15),
         (11,13),(12,13),(14,15),(15,17),(16,17)]
wing.poly(shape, edge)
wing.poly(shape, edge, fill=False)
# Broad inner membrane panels.
wing.poly([(3,4),(6,5),(8,7),(8,10),(6,8),(4,8),(3,9)], web)
wing.poly([(7,5),(10,7),(12,10),(14,13),(12,12),(11,12),(10,13),(9,10)], web)
wing.poly([(12,10),(14,12),(15,14),(15,16),(13,13)], web)
# The cool light follows the raised upper edge.
wing.poly([(2,2),(5,3),(8,5),(10,7),(10,8),(7,6),(5,5),(3,4)], pink)
wing.line(10,8,13,11,slate)
wing.line(13,12,15,14,slate)
wing.line(3,4,3,7,slate)
wing.line(6,5,8,8,slate)
wing.line(8,8,9,11,slate)
# Fingers divide the webbing and terminate in pointed, dark cusps.
wing.line(5,5,3,10,edge)
wing.line(7,6,10,14,edge)
wing.line(10,8,15,16,edge)
for p,q in [((2,8),(3,11)),((3,11),(4,9)),((4,9),(6,9)),
            ((6,9),(8,11)),((8,11),(10,15)),((10,15),(11,13)),
            ((11,13),(12,13)),((12,13),(14,15)),((14,15),(15,17))]:
    wing.line(*p,*q,ink)
wing.set(1,0,ink)
wing.set(2,1,pink)
wing.set(2,2,pink)
wing.set(5,4,slate)
wing.set(9,6,pink)
wing.set(12,9,pink)

other = wing.copy(name='raised_wing_right').mirror('h')
f2 = new_canvas(W, H, name='frame_2_wings_up')
f2.blit(wing,0,0)
f2.blit(other,0,0)
# Keep the face, torso, feet and their original pixels at the same position.
input_canvas.select(9,0,9,16).copy_to(DX+9,DY,f2,mode='over')
# Give both poses the same transparent breathing room.
a = new_canvas(W+2, H+2, name='frame_1')
b = new_canvas(W+2, H+2, name='frame_2')
a.blit(f1,1,1)
b.blit(f2,1,1)
f1, f2 = a, b
view(f1, scale=12, margin=0)
view(f2, scale=12, margin=0)
save('bat_frame_1',f1)
save('bat_frame_2',f2)
finish([f1,f2])
