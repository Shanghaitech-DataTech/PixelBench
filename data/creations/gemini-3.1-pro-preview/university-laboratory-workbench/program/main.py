from pixelbench_api import *

c = new_canvas(64, 64)

# 1. Background
# Wall
c.rect(0, 0, 64, 32, '#B0C4DE')
# Wall tiles
for x in range(0, 64, 8):
    c.line(x, 0, x, 32, '#A4B8D2')
for y in range(0, 32, 8):
    c.line(0, y, 64, y, '#A4B8D2')
# Backsplash
c.rect(0, 32, 64, 4, '#90A4AE')

# Poster
c.rect(40, 4, 20, 16, '#FFFFFF')
c.rect(41, 5, 18, 14, '#F0F0F0')
c.rect(41, 4, 18, 2, '#333333')
c.rect(42, 5, 16, 1, '#FFFFFF')
c.rect(42, 8, 2, 10, '#FF9999')
c.rect(44, 10, 10, 8, '#99CCFF')
c.rect(54, 8, 4, 10, '#99FF99')

# Vent grille
c.rect(24, 6, 10, 6, '#D0D8E0')
c.rect(25, 7, 8, 1, '#A0B4CE')
c.rect(25, 9, 8, 1, '#A0B4CE')

# Power outlet
c.rect(24, 24, 6, 8, '#F5F5F5')
c.rect(25, 26, 1, 2, '#333333')
c.rect(28, 26, 1, 2, '#333333')
c.rect(25, 30, 1, 2, '#333333')
c.rect(28, 30, 1, 2, '#333333')

# 2. Bench
c.rect(0, 36, 64, 18, '#3A3F44')
c.rect(0, 36, 64, 1, '#454B52') # Highlight
c.rect(0, 54, 64, 10, '#282C30')
c.rect(0, 54, 64, 1, '#4C5258') # Lip

# Drawers
c.rect(4, 56, 16, 6, '#30353A')
c.rect(24, 56, 16, 6, '#30353A')
c.rect(44, 56, 16, 6, '#30353A')
c.rect(10, 58, 4, 1, '#A0A0A0')
c.rect(30, 58, 4, 1, '#A0A0A0')
c.rect(50, 58, 4, 1, '#A0A0A0')

# Shadows
c.rect(46, 44, 18, 2, '#2A2E33') # Rack
c.rect(21, 45, 10, 2, '#2A2E33') # Bottle 1
c.rect(29, 45, 8, 2, '#2A2E33') # Bottle 2
c.rect(35, 45, 14, 2, '#2A2E33') # Flask
c.rect(3, 47, 16, 2, '#2A2E33') # Microscope
c.poly([(17, 54), (47, 54), (45, 48), (19, 48)], '#2A2E33') # Notebook

# 3. Rack
c.rect(47, 40, 17, 2, '#8B5A2B')
c.rect(47, 42, 17, 3, '#A0522D')
c.rect(49, 30, 2, 10, '#8B5A2B')
c.rect(60, 30, 2, 10, '#8B5A2B')
c.rect(50, 24, 3, 16, '#F0F8FF')
c.rect(54, 24, 3, 16, '#F0F8FF')
c.rect(58, 24, 3, 16, '#F0F8FF')
c.rect(50, 30, 3, 9, '#FF3333')
c.rect(54, 32, 3, 7, '#33CC33')
c.rect(58, 28, 3, 11, '#3366FF')
c.rect(50, 24, 1, 16, '#FFFFFF')
c.rect(54, 24, 1, 16, '#FFFFFF')
c.rect(58, 24, 1, 16, '#FFFFFF')
c.rect(48, 31, 15, 2, '#A0522D')
c.rect(48, 36, 15, 2, '#A0522D')

# 4. Bottles
# Bottle 1 (Amber)
c.rect(22, 34, 8, 12, '#5C2E16')
c.rect(24, 30, 4, 4, '#5C2E16')
c.rect(23, 29, 6, 2, '#5C2E16')
c.rect(24, 26, 4, 3, '#3E1F0F')
c.rect(23, 37, 6, 6, '#FFFFFF')
c.rect(24, 38, 4, 1, '#000000')
c.rect(24, 40, 3, 1, '#000000')
c.rect(22, 34, 1, 12, '#8B4513')

# Bottle 2 (Green)
c.rect(30, 38, 6, 8, '#2E8B57')
c.rect(31, 35, 4, 3, '#2E8B57')
c.rect(30, 34, 6, 1, '#2E8B57')
c.rect(31, 31, 4, 3, '#F5F5DC')
c.rect(31, 40, 4, 4, '#FFFFFF')
c.rect(32, 41, 2, 1, '#000000')

# Flask
c.poly([(40, 34), (44, 34), (44, 38), (48, 46), (36, 46), (40, 38)], '#E0FFFF')
c.poly([(39, 40), (45, 40), (47, 45), (37, 45)], '#9370DB')
c.rect(39, 33, 6, 2, '#E0FFFF')
c.rect(40, 41, 4, 3, '#FFFFFF')
c.rect(41, 42, 2, 1, '#000000')
c.set(40, 42, '#E0FFFF')
c.set(42, 44, '#E0FFFF')
c.set(44, 41, '#E0FFFF')

# 5. Microscope
c.path("M 18 46 C 22 46 24 40 24 32", '#1E1E1E', fill=False) # Wire
c.rect(4, 44, 14, 4, '#2C2C2C')
c.rect(5, 44, 12, 1, '#3C3C3C')
c.rect(8, 40, 4, 4, '#2C2C2C')
c.path("M 8 40 C 2 30 2 18 10 16 L 14 16 L 14 20 C 8 21 8 30 12 40 Z", '#D0D0D0')
c.circle(10, 38, 3, '#1E1E1E')
c.circle(10, 38, 1, '#A0A0A0')
c.rect(12, 14, 6, 14, '#E0E0E0')
c.rect(14, 10, 2, 4, '#1E1E1E')
c.rect(13, 8, 4, 2, '#1E1E1E')
c.poly([(12, 28), (18, 28), (20, 31), (10, 31)], '#2C2C2C')
c.rect(11, 31, 2, 4, '#A0A0A0')
c.rect(14, 31, 3, 4, '#C0C0C0')
c.rect(18, 31, 2, 3, '#A0A0A0')
c.rect(12, 36, 10, 2, '#1E1E1E')
c.rect(14, 35, 6, 1, '#ADD8E6')
c.rect(13, 35, 1, 1, '#C0C0C0')
c.rect(20, 35, 1, 1, '#C0C0C0')
c.rect(13, 42, 6, 2, '#E0E0E0')

# 6. Notebook
c.poly([(18, 54), (46, 54), (44, 48), (20, 48)], '#8B0000')
c.poly([(19, 53), (45, 53), (43, 49), (21, 49)], '#FDF5E6')
c.line(32, 49, 32, 53, '#D3C1A3')
c.line(23, 50, 30, 50, '#A9A9A9')
c.line(22, 52, 30, 52, '#A9A9A9')
c.line(34, 50, 41, 50, '#A9A9A9')
c.line(34, 52, 42, 52, '#A9A9A9')
c.line(38, 48, 43, 53, '#1E1E1E')
c.set(38, 48, '#C0C0C0')

# 7. Dropper
c.rect(46, 51, 8, 2, '#E0FFFF')
c.rect(46, 51, 3, 2, '#FF3333')
c.rect(54, 50, 5, 4, '#CD5C5C')
c.rect(55, 50, 3, 1, '#F08080')
c.set(45, 51, '#E0FFFF')
c.set(45, 52, '#E0FFFF')

finish(c)
