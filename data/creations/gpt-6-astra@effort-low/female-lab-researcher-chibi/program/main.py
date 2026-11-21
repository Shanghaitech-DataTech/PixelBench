result = new_canvas(16,16,name='researcher')
# Hand-placed sprite pixels: large head above a compact lab-coated body.
colors = {
 'o':'#20202d','h':'#292936','s':'#414152','g':'#56566a',
 'p':'#efbd9b','l':'#ffdab3','d':'#c88d79','b':'#75492e',
 'w':'#fff9ec','c':'#dce6ec','a':'#9baec2','t':'#427f89',
 'n':'#304954','v':'#7de2d5'
}
rows = [
 '.....oooooo.....',
 '....ohhsssho....',
 '...ohhsshhhho...',
 '...ohhhllllho...',
 '...ohllplllho...',
 '...ohlblblpho...',
 '...ohllllllho...',
 '....ohldlho.....',
 '.....odpdo......',
 '....ocwtwco.....',
 '...olwcttcwov...',
 '...odwcnncwov...',
 '....owcwcwo.....',
 '....occacco.....',
 '.....onono......',
 '.....oo.oo......',
]
for y,row in enumerate(rows):
 for x,ch in enumerate(row):
  if ch in colors: result.set(x,y,colors[ch])
view(result)
finish(result)
