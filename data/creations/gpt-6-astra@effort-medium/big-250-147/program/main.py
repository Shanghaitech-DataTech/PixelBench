output=input_canvas.copy(name='output')
pal={p['index']:p['rgba'] for p in input_canvas.palette()}
# Find the solid ridgeline beneath the stippled dusk sky.
heights=[]
for x in range(250):
 h=100
 for y in range(60,105):
  if all(input_canvas.get(x,k)>71 for k in range(y,y+4)):
   h=y;break
 heights.append(h)
# Use the original pixel textures with a daylight palette.
def mix(a,b,t):
 return tuple(round(u+(v-u)*max(0,min(1,t))) for u,v in zip(a,b))
for y in range(147):
 for x in range(250):
  i=input_canvas.get(x,y);r,g,b,a=pal[i]
  if y<heights[x]:
   col=mix((57,159,221),(151,213,239),(y//4)*4/110)
  elif i<=171:
   # Cool shaded slopes and pale, sunlit distant rock.
   t=(r-44)/168
   col=mix((54,87,104),(170,191,173),t)
   if r>150 and r-b>35:
    col=mix((153,173,164),(213,217,186),(r-150)/65)
  else:
   t=(r-20)/96
   col=mix((24,57,42),(127,160,76),t)
  output.set(x,y,col)
view(output)
finish(output)
