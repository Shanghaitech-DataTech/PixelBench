import math
from pixelbench_api import new_canvas, save, view, finish

def length3(x, y, z): return math.sqrt(x*x + y*y + z*z)

def sdSphere(p, c, r):
    return length3(p[0]-c[0], p[1]-c[1], p[2]-c[2]) - r

def sdCapsule(p, a, b, r):
    pax, pay, paz = p[0]-a[0], p[1]-a[1], p[2]-a[2]
    bax, bay, baz = b[0]-a[0], b[1]-a[1], b[2]-a[2]
    b2 = bax*bax + bay*bay + baz*baz
    if b2 == 0: return length3(pax, pay, paz) - r
    h = max(0.0, min(1.0, (pax*bax + pay*bay + paz*baz) / b2))
    return length3(pax - bax*h, pay - bay*h, paz - baz*h) - r

def smin(a, b, k):
    h = max(k - abs(a - b), 0.0) / k
    return min(a, b) - h * h * k * 0.25

def map_world(p):
    # LV (viewer's right, apex)
    lv = sdCapsule(p, (36, 32, 0), (44, 50, 2), 9.0)
    
    # RV (viewer's left/center)
    rv = sdCapsule(p, (26, 36, -4), (34, 46, -2), 8.0)
    
    # RA (viewer's left)
    ra = sdSphere(p, (22, 28, -2), 6.5)
    
    # LA auricle (viewer's right)
    la = sdSphere(p, (44, 26, 2), 4.5)
    
    muscle = smin(lv, rv, 6.0)
    muscle = smin(muscle, ra, 4.0)
    muscle = smin(muscle, la, 4.0)
    
    # Aorta
    asc = sdCapsule(p, (32, 28, -2), (32, 16, -4), 5.0)
    arch = sdCapsule(p, (32, 16, -4), (40, 14, -2), 4.5)
    desc = sdCapsule(p, (40, 14, -2), (42, 24, 2), 4.5)
    aorta = smin(asc, arch, 3.0)
    aorta = smin(aorta, desc, 3.0)
    
    b1 = sdCapsule(p, (32, 15, -3), (28, 6, -3), 1.5)
    b2 = sdCapsule(p, (35, 14, -3), (35, 4, -3), 1.5)
    b3 = sdCapsule(p, (38, 14, -2), (42, 6, -2), 1.5)
    aorta = smin(aorta, b1, 1.0)
    aorta = smin(aorta, b2, 1.0)
    aorta = smin(aorta, b3, 1.0)
    
    # Pulmonary Trunk
    ptr = sdCapsule(p, (28, 30, -7), (34, 20, -5), 4.0)
    pl = sdCapsule(p, (34, 20, -5), (42, 22, -2), 3.0)
    pr = sdCapsule(p, (34, 20, -5), (24, 22, -2), 3.0)
    pulm = smin(ptr, pl, 2.0)
    pulm = smin(pulm, pr, 2.0)
    
    # Vena Cava
    svc = sdCapsule(p, (21, 26, -2), (21, 6, -3), 3.5)
    ivc = sdCapsule(p, (22, 32, -2), (24, 52, -1), 3.5)
    veins = smin(pulm, svc, 1.0)
    veins = smin(veins, ivc, 1.0)
    
    # Fat and Coronary Arteries
    fat_iv = sdCapsule(p, (30, 38, -6.5), (38, 48, -1.5), 1.8)
    fat_av = sdCapsule(p, (24, 32, -4.5), (30, 42, -2.5), 1.8)
    fat = smin(fat_iv, fat_av, 2.0)
    
    ca_iv = sdCapsule(p, (30, 38, -7.0), (38, 48, -2.0), 0.8)
    ca_av = sdCapsule(p, (24, 32, -5.0), (30, 42, -3.0), 0.8)
    ca_branch = sdCapsule(p, (34, 42, -5.0), (28, 46, -4.0), 0.6)
    ca = smin(ca_iv, ca_av, 1.0)
    ca = smin(ca, ca_branch, 1.0)
    
    d_all = smin(muscle, fat, 1.0)
    d_all = smin(d_all, ca, 0.5)
    d_all = smin(d_all, aorta, 1.0)
    d_all = smin(d_all, veins, 1.0)
    
    mat = 1
    min_d = muscle
    if aorta < min_d: min_d = aorta; mat = 2
    if veins < min_d: min_d = veins; mat = 3
    if fat < min_d + 0.5: min_d = fat; mat = 4
    if ca < min_d + 0.5: min_d = ca; mat = 5
    
    return d_all, mat

