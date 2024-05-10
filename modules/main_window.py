import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtGui import QPalette, QColor, QIcon
from .navbar import NavBar

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Default window settings
        self.setWindowTitle("FoC-o-Matic 6000")
        self.setWindowIcon(QIcon("icon.ico"))
        self.setMinimumSize(800, 600)

        # Setup the main layout
        MainWindowLayout = QVBoxLayout()
        ImageEditorLayout = QHBoxLayout()

        # Add the navbar
        MainWindowLayout.addWidget(NavBar())

        # Add the image editor layout
        MainWindowLayout.addLayout(ImageEditorLayout)

        # Add the image grid
        ImageEditorLayout.addWidget(Color("blue"))

        # Add the image data editor
        ImageEditorLayout.addWidget(Color("green"))

        widget = QWidget()
        widget.setLayout(MainWindowLayout)
        self.setCentralWidget(widget)

        self.show()

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        