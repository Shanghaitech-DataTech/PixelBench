result = new_canvas(16,16)
p = {'o':'#70401d','s':'#b76b20','g':'#e9a52b','l':'#ffd65a','h':'#fff2a0','d':'#92501b'}
rows = [
'................',
'.....oooooo.....',
'...oohhhhhhoo...',
'..ohl lllllgso..',
'..ohlllllllgso..',
'.ohllllgllllgso.',
'.ohlllgdglllgso.',
'.ohgggdddggggso.',
'.ohlgdddddglgso.',
'.ohllgddd gllso.',
'.ogllddgddgllso.',
'..ogdglllgdgso..',
'..oglllllllgso..',
'...oossssssoo...',
'.....oooooo.....',
'................']
# Coin face and crisp inset star, using six opaque colours.
rows[3]='..ohlllllllgso..'
rows[9]='.ohllgdddgllgso.'
for y,row in enumerate(rows):
    for x,ch in enumerate(row):
        if ch in p: result.set(x,y,p[ch])
view(result)
finish(result)
