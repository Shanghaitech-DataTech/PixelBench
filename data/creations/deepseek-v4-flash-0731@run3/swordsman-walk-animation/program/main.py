from pixelbench_api import new_canvas, finish

INK=(30,28,36)
HAIR=(206,62,60)
HAIR_D=(152,42,46)
SKIN=(240,196,164)
SKIN_D=(212,162,120)
EYE=(24,24,36)
ARMOR=(128,144,160)
ARMOR_D=(94,110,128)
BELT=(84,56,40)
BOOT=(52,36,28)
BOOT_H=(74,52,42)
CAPE=(24,52,88)
CAPE_D=(12,34,62)
CAPE_H=(58,104,156)
PANTS=(104,72,52)
BLADE=(198,210,222)
BLADE_L=(232,238,244)
GUARD=(200,158,40)
GRIP=(100,64,40)

def draw_frame(c, dx, dy, pose):
    if pose == 0:
        cape = [(12,15),(8,15),(5,16),(3,20),(3,24),(5,28),(9,28),(11,24),(11,18)]
        hl = [(5,19),(4,23),(6,27)]
        bl_rect=(11,24,3,4); bb_rect=(9,27,4,3)
        fl_rect=(15,24,3,4); fb_rect=(16,27,5,3)
        arm_rect=(16,15,2,2); arm2=(17,16,2,2); hand=(19,17,2,2)
        blade=(20,5,2,11); tip=(20,4); bhl=(21,6,1,9)
        guard=(19,16,3,1); grip=(18,17,1,2)
    else:
        cape = [(12,15),(9,16),(6,18),(4,22),(5,26),(9,28),(12,25),(12,19)]
        hl = [(6,19),(5,23),(7,26)]
        bl_rect=(12,24,3,4); bb_rect=(13,27,4,3)
        fl_rect=(14,24,3,4); fb_rect=(14,27,4,3)
        arm_rect=(17,15,2,2); arm2=(18,16,2,2); hand=(20,18,2,2)
        blade=(21,7,2,10); tip=(21,6); bhl=(22,8,1,8)
        guard=(20,17,3,1); grip=(19,18,1,2)

    # cape (behind everything)
    c.poly([(x+dx,y+dy) for x,y in cape], CAPE)
    for (x,y) in hl:
        c.set(x+dx,y+dy,CAPE_H)
    c.set(3+dx,25+dy, CAPE_D)
    # back arm
    if pose==0:
        c.rect(12+dx,17+dy,2,3,ARMOR_D)
        c.rect(10+dx,19+dy,3,2,ARMOR_D)
        c.rect(9+dx,21+dy,2,2,SKIN)
    else:
        c.rect(13+dx,17+dy,2,3,ARMOR_D)
        c.rect(12+dx,20+dy,2,2,ARMOR_D)
        c.rect(12+dx,21+dy,2,2,SKIN)
    # legs
    for (x,y,w,h) in (bl_rect, fl_rect):
        c.rect(x+dx,y+dy,w,h,PANTS)
    for (x,y,w,h) in (bb_rect, fb_rect):
        c.rect(x+dx,y+dy,w,h,BOOT)
        c.rect(x+dx,y+dy,w,1,BOOT_H)
    # torso
    c.rect(11+dx,14+dy,10,10,INK)
    c.rect(12+dx,15+dy,8,10,ARMOR)
    c.rect(12+dx,23+dy,8,2,BELT)
    c.rect(15+dx,23+dy,2,1,GUARD)
    c.rect(12+dx,16+dy,1,7,ARMOR_D)
    # head
    c.rect(11+dx,7+dy,10,8,INK)
    c.rect(12+dx,8+dy,8,7,SKIN)
    c.rect(11+dx,6+dy,10,5,HAIR)
    for sx in (13,15,18):
        c.set(sx+dx,5+dy,HAIR)
    c.rect(13+dx,10+dy,6,1,HAIR_D)
    c.set(17+dx,11+dy,EYE)
    c.set(12+dx,12+dy,SKIN_D)
    # front arm
    c.rect(arm_rect[0]+dx, arm_rect[1]+dy, arm_rect[2], arm_rect[3], ARMOR_D)
    c.rect(arm2[0]+dx, arm2[1]+dy, arm2[2], arm2[3], ARMOR_D)
    # sword
    c.rect(blade[0]+dx, blade[1]+dy, blade[2], blade[3], BLADE)
    c.set(tip[0]+dx, tip[1]+dy, BLADE_L)
    c.rect(bhl[0]+dx, bhl[1]+dy, bhl[2], bhl[3], BLADE_L)
    c.rect(guard[0]+dx, guard[1]+dy, guard[2], guard[3], GUARD)
    c.rect(grip[0]+dx, grip[1]+dy, grip[2], grip[3], GRIP)
    c.rect(hand[0]+dx, hand[1]+dy, hand[2], hand[3], SKIN)

canvas = new_canvas(64, 32)
draw_frame(canvas, 0, 0, 0)
draw_frame(canvas, 32, 0, 1)
print(canvas.stats_text())
print(canvas.matrix_text(indices=False))
finish(canvas)
