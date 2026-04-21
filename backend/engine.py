from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.1)

def train():
    data = np.random.randint(-300, 300, size=(200, 2)).astype(float)
    model.fit(data)

def predict(x, y):
    arr = np.array([[float(x), float(y)]])
    pred = model.predict(arr)
    # Convert numpy types to native Python types for JSON serialization
    return bool(pred[0] == -1)