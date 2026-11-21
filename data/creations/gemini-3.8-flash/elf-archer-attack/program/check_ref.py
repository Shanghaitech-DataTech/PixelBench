import sys
for var in ['reference', 'reference_frames', 'mask']:
    if var in globals():
        print(f"{var} is present: {type(eval(var))}")
    else:
        print(f"{var} is not present")
