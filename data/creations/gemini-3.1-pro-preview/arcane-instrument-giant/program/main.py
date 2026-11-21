import math
import random
from pixelbench_api import new_canvas, finish

def main():
    c = new_canvas(256, 256)

    bg_colors = ['#05050a', '#0a0a14', '#10101a', '#181824']
    stone_colors = ['#111111', '#222222', '#333333', '#444444', '#555555']
    brass_colors = ['#221100', '#442200', '#663300', '#884400', '#aa6600', '#cc8800', '#eeaa00', '#ffcc00', '#ffff66']
    glow_colors = ['#001133', '#003366', '#0066aa', '#00aaff', '#66ccff', '#ccffff', '#ffffff']
    crystal_colors = ['#110022', '#330055', '#550088', '#8800cc', '#bb00ff', '#ee66ff', '#ffffff']

    z_buffer = [[-10000.0 for _ in range(256)] for _ in range(256)]

    def set_pixel(x, y, z, color):
        if 0 <= x < 256 and 0 <= y < 256:
            if z > z_buffer[y][x]:
                z_buffer[y][x] = z
                c.set(x, y, color)

    # Background and Pedestal
    for y in range(256):
        for x in range(256):
            dx = x - 128
            dy = y - 100
            dist = math.sqrt(dx*dx + dy*dy) + random.uniform(-5, 5)
            idx = max(0, min(3, 3 - int(dist / 65)))
            c.set(x, y, bg_colors[idx])
            
            if (20 < x < 40) or (216 < x < 236):
                c.set(x, y, bg_colors[min(3, idx + 1)])
            if x in (20, 40, 216, 236):
                c.set(x, y, bg_colors[max(0, idx - 1)])

    c.poly([(70, 256), (186, 256), (160, 210), (96, 210)], stone_colors[1])
    c.poly([(96, 210), (160, 210), (140, 190), (116, 190)], stone_colors[2])
    
    for _ in range(30):
        rx = random.randint(110, 130)
        ry = random.randint(195, 205)
        c.line(rx, ry, rx + random.randint(5, 10), ry, stone_colors[1])
        
    c.ellipse(128, 190, 45, 14, stone_colors[3])
    c.ellipse(128, 188, 45, 14, stone_colors[4])
    
    c.path("M 70 256 L 96 210 L 116 190", '#000000', fill=False)
    c.path("M 186 256 L 160 210 L 140 190", '#000000', fill=False)
    c.ellipse(128, 190, 45, 14, '#000000', fill=False)
    c.ellipse(128, 188, 45, 14, '#000000', fill=False)
    
    c.ellipse(128, 188, 25, 6, '#050505')

    # Aura
    cx, cy = 128, 110
    for i in range(60, 0, -2):
        idx = int((1 - i/60) * 4)
        idx = max(0, min(3, idx))
        r = i + random.randint(-1, 1)
        c.circle(cx, cy, r, glow_colors[idx])

    # 3D Functions
    def draw_flat_ring(cx, cy, cz, inner_r, outer_r, thickness, rot_x, rot_y, rot_z, has_runes=False):
        cx_rot = math.cos(rot_x); sx_rot = math.sin(rot_x)
        cy_rot = math.cos(rot_y); sy_rot = math.sin(rot_y)
        cz_rot = math.cos(rot_z); sz_rot = math.sin(rot_z)
        
        def rotate(x, y, z):
            x1, y1, z1 = x, y * cx_rot - z * sx_rot, y * sx_rot + z * cx_rot
            x2, y2, z2 = x1 * cy_rot + z1 * sy_rot, y1, -x1 * sy_rot + z1 * cy_rot
            x3, y3, z3 = x2 * cz_rot - y2 * sz_rot, x2 * sz_rot + y2 * cz_rot, z2
            return x3, y3, z3

        for r_step in range(inner_r, outer_r + 1):
            num_t = max(1, int(r_step * 10))
            for t_step in range(num_t):
                theta = t_step * 2 * math.pi / num_t
                x0 = r_step * math.cos(theta)
                y0 = r_step * math.sin(theta)
                
                for z0 in [-thickness/2, thickness/2]:
                    px, py, pz = rotate(x0, y0, z0)
                    nx, ny, nz = rotate(0, 0, 1 if z0 > 0 else -1)
                    
                    lx, ly, lz = 0.577, -0.577, 0.577
                    dot = nx*lx + ny*ly + nz*lz
                    
                    if abs(nz) < 0.15:
                        color = '#000000'
                    else:
                        color_idx = int((dot + 1) / 2 * len(brass_colors))
                        color_idx = max(0, min(len(brass_colors)-1, color_idx))
                        color = brass_colors[color_idx]
                        
                    if has_runes and z0 > 0 and r_step > inner_r + 1 and r_step < outer_r - 1:
                        if math.sin(theta * 24) > 0.7:
                            color = glow_colors[4]
                            
                    set_pixel(int(cx + px), int(cy + py), cz + pz, color)
                    
        for r_edge in [inner_r, outer_r]:
            if r_edge == 0: continue
            num_t = max(1, int(r_edge * 10))
            for t_step in range(num_t):
                theta = t_step * 2 * math.pi / num_t
                x0 = r_edge * math.cos(theta)
                y0 = r_edge * math.sin(theta)
                for z0_step in range(int(thickness) + 1):
                    z0 = -thickness/2 + z0_step
                    px, py, pz = rotate(x0, y0, z0)
                    nx, ny, nz = rotate(math.cos(theta) * (1 if r_edge == outer_r else -1), 
                                        math.sin(theta) * (1 if r_edge == outer_r else -1), 0)
                    
                    lx, ly, lz = 0.577, -0.577, 0.577
                    dot = nx*lx + ny*ly + nz*lz
                    
                    if abs(nz) < 0.2:
                        color = '#000000'
                    else:
                        color_idx = int((dot + 1) / 2 * len(brass_colors))
                        color_idx = max(0, min(len(brass_colors)-1, color_idx))
                        color = brass_colors[color_idx]
                        
                    set_pixel(int(cx + px), int(cy + py), cz + pz, color)

    def draw_torus(cx, cy, cz, radius, tube_r, rot_x, rot_y, rot_z, is_gear=False, has_runes=False):
        cx_rot = math.cos(rot_x); sx_rot = math.sin(rot_x)
        cy_rot = math.cos(rot_y); sy_rot = math.sin(rot_y)
        cz_rot = math.cos(rot_z); sz_rot = math.sin(rot_z)
        
        def rotate(x, y, z):
            x1, y1, z1 = x, y * cx_rot - z * sx_rot, y * sx_rot + z * cx_rot
            x2, y2, z2 = x1 * cy_rot + z1 * sy_rot, y1, -x1 * sy_rot + z1 * cy_rot
            x3, y3, z3 = x2 * cz_rot - y2 * sz_rot, x2 * sz_rot + y2 * cz_rot, z2
            return x3, y3, z3

        num_u = int(radius * 10)
        num_v = int(tube_r * 10)
        
        for i in range(num_u):
            u = i * 2 * math.pi / num_u
            cu = math.cos(u)
            su = math.sin(u)
            
            r_eff = radius
            if is_gear:
                teeth = int(radius / 2)
                wave = math.sin(u * teeth)
                if wave > 0.5:
                    r_eff += tube_r * 1.5
                elif wave > 0:
                    r_eff += tube_r * 1.5 * (wave / 0.5)
                    
            for j in range(num_v):
                v = j * 2 * math.pi / num_v
                cv = math.cos(v)
                sv = math.sin(v)
                
                tx = tube_r * cv * cu
                ty = tube_r * cv * su
                tz = tube_r * sv
                
                px, py, pz = rotate(r_eff*cu + tx, r_eff*su + ty, tz)
                nx, ny, nz = rotate(cv*cu, cv*su, sv)
                
                lx, ly, lz = 0.577, -0.577, 0.577
                dot = nx*lx + ny*ly + nz*lz
                
                if abs(nz) < 0.25:
                    color = '#000000'
                else:
                    color_idx = int((dot + 1) / 2 * len(brass_colors))
                    color_idx = max(0, min(len(brass_colors)-1, color_idx))
                    color = brass_colors[color_idx]
                    
                if has_runes and sv > 0.5 and math.sin(u * 30) > 0.5 and abs(nz) >= 0.25:
                    color = glow_colors[5]
                    
                set_pixel(int(cx + px), int(cy + py), cz + pz, color)

    def draw_sphere(cx, cy, cz, radius, colors, is_glow=False):
        for dy in range(-radius, radius + 1):
            for dx in range(-radius, radius + 1):
                if dx*dx + dy*dy <= radius*radius:
                    z = math.sqrt(radius*radius - dx*dx - dy*dy)
                    nz = z / radius
                    nx = dx / radius
                    ny = dy / radius
                    
                    if is_glow:
                        dist = math.sqrt(dx*dx + dy*dy)
                        idx = int((1 - dist / radius) * len(colors))
                        idx = max(0, min(len(colors)-1, idx))
                        color = colors[idx]
                        set_pixel(int(cx + dx), int(cy + dy), cz + z, color)
                    else:
                        lx, ly, lz = 0.577, -0.577, 0.577
                        dot = nx*lx + ny*ly + nz*lz
                        
                        if nz < 0.25:
                            color = '#000000'
                        else:
                            idx = int((dot + 1) / 2 * len(colors))
                            idx = max(0, min(len(colors)-1, idx))
                            color = colors[idx]
                            
                        set_pixel(int(cx + dx), int(cy + dy), cz + z, color)

    def draw_dial(cx, cy, cz, radius, rot_x, rot_y, rot_z):
        draw_flat_ring(cx, cy, cz, 0, radius, 2, rot_x, rot_y, rot_z, has_runes=False)
        cx_rot = math.cos(rot_x); sx_rot = math.sin(rot_x)
        cy_rot = math.cos(rot_y); sy_rot = math.sin(rot_y)
        cz_rot = math.cos(rot_z); sz_rot = math.sin(rot_z)
        
        def rotate(x, y, z):
            x1, y1, z1 = x, y * cx_rot - z * sx_rot, y * sx_rot + z * cx_rot
            x2, y2, z2 = x1 * cy_rot + z1 * sy_rot, y1, -x1 * sy_rot + z1 * cy_rot
            x3, y3, z3 = x2 * cz_rot - y2 * sz_rot, x2 * sz_rot + y2 * cz_rot, z2
            return x3, y3, z3
            
        for i in range(-2, int(radius)-2):
            px, py, pz = rotate(0, i, 2)
            set_pixel(int(cx+px), int(cy+py), cz+pz, glow_colors[4])

    # Draw 3D Elements
    draw_flat_ring(128, 110, 0, 85, 95, 4, 0.6, 0.3, 0.1, has_runes=True)
    draw_torus(128, 110, 0, 78, 3, -0.4, 1.1, 0.4, is_gear=True, has_runes=False)
    draw_flat_ring(128, 110, 0, 62, 72, 4, 1.2, -0.5, 0.8, has_runes=True)
    draw_torus(128, 110, 0, 52, 2, 0.2, 0.8, -0.6, is_gear=True, has_runes=False)
    draw_flat_ring(128, 110, 0, 35, 45, 3, -0.8, -0.2, 1.2, has_runes=True)
    
    draw_dial(128 - 60, 110 + 50, 20, 18, 0.5, 0.2, 0.0)
    draw_dial(128 + 50, 110 - 50, -10, 15, -0.3, 0.6, 0.5)
    
    draw_sphere(128, 110, 0, 14, glow_colors[2:], is_glow=True)
    
    draw_sphere(128 + 80, 110 + 15, 40, 8, crystal_colors)
    draw_sphere(128 - 70, 110 - 25, -30, 6, crystal_colors)
    draw_sphere(128 + 10, 110 - 75, 20, 7, crystal_colors)
    draw_sphere(128 - 20, 110 + 85, 10, 5, crystal_colors)
    
    # Floating Runes
    random.seed(42)
    for _ in range(20):
        x = 128 + random.randint(-100, 100)
        y = 110 + random.randint(-100, 100)
        z = random.randint(-60, 60)
        
        set_pixel(x, y, z, glow_colors[6])
        set_pixel(x+1, y, z, glow_colors[5])
        set_pixel(x-1, y, z, glow_colors[5])
        set_pixel(x, y+1, z, glow_colors[5])
        set_pixel(x, y-1, z, glow_colors[5])

    finish(c)

if __name__ == "__main__":
    main()
