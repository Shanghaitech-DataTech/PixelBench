result = new_canvas(64,64,background='#111b2b',name='battery-status-set')
# A compact status strip, with identical twelve-pixel battery housings.
edge='#40536b'
body='#c9d9e6'
inside='#202e40'
for i in range(4):
    x=3+15*i
    result.rect(x+4,20,5,3,edge)
    result.rect(x+5,20,3,2,body)
    result.rect(x,23,13,23,edge)
    result.rect(x+1,22,11,25,edge)
    result.rect(x+1,23,11,23,body)
    result.rect(x+2,24,9,21,inside)
    result.line(x+2,24,x+10,24,'#142032')
    n=[18,11,4,13][i]
    col=['#55dca0','#f2c861','#f17873','#4ccae0'][i]
    hi=['#9af0be','#ffe49a','#ffb2a0','#94e8ed'][i]
    result.rect(x+3,43-n+1,7,n,col)
    result.line(x+3,43-n+1,x+9,43-n+1,hi)
    # One dark pixel of internal padding separates fill from frame.
    if i==3:
        result.poly([(x+7,27),(x+3,35),(x+6,35),(x+4,41),(x+10,32),(x+7,32)],'#142032')
        result.poly([(x+7,28),(x+4,34),(x+7,34),(x+5,39),(x+9,33),(x+6,33)],'#fff3b2')
# Small aligned readouts reinforce the states without crowding the icons.
result.text(3,50,'100','#9af0be',spacing=0,font='5x7')
result.text(20,50,'60','#ffe49a',spacing=0,font='5x7')
result.text(35,50,'20','#ffb2a0',spacing=0,font='5x7')
result.text(50,50,'+','#94e8ed',font='5x7')
view(result)
finish(result)
