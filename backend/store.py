from collections import deque
import threading

_targets = deque(maxlen = 100)
_lock = threading.Lock()

def add_target(t):
    with _lock:
        _targets.append(t)
        
def get_targets():
    with _lock:
        return list(_targets)        