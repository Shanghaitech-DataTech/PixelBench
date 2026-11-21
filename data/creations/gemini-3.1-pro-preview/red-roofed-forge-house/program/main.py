import pixelbench_api as api

c = api.new_canvas(128, 128)
c.rect(0, 0, 128, 128, '#7c9554')

def iso(x, y, z, ox=64, oy=25):
    return (int(ox + (x - y) * 2), int(oy + (x + y) - z))

bx, by, bz = 16, 16, 0
bw, bl, bh = 18, 18, 16

# Ground shadow
shadow_pts = [
    iso(bx-2, by-2, bz),
    iso(bx+bw+8, by-2, bz),
    iso(bx+bw+8, by+bl+10, bz),
    iso(bx-2, by+bl+10, bz)
]
c.poly(shadow_pts, '#6a8246')

# Left wall (faces -y) -> Light
c.poly([iso(bx, by+bl, bz), iso(bx+bw, by+bl, bz), iso(bx+bw, by+bl, bz+bh), iso(bx, by+bl, bz+bh)], '#8c9ea8')
# Right wall (faces +x) -> Dark
c.poly([iso(bx+bw, by, bz), iso(bx+bw, by+bl, bz), iso(bx+bw, by+bl, bz+bh), iso(bx+bw, by, bz+bh)], '#5a6975')

# Wooden beams on left wall
c.poly([iso(bx, by+bl, bz), iso(bx+bw, by+bl, bz), iso(bx+bw, by+bl, bz+1), iso(bx, by+bl, bz+1)], '#5c4026')
c.poly([iso(bx, by+bl, bz+bh-1), iso(bx+bw, by+bl, bz+bh-1), iso(bx+bw, by+bl, bz+bh), iso(bx, by+bl, bz+bh)], '#5c4026')
c.poly([iso(bx, by+bl, bz), iso(bx+1, by+bl, bz), iso(bx+1, by+bl, bz+bh), iso(bx, by+bl, bz+bh)], '#5c4026')
c.poly([iso(bx+bw-1, by+bl, bz), iso(bx+bw, by+bl, bz), iso(bx+bw, by+bl, bz+bh), iso(bx+bw-1, by+bl, bz+bh)], '#5c4026')
c.line(*iso(bx, by+bl, bz), *iso(bx+bw, by+bl, bz+bh), '#5c4026')

# Wooden beams on right wall
c.poly([iso(bx+bw, by, bz), iso(bx+bw, by+bl, bz), iso(bx+bw, by+bl, bz+1), iso(bx+bw, by, bz+1)], '#402b12')
c.poly([iso(bx+bw, by, bz+bh-1), iso(bx+bw, by+bl, bz+bh-1), iso(bx+bw, by+bl, bz+bh), iso(bx+bw, by, bz+bh)], '#402b12')
c.poly([iso(bx+bw, by, bz), iso(bx+bw, by+1, bz), iso(bx+bw, by+1, bz+bh), iso(bx+bw, by, bz+bh)], '#402b12')
c.poly([iso(bx+bw, by+bl-1, bz), iso(bx+bw, by+bl, bz), iso(bx+bw, by+bl, bz+bh), iso(bx+bw, by+bl-1, bz+bh)], '#402b12')
c.line(*iso(bx+bw, by, bz), *iso(bx+bw, by+bl, bz+bh), '#402b12')

# Door on right wall
door_y = by + 6
door_w = 6
door_h = 10
c.poly([iso(bx+bw, door_y, bz), iso(bx+bw, door_y+door_w, bz), iso(bx+bw, door_y+door_w, bz+door_h), iso(bx+bw, door_y, bz+door_h)], '#2e1e0a')
c.poly([iso(bx+bw, door_y+1, bz), iso(bx+bw, door_y+door_w-1, bz), iso(bx+bw, door_y+door_w-1, bz+door_h-1), iso(bx+bw, door_y+1, bz+door_h-1)], '#402b12')
c.set(*iso(bx+bw, door_y+door_w-2, bz+door_h/2), '#1a1005')

# Furnace on left wall
fx, fy, fz = bx + 4, by + bl, 0
fw, fl, fh = 10, 6, 10

# Front wall of furnace (y = fy + fl) faces -y (Light)
c.poly([iso(fx, fy+fl, fz), iso(fx+fw, fy+fl, fz), iso(fx+fw, fy+fl, fz+fh), iso(fx, fy+fl, fz+fh)], '#8c9ea8')
# Right wall of furnace (x = fx + fw) faces +x (Dark)
c.poly([iso(fx+fw, fy, fz), iso(fx+fw, fy+fl, fz), iso(fx+fw, fy+fl, fz+fh), iso(fx+fw, fy, fz+fh)], '#5a6975')

