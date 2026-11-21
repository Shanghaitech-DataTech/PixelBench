bg=new_canvas(66,119,'#c4b8b0',name='inspection')
bg.blit(input_canvas,0,0)
view(bg,scale=5,margin=0)
for label, box in [('head',(0,0,66,55)),('body',(0,50,66,40)),('hem',(0,85,66,34))]:
    part=input_canvas.select(*box).preview()
    view(part,scale=6,margin=0)
print(input_canvas.matrix_text(region=(0,0,65,54),indices=False))
print(input_canvas.matrix_text(region=(0,55,65,118),indices=False))
