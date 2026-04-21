# 🛰️ CyberRadar-X (Elite Edition)

A real-time cybersecurity visualization and anomaly detection system built with Python.

## 🔥 Overview

CyberRadar-X simulates a Security Operations Center (SOC) radar:

* Captures network-like traffic
* Processes and analyzes behavior
* Detects anomalies using AI (Isolation Forest)
* Visualizes threats in real-time

## 🧠 Features

* 📡 Real-time radar visualization (PyQt5)
* ⚡ FastAPI backend (REST API)
* 🤖 AI anomaly detection (scikit-learn)
* 🔄 Multi-threaded processing
* 📊 Expandable dashboard system

## 🏗️ Architecture

* Backend: FastAPI + AI Engine
* Frontend: PyQt5 Radar UI
* Data Flow: Processor → Store → API → UI

## 🚀 Installation

```bash
git clone https://github.com/yourusername/cyberradar-x.git
cd cyberradar-x

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

## ▶️ Run

```bash
python main.py
```

* Before API runs at: http://127.0.0.1:8000/docs
* After to see response run at : http://127.0.0.1:8000/targets
* Radar UI launches automatically

## ⚠️ Disclaimer

This project is for educational and research purposes only.

## 👨‍💻 Author

Moe Htet Ar Kar (Phoe Cho)
Cybersecurity Engineer & Python Developer
