import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class MyModel(QAbstractListModel):
    def __init__(self, strlist=None):
        super().__init__()
        self.strlist = strlist or []

    def rowCount(self, parent=None):
        # print('rowCount')
        return len(self.strlist)

    def data(self, index, role):        # view에서 Role별로 data를 읽어감. 그에 맞게 가져갈 Data를 설정해줌.
        r = index.row()
        # print(self.strlist[r])
        if role==Qt.DisplayRole or role==Qt.EditRole:
            return self.strlist[r]
        if role==Qt.BackgroundRole:
            if r%2: return QColor('yellow')
            else: return QColor('green')
        return QVariant()

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable   # 더블클릭시 수정모드로 진입

    def setData(self, index, any, role=Qt.EditRole):
        r = index.row()
        if role != Qt.EditRole: return False
        self.strlist[r] = any
        self.dataChanged.emit(index, index)     # setData는 dataChanged 시그널을 꼭 방출해줘야한다.
        return True

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole: return QVariant()
        if orientation == Qt.Horizontal:
            return f'column:{section}'
        else:
            return f'row:{section}'

    # def insertRow(self, pos):
    #     pass

    # def removeRow(self, pos):
    #     pass


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        data = ['item1', 'item2', 'item3', 'item4', 'item5']
        self.model = MyModel(data)
        self.listView.setModel(self.model)
        self.tableView.setModel(self.model)

        self.btnAdd.clicked.connect(self.addData)
        self.btnInsert.clicked.connect(self.insertData)
        self.btnDelete.clicked.connect(self.deleteData)
        self.model.dataChanged.connect(self.dataChange)

    def dataChange(self, index):
        print('data changed:', index.data())

    def addRow(self, index):
        if self.lineEdit.text():
            self.model.setData(index, self.lineEdit.text())
        else:
            self.listView.edit(index)
        self.listView.setCurrentIndex(index)

    def addData(self):
        row = self.model.rowCount(QModelIndex())
        self.model.insertRow(row)
        index = self.model.index(row)
        self.addRow(index)

    def insertData(self):
        row = self.listView.currentIndex().row()
        self.model.insertRow(row)
        index = self.model.index(row)
        self.addRow(index)

    def deleteData(self):
        self.model.removeRow(self.listView.currentIndex().row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
