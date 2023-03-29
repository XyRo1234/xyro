from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class figureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvas(self.fig)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.toolbar)
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def make_plot(self, facet_grid):
        self.fig.clf()
        facet_grid.fig.set_size_inches(self.canvas.figure.get_size_inches())
        self.canvas.figure = facet_grid.fig
        # self.canvas.figure.tight_layout()
        self.canvas.draw()
