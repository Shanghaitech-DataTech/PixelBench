exec(open('main.py').read().replace("print(result.matrix_text(region=(81,103,117,143)))",''))
w,h,raw=result.to_rgba(); a=np.frombuffer(raw,dtype=np.uint8).reshape(h,w,4)
for y in range(108,163):
 s=''
 for x in range(36,135):
  r,g,b,_=map(int,a[y,x]);
  if r>g*1.25 and r>40: ch='R'
  elif max(r,g,b)>140: ch='*'
  elif b>r*1.6 and b>g*1.5: ch='P'
  elif max(r,g,b)<45: ch='.'
  elif max(r,g,b)<80: ch=':'
  else: ch='+'
  s+=ch
 print(y,s)
