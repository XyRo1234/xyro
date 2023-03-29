import sys

from PyQt5.QtCore import QModelIndex
from PyQt5.QtWidgets import QApplication, QMainWindow
from pandas import DataFrame,read_csv
from pandasModel import pandasModel
from gui import Ui_MainWindow

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.df = DataFrame()
        self.openFile()

        # signal
        self.tableView.verticalHeader().sectionClicked.connect(self.drawBar)
        self.tableView.clicked.connect(self.drawBar)


    def drawBar(self, index):
        if isinstance(index, QModelIndex):
            row = index.row()
        else:
            row = index

        subject = self.df.columns[5:8]
        score = self.df.iloc[row, 5:8]
        self.widget.ax.clear()
        self.widget.ax.bar(subject, score)
        self.widget.ax.set_title(self.df.iloc[row,0])
        self.widget.ax.set_xlabel('Subject')
        self.widget.ax.set_ylabel('Score')
        self.widget.fig.tight_layout()
        self.widget.canvas.draw()

    def openFile(self):
        file_name = 'score.csv'
        self.df = read_csv(file_name)
        model = pandasModel(self.df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
