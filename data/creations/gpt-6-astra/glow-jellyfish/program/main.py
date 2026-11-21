result = new_canvas(16, 16, name='glow_jellyfish')
# A compact, dark-edged silhouette with a luminous glassy bell.
colors = {
 'o':'#14263f', 's':'#225477', 'b':'#267d9dcc',
 'c':'#3cb8cbdc', 'l':'#7ce9edee', 'h':'#d8fff9',
 'v':'#607ac4', 't':'#47c9d9', 'p':'#a9fff4',
 'g':'#4bcef035'
}
rows = [
 '................',
 '......oooo......',
 '....oolhhloo....',
 '...olhhllccbo...',
 '..olhllcccbbso..',
 '..ohlccclcbbso..',
 '.oslcclplcbbvso.',
 '.osccclllcbvvso.',
 '.olllpptppllllo.',
 '..oootootootoo..',
 '....otootoot....',
 '....otootooto...',
 '...oto.opo.oto..',
 '...opo.....opo..',
 '................',
 '................',
]
for y,row in enumerate(rows):
 for x,ch in enumerate(row):
  if ch != '.': result.set(x,y,colors[ch])
view(result, scale=24)
save('glow-jellyfish', result)
finish(result)
