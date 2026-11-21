# Four consistent, hand-pixelled portraits in a transparent 2x2 sheet.
P = {
    'ink':'#251e32', 'hairdark':'#573047', 'hair':'#9d4c50',
    'hairlight':'#d87861', 'hairshine':'#f2aa79',
    'skinshadow':'#cf8875', 'skin':'#f2b991', 'skinlight':'#ffdbad',
    'blush':'#e99a83', 'white':'#fff3d9',
    'tealdark':'#204b60', 'teal':'#317e89', 'teallight':'#66b6b4',
    'gold':'#efc77e', 'mouth':'#71384b', 'tongue':'#ed8c8e'
}

def portrait(emotion):
    c=new_canvas(32,32,name=emotion)
    def poly(pts,col): c.poly(pts,P[col])
    def rect(x,y,w,h,col): c.rect(x,y,w,h,P[col])
    def line(x,y,u,v,col): c.line(x,y,u,v,P[col])
    def dot(x,y,col): c.set(x,y,P[col])
    # Matching jacket and small ivory shirt, behind the big head.
    poly([(8,25),(12,24),(21,24),(25,26),(28,28),(28,31),(4,31),(4,28)],'ink')
    poly([(8,26),(12,26),(16,29),(21,26),(24,27),(27,29),(27,30),(5,30),(5,29)],'teal')
    poly([(5,29),(8,27),(10,27),(9,30),(5,30)],'teallight')
    poly([(23,27),(26,29),(27,30),(22,30)],'tealdark')
    poly([(12,25),(20,25),(21,28),(17,30),(15,30),(11,28)],'ink')
    poly([(13,25),(19,25),(19,27),(17,29),(15,29),(13,27)],'skinshadow')
    rect(14,25,4,2,'skin')
    poly([(12,27),(15,29),(17,29),(20,27),(19,30),(13,30)],'white')
    line(10,27,12,30,'tealdark')
    line(21,27,20,30,'teallight')
    dot(22,29,'gold')
    # Hair silhouette, including the same off-centre tuft and side locks.
    poly([(11,2),(18,2),(18,3),(22,3),(22,4),(25,4),(25,6),(27,6),(27,9),
          (28,9),(28,17),(27,17),(27,21),(28,23),(25,23),(25,25),(21,25),
          (21,24),(9,24),(9,25),(5,25),(5,23),(3,23),(4,19),(3,17),
          (3,10),(4,10),(4,7),(6,7),(6,5),(9,5),(9,4),(11,4)],'ink')
    poly([(11,4),(18,3),(18,4),(22,4),(22,5),(24,5),(24,7),(26,7),(26,10),
          (27,10),(27,17),(26,17),(26,21),(26,23),(24,23),(24,24),(22,24),
          (22,23),(8,23),(8,24),(6,24),(6,22),(5,22),(5,18),(4,16),
          (4,11),(5,11),(5,8),(7,8),(7,6),(10,6)],'hairdark')
    poly([(11,4),(18,4),(19,5),(23,5),(25,8),(26,11),(25,17),(23,21),
          (8,21),(5,16),(5,10),(8,6),(11,6)],'hair')
    # Neck outline and ears.
    rect(12,23,9,3,'ink')
    rect(13,23,7,3,'skinshadow')
    poly([(5,14),(8,14),(9,16),(8,20),(6,20),(5,18)],'ink')
    rect(6,15,3,4,'skinshadow')
    rect(6,15,2,2,'skin')
    poly([(24,14),(27,14),(28,16),(27,19),(25,20),(24,18)],'ink')
    rect(25,15,2,4,'skinshadow')
    rect(25,15,2,2,'skin')
    # Peach oval. Flat planes keep the small features crisp.
    poly([(9,9),(15,8),(21,8),(24,10),(25,13),(25,20),(23,23),(20,25),
          (13,25),(10,23),(8,21),(7,18),(7,13)],'ink')
    poly([(10,9),(16,9),(21,9),(23,11),(24,14),(24,20),(22,23),(19,24),
          (14,24),(11,22),(9,20),(8,17),(8,13)],'skinshadow')
    poly([(10,10),(16,9),(21,9),(23,11),(23,20),(21,22),(18,23),(14,23),
          (11,21),(9,19),(9,13)],'skin')
    poly([(11,10),(17,9),(21,10),(22,12),(22,18),(20,20),(13,20),(10,18),(10,13)],'skinlight')
    rect(9,19,3,1,'blush')
    rect(21,19,3,1,'blush')
    dot(17,18,'skinshadow')
    dot(16,18,'skin')
    # Features are varied without changing the model or accessories.
    if emotion=='calm':
        line(10,12,13,12,'hairdark')
        line(19,12,22,12,'hairdark')
        line(10,14,13,14,'ink')
        line(19,14,22,14,'ink')
        rect(10,15,4,3,'white')
        rect(19,15,4,3,'white')
        rect(11,14,2,4,'ink')
        rect(20,14,2,4,'ink')
        dot(11,15,'white'); dot(20,15,'white')
        dot(12,17,'teal'); dot(21,17,'teal')
        line(15,21,18,21,'mouth')
        dot(18,20,'skinshadow')
    elif emotion=='smiling':
        line(10,12,12,11,'hairdark'); dot(13,12,'hairdark')
        line(19,11,21,11,'hairdark'); dot(22,12,'hairdark')
        line(10,16,11,15,'ink'); line(11,15,12,15,'ink'); dot(13,16,'ink')
        line(19,16,20,15,'ink'); line(20,15,21,15,'ink'); dot(22,16,'ink')
        rect(9,18,4,2,'blush'); rect(20,18,4,2,'blush')
        poly([(13,20),(20,20),(19,23),(18,24),(15,24),(14,23)],'ink')
        rect(14,20,5,1,'white')
        rect(15,21,4,2,'mouth')
        rect(16,22,2,1,'tongue')
    elif emotion=='angry':
        line(10,12,13,14,'ink'); dot(11,12,'ink'); dot(13,13,'ink')
        line(19,14,22,12,'ink'); dot(19,13,'ink'); dot(21,12,'ink')
        rect(10,15,4,3,'white'); rect(19,15,4,3,'white')
        rect(12,15,2,3,'ink'); rect(19,15,2,3,'ink')
        dot(12,15,'teal'); dot(20,15,'teal')
        line(10,14,13,15,'ink'); line(19,15,22,14,'ink')
        dot(16,14,'skinshadow'); dot(16,15,'skinshadow')
        line(14,22,15,21,'mouth'); line(15,21,18,21,'mouth'); dot(19,22,'mouth')
        line(15,23,18,23,'skinshadow')
    elif emotion=='surprised':
        line(10,11,12,10,'hairdark'); dot(13,11,'hairdark')
        line(19,10,21,10,'hairdark'); dot(22,11,'hairdark')
        for x in (10,19):
            rect(x,13,4,6,'ink')
            rect(x-1,14,6,3,'ink')
            rect(x,14,4,4,'white')
            rect(x+1,15,2,2,'ink')
            dot(x+1,14,'white')
        rect(15,20,4,4,'mouth')
        rect(14,21,1,2,'ink'); rect(19,21,1,2,'ink')
        rect(16,21,2,2,'ink')
        rect(16,23,2,1,'tongue')
    # Front fringe: identical long diagonal sweep in every cell.
    poly([(7,8),(10,6),(15,5),(21,6),(24,8),(25,11),(25,15),(23,16),(23,12),
          (21,9),(18,9),(16,10),(13,10),(13,11),(10,12),(9,15),(7,16),(6,13)],'ink')
    poly([(7,8),(11,6),(16,6),(21,7),(23,8),(24,11),(24,14),(23,11),(21,8),
          (18,8),(16,9),(13,9),(13,10),(10,11),(8,14),(7,14)],'hair')
    poly([(8,8),(11,6),(16,6),(19,7),(17,8),(13,8),(13,9),(10,10),(8,12)],'hairlight')
    line(10,7,13,6,'hairshine'); line(14,6,16,6,'hairshine')
    line(20,6,23,8,'hairlight')
    line(25,10,25,13,'hairlight')
    line(5,12,5,16,'hairlight')
    dot(6,18,'hair')
    line(6,21,7,23,'hair')
    line(25,21,24,23,'hair')
    # Single matching gold ear stud.
    dot(26,18,'gold')
    return c

result=new_canvas(64,64,name='character_emotion_set')
for emotion,x,y in [('calm',0,0),('smiling',32,0),('angry',0,32),('surprised',32,32)]:
    result.blit(portrait(emotion),x,y)
view(result,scale=8,margin=0)
save('character_emotion_set',result)
finish(result)
