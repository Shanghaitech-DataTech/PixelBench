s=input_canvas.select(0,0,66,119).resize(28,50).preview()
# Palette letters retain the exact source colors.
def stamp(c, rows, y=0, x=0):
    for j,row in enumerate(rows):
        for i,ch in enumerate(row):
            c.set(x+i,y+j,None if ch=='.' else ord(ch)-96)
head=[
'.......aaaaa..aaaaa.........',
'......abcabbaabbacbaa.......',
'.....abcabccccbcccbacba.....',
'....aacdaccddccddccadcaa....',
'...abadedbccddcdccbdedaba...',
'...acaddedcddddddcdeddaca...',
'..abdbcefeddccccddefecbdba..',
'..acdeccbddcabbacddbccedca..',
'..bdcfdaedeabccbaedeadfcda..',
'..cdbdacfeeaaaaaaeefcadbca..',
'..cfacafccfaagggggafccfaca..',
'..adfaadabcaaggggggcbaafda..',
'...bdcaabaaaaaaggggaacdcaa..',
'...acdacaaccggggggggcca.....',
'...iaaacchhhgggggggghha.....',
'...ighahaajhggggggghaag.....',
'....ighaakiikhgggghkiik.....',
'....ihjhlimmlgggggglmilg....',
'.....iijgnnnlgggggglnngg....',
'.......ihhggggggggggggga...',
'........ijohgggggggghja....',
'.........jjjohgggghojj.....',
'..........pjjjjjjjjjp......',
]
# Shape the torso and skirt around the rotated centerline, preserving folds.
def base():
    c=new_canvas(28,50)
    for y in range(23,50):
        for x in range(28):
            # shoulder and arm profile narrow more than the skirt
            scale=.82 if y<38 else .92
            shift=1 if y<37 else 0
            sx=round((x-13.5-shift)/scale+13.5)
            if 0<=sx<28:
                v=s.get(sx,y)
                # remove foreground braid; underlying dress is reconstructed
                if v in range(1,7):
                    v=19 if x<20 else 17
                c.set(x,y,v)
    # Reconstruct the far puff sleeve and the curved edge of the neckline.
    c.poly([(19,23),(22,24),(24,27),(23,29),(20,29),(18,26)],16)
    c.poly([(19,24),(21,24),(23,27),(22,28),(20,28)],17)
    c.line(20,25,22,27,19)
    c.poly([(17,24),(19,25),(20,29),(18,31),(17,28)],19)
    stamp(c,head)
    return c
braid=[
'..abca...',
'.abbdda..',
'accfcaa..',
'acdbabafa',
'efdababca',
'fdabcdaba',
'acdadfaa.',
'feedaba..',
'dcaacda..',
'adbaaa...',
'.acaa....',
'..aa.....']
a=base()
# Far shoulder braid is partly hidden by the profile.
for y in range(23,32):
    for x in range(23,26):
        col=s.get(min(27,x+1),y)
        if col in range(1,7): a.set(x,y,col)
b=base().mirror()
stamp(b,braid,19,18)
# Back: source hem and arms, with a closed rear bodice and hair covering the nape.
r=s.copy(name='rear_work')
r.clear(0,0,28,31)
back=[
'.......aaaaa....aaaaa.......',
'......abcabbaaaabbacba......',
'.....abcabccccbcccbacba.....',
'....aacdaccddccddccadcaa....',
'...abadedbccddcdccbdedaba...',
'...acaddedcddddddcdeddaca...',
'..abdbcefeddccccddefecbdba..',
'..acdeccbddcabbacddbccedca..',
'.abdcfdaedeabccbaedeadfcdba.',
'.acdbdacfeedccddeefcadbdca.',
'.acfacafccfedddeefccfacafca.',
'..adfaadabcddddddcbadaafda..',
'..abdcaabadedddedabaacdba..',
'...acdacacdeccedcacadca....',
'...abdcadcfdaadcfdacdbca...',
'....acdbacefaafecabdcaa....',
'....acfdabddccd dbadfca....'.replace(' ',''),
'.....adfcabdccdbacdfa......',
'......acdfadccdafdca.......',
'.......adcfaddafcda........',
'.......aacdfccfdcaa........',
'.....pppacdfddfcappp.......',
'....pqqqacdfccfcaqqqp......',
'...pqrrsqacddcaqssrqp.....',
'..ptrsrsqsaccaasssrsrtp....',
'..pqsqssqstaaatqssqsqp....',
'...pqsstqssttssqtssqp.....',
'..ijpppqqssssssqqpppji....',
'..iohopqqssttssqqpoh oi...'.replace(' ',''),
'..ighjppqqsttsqqppjhgi....',
'.iouojipptqttqtp pijouoi..'.replace(' ',''),
]
# Use source sleeves and arms to retain silhouette, replacing back bodice.
for y in range(21,38):
    for x in range(28):
        col=s.get(x,y)
        if col>=7: r.set(x,y,col)
# closed back in original dress colors
r.poly([(10,23),(18,23),(20,30),(18,36),(10,36),(8,30)],17)
r.poly([(11,24),(17,24),(18,30),(16,35),(11,35)],19)
r.line(14,25,14,35,20)
r.set(13,29,18);r.set(13,32,18)
stamp(r,back[:23])
# Braid descends on her left, now visible on the left of the back.
stamp(r,braid,20,5)
# clean remaining source braid colors on right shoulder
for y in range(23,32):
    for x in range(17,27):
        if r.get(x,y) in range(1,7):
            r.set(x,y,17 if x<23 else None)
# Rebuild the right sleeve where the original braid overlapped.
r.poly([(19,23),(22,24),(24,27),(23,29),(20,29),(18,26)],16)
r.poly([(19,24),(21,24),(23,27),(22,28),(20,28)],17)
r.line(20,25,22,27,19)
f1=new_canvas(66,119,name='left_45');a.select(0,0,28,50).resize(66,119).copy_to(0,0,f1)
f2=new_canvas(66,119,name='right_45');b.select(0,0,28,50).resize(66,119).copy_to(0,0,f2)
f3=new_canvas(66,119,name='rear');r.select(0,0,28,50).resize(66,119).copy_to(0,0,f3)
view(f1);view(f2);view(f3)
finish([f1,f2,f3])
