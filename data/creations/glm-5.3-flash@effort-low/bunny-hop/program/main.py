W, H = 36, 28
f1 = input_canvas.copy(name='frame1')
big = new_canvas(W, H, name='f1big')
big.blit(f1, 5, 0)
f1 = big

# frame 2: mid-leap rabbit, facing right, body stretched
f2 = new_canvas(W, H, name='frame2')
D = '#efe9e7'; A = '#3a3737'; C = '#827c7c'; E = '#d6b39d'; B = '#b7b3b2'
# body (stretched, angled up toward front)
f2.ellipse(18, 16, 9, 5, D)
# head
f2.circle(28, 11, 4, D)
# ears swept back
f2.line(27, 8, 22, 2, D); f2.line(28, 8, 22, 2, D)
f2.line(29, 8, 25, 3, D); f2.line(30, 8, 25, 3, D)
# tail
f2.circle(9, 14, 2, D)
# hind legs extended back-down
f2.line(13, 19, 6, 23, D); f2.line(14, 20, 7, 24, D)
f2.line(6, 23, 4, 23, D); f2.line(7, 24, 5, 24, D)
# front legs tucked forward
f2.line(25, 19, 27, 23, D); f2.line(26, 19, 28, 22, D)
f2.line(27, 23, 29, 23, D); f2.line(28, 22, 30, 22, D)
# outline everything
f2.outline(A)
# inner ear
f2.set(24, 4, E); f2.set(25, 5, E); f2.set(23, 5, E)
# eye
f2.set(29, 10, A)
# shading on belly
f2.line(15, 19, 22, 19, C)
# nose
f2.set(32, 11, E)
# eye (after outline)
f2.set(29, 10, A); f2.set(30, 10, A)

print(f1.stats_text()); print(f2.stats_text())
print(f2.matrix_text())
finish([f1, f2])
