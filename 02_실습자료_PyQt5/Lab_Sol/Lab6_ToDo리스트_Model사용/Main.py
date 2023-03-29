import sys, json, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class MyModel(QAbstractListModel):
    def __init__(self, todos=None):
        super().__init__()
        self.todos = todos or []

    def setData(self, index, any, role=None):
        if role != Qt.DisplayRole and role != Qt.CheckStateRole: return False
        r = index.row()
        print(any)
        if role==Qt.DisplayRole or Qt.EditRole:
            status, text = self.todos[r]
            self.todos[r] = [not status, text]

        if role==Qt.CheckStateRole:
            if any == Qt.Checked:
                self.todos[r][0] = True
            else:
                self.todos[r][0] = False
        self.dataChanged.emit(index,index)
        return True

        # if not index.isValid() or role != Qt.CheckStateRole:
        #     return False
        # row = index.row()
        # status, text = self.todos[row]
        # self.todos[row] = [not status, text]
        # self.dataChanged.emit(index, index)
        # return True    


    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable

    def data(self, index, role):
        r = index.row()
        if role==Qt.DisplayRole:
            return self.todos[index.row()][1]    # [T/F, 할일]
        if role==Qt.CheckStateRole:
            if self.todos[r][0]:
                return Qt.Checked
            else:
                return Qt.Unchecked
        return QVariant()

    def rowCount(self, index=None):
        return len(self.todos)


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # make empty
        self.model = MyModel()
        self.loadFile()
        self.lstTodo.setModel(self.model)

        self.btnAdd.clicked.connect(self.add)
        self.btnDelete.clicked.connect(self.delete)
        self.btnComplete.clicked.connect(self.complete)
        self.btnDelComplet.clicked.connect(self.completeDel)
        self.lineEdit.returnPressed.connect(self.add)
        self.model.dataChanged.connect(self.saveFile)


    def add(self):
        text = self.lineEdit.text()
        if text:
            self.model.todos.append([False,text])
            self.model.layoutChanged.emit()
            self.lineEdit.setText('')
            self.lineEdit.setFocus()
            self.saveFile()

    def delete(self):
        row = self.lstTodo.currentIndex().row()
        del self.model.todos[row]
        self.model.layoutChanged.emit()
        self.lstTodo.clearSelection()
        self.saveFile()

    def complete(self):
        indexes = self.lstTodo.selectedIndexes()
        for index in indexes:
            r = index.row()
            self.model.todos[r][0] = True
        self.model.layoutChanged.emit()
        self.lstTodo.clearSelection()
        self.saveFile()

    def completeDel(self):
        self.model.todos = [val for val in self.model.todos if val[0] == False]
        self.model.layoutChanged.emit()
        self.saveFile()

    def loadFile(self):
        try:
            with open('data.db', 'r')as f:
                self.model.todos = json.load(f)
        except:
            print('error')

    def saveFile(self):
        with open('data.db', 'w') as f:
            json.dump(self.model.todos, f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
