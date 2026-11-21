"""Append-only episode events, durable even if the agent loop is interrupted."""
import json
import os
import time


class EventLog(list):
    def __init__(self, path=None):
        super().__init__()
        self.path = path

    def append(self, event):
        row = dict(event, timestamp=time.time())
        if self.path is not None:
            with self.path.open('a', encoding='utf-8') as stream:
                stream.write(json.dumps(row, ensure_ascii=False) + '\n')
                stream.flush()
                os.fsync(stream.fileno())
        super().append(row)
