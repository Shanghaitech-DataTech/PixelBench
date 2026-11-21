src = open('main.py').read()
src = src.replace("save('magic-forest-cottage', c)", "pass").replace("finish(c)", "pass")
ns = {}
exec(compile(src, 'main.py', 'exec'), ns)
c = ns['c']

def show(name, region):
    print('=' * 20, name, region)
    print(c.matrix_text(region=region))

show('bottom center mist', (46, 112, 100, 127))
show('left mist over ground', (0, 96, 30, 112))
