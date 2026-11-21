output=input_canvas.copy(name='output')
dark='#613642'
mid='#95524c'
light='#c46f5b'
# Connected, stepped rivulets running from the scoop over the cone.
output.poly([(22,30),(30,30),(30,34),(28,36),(28,41),(27,43),(25,43),(24,41),(24,36),(22,35)],dark)
output.poly([(24,31),(28,31),(28,34),(27,36),(27,40),(26,41),(25,40),(25,35),(24,34)],mid)
output.rect(25,34,1,5,light)
output.poly([(31,30),(40,30),(40,35),(38,37),(38,42),(36,43),(36,47),(35,49),(33,49),(32,47),(32,43),(33,41),(33,36),(31,34)],dark)
output.poly([(33,31),(38,31),(38,34),(36,36),(36,41),(35,43),(35,47),(34,48),(33,46),(34,42),(34,35)],mid)
output.rect(34,35,1,6,light)
output.rect(33,44,1,3,light)
# Short rounded melt at the outside rim.
output.rect(40,32,3,6,dark)
output.rect(40,37,2,3,dark)
output.rect(40,33,1,5,mid)
view(output)
finish(output)
