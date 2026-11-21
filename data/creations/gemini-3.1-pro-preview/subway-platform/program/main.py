import pixelbench_api
from pixelbench_api import new_canvas, flatten, finish

def draw_subway():
    # Palette
    C_CEILING = '#202025'
    C_WALL = '#15151a'
    C_FLOOR_BACK = '#303035'
    C_FLOOR_FRONT = '#404048'
    C_YELLOW_LINE = '#d0a010'
    C_TRAIN_BODY = '#e0e0e0'
    C_TRAIN_DARK = '#909090'
    C_TRAIN_WINDOW = '#202530'
    C_TRAIN_STRIPE = '#d03030'
    C_TRAIN_BLUR1 = '#c0c0c0'
    C_TRAIN_BLUR2 = '#a0a0a0'
    C_TRAIN_BLUR3 = '#b04040'
    C_GLASS = '#80c0d060'
    C_PILLAR = '#252525'
    C_PILLAR_HL = '#454545'
    C_SIGN_BG = '#f0f0f0'
    C_SIGN_BORDER = '#202020'
    C_BENCH = '#604030'
    C_BENCH_LEG = '#202020'
    C_PASS1_TOP = '#305080'
    C_PASS1_BOT = '#202020'
    C_PASS2_TOP = '#804030'
    C_PASS2_BOT = '#303040'
    C_PASS3_TOP = '#406040'
    C_PASS3_BOT = '#202020'
    C_SKIN = '#d0a080'
    C_SHADOW = '#10101580'

    bg = new_canvas(64, 64)
    train = new_canvas(64, 64)
    doors = new_canvas(64, 64)
    fg = new_canvas(64, 64)

    # 1. Background
    bg.rect(0, 0, 64, 64, C_WALL)
    bg.rect(0, 42, 64, 22, C_FLOOR_BACK)
    bg.rect(0, 46, 64, 18, C_FLOOR_FRONT)
    bg.rect(0, 44, 64, 2, C_YELLOW_LINE)
    for x in range(0, 64, 8):
        bg.line(x, 46, x, 64, '#35353d')
    for y in range(48, 64, 4):
        bg.line(0, y, 64, y, '#35353d')

    bg.rect(0, 0, 64, 8, C_CEILING)
    bg.rect(0, 8, 64, 2, '#404045')
    for x in range(4, 64, 16):
        bg.rect(x, 2, 8, 2, '#ffffff')
        bg.rect(x, 4, 8, 1, '#ffffff80')

    # 2. Train arriving
    train.rect(0, 12, 52, 28, C_TRAIN_BODY)
    train.poly([(52, 12), (60, 16), (62, 36), (58, 40), (52, 40)], C_TRAIN_BODY)
    train.rect(0, 40, 58, 2, C_TRAIN_DARK)

    train.rect(0, 36, 56, 2, C_TRAIN_STRIPE)
    train.poly([(56, 36), (59, 36), (60, 38), (56, 38)], C_TRAIN_STRIPE)

    train.rect(0, 16, 50, 8, C_TRAIN_WINDOW)
    train.poly([(50, 16), (56, 18), (57, 24), (50, 24)], C_TRAIN_WINDOW)

    for x in [8, 32]:
        train.rect(x, 14, 12, 22, '#c0c0c0')
        train.rect(x+1, 16, 4, 8, C_TRAIN_WINDOW)
        train.rect(x+7, 16, 4, 8, C_TRAIN_WINDOW)
        train.line(x+6, 14, x+6, 35, '#a0a0a0')

    train.line(4, 18, 16, 18, C_TRAIN_BLUR1)
    train.line(20, 19, 32, 19, C_TRAIN_BLUR1)
    train.line(8, 21, 24, 21, C_TRAIN_BLUR2)
    train.line(2, 29, 14, 29, C_TRAIN_BLUR3)
    train.line(24, 28, 36, 28, C_TRAIN_BLUR3)
    train.line(10, 32, 26, 32, C_TRAIN_BLUR1)
    train.line(6, 28, 18, 28, C_TRAIN_BLUR1)
    train.line(30, 29, 42, 29, C_TRAIN_BLUR2)
    
    train.line(62, 20, 64, 20, C_TRAIN_BLUR1)
    train.line(60, 32, 64, 32, C_TRAIN_BLUR1)

    # 3. Platform Screen Doors
    doors.rect(0, 12, 64, 28, C_GLASS)
    for x in [12, 32, 52]:
        doors.rect(x-1, 12, 2, 28, '#404040')
    doors.line(4, 14, 14, 34, '#ffffff30')
    doors.line(8, 14, 18, 34, '#ffffff30')
    doors.line(24, 14, 34, 34, '#ffffff30')
    doors.line(44, 14, 54, 34, '#ffffff30')

    for x in [0, 20, 40, 60]:
        doors.rect(x, 8, 4, 34, C_PILLAR)
        doors.line(x+1, 8, x+1, 41, C_PILLAR_HL)
        doors.rect(x, 8, 20, 4, C_PILLAR)
        doors.line(x, 11, x+20, 11, C_PILLAR_HL)
        doors.rect(x-1, 40, 6, 2, C_PILLAR_HL)

    # 4. Foreground
    fg.rect(14, 0, 1, 3, '#101010')
    fg.rect(25, 0, 1, 3, '#101010')
    fg.rect(44, 0, 1, 3, '#101010')
    fg.rect(51, 0, 1, 3, '#101010')

    fg.rect(12, 3, 16, 6, C_SIGN_BORDER)
    fg.rect(13, 4, 14, 4, C_SIGN_BG)
    fg.rect(14, 5, 4, 2, '#000000')
    fg.rect(19, 5, 6, 1, '#000000')

    fg.rect(42, 3, 12, 5, C_SIGN_BORDER)
    fg.rect(43, 4, 10, 3, '#2020a0')
    fg.rect(44, 5, 8, 1, '#ffffff')

    fg.rect(8, 57, 16, 2, C_SHADOW)
    fg.rect(8, 52, 16, 2, C_BENCH) 
    fg.rect(8, 49, 16, 2, C_BENCH) 
    fg.rect(10, 54, 2, 3, C_BENCH_LEG)
    fg.rect(20, 54, 2, 3, C_BENCH_LEG)
    fg.rect(9, 50, 1, 2, C_BENCH_LEG)
    fg.rect(22, 50, 1, 2, C_BENCH_LEG)

    # Pass 1: Sitting
    fg.rect(12, 45, 5, 6, C_PASS1_TOP) 
    fg.rect(13, 42, 3, 3, C_SKIN) 
    fg.rect(13, 41, 3, 1, '#000000') 
    fg.rect(13, 42, 1, 2, '#000000') 
    fg.rect(12, 50, 6, 2, C_PASS1_BOT) 
    fg.rect(16, 52, 2, 6, C_PASS1_BOT) 
    fg.rect(14, 47, 3, 3, C_SKIN) 
    fg.set(15, 46, '#ffffff') 

    # Pass 2: Leaning
    fg.rect(30, 58, 6, 2, C_SHADOW)
    fg.rect(34, 42, 4, 4, C_PASS2_TOP) 
    fg.rect(33, 46, 4, 4, C_PASS2_TOP) 
    fg.rect(32, 39, 3, 3, C_SKIN) 
    fg.rect(32, 38, 3, 1, '#000000') 
    fg.rect(34, 39, 1, 2, '#000000') 
    fg.rect(33, 50, 4, 8, C_PASS2_BOT) 
    fg.rect(34, 44, 2, 5, C_PASS2_TOP) 
    fg.set(34, 49, C_SKIN) 

    # Pass 3: Briefcase
    fg.rect(48, 58, 6, 2, C_SHADOW)
    fg.rect(49, 41, 4, 9, C_PASS3_TOP) 
    fg.rect(48, 38, 3, 3, C_SKIN) 
    fg.rect(47, 37, 4, 1, '#101010') 
    fg.rect(46, 38, 6, 1, '#101010') 
    fg.rect(49, 50, 4, 8, C_PASS3_BOT) 
    fg.rect(48, 44, 2, 6, C_PASS3_TOP) 
    fg.rect(45, 49, 4, 4, '#402010') 

    final = flatten([bg, train, doors, fg])
    finish(final)

if __name__ == "__main__":
    draw_subway()