# Furnace top slope faces -y, +z (Light)
c.poly([iso(fx, fy, fz+fh+4), iso(fx+fw, fy, fz+fh+4), iso(fx+fw, fy+fl, fz+fh), iso(fx, fy+fl, fz+fh)], '#d95763')
for i in range(1, int(fw)):
    tile_x = fx + i
    c.line(*iso(tile_x, fy, fz+fh+4), *iso(tile_x, fy+fl, fz+fh), '#e66e7a')
for i in range(1, int(fl)):
    tile_y = fy + i
    tile_z = fz+fh+4 - (i/fl)*4
    c.line(*iso(fx, tile_y, tile_z), *iso(fx+fw, tile_y, tile_z), '#e66e7a')

# Furnace right side triangle (x = fx + fw) faces +x (Dark)
c.poly([iso(fx+fw, fy, fz+fh), iso(fx+fw, fy+fl, fz+fh), iso(fx+fw, fy, fz+fh+4)], '#b03b46')

# Furnace opening
ox, oy, oz = fx + 2, fy + fl, 0
ow, oh = 6, 6
c.poly([iso(ox, oy, oz), iso(ox+ow, oy, oz), iso(ox+ow, oy, oz+oh), iso(ox, oy, oz+oh)], '#222222')
gx, gy, gz = ox + 1, oy, oz + 1
gw, gh = 4, 4
c.poly([iso(gx, gy, gz), iso(gx+gw, gy, gz), iso(gx+gw, gy, gz+gh), iso(gx, gy, gz+gh)], '#df7126')
c.poly([iso(gx+1, gy, gz+1), iso(gx+gw-1, gy, gz+1), iso(gx+gw-1, gy, gz+gh-1), iso(gx+1, gy, gz+gh-1)], '#fbf236')

# Gable wall
c.poly([iso(bx, by+bl, bz+bh), iso(bx+bw, by+bl, bz+bh), iso(bx+bw/2, by+bl, bz+bh+10)], '#8c9ea8')
c.line(*iso(bx, by+bl, bz+bh), *iso(bx+bw/2, by+bl, bz+bh+10), '#5c4026')
c.line(*iso(bx+bw, by+bl, bz+bh), *iso(bx+bw/2, by+bl, bz+bh+10), '#5c4026')

# Roof
rx, ry = bx - 2, by - 2
rw, rl = bw + 4, bl + 4
rz = bz + bh
ridge_x = rx + rw/2
ridge_z = rz + 12

# Left slope (Light)
l1 = iso(rx, ry, rz)
l2 = iso(ridge_x, ry, ridge_z)
l3 = iso(ridge_x, ry+rl, ridge_z)
l4 = iso(rx, ry+rl, rz)
c.poly([l1, l2, l3, l4], '#d95763')

# Roof tiles left (Light side)
for i in range(1, int(rw/2)):
    tile_x = rx + i
    tile_z = rz + (i / (rw/2)) * (ridge_z - rz)
    c.line(*iso(tile_x, ry, tile_z), *iso(tile_x, ry+rl, tile_z), '#e66e7a')
for i in range(1, int(rl)):
    tile_y = ry + i
    c.line(*iso(rx, tile_y, rz), *iso(ridge_x, tile_y, ridge_z), '#e66e7a')

# Left slope thickness (faces -x)
lt1 = iso(rx, ry, rz)
lt2 = iso(rx, ry+rl, rz)
lt3 = iso(rx, ry+rl, rz-1)
lt4 = iso(rx, ry, rz-1)
c.poly([lt1, lt2, lt3, lt4], '#ac3232')

# Right slope (Dark)
p1 = iso(ridge_x, ry, ridge_z)
p2 = iso(rx+rw, ry, rz)
p3 = iso(rx+rw, ry+rl, rz)
p4 = iso(ridge_x, ry+rl, ridge_z)
c.poly([p1, p2, p3, p4], '#b03b46')

# Roof tiles right (Dark side)
for i in range(1, int(rw/2)):
    tile_x = ridge_x + i
    tile_z = ridge_z - (i / (rw/2)) * (ridge_z - rz)
    c.line(*iso(tile_x, ry, tile_z), *iso(tile_x, ry+rl, tile_z), '#8a2b36')
for i in range(1, int(rl)):
    tile_y = ry + i
    c.line(*iso(ridge_x, tile_y, ridge_z), *iso(rx+rw, tile_y, rz), '#8a2b36')

