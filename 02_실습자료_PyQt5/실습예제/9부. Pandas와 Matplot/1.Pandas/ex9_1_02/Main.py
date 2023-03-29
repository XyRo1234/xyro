import sys, os

from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow
from pandasModel import *


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.df = pd.DataFrame()
        # signal
        self.btnOpen.clicked.connect(self.openFile)
        self.cboCountry.currentTextChanged.connect(self.viewCountry)

    def viewCountry(self, txt):
        if txt:
            if txt == 'ALL':
                df = self.df
            else:
                df = self.df.groupby('Country').get_group(txt)
            self.drawDf(df)

    def drawDf(self, df):
        model = pandasModel(df)
        self.tableView.setModel(model)

        self.tableView.resizeColumnsToContents()

    def openFile(self):
        file_name = 'ramen.csv'
        self.df = pd.read_csv(file_name)

        df = self.df.copy()

        self.cboCountry.addItem('ALL')
        self.cboCountry.addItems(df.groupby('Country').groups.keys())
        self.drawDf(self.df)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
