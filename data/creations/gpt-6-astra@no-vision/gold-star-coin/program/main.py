c = new_canvas(16, 16, name='gold-star-coin')
colors = {'X':'#70400d', 'o':'#bd7412', 'g':'#efa91e', 'Y':'#ffd455', 'H':'#fff0a1', 's':'#a65a0b'}
rows = [
'................',
'.....XXXXXX.....',
'...XXooooooXX...',
'..XooHHHHYgooX..',
'..XoHYYYsYYYgX..',
'.XoHYYYYsYYYYoX.',
'.XoHYYsssssYYoX.',
'.XoYYYsssssYYoX.',
'.XoYYYYsssYYYoX.',
'.XoYYYsssssYYoX.',
'.XogYYssYssYYoX.',
'..XogYsYYYsYoX..',
'..XoogYYYYgooX..',
'...XXooooooXX...',
'.....XXXXXX.....',
'................']
for y, row in enumerate(rows):
    for x, ch in enumerate(row):
        if ch != '.': c.set(x, y, colors[ch])
print(c.stats_text())
print(c.matrix_text())
finish(c)
