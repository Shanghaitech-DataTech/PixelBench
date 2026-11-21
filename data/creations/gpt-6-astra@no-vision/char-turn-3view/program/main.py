# Original character palette and logical pixel grid, inspected from input_canvas.
chars='.abcdefghijklmnopqrstuvw'
palette={s:i for i,s in enumerate(chars)}
# A three-quarter turn toward screen right (the character's left).
right=[
'........aaaaa...aaaaa.......',
'.......abcabbaaaabbacba.....',
'......abcabccccbcccbacba....',
'.....aacdaccddccddccadcaa...',
'....abadedbccddcdccbdedaba..',
'....acaddedcddddddcdeddaca..',
'...abdbcefeddccccddefecbda..',
'...acdeccbddcabbacddbccedca.',
'..abdcfdaedeabccbaedeadfcda.',
'..acdbdacfeeaaaaaaeefcadbca.',
'..acfacafccfagggggafccfacaa.',
'...adfaadabcagggggacbadaada.',
'...abdcaabaaaaggggaaaabacaa.',
'....acdagaaaccgggggccaadca..',
'....iaaachhhghgggggghcaaai..',
'....ighahaajhgggggghjaagai..',
'.....igaakiikkhggggkiikai...',
'.....ihjhlimllggggglimlii...',
'......ijgnnnlgggggglnnggi...',
'.......ihgggggggggggggggii.',
'.......ijohgggggggggghgii..',
'.....ppppjjohggggghoojiaca..',
'....pqqqqqpjjhhhhjjjipaabda.',
'...pqrrsqsphooooooohpaacfa..',
'..ptrsrsqsqthooooohtqacdbca.',
'..pqsqssqssqthhhhhtqaefdaa..',
'...pqsstqsssstgggtssaedaba..',
'..ijpppqqsrssstttsssaadcaa..',
'..iohopqqsrrsssssssracdaai..',
'..ighjppqqsssssssssradaphi..',
'.iouojipptttqssssqttaapjoi..',
'.iuujivipqtqssssssqtqpijuui.',
'iougojwvptqtsssssstqtpjguoi.',
'iguggowptpqtqssssqtqptguggi.',
'igggjvpttpptqqqqqqtpptggji.',
'ijggjpttqpqpttqqqttpqptgji.',
'.ioghptqpqqtqqqqqqtqqphoi..',
'..iiptqtqstqssssssqtsqtpi...',
'....pqttqsqsssrrsssqsqtqp...',
'...ptqtqsqsssqrrqsssqsqtp...',
'...pqtqssqrsqqrrqqsrqsqtqp..',
'...pspqrqsrqqsrrsqqrsqrqsp..',
'..pqspsrtsrqqsrrsqrrstrsqp..',
'..psptrqtrrqqsrrsqrrtqrtsp..',
'..pqpqrtsrrttsrrstrrrstrqp..',
'...ppsrtrrsttsrrstrrrtrspp..',
'...ppqspsrqttrrrrtqrrspsqp..',
'....ptqpqstttrrrrttsqpqtp...',
'.....pppqqttpssssptqqppp....',
'.......pppppppppppppp......',
]
# Wrap the original curl clusters around the turned head, preserving their colours.
original=[]
ys=[0,2,5,7,10,12,14,17,19,21,24,26,29,31,33,36,38,40,43,45,48,50,52,55,57,59,62,64,66,69,71,74,76,78,81,83,85,88,90,93,95,97,100,102,104,107,109,112,114,116]
for sy in ys:
    original.append(''.join(chars[input_canvas.get(int((x+.5)*66/28),sy)] for x in range(28)))
for y in range(14):
    r=['.']*28
    for x in range(3,26):
        sx=1+(x-3)*13/14 if x<=17 else 14+(x-17)*12/8
        r[x]=original[y][round(sx)]
    right[y]=''.join(r)
def rowparts(parts):
    r=['.']*28
    for x,s in parts:
        r[x:x+len(s)]=s
    assert len(r)==28
    return ''.join(r)
