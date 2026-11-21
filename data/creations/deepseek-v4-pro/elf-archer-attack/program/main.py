from pixelbench_api import *

# Frame 1: original content
f1 = input_canvas.copy(name='frame1')

# Frame 2: drawn bow
f2 = input_canvas.copy(name='frame2')

string = f2.color('#f6d39b', name='string')   # tan, id 12
skin   = f2.color('#c5956a', name='skin')     # id 3
sleeve = f2.color('#687862', name='sleeve')   # gray-green, id 32

# --- erase the relaxed (straight) bowstring ---
old_string = [
    (27,8),(27,9),(27,10),(27,11),(27,12),
    (26,14),(26,15),(26,16),(26,17),(26,18),
    (25,25),(25,26),(24,28),(25,29),(25,30),(25,31),(24,32),(25,33),
]
for x,y in old_string:
    f2.set(x,y,None)

# --- draw the pulled-back string as a V ---
# top tip attaches near (27,8); bottom tip near (25,33); nock at the face
nock = (16,8)
f2.line(27,8,nock[0],nock[1],string)
f2.line(nock[0],nock[1],25,33,string)

# --- rear arm: upper arm (shoulder -> elbow) and forearm (elbow -> hand) ---
f2.line(14,13,11,12,sleeve)   # upper arm, elbow pointing back-left
f2.line(11,12,16,8,sleeve)    # forearm up to the nock

# --- rear hand at the nocking point ---
for x,y in [(16,8),(16,7),(17,8),(15,8)]:
    f2.set(x,y,skin)

print('f1 stats:', f1.stats_text())
print('f2 stats:', f2.stats_text())

finish([f1, f2])
