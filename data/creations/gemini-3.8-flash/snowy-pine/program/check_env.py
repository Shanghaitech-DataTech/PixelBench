import os, sys

print("Current dir:", os.getcwd())
print("Files in dir:", os.listdir('.'))
if os.path.exists('..'):
    print("Files in parent:", os.listdir('..'))

try:
    print("reference:", reference)
except Exception as e:
    print("reference err:", e)

try:
    print("reference_frames:", reference_frames)
except Exception as e:
    print("reference_frames err:", e)

try:
    print("mask:", mask)
except Exception as e:
    print("mask err:", e)
