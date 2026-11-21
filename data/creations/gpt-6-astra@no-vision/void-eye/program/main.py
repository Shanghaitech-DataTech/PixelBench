from pixelbench_api import *
import math

result = new_canvas(64, 64, name='void-eye')
c = result
# A compact, cool palette with a few pale accents.
p = {
 'ink':'#100e20', 'deep':'#1b1531', 'shade':'#291d43',
 'plum':'#3a2858', 'mid':'#51376e', 'lit':'#6d4c8e',
 'edge':'#9470af', 'glint':'#b998cc',
 'socket':'#171123', 'sclshadow':'#665479', 'sclmid':'#a18da9',
 'sclera':'#d3c4d4', 'white':'#f2e5e4',
 'irisblack':'#211239', 'irisdeep':'#33144f', 'iris':'#4b1e70',
 'irislit':'#683392', 'irisbright':'#8850ad', 'irisrim':'#a477bf',
 'pupil':'#100c25', 'glowdark':'#493968', 'glow':'#9584bf', 'core':'#c6bfeb'
}
def P(d, col): c.path(d,p.get(col,col))
def L(x,y,xx,yy,col): c.line(x,y,xx,yy,p.get(col,col))
def R(x,y,w,h,col): c.rect(x,y,w,h,p.get(col,col))
# Soft, translucent contact shadow, clearly separated from the creature.
c.ellipse(32,57,19,4,'#100d2410')
c.ellipse(32,57,15,3,'#100d241a')
c.ellipse(32,57,11,2,'#100d2426')
c.ellipse(32,57,6,1,'#100d242a')
# Rear appendages: short, heavy, curled rather than long dangling legs.
P('M 15 23 Q 8 24 7 29 Q 5 35 9 38 Q 12 39 14 36 L 12 35 Q 8 35 11 30 L 18 30 Z','ink')
P('M 13 25 Q 8 27 8 32 Q 7 35 10 36 L 12 36 Q 8 34 11 30 L 17 29 Z','plum')
L(9,29,9,32,'lit'); L(10,27,12,26,'mid')
P('M 49 23 Q 57 23 58 29 Q 60 35 56 37 Q 52 38 51 34 L 54 33 Q 56 35 56 31 Q 54 29 49 30 Z','ink')
P('M 51 25 Q 57 26 57 31 Q 58 35 55 35 L 54 34 Q 57 34 54 30 L 50 29 Z','plum')
L(54,26,56,28,'lit')
# Lower curls, with a near-black silhouette and purple turned surfaces.
P('M 15 35 Q 10 41 13 46 Q 15 50 20 47 L 23 43 L 21 40 Q 19 47 16 45 Q 14 43 20 38 Z','ink')
P('M 16 36 Q 12 42 15 46 Q 18 48 21 43 L 21 42 Q 18 46 16 44 Q 15 41 20 38 Z','mid')
L(14,42,15,39,'lit'); L(16,46,18,46,'plum')
P('M 23 39 Q 19 46 23 51 Q 26 54 30 50 L 31 46 L 28 44 Q 28 50 25 49 Q 23 47 28 42 Z','ink')
P('M 24 41 Q 21 47 25 51 L 28 50 L 29 47 L 27 49 L 25 48 L 26 43 Z','plum')
L(23,45,23,47,'lit'); L(24,49,25,50,'mid')
P('M 35 40 Q 33 46 37 50 Q 42 54 44 49 L 43 45 L 40 43 L 41 48 Q 38 49 38 45 L 40 41 Z','ink')
P('M 36 42 Q 35 47 39 50 L 41 50 L 43 48 L 41 46 L 41 48 L 39 48 L 38 44 Z','plum')
L(36,44,37,47,'lit')
P('M 44 35 Q 51 37 52 42 Q 53 47 49 48 Q 45 48 44 44 L 46 42 Q 48 46 49 43 Q 49 40 43 40 Z','ink')
P('M 46 37 Q 51 40 50 44 L 48 46 L 46 44 L 48 44 L 48 41 L 44 39 Z','mid')
L(49,40,50,42,'lit')
# Main floating mass, stepped outline and broad sculptural shadow planes.
P('M 26 7 L 36 7 L 43 10 L 49 15 L 52 20 L 54 28 L 52 35 L 47 41 L 39 45 L 28 46 L 20 43 L 14 38 L 10 31 L 10 23 L 13 16 L 19 11 Z','ink')
P('M 25 9 L 36 9 L 43 12 L 48 17 L 51 23 L 52 29 L 49 36 L 43 41 L 35 44 L 26 43 L 18 39 L 13 32 L 12 24 L 15 17 L 20 13 Z','shade')
P('M 25 9 L 35 9 L 42 12 L 46 17 L 46 23 L 42 29 L 33 34 L 22 36 L 16 31 L 14 24 L 16 18 L 21 13 Z','plum')
P('M 25 10 L 34 10 L 40 12 L 44 16 L 43 20 L 33 23 L 23 28 L 17 27 L 16 21 L 19 16 Z','mid')
P('M 24 12 L 32 11 L 38 13 L 40 15 L 31 14 L 24 17 L 20 21 L 18 21 L 20 16 Z','lit')
L(25,11,32,11,'edge'); L(20,14,23,12,'edge')
# Lower fleshy rim catches a narrow reflected light.
P('M 15 31 L 20 35 L 29 38 L 40 37 L 48 32 L 48 36 L 42 40 L 33 42 L 25 41 L 18 37 Z','plum')
L(22,39,28,41,'mid'); L(29,42,35,42,'mid')
L(39,40,43,38,'mid'); L(49,27,50,30,'mid')
# Almond eye socket.
P('M 12 25 Q 20 16 30 16 Q 43 15 51 25 Q 45 37 32 38 Q 19 37 12 27 Z','socket')
# The pale sclera is restricted to the almond, contrasting with the dark hide.
P('M 15 25 Q 22 19 31 18 Q 42 18 48 25 Q 42 34 32 35 Q 22 34 15 27 Z','sclshadow')
P('M 15 25 Q 23 19 31 19 Q 41 19 47 25 Q 40 32 30 33 Q 21 32 15 26 Z','sclmid')
P('M 16 25 Q 23 19 31 20 Q 39 19 44 23 Q 40 29 30 31 Q 20 30 16 26 Z','sclera')
P('M 18 24 Q 23 21 26 21 L 24 25 L 20 27 L 18 26 Z','white')
# Circular iris with a dark rim, shaded upper hemisphere and luminous lower fibres.
c.ellipse(32,26,10,10,p['irisblack'])
c.ellipse(32,26,9,9,p['irisdeep'])
P('M 25 24 Q 27 19 32 18 Q 39 19 40 25 L 39 31 L 35 35 L 29 35 L 25 31 Z','iris')
P('M 24 27 L 27 30 L 31 32 L 36 31 L 40 27 L 39 32 L 35 35 L 29 35 L 25 32 Z','irislit')
# Deliberate short radial segments, no random surface noise.
for a,co in [(10,'irisbright'),(35,'irislit'),(60,'irisbright'),(82,'irisrim'),(105,'irisbright'),(130,'irisbright'),(153,'irislit'),(175,'irisbright'),(205,'irislit'),(230,'irislit'),(290,'irislit'),(325,'irisbright')]:
    t=math.radians(a)
    x1=round(32+6*math.cos(t)); y1=round(26+6*math.sin(t))
    x2=round(32+8*math.cos(t)); y2=round(26+8*math.sin(t))
    L(x1,y1,x2,y2,co)
