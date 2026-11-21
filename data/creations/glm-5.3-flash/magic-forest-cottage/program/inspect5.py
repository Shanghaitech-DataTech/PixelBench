src = open('main.py').read()
src = src.replace("save('magic-forest-cottage', c)", "pass").replace("finish(c)", "pass")
ns = {}
exec(compile(src, 'main.py', 'exec'), ns)
c = ns['c']

def show(name, region):
    print('=' * 20, name, region)
    print(c.matrix_text(region=region))

show('path', (40, 96, 96, 127))
show('bottom-left', (0, 96, 40, 127))
show('bottom-right', (96, 96, 127, 127))
