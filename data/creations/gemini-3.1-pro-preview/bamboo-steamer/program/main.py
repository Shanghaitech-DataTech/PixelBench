import sys
from pixelbench_api import new_canvas, flatten, finish, view, save

def draw():
    c_back = new_canvas(32, 32, name="back")
    c_dump = new_canvas(32, 32, name="dump")
    c_front = new_canvas(32, 32, name="front")
    c_lid = new_canvas(32, 32, name="lid")
    c_steam = new_canvas(32, 32, name="steam")
    
    # Palette
    palette = {
        'outline': '#4a2e1b',
        'base_dark': '#8c5a35',
        'base_mid': '#c28b5b',
        'base_light': '#e6b781',
        'inside_dark': '#362113',
        'dump_high': '#ffffff',
        'dump_base': '#fff3e0',
        'dump_shadow': '#d4bfa6',
        'steam_base': '#ffffffaa',
        'steam_high': '#ffffffff'
    }
    for c in [c_back, c_dump, c_front, c_lid, c_steam]:
        for k, v in palette.items():
            c.color(v, k)

    # --- BACK ---
    c_back.ellipse(16, 18, 12, 3, 'base_mid')
    c_back.ellipse(16, 18, 10, 2, 'inside_dark')
    c_back.path("M 4 18 A 12 3 0 0 1 28 18", 'outline', fill=False)
    c_back.path("M 6 18 A 10 2 0 0 1 26 18", 'outline', fill=False)

    # --- DUMPLINGS ---
    def draw_dumpling(c, cx, cy):
        # Base fill
        c.line(cx-2, cy, cx+2, cy, 'dump_base')
        c.line(cx-3, cy-1, cx+3, cy-1, 'dump_base')
        c.line(cx-4, cy-2, cx+4, cy-2, 'dump_base')
        c.line(cx-4, cy-3, cx+4, cy-3, 'dump_base')
        c.line(cx-3, cy-4, cx+3, cy-4, 'dump_base')
        c.line(cx-2, cy-5, cx+2, cy-5, 'dump_base')
        c.line(cx-1, cy-6, cx+1, cy-6, 'dump_base')
        
        # Outline
        c.line(cx-2, cy+1, cx+2, cy+1, 'outline')
        c.set(cx-3, cy, 'outline')
        c.set(cx+3, cy, 'outline')
        c.set(cx-4, cy-1, 'outline')
        c.set(cx+4, cy-1, 'outline')
        c.set(cx-5, cy-2, 'outline')
        c.set(cx+5, cy-2, 'outline')
        c.set(cx-5, cy-3, 'outline')
        c.set(cx+5, cy-3, 'outline')
        c.set(cx-4, cy-4, 'outline')
        c.set(cx+4, cy-4, 'outline')
        c.set(cx-3, cy-5, 'outline')
        c.set(cx+3, cy-5, 'outline')
        c.set(cx-2, cy-6, 'outline')
        c.set(cx+2, cy-6, 'outline')
        c.line(cx-1, cy-7, cx+1, cy-7, 'outline')

        # Pleats / Shading
        c.set(cx-2, cy-2, 'dump_shadow')
        c.set(cx+2, cy-2, 'dump_shadow')
        c.set(cx-1, cy-3, 'dump_shadow')
        c.set(cx+1, cy-3, 'dump_shadow')
        c.set(cx, cy-4, 'dump_shadow')
        c.set(cx, cy-5, 'dump_shadow')
        c.set(cx, cy-6, 'dump_shadow')
        
        # Highlight
        c.set(cx-2, cy-3, 'dump_high')
        c.set(cx-1, cy-4, 'dump_high')
        c.set(cx-2, cy-4, 'dump_high')

    draw_dumpling(c_dump, 11, 16)
    draw_dumpling(c_dump, 21, 16)
    draw_dumpling(c_dump, 16, 18)

    # --- FRONT ---
    c_front.rect(4, 18, 25, 8, 'base_mid')
    c_front.rect(4, 18, 4, 8, 'base_dark')
    c_front.rect(24, 18, 4, 8, 'base_light')
    
    c_front.ellipse(16, 26, 12, 3, 'base_mid')
    c_front.path("M 4 26 A 12 3 0 0 0 28 26", 'outline', fill=False)
    
    c_front.line(4, 18, 4, 26, 'outline')
    c_front.line(28, 18, 28, 26, 'outline')
    
    c_front.path("M 4 21 A 12 3 0 0 0 28 21", 'outline', fill=False)
    c_front.path("M 4 24 A 12 3 0 0 0 28 24", 'outline', fill=False)

    c_front.path("M 4 18 A 12 3 0 0 0 28 18 L 26 18 A 10 2 0 0 1 6 18 Z", 'base_light', fill=True)
    c_front.path("M 4 18 A 12 3 0 0 0 28 18", 'outline', fill=False)
    c_front.path("M 6 18 A 10 2 0 0 0 26 18", 'outline', fill=False)

    # --- LID ---
    lx, ly = 19, 10
    c_lid.rect(lx-12, ly-3, 25, 4, 'base_mid')
    c_lid.ellipse(lx, ly, 12, 3, 'base_mid')
    c_lid.ellipse(lx, ly-3, 12, 3, 'base_mid')

    c_lid.rect(lx-12, ly-3, 4, 4, 'base_dark')
    c_lid.rect(lx+8, ly-3, 4, 4, 'base_light')

    c_lid.line(lx-12, ly-3, lx-12, ly, 'outline')
    c_lid.line(lx+12, ly-3, lx+12, ly, 'outline')
    c_lid.path(f"M {lx-12} {ly} A 12 3 0 0 0 {lx+12} {ly}", 'outline', fill=False)
    c_lid.path(f"M {lx-12} {ly-3} A 12 3 0 0 0 {lx+12} {ly-3}", 'outline', fill=False)
    c_lid.path(f"M {lx-12} {ly-3} A 12 3 0 0 1 {lx+12} {ly-3}", 'outline', fill=False)

    # Woven pattern
    c_lid.line(lx-8, ly-3, lx+8, ly-3, 'base_dark')
    c_lid.line(lx-6, ly-4, lx+6, ly-4, 'base_dark')
    c_lid.line(lx-6, ly-2, lx+6, ly-2, 'base_dark')
    c_lid.line(lx-4, ly-4, lx-4, ly-2, 'base_dark')
    c_lid.line(lx, ly-4, lx, ly-2, 'base_dark')
    c_lid.line(lx+4, ly-4, lx+4, ly-2, 'base_dark')
    
    # Highlight
    c_lid.line(lx+2, ly-4, lx+6, ly-4, 'base_light')
    c_lid.line(lx+3, ly-5, lx+5, ly-5, 'base_light')

    # Handle
    c_lid.rect(lx-2, ly-5, 5, 3, 'base_dark')
    c_lid.line(lx-2, ly-5, lx+2, ly-5, 'outline')
    c_lid.line(lx-2, ly-3, lx+2, ly-3, 'outline')
    c_lid.line(lx-2, ly-5, lx-2, ly-3, 'outline')
    c_lid.line(lx+2, ly-5, lx+2, ly-3, 'outline')

    # --- STEAM ---
    def draw_puff(c, x, y, r):
        c.circle(x, y, r, 'steam_base')
        if r > 1:
            c.set(x-1, y-1, 'steam_high')
            c.set(x, y-1, 'steam_high')

    draw_puff(c_steam, 8, 16, 2)
    draw_puff(c_steam, 6, 13, 2)
    draw_puff(c_steam, 9, 10, 3)
    draw_puff(c_steam, 11, 6, 2)
    draw_puff(c_steam, 13, 3, 1)

    draw_puff(c_steam, 28, 14, 1)
    draw_puff(c_steam, 30, 11, 1)

    final = flatten([c_back, c_dump, c_front, c_lid, c_steam])
    finish(final)

if __name__ == "__main__":
    draw()