L(28,33,30,34,'irisbright'); L(33,34,35,33,'irisrim')
# The abyssal vertical pupil contains a faint lavender ember.
P('M 32 18 L 35 23 L 35 29 L 32 35 L 29 29 L 29 24 Z','pupil')
P('M 32 21 L 33 24 L 33 29 L 32 32 L 31 29 L 31 24 Z','glowdark')
L(32,24,32,29,'glow'); L(32,25,32,27,'core')
# One small specular catchlight, offset from the glowing pupil.
R(26,21,2,2,'glint'); c.set(26,21,p['white']); c.set(28,23,p['irisrim'])
# Heavy sloped upper lid integrates the eye into the monster.
P('M 12 25 L 17 20 L 24 17 L 31 16 L 39 17 L 46 21 L 51 25 L 47 24 L 41 21 L 33 19 L 25 19 L 18 22 Z','deep')
L(17,20,23,17,'mid'); L(24,17,30,16,'lit'); L(31,16,37,17,'mid')
L(39,18,44,20,'plum')
# Lid ends and bottom rim are kept clean and directional.
L(15,29,20,33,'ink'); L(21,34,27,36,'plum'); L(28,37,35,37,'mid')
L(37,36,43,33,'plum'); L(44,32,48,28,'deep')
# Small creases and edge accents distinguish the skin from a smooth eyeball.
L(14,20,16,17,'edge'); L(13,23,13,27,'mid')
L(18,33,20,35,'lit'); c.set(21,36,p['mid'])
L(45,15,47,18,'mid'); L(49,20,50,23,'plum')
L(27,12,30,12,'glint')
print(c.stats_text())
print(c.matrix_text(region=(10,15,53,38)))
save('void-eye',result)
finish(result)