right[14]=rowparts([(4,'iaacdchhhgggggggggghcai')])
right[15]=rowparts([(5,'icdahhhgg'),(14,'aaajggggjaai')])
right[16]=rowparts([(5,'iacahhggg'),(14,'kiikkgggkiki')])
right[17]=rowparts([(6,'idhhjjgg'),(14,'limllggglmi'),(25,'i')])
right[18]=rowparts([(7,'iijhhgg'),(14,'gnnllgggnng'),(25,'i')])
right[19]=rowparts([(9,'ihgggggggggggghggii')])
right[20]=rowparts([(9,'ijohggggggggghgii')])
# Add the narrow far-side eye and warm cheek, absent from the back silhouette.
right[15]=right[15][:10]+'aajh'+right[15][14:]
right[16]=right[16][:10]+'aki'+right[16][13:]
right[17]=right[17][:10]+'hlim'+right[17][14:]
right=[r.ljust(28,'.') for r in right]
# The opposite turn uses the same volume but exposes the braid on the near shoulder.
left=[r[::-1] for r in right]
# Replace the small far braid with the plain puffed sleeve and arm.
# Rows are replaced below as complete pixel rows so all contours remain editable.
left_rows={
19:'..iiggggggggggggghi........',
20:'...iighgggggggghoji........',
21:'....ijooohgggghojjpppp.....',
22:'...ipijjhhhhjjjjpqqqqqp....',
23:'...pqhooooooohpssqssrrqp...',
24:'...pqt hoooohtqssqsrssrtp..'.replace(' ',''),
25:'...pqthhhhhtqsssqssqssqp...',
26:'...psstgggtsssstqssstqp....',
27:'...ijastttsssssrsqqpppji...',
28:'...iaadsssssssrrsqqpohoi...',
29:'...ihacaasssssssqqppjhgi...',
30:'...iojaaatqssqtttppi jouoi.'.replace(' ',''),
31:'..iuujipqtqssssqtqpivijuui.',
32:'..iougjptqtsssstqtpvwjoguoi',
33:'..iggugtpqtqssqtqptpwoggugi',
34:'..ijggtpptqqqqtpptt pvg ggi'.replace(' ',''),
35:'..ijgtpqpqptqqtpqpqttpjggji',
36:'...iopqqtqqqqtqqpqtphgoi..',
}
for y,r in left_rows.items(): left[y]=r
# Rear: same curled crown, full back of the hair, and braid on screen left.
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
'.acdbdacfeeacddcaeefcadbdca.',
'.acfacafccfaddddafccfacafca.',
'..adfaadabcddeeddcbadaafda..',
'..abdcaabaadcddaabaabaacdba.',
'...acdacccbabccbabccc adca...'.replace(' ',''),
'...aaabddedaccacaddedbaaa...',
'....abdeffedaddadeffedba....',
'....acddccddaeedaddccddca...',
'....abdcaacddeeddcaacdba....',
'.....acdbbdcaccacdbbdca.....',
'....aabddccdabbdaccddbaa....',
'...abbdaabddcccddbaabbaa....',
'..aacfcaacbbdddbbcaacpppp..',
'.afabdcaaabccccbaaaapqqqqqp.',
'.acbabdefaaghhhgaapsqsrrrqp.',
'.abadcbdafathhohtqssqsrsrtp.',
'..aafdadcaathhhtqsssqssqsqp.',
'...pabadeefatgtsssstssstqp..',
'..ajaa ccdadsstttssqqpppji..'.replace(' ',''),
'..iaaaaabdars sssrsqqpohoi..'.replace(' ',''),
'..ighpacassssssssqqppjhgi..',
'.iouojipaaatqssqtttppijouoi.',
'.iuujivipqtqssssqtqpivijuui.',
'iougojwvptqtsssstqtpvwjoguoi',
'iguggowptpqtqssqtqptpwoggugi',
'igggjvpttpptqqqqtppttpgjgggi',
'ijggjpttqpqptqqtpqpqttpjggji',
'.ioghptqpqqtqqqqtqqpqtphgoi.',
'..iiptqtqstqssssqtsqtqtpii..',
'....pqttqsqssrrssqsqttqp....',
'...ptqtqsqssqrrqssqsqtqtp...',
'...pqtqssqrsqrrqsrqssqtqp...',
'...pspqrqsrqqrrqqrsqrqpsp...',
'..pqspsrtsrqsrrsqrstrspsqp..',
'..psptrqtrrqsrrsqrrtqrtpsp..',
'..pqpqrtsrrtsrrstrrstrqpqp..',
'...ppsrtrrstsrrstsrrtrspp...',
'...ppqspsrqtrrrrtqrspsqpp...',
'....ptqpqsttrrrrttsqpqtp....',
'.....pppqqtpssssptqqppp.....',
'.......pppppppppppppp.......',
]
# A visible near-side braid overlaps the left-turn shoulder and bodice.
braid=[
'...abca',
'..abbda',
'.aacfca',
'afabdcaa',
'acbabdefa',
'abadcbdafa',
'.aafdadcaa',
'..abadeefa',
'..aaccdada',
'...aaaabda',
'.....acaa',
'......aa',
]
for j,row in enumerate(braid):
    y=19+j
    rr=list(left[y].ljust(28,'.')[:28])
    for x,ch in enumerate(row):
        if ch!='.': rr[x+1]=ch
    left[y]=''.join(rr)

def draw_grid(rows,name):
    assert len(rows)==50,(name,len(rows))
    c=new_canvas(66,119,name=name)
    for y in range(119):
        gy=min(49, int((y+.5)*50/119))
        row=rows[gy].ljust(28,'.')[:28]
        for x in range(66):
            gx=min(27,int((x+.5)*28/66))
            ch=row[gx]
            if ch!='.': c.set(x,y,palette[ch])
    return c
f1=draw_grid(right,'left_45')
f2=draw_grid(left,'right_45')
f3=draw_grid(back,'rear')
for name,rows in [('right',right),('left',left),('back',back)]:
    print(name,'row lengths:',[(i,len(r)) for i,r in enumerate(rows) if len(r)!=28])
    for y,r in enumerate(rows): print(f'{y:02}',r)
for c in [f1,f2,f3]: print(c.stats_text())
print(f1.matrix_text(region=(19,31,58,50)))
finish([f1,f2,f3])
