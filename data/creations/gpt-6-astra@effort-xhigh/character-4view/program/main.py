# Four-view cheerleader sprite sheet, native 64 x 64.
P = {
    'O':'#292638', 'H':'#623a3c', 'h':'#9d5746', 'L':'#d58b59',
    's':'#c9816b', 'S':'#f0b58c', 'P':'#ffdbab', 'b':'#e99289',
    'R':'#e64d69', 'r':'#aa3459', 'l':'#ff8190',
    'w':'#fff4db', 'g':'#b7c4ce', 'd':'#69748e',
    'Y':'#f7c64b', 'y':'#cd872e', 'W':'#fff0a2', 'B':'#895735'
}
def stamp(c,x,y,rows):
    for j,row in enumerate(rows):
        for i,k in enumerate(row):
            if k != '.': c.set(x+i,y+j,P[k])
def line(c,x1,y1,x2,y2,k): c.line(x1,y1,x2,y2,P[k])
def rect(c,x,y,w,h,k): c.rect(x,y,w,h,P[k])
def poly(c,pts,k): c.poly(pts,P[k])

def pom(c,x,y,flip=False):
    rows=[
      '..O.O..',
      '.OWOYO.',
      'OWWYYYO',
      'OYWYyYO',
      'OYWYYyO',
      '.OyOyO.',
      '..O.O..',
    ]
    if flip: rows=[r[::-1] for r in rows]
    stamp(c,x,y,rows)

def bow(c,x,y):
    stamp(c,x,y,[
      'OO...OO',
      'OWO.OYO',
      'OWYOYYO',
      '.OOYOO.',
      '..O.O..',
    ])

def legs_front(c,back=False):
    # Bare knees, white ankle socks, and matching court shoes.
    stamp(c,11,22,[
      '.OOO...OOO.',
      '.OSO...OsO.',
      '.OSO...OSO.',
      '.OSO...OSO.',
      '.OwO...OwO.',
      '.OgO...OgO.',
      'OwwwO.OwwwO',
      'OOOOO.OOOOO',
    ])
    if back:
        rect(c,12,28,2,1,'R'); rect(c,18,28,2,1,'R')
    else:
        c.set(13,28,P['g']); c.set(19,28,P['g'])
        c.set(12,27,P['R']); c.set(19,27,P['R'])

def torso_front(c,back=False):
    # Outstretched arms, with the hands tucked into pom-poms.
    stamp(c,7,13,['...OO','..OsO','.OPSO','OSSO.','OSO..','.O...'])
    stamp(c,20,13,['OO...','OSO..','OSPO.','.OSSO','..OSO','...O.'])
    poly(c,[(12,13),(20,13),(21,19),(11,19)],'O')
    poly(c,[(13,14),(19,14),(20,18),(12,18)],'R')
    line(c,13,15,12,18,'l'); line(c,19,15,20,18,'r')
    if not back:
        line(c,13,14,16,17,'w'); line(c,19,14,16,17,'w')
        rect(c,14,13,5,1,'S'); rect(c,15,14,3,1,'s')
    else:
        rect(c,14,13,5,2,'s'); line(c,13,14,15,16,'w'); line(c,19,14,17,16,'w')
    # White waistband and flared, shaded pleats.
    rect(c,12,18,9,1,'w')
    poly(c,[(12,19),(20,19),(23,23),(9,23)],'O')
    poly(c,[(13,19),(19,19),(21,22),(11,22)],'R')
    line(c,14,20,13,22,'r'); line(c,18,20,19,22,'r')
    line(c,15,20,15,21,'l'); line(c,20,21,21,22,'l')
    line(c,10,22,22,22,'w')
    line(c,10,23,22,23,'O')

def front():
    c=new_canvas(32,32,name='front')
    # High ponytail visible beyond the right shoulder.
    stamp(c,20,4,[
      '.OOO..', 'OHLHO.', 'OHhLHO', '.OhhHO', '.OhhHO',
      '.OhhHO', '..OhHO', '..OHHO', '.OHHO.', '..OO..'
    ])
    legs_front(c)
    torso_front(c)
    stamp(c,10,3,[
      '...OOOOOO....',
      '.OOHHhLhHOO..',
      'OHHhLLhhhHHO.',
      'OHhLLhhhHHHHO',
      'OHHhSSSSSSSHO',
      'OHSPSSSSPSSHO',
      'OSSSOSSSOSSSO',
      '.OSbOSSSObSO.',
      '..OSSSwSSSO..',
      '...OSSSSSO...',
    ])
    bow(c,17,1)
    pom(c,3,16)
    pom(c,23,16,True)
    return c

