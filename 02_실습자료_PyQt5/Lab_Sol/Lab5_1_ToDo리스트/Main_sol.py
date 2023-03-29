import sys, os, json
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.todo = []
        self.loadFile()
        self.btnAdd.clicked.connect(self.addTodo)
        self.btnComplete.clicked.connect(self.makeComplete)
        self.btnDelComplete.clicked.connect(self.delComplete)
        self.btnDelSelect.clicked.connect(self.delSelected)
        self.lstTodo.currentRowChanged.connect(self.lstTodo.setFocus)
        self.lstTodo.itemChanged.connect(self.makeChecked)

    def makeChecked(self, item):
        row = self.lstTodo.row(item)
        self.todo[row][1] = True if item.checkState() == Qt.Checked else False
        self.saveFile()
        self.lstTodo.setFocus()

    def delSelected(self):
        row = self.lstTodo.currentRow()
        self.lstTodo.takeItem(row)
        del self.todo[row]
        self.saveFile()


        # Multi Selection
        # l = self.lstTodo.selectedItems()
        # if l:
        #     for item in l:
        #         row = self.lstTodo.row(item)
        #         self.lstTodo.takeItem(row)
        #         del self.todo[row]
        # self.saveFile()
    def delComplete(self):
        for i in range(self.lstTodo.count() - 1, -1, -1):
            if self.lstTodo.item(i).checkState() == Qt.Checked:
                self.lstTodo.takeItem(i)
                del self.todo[i]

        self.saveFile()

    def makeComplete(self):
        self.lstTodo.currentItem().setCheckState(Qt.Checked)
        self.makeChecked(self.lstTodo.currentItem())

    def addTodoItem(self, todolst):
        new_item = QListWidgetItem()
        new_item.setText(todolst[0])
        new_item.setFlags(new_item.flags() | Qt.ItemIsUserCheckable)
        if todolst[1] == False:
            new_item.setCheckState(Qt.Unchecked)
        else:
            new_item.setCheckState(Qt.Checked)
        self.lstTodo.addItem(new_item)

    def addTodo(self):
        self.todo.append([self.lineEdit.text(), False])
        self.addTodoItem(self.todo[-1])
        self.saveFile()

    def loadFile(self):
        try:
            with open('todo.dat', 'r', encoding='utf-8')as f:
                self.todo = json.load(f)
            for i in self.todo:
                self.addTodoItem(i)
        except:
            print('error')

    def saveFile(self):
        with open('todo.dat', 'w', encoding='utf-8') as f:
            json.dump(self.todo, f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
