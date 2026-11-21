result = new_canvas(16,16,name='mushroomling')
colors = {'X':'#292333','R':'#db424b','W':'#fff2dc','T':'#dba878'}
rows = [
'................',
'.....XXXXXX.....',
'...XXRRRRRRXX...',
'..XRRWWRRRWRRX..',
'.XRRRWWRRWWWRRX.',
'.XRRRRRRRRWRRRX.',
'XRRWWRRRRRRRWRRX',
'XRRWWRRWWRRWWRRX',
'XXXXXXXXXXXXXXXX',
'...XWWWWWWWWX...',
'..XTWXXWWXXWTX..',
'.XTWWXXWWXXWWTX.',
'.XXXWWWWWWWWXXX.',
'...XTTWWWWTTX...',
'...XTTXXXXTTX...',
'....XX....XX....',
]
for y,row in enumerate(rows):
    for x,p in enumerate(row):
        if p in colors: result.set(x,y,colors[p])
view(result)
finish(result)
