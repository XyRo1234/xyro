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
        if not index.isValid() or role != Qt.CheckStateRole:
            return False
        row = index.row()
        status, text = self.todos[row]
        self.todos[row] = [not status, text]
        self.dataChanged.emit(index, index)
        return True

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsUserCheckable

    def data(self, index, role):

        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.CheckStateRole:
            row = index.row()
            status, text = self.todos[row]
            if status:
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
        self.model = MyModel()
        self.loadFile()
        self.lstTodo.setModel(self.model)
        self.btnAdd.clicked.connect(self.add)
        self.btnDelete.clicked.connect(self.delete)
        self.btnComplete.clicked.connect(self.complete)
        self.btnDelComplet.clicked.connect(self.completeDel)
        self.lineEdit.editingFinished.connect(self.add)
        self.model.dataChanged.connect(self.saveFile)

    def add(self):
        text = self.lineEdit.text()
        if text:
            self.model.todos.append([False, text])
            self.model.layoutChanged.emit()
            self.lineEdit.setText("")
            self.lineEdit.setFocus()
            self.saveFile()

    def delete(self):
        row = self.lstTodo.currentIndex().row()
        del self.model.todos[row]
        self.model.layoutChanged.emit()
        self.lstTodo.clearSelection()
        self.saveFile()

        # Multi Select
        # indexes = self.lstTodo.selectedIndexes()
        # if indexes:
        #     delitem = [self.model.todos[index.row()] for index in indexes]
        #     for val in delitem:
        #         self.model.todos.remove(val)
        #
        #     self.model.layoutChanged.emit()
        #     self.lstTodo.clearSelection()
        #     self.saveFile()

    def complete(self):
        indexes = self.lstTodo.selectedIndexes()
        if indexes:
            for index in indexes:
                row = index.row()
                self.model.todos[row][0] = True
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
