f1 = new_canvas(62,61,name='idle_1_original')
f1.blit(input_canvas,2,2)
def breathe(name,delta):
    c=new_canvas(62,61,name=name)
    for y in range(-1,57):
        sy=round((y-delta)/(1-delta/46)) if y<46 else y
        if 0<=sy<57:
            for x in range(58):
                c.set(x+2,y+2,input_canvas.get(x,sy))
    return c
f2=breathe('idle_2_inhale',-1)
f3=breathe('idle_3_exhale',1)
view(f1)
view(f2)
view(f3)
finish([f1,f2,f3])
