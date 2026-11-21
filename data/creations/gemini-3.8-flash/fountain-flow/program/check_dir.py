import os
print("cwd:", os.getcwd())
print("cwd listdir:", os.listdir('.'))
if os.path.exists('..'):
    print("parent listdir:", os.listdir('..'))
