from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QPainter, QColor, QPen
import math
from frondend.client import fetch_targets

class Radar(QWidget):
      def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyber-Radar")
        self.setGeometry(100, 100, 800, 800)
        
        self.angle = 0
        self.targets = []
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_radar)
        
        self.timer.start(50)
        self._fetch_counter = 0
        
      def update_radar(self):
        self.angle += 0.05
        if self.angle >= 2 * math.pi:
          self.angle = 0

        self._fetch_counter += 1
        if self._fetch_counter >= 10:
          self._fetch_counter = 0
          try:
            self.targets = fetch_targets(timeout=0.5)
          except Exception:
            pass

        self.update()

      def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.fillRect(self.rect(), QColor(10, 10, 10))

        cx, cy = self.width() // 2, self.height() // 2
        pen = QPen(QColor(0, 255, 0), 1)
        painter.setPen(pen)

        for r in range(100, 400, 100):
          painter.drawEllipse(cx - r, cy - r, r * 2, r * 2)

        x = cx + 350 * math.cos(self.angle)
        y = cy + 350 * math.sin(self.angle)
        painter.setPen(QPen(QColor(0, 255, 0), 3))
        painter.drawLine(cx, cy, int(x), int(y))

        for t in self.targets:
          try:
            color = QColor(255, 50, 50) if t.get("danger") else QColor(0, 255, 0)
            painter.setPen(QPen(color, 5))
            px = cx + int(t.get("x", 0))
            py = cy + int(t.get("y", 0))
            painter.drawPoint(px, py)
          except Exception:
            continue