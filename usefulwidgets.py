from PyQt5.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QMainWindow, QPushButton
import matplotlib.pyplot as plt
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class CustomDialog(QDialog):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel(text)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class OkThen(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ok Then")
        self.setGeometry(900, 500, 200, 40)


class Chart(QDialog):
    def __init__(self, arrx, arry):
        self.arrx = arrx
        self.arry = arry
        super(Chart, self).__init__()
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.button = QPushButton('Build')
        self.button.clicked.connect(self.build)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def build(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(self.arry, self.arrx, '.')
        self.canvas.draw()
