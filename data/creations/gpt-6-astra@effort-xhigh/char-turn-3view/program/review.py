exec(open('main.py').read())
for name,g in [('left',q1),('right',q2),('rear',rear)]:
    print(name)
    print('   '+''.join(str(i//10 or ' ') for i in range(28)))
    print('   '+''.join(str(i%10) for i in range(28)))
    for y,r in enumerate(g): print(f'{y:02} '+''.join(r))
