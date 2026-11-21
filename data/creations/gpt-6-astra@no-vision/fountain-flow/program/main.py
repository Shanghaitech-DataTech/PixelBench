c = new_canvas(64,86,name='running_fountain')
c.blit(input_canvas,0,10)
# The original stonework and golden basin remain beneath the new water.
shadow='#247aab'; water='#36b9da'; light='#81e4ed'; foam='#d9ffff'; white='#ffffff'
def line(x,y,X,Y,col): c.line(x,y+10,X,Y+10,col)
def rect(x,y,w,h,col): c.rect(x,y+10,w,h,col)
def dot(x,y,col): c.set(x,y+10,col)
def path(d,col):
    # Draw SVGs on an offset working layer, using coordinates in final space.
    c.path(d,col,fill=False)
def ripple(x,y,w):
    line(x,y,x+w-1,y,light)
    dot(x-1,y-1,water); dot(x+w,y-1,water)
# Small ripples following the perspective of the bowls.
for args in [(25,11,4),(34,11,4),(19,18,4),(40,18,4),(27,20,4),(34,21,3),(16,27,4),(44,27,4),(25,29,5),(34,30,5),(12,49,5),(46,49,5),(15,53,5),(43,53,5),(26,55,7),(34,56,5)]: ripple(*args)
# Arcing jets above the finial; each path is a crisp one-pixel stroke.
path('M 31 11 Q 29 2 25 3 Q 21 5 22 17',water)
path('M 32 11 Q 35 1 39 4 Q 42 8 41 17',water)
path('M 31 10 Q 28 1 25 4 Q 23 7 23 16',light)
path('M 32 10 Q 35 2 38 4 Q 40 7 40 16',foam)
line(31,-6,31,3,light); line(32,-5,32,5,water)
line(31,-6,31,-3,foam)
dot(30,-7,light); dot(32,-8,foam)
dot(21,4,light); dot(42,3,light); dot(26,-6,foam); dot(37,-7,water)
# Spray lands on the smallest basin.
for x in (23,40):
    line(x-1,10,x+1,10,foam); dot(x,9,light)
# Short falls over the first carved rim.
for x in (27,36):
    rect(x,14,3,6,water)
    line(x,14,x,18,light); line(x+1,15,x+1,20,foam)
    dot(x+2,20,light)
    line(x-1,21,x+3,21,light); dot(x,20,white)
# Falls over the middle rim, widening as they land.
for x in (22,40):
    rect(x,23,3,6,water)
    line(x,23,x+1,26,light); line(x+1,25,x+1,29,foam)
    dot(x+2,28,light)
    line(x-2,30,x+3,30,light)
    dot(x-1,29,foam); dot(x+3,29,foam)
# Main spillways: narrow ribbons allow the sculpted pedestal to show.
for x in (20,41):
    rect(x,33,3,4,water)
    rect(x,37,4,11,water)
    rect(x-1,48,5,5,water)
    line(x,33,x+1,37,light)
    line(x+1,37,x+1,44,foam)
    line(x+1,45,x,50,light)
    line(x+2,38,x+2,48,light)
    line(x+3,40,x+3,46,shadow)
    line(x,49,x,52,foam)
    dot(x+2,51,foam); dot(x+1,53,white)
    # Flecks and little upward splash spikes around the impact.
    line(x-4,54,x+5,54,water)
    line(x-3,53,x+4,53,light)
    line(x-2,54,x+3,54,foam)
    line(x-3,50,x-1,52,foam)
    line(x+4,49,x+3,51,light)
    dot(x-4,48,light); dot(x+5,47,foam)
    dot(x-2,55,light); dot(x+4,55,light)
# Fine side drips from the wide bowl.
for x in (14,49):
    line(x,30,x,34,light)
    line(x,36,x,39,water)
    dot(x,41,foam)
    line(x-1,44,x+2,44,light)
print(c.stats_text())
print(c.matrix_text(region=(17,39,47,66)))
save('fountain_flow',c)
finish(c)
