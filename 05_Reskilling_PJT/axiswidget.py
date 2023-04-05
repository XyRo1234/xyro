
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import*
import matplotlib.pyplot as plt
from matplotlib import tight_layout
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class axisWidget(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)



