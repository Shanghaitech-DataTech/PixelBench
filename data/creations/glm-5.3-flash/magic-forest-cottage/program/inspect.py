import sys
src = open('main.py').read()
# strip the finish/save tail for inspection
src = src.replace("save('magic-forest-cottage', c)", "pass").replace("finish(c)", "pass")
ns = {}
exec(compile(src, 'main.py', 'exec'), ns)
c = ns['c']

def show(name, region):
    print('=' * 20, name, region)
    print(c.matrix_text(region=region))

show('cottage', (24, 60, 86, 104))
show('moon', (76, 8, 112, 44))
show('well', (94, 46, 127, 112))
