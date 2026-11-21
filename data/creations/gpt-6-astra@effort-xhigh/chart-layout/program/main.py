# Fruit counts, with a common horizontal scale of six pixels per item.
result = new_canvas(128, 64, background='#111c2a', name='fruit_chart')
c = result
bg = '#111c2a'
plot = '#152233'
grid = '#253449'
axis = '#43536a'
ink = '#eaf0ed'
muted = '#718399'

# Quiet chart panel and ruler. The fruit gutter is deliberately unlabelled.
c.rect(22, 3, 92, 55, plot)
for x in [52,82,112]:
    for y in range(4,57,3):
        c.set(x,y,grid)
c.line(21,4,21,57,axis)
c.line(21,57,113,57,axis)

# A tiny pixel numeral alphabet for the unobtrusive ruler.
digits = {
 '0':['111','101','101','101','111'],
 '1':['010','110','010','010','111'],
 '2':['111','001','111','100','111'],
 '3':['111','001','111','001','111'],
 '4':['101','101','111','001','001'],
 '5':['111','100','111','001','111'],
 '6':['111','100','111','101','111'],
 '7':['111','001','010','010','010'],
 '8':['111','101','111','101','111'],
 '9':['111','101','111','001','111']
}
def small_text(x,y,s,color):
    for ch in s:
        for yy,row in enumerate(digits[ch]):
            for xx,p in enumerate(row):
                if p=='1': c.set(x+xx,y+yy,color)
        x += 4
for x,s in [(22,'0'),(52,'5'),(82,'10'),(112,'15')]:
    c.set(x,58,axis)
    small_text(x-(len(s)*4-1)//2,59,s,muted)

fruits = [
    (9,10,'#e95665','#ff8586','#b43b54'),
    (20,5,'#e9bd48','#ffe17c','#ae8235'),
    (31,7,'#f08c3e','#ffb65a','#bd5d32'),
    (42,14,'#e4d65c','#fff391','#aaa443'),
    (53,2,'#a27bd8','#c8a5f3','#70509f'),
]
for y,value,base,light,shadow in fruits:
    w=value*6
    c.rect(22,y-3,w,7,base)
    c.rect(22,y-3,w,1,light)
    c.rect(22,y+3,w,1,shadow)
    c.set(22,y-2,light)
    # Count labels are the only prominent text on the chart.
    c.text(22+w+4,y-3,str(value),ink)

# Hand-placed miniatures, using the same palette as their corresponding bar.
colors = {
 '.':None, 'd':'#301f35', 's':'#b43b54', 'r':'#e95665', 'h':'#ff8586',
 'w':'#ffd0b6', 't':'#987147', 'g':'#4e9f6a', 'l':'#90c576',
 'b':'#ae8235', 'y':'#e9bd48', 'Y':'#ffe17c', 'C':'#fff0b3',
 'o':'#bd5d32', 'O':'#f08c3e', 'H':'#ffb65a',
 'e':'#aaa443', 'L':'#e4d65c', 'E':'#fff391',
 'p':'#70509f', 'P':'#a27bd8', 'Q':'#c8a5f3', 'D':'#493660'
}
def sprite(x,y,rows):
    for yy,row in enumerate(rows):
        for xx,p in enumerate(row):
            if p!='.': c.set(x+xx,y+yy,colors[p])

# Apple: cleft shoulders, a short stem and a separate green leaf.
sprite(3,2,[
 '.......t.....',
 '......t.gg...',
 '......tlg....',
 '..srrsrrrs...',
 '.srhhrrrrrs..',
 '.rhwrrrrrrs..',
 '.rhrrrrrrrs..',
 '.srrrrrrrrs..',
 '..srrrrrss...',
 '...ssrsss....',
])
# Banana: an upturned crescent with a pale inner edge and ochre peel.
sprite(3,15,[
 '...........t.',
 '..........ty.',
 '..........YY.',
 '.t.......YYY.',
 '.yY.....YYyb.',
 '.yYY..CYYYyb.',
 '..yYYYYYYyb..',
 '...yyyyybb...',
 '....bbbb.....',
])
# Orange: round citrus with a tiny leaf and stippled rind.
sprite(3,26,[
 '.......gl....',
 '......tgg....',
 '....oOOOo....',
 '...oHHOOOo...',
 '..oHCHOOOOo..',
 '..OHHOOOOOo..',
 '..OOOOOOOOo..',
 '...OOOOOoo...',
 '....ooooo....',
])
# Lemon: pointed ends and an elongated, pale-yellow body.
sprite(3,37,[
 '.........gg..',
 '.......gle...',
 '....eLLLee...',
 '...LEEEELLLe.',
 '..LECEELLLLe.',
 '.eLEELLLLLLe.',
 '..eLLLLLLLe..',
 '...eLLLLee...',
 '....eeee.....',
])
# Grapes: small discrete berries in a tapered bunch.
sprite(3,47,[
 '.......t.....',
 '....ggt......',
 '...glgg......',
 '..DpPDpPD....',
 '..pQPPQPp....',
 '..DpPDpPD....',
 '...pQPQPp....',
 '...DpPPD.....',
 '....pQPp.....',
 '.....pp......',
])
view(result, scale=6, margin=0)
save('fruit_chart', result)
finish(result)
