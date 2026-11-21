# Clear midday version of the supplied mountain landscape.
# All terrain and tree pixels retain their original positions and texture.
import math
output = input_canvas.copy(name='output')
pal = {e['index']:e['rgba'] for e in input_canvas.palette()}

def blend(a,b,t):
    t=max(0,min(1,t))
    return tuple(round(u+(v-u)*t) for u,v in zip(a,b))

# Discrete bands, with sparse ordered transitions in the original pixel scale.
bayer=((0,8,2,10),(12,4,14,6),(3,11,1,9),(15,7,13,5))
def sky(x,y):
    t=min(y/68,1)
    step=t*12
    k=int(step)
    if step-k > (bayer[y%4][x%4]+0.5)/16:
        k+=1
    return blend((69,166,224),(167,219,237),k/12)

# Far ridges are lightly veiled by clear blue atmospheric perspective.
def distant(r,g,b):
    if r>=178 and g>=110:
        # Tiny sunlit ridges behind the main range.
        return blend((185,213,219),(215,231,230),(r-178)/32)
    return blend((112,164,190),(172,211,226),(r-132)/40)

def mountain(r,g,b):
    # Warm light on the distant snowy peak becomes neutral daylight.
    if r>154 and r-g>53:
        return blend((171,200,210),(236,244,235),(r-156)/56)
    if r>115 and r-g>48:
        return blend((126,162,181),(183,207,213),(r-116)/40)
    # Broad rock planes and their cool shaded faces.
    light=(r-44)/104
    return blend((66,110,139),(154,192,206),light)

def forest(r,g,b):
    # Near-black silhouettes open into deep evergreen shade.
    if b > r*0.75:
        return blend((32,68,62),(64,108,83),(r-28)/52)
    return blend((26,65,45),(137,168,89),(r-20)/96)

for y in range(147):
    for x in range(250):
        idx=input_canvas.get(x,y)
        r,g,b,a=pal[idx]
        if y<=50:
            color=sky(x,y)
        elif idx<=71:
            # Heal the low sun and its fringe with the surrounding haze texture.
            if 102<=x<=146 and y<=57:
                source_idx=input_canvas.get(x-68,y)
                r,g,b,a=pal[source_idx]
            if y<=56:
                # Sky-to-horizon transition keeps the original stippled texture.
                depth=max(0,(172-r)/40)
                color=blend(sky(x,y),distant(r,g,b),depth*max(0,(y-50)/6))
            else:
                color=distant(r,g,b)
        elif y>=96 and (idx>=172 or (r<65 and b<49)):
            color=forest(r,g,b)
        else:
            color=mountain(r,g,b)
        output.set(x,y,color)
view(output,scale=3,margin=0)
save('clear_noon',output)
finish(output)
