import sys, os

from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow
from pandasModel import *


# 한글 지원
# import matplotlib
# import matplotlib.font_manager as fm
# fm.get_fontconfig_fonts()
# font_location = 'C:/Windows/Fonts/gulim.ttc' # For Windows
# font_name = fm.FontProperties(fname=font_location).get_name()
# matplotlib.rc('font', family=font_name)

class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.df = pd.DataFrame()
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
        # Todo 1: subject와 score를 사용하여 bar 그래프 그리기
        # Todo 2: 해당학생의 이름을 title에 표시
        # Todo 3: xlabel과 ylabel 추가

    def openFile(self):
        file_name = 'score.csv'
        self.df = pd.read_csv(file_name)
        model = pandasModel(self.df)
        self.tableView.setModel(model)
        self.tableView.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
