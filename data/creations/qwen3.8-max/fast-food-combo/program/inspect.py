src = open('main.py').read()
src = src.replace('view(c)', 'pass').replace('save("combo", c)', 'pass').replace('finish(c)', 'pass')
g = dict(globals())
exec(compile(src, 'main.py', 'exec'), g)
c = g['c']
print("=== sauce cups region ===")
print(c.matrix_text(region=(29, 45, 60, 58)))
print("=== cup top / straw / ice ===")
print(c.matrix_text(region=(38, 4, 59, 20)))
