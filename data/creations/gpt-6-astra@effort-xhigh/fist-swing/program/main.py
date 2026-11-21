# Original palette, sampled without changing it.
col = {'a':'#222034', 'b':'#45283c', 'c':'#eec39a', 'd':'#663931',
       'e':'#df7126', 'f':'#8f563b', 'g':'#847e87', 'h':'#3f3f74',
       'i':'#5b6ee1', 'j':'#cbdbfc'}
# Both frames have room around the original silhouette and the extended fist.
W,H = 37,46
OX,OY = 3,1
f1 = new_canvas(W,H,name='frame_1_original')
f1.blit(input_canvas,OX,OY)
f2 = f1.copy(name='frame_2_left_jab')
def row(y,x,s):
    for i,ch in enumerate(s):
        f2.set(OX+x+i,OY+y,None if ch == '.' else col[ch])
# Erase the bent forearm and fist, keeping the face, neck and torso.
for y,x in [(7,14),(8,13),(9,13),(10,12),(11,13),(12,14),(13,15),(14,16),(15,17)]:
    f2.clear(OX+x,OY+y,W-(OX+x),1)
# Reconnect the shoulder to an extended upper arm and a compact closed fist.
# Coordinates below use the original sprite's pixel grid.
row(9, 12, 'aaaaa..........aaaa')
row(10,12, 'a' + 'c'*4 + 'a'*10 + 'c'*4 + 'a')
row(11,12, 'c'*13 + 'e' + 'c'*3 + 'e'*2 + 'a')
row(12,12, 'eccc' + 'e'*10 + 'ccecea')
row(13,12, 'c' + 'e'*10 + 'f'*4 + 'eeefa')
row(14,13, 'e' + 'f'*6 + 'a'*11)
row(15,14, 'efaaaa')
row(16,15, 'ea')
# Verify the original frame is an exact translated copy.
for y in range(44):
    for x in range(29):
        assert f1.get(x+OX,y+OY) == input_canvas.get(x,y)
save('frame_1_original',f1)
save('frame_2_left_jab',f2)
view(f1,scale=10,margin=1)
view(f2,scale=10,margin=1)
finish([f1,f2])
