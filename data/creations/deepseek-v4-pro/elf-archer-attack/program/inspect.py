from pixelbench_api import *

c = input_canvas
# Print with coordinate rulers
print("   " + "".join(str((i//5)%10) if i%5==0 else " " for i in range(35)))
print("   " + "".join(str(i%10) for i in range(35)))
lines = c.matrix_text(region=(0,0,34,46)).splitlines()
for r,line in enumerate(lines):
    print(f"{r:2d} {line}")
