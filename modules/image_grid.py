from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

class ImageGrid(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ImageGrid, self).__init__(parent)

        self.setAutoFillBackground(True)

        # Create a QColor object with the desired RGB values
        color = QtGui.QColor(35, 35, 35)  # Solid white color

        # Create a QPalette and set the background color
        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, color)
        self.setPalette(palette)

        # Set layouts76
        mainLayout = QtWidgets.QVBoxLayout()
        buttonLayout = QtWidgets.QHBoxLayout()

        # Create widgets for demonstration
        button1 = QtWidgets.QPushButton("Save Project")
        button2 = QtWidgets.QPushButton("Load Project")
        button3 = QtWidgets.QPushButton("Settings")
        button4 = QtWidgets.QPushButton("Log")

        # Add widgets to layouts
        buttonLayout.addWidget(button1)
        buttonLayout.addWidget(button2)
        buttonLayout.addWidget(button3)
        buttonLayout.addWidget(button4)

        mainLayout.addLayout(buttonLayout)
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(5, 5, 5, 5)

        self.setFixedHeight(45)

        self.setLayout(mainLayout)
