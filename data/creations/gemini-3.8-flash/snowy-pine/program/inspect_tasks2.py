import pixelbench.tasks
import os

print(dir(pixelbench.tasks))
t_dir = os.path.dirname(pixelbench.tasks.__file__)
print("tasks dir:", t_dir)
print("files in tasks:", os.listdir(t_dir))
