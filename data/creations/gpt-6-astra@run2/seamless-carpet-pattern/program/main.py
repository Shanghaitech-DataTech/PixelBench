result = new_canvas(32,32,background='#71312d',name='Emberloom')
# A mirrored loom repeat keeps both pairs of opposite edge pixels identical.
ink='#40262b'; dark='#59282c'; rust='#994634'; terra='#b75c3d'
gold='#d69a51'; light='#edc47c'; cream='#f5dba0'; olive='#7f7745'; leaf='#aaa05b'
for y in range(32):
    for x in range(32):
        u=min(x,31-x); v=min(y,31-y)
        col = '#7f372f' if (u+v)%2==0 else '#71312d'
        if u==0 or v==0: col=dark
        if u==1 or v==1: col=gold if (u+v)%3 else '#ac713e'
        if u==2 or v==2: col=dark
        d=abs(x-15.5)+abs(y-15.5)
        if d<=13: col=ink
        if d<=12: col=gold
        if d<=11: col=light if (u+v)%2 else gold
        if d<=10: col=ink
        if d<=9: col=terra if (u+v)%2 else rust
        if d<=7: col=dark
        if d<=6: col=ink if (u+v)%2 else dark
        result.set(x,y,col)
# Symmetric flowers, curling stems and gold knots in the border.
def sym(x,y,c):
    for xx in {x,31-x}:
        for yy in {y,31-y}: result.set(xx,yy,c)
# corner rosettes on a dark ground, each with four warm petals
for y in range(3,10):
    for x in range(3,10):
        dx=x-6; dy=y-6
        if abs(dx)+abs(dy)<=4: sym(x,y,dark)
        if (abs(dx)<=1 and abs(dy)<=3) or (abs(dy)<=1 and abs(dx)<=3): sym(x,y,gold)
        if (dx==0 and abs(dy)==2) or (dy==0 and abs(dx)==2): sym(x,y,cream)
sym(6,6,rust)
# paired leaves form the climbing floral border
for x,y in [(9,5),(10,4),(11,4),(12,5),(12,6),(5,9),(4,10),(4,11),(5,12),(6,12)]: sym(x,y,olive)
for x,y in [(10,5),(11,5),(5,10),(5,11)]: sym(x,y,leaf)
for x,y in [(14,3),(15,4),(14,5),(3,14),(4,15),(5,14)]: sym(x,y,gold)
sym(15,3,cream); sym(3,15,cream)
# The medallion is an eight-petalled woven flower.
for y in range(11,21):
    for x in range(11,21):
        dx=abs(x-15.5); dy=abs(y-15.5)
        if (dx<=1.5 and dy<=4.5) or (dy<=1.5 and dx<=4.5):
            result.set(x,y,gold)
        if (dx<=0.5 and 2.5<=dy<=3.5) or (dy<=0.5 and 2.5<=dx<=3.5):
            result.set(x,y,cream)
        if dx==2.5 and dy==2.5: result.set(x,y,light)
        if dx<=1.5 and dy<=1.5: result.set(x,y,rust)
        if dx<=0.5 and dy<=0.5: result.set(x,y,cream)
view(result,scale=12,margin=0)
# Preview the repeat without submitting the inspection sheet.
repeat=new_canvas(96,96,background=ink,name='Repeat preview')
for ty in range(3):
    for tx in range(3): repeat.blit(result,tx*32,ty*32)
view(repeat,scale=5,margin=0)
save('emberloom-carpet',result)
finish(result)
