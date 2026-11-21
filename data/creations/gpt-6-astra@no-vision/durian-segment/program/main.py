result=input_canvas.copy(name='output')
# Follow the bottom segment's stepped contour without touching the middle segment.
limits={33:21,34:22,35:24,36:24,37:26,38:26,39:26,40:26,41:28,42:28,43:28,44:29,45:30,46:31,47:32,48:33,49:28,50:27}
flesh={input_canvas.color('#ffda45'), input_canvas.color('#ffc830'), input_canvas.color('#e08c37')}
removed=set()
for y,right in limits.items():
    for x in range(6,right+1):
        if input_canvas.get(x,y) in flesh:
            result.set(x,y,'#fbf4c9')
            removed.add((x,y))
# A quiet recessed edge in the newly exposed pith, following the removed lobe.
shade='#e6d5a2'
lightshade='#f0e5b8'
for y,left,right in [(38,24,25),(39,24,25),(40,24,25),(41,25,27),(42,26,27),(43,26,27),(44,27,28),(45,27,29),(46,26,30),(47,23,31),(48,20,30),(49,20,27),(50,21,25)]:
    for x in range(left,right+1):
        if (x,y) in removed:
            result.set(x,y,shade if x==right or y==49 else lightshade)
print(result.stats_text())
print(result.matrix_text(region=(5,32,35,51)))
finish(result)
