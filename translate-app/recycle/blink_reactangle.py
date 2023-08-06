import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen

class Overlay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setGeometry(0, 0, 1366, 768)  # Set to your screen resolution
        self.show()

        self.show_rect = False
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.toggle_rect)
        self.timer.start(200)

    def toggle_rect(self):
        self.show_rect = not self.show_rect
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(Qt.PenStyle.NoPen)  # No border
        painter.setPen(pen)

        brush = QBrush(QColor(0, 0, 0, 0))  # Transparent background
        painter.setBrush(brush)
        painter.drawRect(self.rect())

        if self.show_rect:
            painter.setPen(QColor(255, 0, 0))
            painter.drawRect(100, 100, 300, 200)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    overlay = Overlay()
    sys.exit(app.exec())
