from pixelbench_api import new_canvas, finish

c = new_canvas(32, 32)

# Draw cable
c.path("M 8 3 Q 8 1 5 2 Q 2 3 3 8 Q 1 15 4 20 Q 7 25 5 28 Q 8 31 13 29 Q 18 27 21 29 Q 25 30 27 27 Q 29 24 28 20", '#252525', fill=False)

# Earbud 1
c.line(28, 20, 28, 18, '#7A8791')
c.rect(27, 16, 2, 2, '#B0BCC2')
c.line(26, 16, 26, 17, '#404040')

# Earbud 2
c.path("M 21 29 Q 23 26 25 25", '#252525', fill=False)
c.line(25, 25, 26, 23, '#7A8791')
c.rect(26, 21, 2, 2, '#B0BCC2')
c.line(25, 21, 25, 22, '#404040')

# Jack
c.rect(7, 4, 2, 2, '#7A8791')
c.set(7, 4, '#404040')

# Buttons
c.rect(11, 4, 4, 2, '#D95A2B')
c.line(11, 4, 14, 4, '#F08A5D')

c.rect(16, 4, 3, 2, '#B0BCC2')
c.line(16, 4, 18, 4, '#FFFFFF')

c.rect(20, 4, 3, 2, '#B0BCC2')
c.line(20, 4, 22, 4, '#FFFFFF')

c.rect(24, 4, 3, 2, '#B0BCC2')
c.line(24, 4, 26, 4, '#FFFFFF')

# Body Base
c.rect(5, 6, 22, 23, '#1F456E')

# Top Silver Trim
c.rect(5, 6, 22, 4, '#B0BCC2')
c.line(5, 9, 26, 9, '#7A8791')
c.line(5, 6, 26, 6, '#FFFFFF')

# Body Highlights/Shadows
c.line(5, 10, 5, 28, '#3B6999')
c.line(26, 10, 26, 28, '#112842')
c.line(5, 28, 26, 28, '#112842')

# Volume Control
c.rect(27, 10, 2, 5, '#7A8791')
c.line(28, 10, 28, 14, '#404040')
c.set(27, 11, '#404040')
c.set(27, 13, '#404040')

# Window Bevel
c.line(6, 11, 24, 11, '#112842')
c.line(6, 11, 6, 22, '#112842')
c.line(6, 22, 24, 22, '#3B6999')
c.line(24, 11, 24, 22, '#3B6999')

# Clear Window
c.clear(7, 12, 17, 10)

# Cassette details
c.line(8, 13, 10, 13, '#E8ECEF')
c.line(20, 13, 22, 13, '#E8ECEF')
c.rect(11, 20, 9, 2, '#E8ECEF', fill=False)
c.set(12, 20, '#2A2A2A')
c.set(18, 20, '#2A2A2A')
c.set(15, 20, '#E8ECEF')

# Tape line
c.line(11, 19, 19, 19, '#2A2A2A')

# Reels
for cx in [11, 19]:
    c.circle(cx, 16, 3, '#2A2A2A')
    c.circle(cx, 16, 2, '#E8ECEF')
    c.set(cx, 16, '#00000000')
    c.set(cx-1, 15, '#00000000')
    c.set(cx+1, 15, '#00000000')
    c.set(cx-1, 17, '#00000000')
    c.set(cx+1, 17, '#00000000')

# Glare on Window
c.line(9, 12, 18, 21, '#FFFFFF30')
c.line(13, 12, 22, 21, '#FFFFFF30')

# Body details (Groove and Logo)
c.line(7, 24, 24, 24, '#112842')
c.line(7, 25, 24, 25, '#3B6999')
c.rect(8, 26, 3, 1, '#E0E5E8')
c.set(12, 26, '#D95A2B')

finish(c)