# Right slope thickness (faces +x)
t1 = iso(rx+rw, ry, rz)
t2 = iso(rx+rw, ry+rl, rz)
t3 = iso(rx+rw, ry+rl, rz-1)
t4 = iso(rx+rw, ry, rz-1)
c.poly([t1, t2, t3, t4], '#7a2020')

# Gable edge thickness (Front, faces -y)
g1 = iso(rx, ry+rl, rz)
g2 = iso(ridge_x, ry+rl, ridge_z)
g3 = iso(ridge_x, ry+rl, ridge_z-1)
g4 = iso(rx, ry+rl, rz-1)
c.poly([g1, g2, g3, g4], '#e66e7a')

g5 = iso(ridge_x, ry+rl, ridge_z)
g6 = iso(rx+rw, ry+rl, rz)
g7 = iso(rx+rw, ry+rl, rz-1)
g8 = iso(ridge_x, ry+rl, ridge_z-1)
c.poly([g5, g6, g7, g8], '#ac3232')

# Chimney
cx, cy = bx + 10, by + 4
cw, cl, ch = 4, 4, 8
cz_top = ridge_z + 6

def roof_z(x):
    if x < ridge_x:
        return rz + (x - rx) * (ridge_z - rz) / (rw/2)
    else:
        return ridge_z - (x - ridge_x) * (ridge_z - rz) / (rw/2)

# Left wall (faces -y) -> Light
c.poly([iso(cx, cy+cl, roof_z(cx)), iso(cx+cw, cy+cl, roof_z(cx+cw)), iso(cx+cw, cy+cl, cz_top), iso(cx, cy+cl, cz_top)], '#8c9ea8')
# Right wall (faces +x) -> Dark
c.poly([iso(cx+cw, cy, roof_z(cx+cw)), iso(cx+cw, cy+cl, roof_z(cx+cw)), iso(cx+cw, cy+cl, cz_top), iso(cx+cw, cy, cz_top)], '#5a6975')
# Top
c.poly([iso(cx, cy, cz_top), iso(cx+cw, cy, cz_top), iso(cx+cw, cy+cl, cz_top), iso(cx, cy+cl, cz_top)], '#3a444c')
# Hole
c.poly([iso(cx+1, cy+1, cz_top), iso(cx+cw-1, cy+1, cz_top), iso(cx+cw-1, cy+cl-1, cz_top), iso(cx+1, cy+cl-1, cz_top)], '#111111')

# Sign
sx, sy, sz = bx + bw + 6, by + 12, 0
c.poly([iso(sx, sy, sz), iso(sx+1, sy, sz), iso(sx+1, sy, sz+8), iso(sx, sy, sz+8)], '#664b1f')
c.poly([iso(sx+1, sy, sz), iso(sx+1, sy-1, sz), iso(sx+1, sy-1, sz+8), iso(sx+1, sy, sz+8)], '#402b12')
board_x = sx - 1
board_w = 5
board_h = 4
board_z = sz + 5
c.poly([iso(board_x, sy, board_z), iso(board_x+board_w, sy, board_z), iso(board_x+board_w, sy, board_z+board_h), iso(board_x, sy, board_z+board_h)], '#a38247')
c.poly([iso(board_x, sy, board_z), iso(board_x+board_w, sy, board_z), iso(board_x+board_w, sy, board_z+board_h), iso(board_x, sy, board_z+board_h)], '#402b12', fill=False)
c.set(*iso(board_x+2, sy, board_z+2), '#222222')
c.set(*iso(board_x+3, sy, board_z+2), '#222222')
c.set(*iso(board_x+2, sy, board_z+1), '#222222')

def draw_barrel(c, x, y, z, r=2.5, h=6):
    cx, cy = iso(x, y, z+h)
    bx, by = iso(x, y, z)
    rx = int(r * 2)
    ry = int(r)
    c.ellipse(bx, by, rx, ry, '#402b12')
    c.rect(bx - rx, cy, rx * 2 + 1, by - cy, '#664b1f')
    c.ellipse(bx, by - int(h*0.3), rx, ry, '#222222', fill=False)
    c.ellipse(bx, by - int(h*0.7), rx, ry, '#222222', fill=False)
    c.ellipse(cx, cy, rx, ry, '#8a6f30')
    c.line(cx - rx + 1, cy, cx + rx - 1, cy, '#664b1f')

draw_barrel(c, bx+2, by+bl+8, 0)
draw_barrel(c, bx+6, by+bl+10, 0)
draw_barrel(c, bx+4, by+bl+9, 6)

api.finish(c)