def back():
    c=new_canvas(32,32,name='back')
    legs_front(c,True)
    torso_front(c,True)
    stamp(c,10,3,[
      '...OOOOOO....',
      '.OOHhLLhHOO..',
      'OHhLLLLhhHHO.',
      'OHhLLLhhhHHHO',
      'OHhLhhhhHHHHO',
      'OHhhhhhhHHHHO',
      'OHHhhhhHHHHHO',
      '.OHHHHHHHHHO.',
      '..OHHHHHHHO..',
      '...OOOOOOO...',
    ])
    # The same ponytail falls over the back of the jersey.
    stamp(c,14,6,[
      '.OOOOO.',
      'OHhLhHO',
      'OHLLhHO',
      'OHLLhHO',
      'OHLLhHO',
      '.OhLhHO',
      '.OhhhHO',
      '.OhhhHO',
      '..OhhHO',
      '..OHHO.',
      '...OO..',
    ])
    bow(c,13,2)
    pom(c,3,16)
    pom(c,23,16,True)
    return c

def left():
    c=new_canvas(32,32,name='left')
    # Ponytail, behind the profile.
    stamp(c,19,4,[
      '.OOO..', 'OHhHO.', 'OHLLHO', 'OHhLHO', 'OHhLHO',
      '.OhhHO', '.OhhHO', '.OhhHO', '.OHHO.', '..OO..'
    ])
    # Far leg is offset a pixel so both shoes can be read.
    stamp(c,15,22,[
      '.OOOO.', '.OSsO.', '.OSsO.', '.OSsO.', '.OwgO.',
      '.OwgO.', 'OgggO.', 'OOOOO.'
    ])
    stamp(c,11,22,[
      '..OOO.', '..OSO.', '..OSO.', '..OSO.', '..OwO.',
      '..OwO.', 'OwwwO.', 'OOOOO.'
    ])
    c.set(14,27,P['R'])
    # Both arms project to the front in profile; far pom sits one pixel higher.
    stamp(c,13,14,['..OOO','..OsO','.OsO.','OsO..','.O...'])
    pom(c,10,16,True)
    poly(c,[(14,13),(19,13),(20,19),(12,19)],'O')
    poly(c,[(14,14),(18,14),(19,18),(13,18)],'R')
    line(c,13,15,14,16,'w')
    rect(c,14,13,4,1,'s')
    rect(c,13,18,7,1,'w')
    poly(c,[(13,19),(19,19),(22,23),(10,23)],'O')
    poly(c,[(14,19),(18,19),(20,22),(12,22)],'R')
    line(c,17,20,18,22,'r')
    line(c,14,20,13,22,'l')
    line(c,11,22,21,22,'w')
    line(c,11,23,21,23,'O')
    # Exposed near shoulder and lowered forearm.
    stamp(c,13,13,[
      '..OO..', '.OPSO.', '.OSSO.', '.OsO..', 'OSSO..', 'OSO...', '.O....'
    ])
    stamp(c,9,3,[
      '.....OOOOO...',
      '...OOHLhhHOO.',
      '..OHLLLhhHHHO',
      '..OhLLhhhHHHO',
      '..OSSHhhhHHHO',
      '..OPSSHHHHHHO',
      '.OSOSSHHHHHHO',
      'OSSSSSsHHHHO.',
      '.O SSSSHHHO..'.replace(' ',''),
      '..OsssOOO....',
    ])
    bow(c,18,1)
    pom(c,8,17)
    return c

result=new_canvas(64,64,name='cheerleader_four_views')
f=front(); b=back(); l=left(); r=l.copy(name='right').mirror('h')
result.blit(f,0,0).blit(b,32,0).blit(l,0,32).blit(r,32,32)
view(result,scale=8,margin=0)
save('cheerleader_four_views',result)
finish(result)