def calc_normal(p):
    eps = 0.01
    dx = map_world((p[0]+eps, p[1], p[2]))[0] - map_world((p[0]-eps, p[1], p[2]))[0]
    dy = map_world((p[0], p[1]+eps, p[2]))[0] - map_world((p[0], p[1]-eps, p[2]))[0]
    dz = map_world((p[0], p[1], p[2]+eps))[0] - map_world((p[0], p[1], p[2]-eps))[0]
    l = length3(dx, dy, dz)
    if l == 0: return (0,0,1)
    return (dx/l, dy/l, dz/l)

def render():
    c = new_canvas(64, 64)
    light_dir = (-0.5, -0.6, -1.0)
    ll = length3(*light_dir)
    light_dir = (light_dir[0]/ll, light_dir[1]/ll, light_dir[2]/ll)
    
    pal_muscle = [(40,15,20), (75,20,30), (115,30,40), (160,40,50), (200,55,65), (230,80,90)]
    pal_aorta = [(80,20,25), (130,30,35), (180,45,50), (230,65,70), (250,95,100)]
    pal_veins = [(25,35,60), (45,65,100), (65,95,140), (95,135,190), (130,180,230)]
    pal_fat = [(140,120,50), (180,160,70), (220,200,100), (250,240,140)]
    pal_coronary = [(120,20,20), (180,40,30), (240,70,50), (255,110,80)]
    
    for y in range(64):
        for x in range(64):
            ro = (x, y, -50)
            rd = (0, 0, 1)
            
            t = 0
            hit = False
            mat = 0
            for i in range(80):
                p = (ro[0], ro[1], ro[2] + t)
                d, m = map_world(p)
                if d < 0.1:
                    hit = True
                    mat = m
                    break
                t += d * 0.8
                if t > 100:
                    break
                    
            if hit:
                p = (ro[0], ro[1], ro[2] + t)
                n = calc_normal(p)
                diff = n[0]*light_dir[0] + n[1]*light_dir[1] + n[2]*light_dir[2]
                diff = max(0.0, diff)
                amb = 0.2 + 0.1 * n[1] 
                
                rim = max(0.0, n[0]*0.8 + n[2]*0.6)
                rim = math.pow(rim, 4.0) * 0.3
                
                I = (-light_dir[0], -light_dir[1], -light_dir[2])
                dotIN = I[0]*n[0] + I[1]*n[1] + I[2]*n[2]
                rx = I[0] - 2*dotIN*n[0]
                ry = I[1] - 2*dotIN*n[1]
                rz = I[2] - 2*dotIN*n[2]
                spec = rx*0 + ry*0 + rz*(-1)
                spec = max(0.0, spec)
                spec = math.pow(spec, 8.0) * 0.6
                
                light = diff * 0.6 + amb + spec * 0.8 + rim
                
                if mat == 1: pal = pal_muscle
                elif mat == 2: pal = pal_aorta
                elif mat == 3: pal = pal_veins
                elif mat == 4: pal = pal_fat
                elif mat == 5: pal = pal_coronary
                else: pal = [(255,0,255)]
                
                idx = int(light * len(pal))
                idx = max(0, min(len(pal)-1, idx))
                
                c.set(x, y, pal[idx])
                
    c.outline((25, 10, 15))
    return c

c = render()
finish(c)
