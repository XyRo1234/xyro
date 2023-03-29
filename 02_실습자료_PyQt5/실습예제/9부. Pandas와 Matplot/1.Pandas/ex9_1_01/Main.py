import sys, os

from PyQt5.QtWidgets import *
import numpy as np

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
        self.btnStudent.clicked.connect(self.countStudent)
        self.btnAve.clicked.connect(self.calAverage)
        self.cboGrade.currentTextChanged.connect(self.viewGrade)

    def viewGrade(self, txt):
        if txt:
            if txt == 'ALL':
                df = self.df
            else:
                df = self.df[self.df.grade == int(txt)].copy()
            self.drawDf(df)

    def drawDf(self, df):
        model = pandasModel(df)
        self.tableView.setModel(model)

        self.tableView.resizeColumnsToContents()

    def openFile(self):
        file_name = 'score.csv'
        self.df = pd.read_csv(file_name)
        arr = np.sort(self.df.grade.unique())
        self.cboGrade.clear()
        self.cboGrade.addItem('ALL')
        self.cboGrade.addItems([str(x) for x in arr])
        self.drawDf(self.df)

    def calAverage(self):
        df = self.df.copy()
        df = df.set_index('names')
        df = df.loc[:, 'kor':'mat']
        df['합계'] = df.sum(axis=1)
        df['평균'] = df.loc[:, 'kor':'mat'].mean(axis=1).round()
        self.drawDf(df)

    def countStudent(self):
        df = self.df.copy()
        grade = df['grade'].value_counts()
        df2 = grade.to_frame(name='학생수').sort_index()
        df2.rename(index=lambda x: str(x) + '학년', inplace=True)
        self.drawDf(df2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
