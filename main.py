import sys
import threading
import uvicorn
from PyQt5.QtWidgets import QApplication
from frondend.radar_ui import Radar 

def run_api():
    uvicorn.run("backend.app:app", host="127.0.0.1", port=8000)
    
if __name__ == "__main__":
    threading.Thread(target = run_api, daemon = True).start()
    app = QApplication(sys.argv)
    win = Radar()
    win.show()
    sys.exit(app.exec_())    