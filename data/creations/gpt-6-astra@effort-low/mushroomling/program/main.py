result = new_canvas(16,16)
palette = {'X':'#282333','R':'#d84b4e','W':'#fff1d7','B':'#d9ae7e'}
rows = [
'................',
'.....XXXXXX.....',
'...XXRRRRRRXX...',
'..XRRWWRRRRRRX..',
'.XRRRWWRRRWWRRX.',
'.XRRRRRRRRWWRRX.',
'XRRWWRRRRRRRRRRX',
'XRRWWRRRWWRRRRRX',
'XXXXXXXXXXXXXXXX',
'...XWWWWWWWWX...',
'..XBWXXWWXXWBX..',
'.XWBWXXWWXXWBWX.',
'.XXBXWWWWWWXBXX.',
'....XBBBBBBX....',
'...XWWXXXXWWX...',
'...XXX....XXX...']
for y,row in enumerate(rows):
    for x,p in enumerate(row):
        if p in palette: result.set(x,y,palette[p])
view(result)
finish(result)
