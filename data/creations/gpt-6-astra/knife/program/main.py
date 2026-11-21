turned = input_canvas.select(0,0,93,128).flip('h').rotate(54, algorithm='rotsprite').preview()
knife = turned.select(3,63,154,29).preview()
result = new_canvas(250,112,name='rightward_thrust')
# Soft, staggered echoes of the actual knife retain the original pixel colours.
w,h,data = knife.to_rgba()
def echo(dx,dy,opacity):
    layer = new_canvas(250,112)
    for y in range(h):
        for x in range(w):
            i=(y*w+x)*4
            r,g,b,a=data[i:i+4]
            if a:
                layer.set(dx+x,dy+y,(r,g,b,round(a*opacity)))
    result.blit(layer,0,0)
echo(14,22,0.20)
echo(42,35,0.40)
# Long translucent streaks give the motion a clear left-to-right direction.
result.poly([(4,60),(57,58),(106,60),(55,62)],'#bfc9f44a')
result.poly([(24,75),(76,70),(145,71),(79,74)],'#bfc9f438')
result.line(2,45,27,45,'#dae0ff42')
result.line(26,31,53,31,'#dae0ff34')
# A narrow luminous envelope extends beyond the point.
result.poly([(24,45),(86,44),(170,47),(217,53),(245,62),(225,66),(236,61),(211,57),(168,51),(85,48)],'#d5e0ff70')
result.poly([(37,46),(91,46),(170,49),(214,55),(243,62),(229,62),(210,58),(168,52),(91,48)],'#ffffff')
result.poly([(245,62),(227,72),(192,81),(147,86),(93,86),(149,82),(191,77),(223,69)],'#d5e0ff70')
result.poly([(244,62),(226,70),(191,79),(148,83),(113,83),(149,81),(190,76),(225,67)],'#ffffff')
# The solid foreground pose is kept completely readable.
result.blit(knife,72,49)
# A crisp white glint on the lower edge feeds into the slash.
result.line(198,76,215,70,'#ffffff')
result.line(216,69,224,63,'#ffffff')
result.line(232,60,246,62,'#ffffff')
view(result)
finish(result)
