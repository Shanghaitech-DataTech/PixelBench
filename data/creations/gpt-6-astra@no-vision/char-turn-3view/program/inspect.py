chars='.abcdefghijklmnopqrstuvw'
rows=[]
for y in range(119):
    r=[input_canvas.get(x,y) for x in range(66)]
    if not rows or r!=rows[-1][1]: rows.append((y,r))
print('distinct runs',len(rows),[y for y,r in rows])
for j,(y,r) in enumerate(rows):
    print(f'{j:02} {y:03}', ''.join(chars[r[int((x+.5)*66/28)]] for x in range(28)))
