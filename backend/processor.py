import threading
import random
import time
from backend.store import add_target
from backend.engine import predict, train


def process():
    train()
    while True:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)

        danger = predict(x, y)

        add_target({
            "x": x,
            "y": y,
            "danger": danger,
        })
        
        time.sleep(0.1)


def start_processing():
    threading.Thread(target=process, daemon=True).start()