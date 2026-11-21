c = new_canvas(64, 64, name="subway_platform")

# Compact night-station palette
ink = '#101b28'
wall = '#253747'
wall_hi = '#344b5b'
shadow = '#182735'
steel = '#718a98'
steel_hi = '#b7c9c8'
glass = '#284958'
glass_hi = '#3d7180'
light = '#e5e7cf'
yellow = '#f2c75d'
orange = '#e58c52'
red = '#cf5a56'
blue = '#5a91a3'
blue_hi = '#86bbc0'
cream = '#f3dfb2'
black = '#0c131d'

# Wall and ceiling
c.rect(0, 0, 64, 63, wall)
c.rect(0, 0, 64, 5, ink)
c.rect(0, 5, 64, 2, wall_hi)
c.rect(0, 7, 64, 2, shadow)
c.rect(0, 9, 64, 1, '#526777')
# Wall panel rhythm
for x in (2, 19, 36, 53):
    c.rect(x, 10, 1, 14, shadow)
    c.rect(x+1, 10, 1, 14, wall_hi)
# Overhead station sign
c.rect(5, 2, 24, 9, ink)
c.rect(6, 3, 22, 7, '#d9ddc9')
c.rect(6, 3, 22, 1, yellow)
c.text(8, 5, 'METRO', ink, font='5x7')
# Route marker and small wayfinding sign
c.rect(47, 3, 12, 8, ink)
c.rect(48, 4, 10, 6, blue)
c.text(50, 5, '2', light, font='5x7')
c.rect(32, 12, 22, 7, ink)
c.rect(33, 13, 20, 5, '#d9ddc9')
c.text(34, 14, '2 MIN', ink, spacing=0, font='5x7')

# Train body, slightly blurred by horizontal speed streaks
for yy, x0, x1, col in [(15,0,16,blue_hi),(18,2,26,steel_hi),(21,0,19,blue),(25,0,13,steel_hi)]:
    c.rect(x0, yy, x1-x0, 1, col)
c.rect(0, 26, 64, 13, '#718894')
c.rect(0, 27, 64, 2, steel_hi)
c.rect(0, 37, 64, 2, '#425d6a')
# Train windows with warm interiors
for x in (3, 16, 29, 42):
    c.rect(x, 29, 9, 7, ink)
    c.rect(x+1, 30, 7, 5, '#8ab2b4')
    c.rect(x+2, 31, 4, 3, '#d6d4b0')
    c.set(x+6, 31, yellow)
# Car seams and lower stripe
for x in (13, 26, 39, 52):
    c.rect(x, 27, 1, 11, '#536b78')
c.rect(0, 38, 64, 1, yellow)
c.rect(0, 39, 64, 1, ink)
# Arriving train's bright leading cab at right
c.poly([(54,26),(61,26),(64,29),(64,38),(54,38)], '#a9bdba')
c.poly([(57,28),(62,28),(63,30),(63,34),(57,34)], '#304f5d')
c.rect(58, 29, 4, 2, blue_hi)
c.rect(62, 35, 2, 2, yellow)
c.rect(55, 37, 9, 2, ink)
# Speed marks in front of train and behind platform structure
for y, x, w, color in [(20,1,12,blue_hi),(22,20,8,steel_hi),(24,4,9,blue_hi),(31,0,7,light),(35,2,11,steel_hi)]:
    c.rect(x, y, w, 1, color)

# Platform screen doors: repeated glass bays and clear frames
c.rect(0, 40, 64, 2, ink)
c.rect(0, 42, 64, 11, glass)
for x in (1, 16, 31, 46, 61):
    c.rect(x, 41, 1, 12, steel_hi)
    c.rect(x+1, 42, 1, 10, '#416b78')
# Glass reflections and door openings
for x in (5, 20, 35, 50):
    c.rect(x, 43, 1, 7, glass_hi)
    c.rect(x+1, 43, 1, 7, '#355d6b')
    c.rect(x+9, 44, 1, 5, '#527986')
    c.rect(x+3, 45, 4, 1, blue_hi)
    c.rect(x+3, 48, 4, 1, blue_hi)
# Door warning band and caution marks
c.rect(0, 51, 64, 2, yellow)
for x in range(2,64,6):
    c.poly([(x,51),(x+2,51),(x,53)], ink)
# Door status lights
for x in (14, 29, 44, 59):
    c.rect(x, 40, 2, 1, yellow)

# Platform floor and edge
c.rect(0, 53, 64, 11, '#344654')
c.rect(0, 53, 64, 1, light)
c.rect(0, 55, 64, 2, '#c5b985')
c.rect(0, 57, 64, 7, '#2b3b49')
for x in range(3,64,12):
    c.rect(x, 58, 1, 6, '#405361')
# Bench at left foreground
c.rect(3, 44, 13, 2, ink)
c.rect(4, 43, 11, 2, steel_hi)
c.rect(4, 46, 11, 2, blue)
c.rect(5, 48, 2, 5, ink)
c.rect(12, 48, 2, 5, ink)
c.rect(3, 52, 12, 1, steel_hi)

# Passenger 1: standing with a tote, left of centre
c.circle(23, 37, 2, '#d7a47b')
c.rect(21, 36, 4, 1, black)
c.rect(21, 40, 5, 7, orange)
c.rect(20, 41, 1, 5, '#d7a47b')
c.rect(26, 41, 1, 4, '#d7a47b')
c.rect(21, 47, 2, 6, black)
c.rect(24, 47, 2, 6, black)
c.rect(20, 53, 3, 1, ink)
c.rect(24, 53, 3, 1, ink)
c.rect(27, 45, 3, 5, '#b6a46b')
c.rect(27, 44, 3, 2, yellow)
# Passenger 2: seated on the bench, profile, legs angled forward
c.circle(9, 39, 2, '#c88969')
c.rect(7, 38, 4, 1, black)
c.rect(7, 42, 5, 4, blue)
c.rect(11, 44, 4, 2, blue)
c.rect(12, 46, 2, 5, black)
c.rect(14, 50, 4, 2, black)
c.rect(6, 46, 2, 5, black)
# Passenger 3: walking briskly, arm trailing, coat and separated stride
c.circle(39, 36, 2, '#e0b58b')
c.rect(37, 35, 4, 1, black)
c.rect(37, 39, 5, 7, '#527f91')
c.poly([(37,40),(34,42),(33,41),(36,39)], '#e0b58b')
c.poly([(42,40),(45,42),(44,43),(41,42)], '#e0b58b')
c.poly([(38,46),(41,46),(39,50),(35,53),(34,52)], black)
c.poly([(41,46),(43,47),(44,51),(48,52),(48,53),(42,53),(40,50)], black)
c.rect(33, 52, 4, 1, ink)
c.rect(46, 52, 4, 1, ink)
# Subtle pixels of reflected station light on floor
c.rect(22, 56, 5, 1, '#65777a')
c.rect(36, 56, 6, 1, '#61777a')
c.rect(49, 56, 4, 1, '#65777a')

print(c.stats_text())
print(c.matrix_text(region=(0, 35, 63, 63)))
finish(c)
