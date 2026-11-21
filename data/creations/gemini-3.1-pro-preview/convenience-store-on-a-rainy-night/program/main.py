import pixelbench_api as api
from pixelbench_api import new_canvas, flatten, finish

def main():
    c = new_canvas(64, 64)
    
    # 1. Background
    c.rect(0, 0, 64, 25, '#1a1c29')
    c.rect(0, 0, 64, 8, '#13151f') # darker sky top
    
    c.rect(0, 10, 15, 15, '#232635')
    c.rect(12, 15, 10, 10, '#232635')
    c.rect(45, 8, 20, 17, '#232635')
    
    # distant lit windows
    c.rect(4, 12, 1, 2, '#aaaa55')
    c.rect(8, 16, 1, 2, '#aaaa55')
    c.rect(50, 12, 1, 2, '#aaaa55')
    c.rect(55, 15, 1, 2, '#aaaa55')
    c.rect(58, 10, 1, 2, '#aaaa55')
    
    # 2. Street and Sidewalk
    c.rect(0, 48, 64, 8, '#3b3e4f')
    c.rect(0, 56, 64, 8, '#2a2d3b')
    
    # 3. Store Interior Base
    store_x, store_y, store_w, store_h = 8, 15, 52, 33
    c.rect(store_x+2, store_y+7, store_w-4, store_h-7, '#ffffe6') # wall
    c.rect(10, 42, 48, 6, '#d0d0c0') # floor
    
    # Ceiling lights
    c.rect(12, 22, 6, 2, '#ffffff')
    c.rect(24, 22, 6, 2, '#ffffff')
    c.rect(36, 22, 6, 2, '#ffffff')
    c.rect(48, 22, 6, 2, '#ffffff')

    # 4. Shelves and Fridge
    for sy in range(26, 42, 4):
        c.rect(12, sy, 10, 1, '#d2b48c')
        c.rect(13, sy-2, 2, 2, '#ff4444')
        c.rect(16, sy-3, 2, 3, '#4444ff')
        c.rect(19, sy-2, 2, 2, '#44ff44')
        
    c.rect(24, 26, 14, 16, '#dddddd')
    c.rect(25, 27, 12, 14, '#aaddff')
    for fy in range(30, 40, 3):
        c.rect(25, fy, 12, 1, '#ffffff')
        c.rect(26, fy-2, 2, 2, '#ff0000')
        c.rect(29, fy-2, 2, 2, '#00ff00')
        c.rect(32, fy-2, 2, 2, '#0000ff')
        c.rect(35, fy-2, 1, 2, '#ffaa00')

    # Clerk
    c.rect(48, 28, 6, 9, '#3366cc')
    c.rect(49, 25, 4, 3, '#ffccaa')
    c.rect(49, 24, 4, 1, '#222222')

    # 5. Counter
    c.rect(40, 36, 16, 12, '#e0e0e0')
    c.rect(40, 36, 16, 2, '#ffffff')
    c.rect(42, 32, 6, 4, '#888888')
    c.rect(43, 33, 4, 2, '#aaaaaa')

    # 6. Exterior Base
    c.rect(store_x, store_y+7, 2, store_h-7, '#dddddd')
    c.rect(store_x+store_w-2, store_y+7, 2, store_h-7, '#dddddd')
    
    c.rect(store_x, store_y, store_w, 2, '#00aa55')
    c.rect(store_x, store_y+2, store_w, 3, '#ffffff')
    c.rect(store_x, store_y+5, store_w, 2, '#0055aa')
    
    c.rect(10, 22, 48, 1, '#555555') # shadow under signboard
    
    c.rect(40, 15, 19, 7, '#ffffff')
    c.text(41, 15, "24H", '#ff0000', font="5x7")

    # 7. Window Frames
    c.rect(10, 22, 1, 26, '#cccccc')
    c.rect(57, 22, 1, 26, '#cccccc')
    c.rect(10, 34, 48, 1, '#cccccc')
    
    # Doors
    c.rect(20, 22, 1, 26, '#dddddd')
    c.rect(27, 22, 1, 26, '#dddddd')
    c.rect(20, 34, 8, 1, '#dddddd') # slid left door horizontal bar
    
    c.rect(33, 22, 1, 26, '#cccccc')
    c.rect(40, 22, 1, 26, '#cccccc')
    c.rect(33, 34, 8, 1, '#cccccc') # right door horizontal bar
    
    c.rect(26, 35, 1, 4, '#999999')
    c.rect(34, 35, 1, 4, '#999999')

    # 8. Person Entering
    px, py = 27, 30
    c.rect(px+2, py, 4, 4, '#ee3333')
    c.rect(px+1, py+4, 6, 10, '#ee3333')
    c.rect(px+4, py+2, 2, 2, '#ffccaa')
    c.rect(px+2, py+14, 2, 4, '#222222')
    c.rect(px+4, py+14, 2, 4, '#222222')
    c.rect(px+1, py+17, 2, 1, '#aa4400')
    c.rect(px+5, py+17, 2, 1, '#aa4400')

    # 9. Light spill
    c.rect(10, 48, 48, 6, '#fffacd')
    c.dither(10, 54, 48, 2, ['#fffacd', '#3b3e4f'])

    # 10. Umbrella Rack
    rx, ry = 14, 44
    c.rect(rx, ry, 6, 8, '#666666', fill=False)
    c.line(rx+1, ry-4, rx+3, ry+5, '#33cc33')
    c.line(rx+4, ry-2, rx+2, ry+5, '#3333ff')
    c.rect(rx, ry+6, 6, 2, '#555555')

    # 11. Bicycle
    bx, by = 46, 42
    c.circle(bx+3, by+8, 3, '#555555', fill=False)
    c.circle(bx+11, by+8, 3, '#555555', fill=False)
    c.line(bx+3, by+8, bx+7, by+4, '#888888')
    c.line(bx+7, by+4, bx+11, by+8, '#888888')
    c.line(bx+5, by+8, bx+9, by+2, '#888888')
    c.line(bx+7, by+4, bx+5, by+8, '#888888')
    c.rect(bx+4, by+2, 3, 1, '#333333')
    c.line(bx+9, by+2, bx+9, by-1, '#888888')
    c.rect(bx+8, by-1, 3, 1, '#333333')

    # 12. Puddles & Reflections
    c.rect(15, 57, 10, 3, '#3b4359')
    c.rect(17, 58, 6, 1, '#fffacd')
    
    c.rect(35, 59, 15, 4, '#3b4359')
    c.rect(37, 60, 10, 2, '#fffacd')
    c.rect(38, 61, 8, 1, '#00aa55')
    
    c.rect(5, 56, 6, 2, '#3b4359')

    # 13. Rain Layer
    rain_c = new_canvas(64, 64)
    rain_c.line(12, 25, 20, 48, '#ffffff44')
    rain_c.line(16, 25, 24, 48, '#ffffff44')
    rain_c.line(42, 25, 50, 48, '#ffffff44')
    rain_c.line(46, 25, 54, 48, '#ffffff44')
    rain_c.line(50, 25, 58, 48, '#ffffff44')
    
    for i in range(0, 64, 5):
        for j in range(0, 64, 7):
            rx_pos = (i * 3 + j * 5) % 64
            ry_pos = (i * 7 + j * 11) % 64
            rain_c.line(rx_pos, ry_pos, rx_pos-1, ry_pos+2, '#ffffff44')

    final = flatten([c, rain_c])
    finish(final)

if __name__ == "__main__":
    main()
