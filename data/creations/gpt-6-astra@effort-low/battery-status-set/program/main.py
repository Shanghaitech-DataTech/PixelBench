result = new_canvas(64,64, '#101a2a', name='battery-status-set')
# Quiet panel with a compact, aligned set of battery indicators.
result.rect(1,17,62,31,'#19273b')
result.line(3,17,60,17,'#283b51')
result.line(3,47,60,47,'#0b1220')
for x,level,col,light in [(3,20,'#32c987','#86efac'),(18,12,'#e8ad45','#ffe39a'),(33,4,'#ed606c','#ffa0a3'),(48,10,'#459ee5','#8dd7fa')]:
    # Identical shell and terminal geometry.
    result.rect(x+4,20,5,3,'#a6bed0')
    result.line(x+5,20,x+7,20,'#eff8ff')
    result.rect(x,23,13,25,'#090f1c')
    result.rect(x,23,13,23,'#a6bed0')
    result.line(x+1,23,x+11,23,'#edf7ff')
    result.line(x,24,x,44,'#d5e8f2')
    result.line(x+12,24,x+12,44,'#6a829f')
    result.rect(x+2,25,9,19,'#24364c')
    h = round(level*19/20)
    result.rect(x+2,44-h,9,h,col)
    result.line(x+2,44-h,x+10,44-h,light)
    if h>2: result.line(x+2,45-h,x+2,42,light)
# A dark keyline keeps the charging bolt readable over its fill.
result.poly([(55,26),(50,35),(54,35),(52,42),(60,31),(56,31),(58,26)],'#0c233b')
result.poly([(55,27),(52,34),(55,34),(54,39),(58,32),(55,32),(57,27)],'#fff2ac')
# Percentage captions are spaced to match each icon's centre.
result.text(2,51,'100','#a6bed0',spacing=0)
result.text(20,51,'60','#a6bed0',spacing=0)
result.text(35,51,'20','#a6bed0',spacing=0)
result.text(50,51,'CH','#8dd7fa',spacing=0)
view(result)
finish(result)
