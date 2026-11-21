# A repeatable timber floor tile: three boards, staggered end joints.
result = new_canvas(16, 16, background='#a67343', name='wooden_planks')
C = {'seam':'#51321f', 'edge':'#79502f', 'grain':'#915d34',
     'mid':'#a67343', 'light':'#bc8952', 'shine':'#cc9c63',
     'darkboard':'#9b663b', 'knot':'#684025'}
# Vertical plank grooves repeat on the left boundary of the tile.
for left, right, end in [(1,4,3),(6,9,11),(11,15,7)]:
    result.rect(left,0,right-left+1,16,C['mid'])
    # Opposite ends have slightly different heartwood tones.
    for y in range(16):
        if (left == 1 and y < end) or (left == 6 and y > end) or (left == 11 and y < end):
            result.line(left,y,right,y,C['darkboard'])
        result.set(left,y,C['light'])
        result.set(right,y,C['edge'])
    result.line(left,end-1,right,end-1,C['edge'])
    result.line(left,end,right,end,C['seam'])
    result.line(left,end+1,right,end+1,C['light'])
    result.set(left,end+1,C['shine'])
for x in [0,5,10]:
    result.line(x,0,x,15,C['seam'])
# Irregular, narrow grain follows the length of each board.
for x,y in [(3,0),(3,1),(2,5),(2,6),(3,7),(3,12),(2,13),(2,14),(3,15),
            (8,0),(8,1),(7,2),(7,3),(7,4),(8,5),(8,6),(8,7),(7,9),(8,13),(8,14),(8,15),
            (13,0),(13,1),(14,2),(14,3),(13,4),(13,5),(13,9),(12,10),(14,15)]:
    result.set(x,y,C['grain'])
for x,y in [(2,0),(2,1),(3,5),(3,6),(2,12),(3,14),
            (7,0),(8,3),(8,4),(7,7),(7,8),(7,14),
            (12,1),(12,2),(13,3),(12,5),(14,9),(14,10),(12,15)]:
    result.set(x,y,C['light'])
# Two compact knots, with dark cores and bent grain around them.
for x,y,col in [(2,8,'grain'),(3,8,'edge'),(1,9,'grain'),(2,9,'knot'),(3,9,'edge'),
                (2,10,'edge'),(3,10,'light'),(2,11,'grain'),
                (13,10,'grain'),(12,11,'grain'),(13,11,'edge'),(14,11,'grain'),
                (12,12,'edge'),(13,12,'knot'),(14,12,'edge'),
                (12,13,'light'),(13,13,'edge'),(14,13,'grain'),(13,14,'grain')]:
    result.set(x,y,C[col])
print(result.stats_text())
print(result.matrix_text())
finish(result)
