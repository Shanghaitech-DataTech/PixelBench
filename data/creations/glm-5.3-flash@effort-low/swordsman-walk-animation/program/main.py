from pixelbench_api import *

SKIN="#f0c8a0"; HAIR="#d84828"; HAIR_D="#a83018"
CAPE="#20386e"; CAPE_D="#16264c"
TUNIC="#8a6a3a"; TUNIC_D="#6a4c28"
PANT="#4a4458"; BOOT="#3a2c1e"
BLADE="#c8d0dc"; BLADE_D="#8890a0"
BELT="#5a3a20"; OUT="#241820"

def frame(phase):
    c = new_canvas(32,32, background=None)
    bob = 0 if phase==0 else 1
    # ---- cape (behind), waving ----
    if phase==0:
        cape = [(13,9),(12,11),(11,14),(11,17),(12,20),(13,23)]
    else:
        cape = [(13,9),(12,11),(11,14),(11,17),(12,20),(14,23)]
    for (x,y) in cape:
        c.rect(x,y,3,2,CAPE)
    c.line(12,10,13,23,CAPE_D)
    # ---- legs ----
    yb = 18+bob
    if phase==0:
        c.line(20,yb,23,yb+4,PANT); c.line(19,yb+1,21,yb+5,PANT)
        c.rect(23,yb+4,3,2,BOOT); c.rect(20,yb+5,3,2,BOOT)
        c.line(17,yb,15,yb+4,PANT); c.line(18,yb,16,yb+5,PANT)
        c.rect(14,yb+4,3,2,BOOT)
    else:
        c.line(19,yb,20,yb+5,PANT); c.line(20,yb,21,yb+5,PANT)
        c.rect(19,yb+5,3,2,BOOT)
        c.line(17,yb,16,yb+4,PANT)
        c.rect(15,yb+4,3,2,BOOT)
    # ---- torso ----
    c.rect(16,10+bob,7,8,TUNIC)
    c.rect(16,10+bob,2,8,TUNIC_D)
    c.rect(16,16+bob,7,2,BELT)
    # ---- head ----
    hy = 3+bob
    c.rect(18,hy,7,8,SKIN)
    c.rect(16,hy,4,8,HAIR)
    c.rect(17,hy-1,8,3,HAIR)
    c.rect(24,hy+1,1,3,HAIR)
    c.rect(16,hy+6,2,3,HAIR_D)
    # ---- arm ----
    ay = 12+bob
    if phase==0:
        c.line(22,ay,25,ay+2,SKIN); hx,hy2 = 25,ay+2
    else:
        c.line(22,ay,25,ay+1,SKIN); hx,hy2 = 25,ay+1
    c.rect(24,ay,2,2,TUNIC)
    # ---- outline everything drawn so far ----
    c.outline(OUT)
    # ---- redraw interior details over the outline ----
    c.set(24,hy+4,OUT)              # eye
    c.rect(16,16+bob,7,2,BELT)      # belt
    # boots
    if phase==0:
        c.rect(23,yb+4,3,2,BOOT); c.rect(20,yb+5,3,2,BOOT); c.rect(14,yb+4,3,2,BOOT)
    else:
        c.rect(19,yb+5,3,2,BOOT); c.rect(15,yb+4,3,2,BOOT)
    # ---- long sword: thick blade so it survives ----
    c.rect(hx-1,hy2,3,2,BELT)                       # hilt+guard
    for i in range(9):                              # blade, 2px wide, angled down
        c.set(hx+1+i//3, hy2+2+i, BLADE)
        c.set(hx+2+i//3, hy2+2+i, BLADE)
    c.set(hx+4,hy2+10,BLADE)                        # tip
    c.set(hx+5,hy2+10,BLADE_D)
    c.set(hx+2,hy2+2,BLADE_D)
    return c

f0 = frame(0); f1 = frame(1)
result = new_canvas(64,32, name="swordsman-walk")
result.blit(f0,0,0); result.blit(f1,32,0)
print(result.stats_text())
finish(result)
