from pixelbench_api import new_canvas, finish

O=(58,36,18)      # dark outline
W=(164,104,52)    # wood
L=(194,138,84)    # light wood
D=(102,62,28)     # dark wood shade
G=(222,180,88)    # gold/brass
B=(26,12,6)       # near black

c = new_canvas(16,16)

# --- Bow ring ---
c.circle(7,4,3,O)              # dark disc
c.circle(7,4,2,W)              # wood band
c.circle(7,4,1,"transparent")  # hole
c.circle(7,4,2,G,fill=False)   # brass ring around hole
# highlights on bow
c.set(6,2,L); c.set(7,2,L)
c.set(5,3,L)
# lower right shading on bow
c.set(5,5,D); c.set(8,5,D)

# --- Shaft ---
c.rect(6,7,3,6,O)      # silhouette x6-8 y7-12
c.rect(6,7,3,4,W)      # wood shaft x6-8 y7-10
c.rect(6,7,1,4,L)      # left highlight
c.rect(8,7,1,4,D)      # right shade

# brass collar near bottom of shaft
c.rect(6,11,3,1,G)

# --- Teeth ---
c.rect(4,10,2,2,O)     # left tooth silhouette
c.rect(4,10,1,2,W)     # left tooth wood
c.rect(9,12,2,1,O)     # right tooth silhouette
c.rect(9,12,1,1,W)     # right tooth wood

print(c.stats_text())
print(c.matrix_text())
finish(c)
