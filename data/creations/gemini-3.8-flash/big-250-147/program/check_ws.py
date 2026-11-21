import os
import json

ws_path = os.environ.get("PIXELBENCH_CHECKPOINT")
if ws_path and os.path.exists(ws_path):
    with open(ws_path, 'r') as f:
        data = json.load(f)
        print("Keys in workspace.json:", list(data.keys()))
        if "task" in data:
            print("Task info:", data["task"])
        if "instruction" in data:
            print("Instruction:", data["instruction"])
        if "metadata" in data:
            print("Metadata:", data["metadata"])
else:
    print("No workspace.json found")
