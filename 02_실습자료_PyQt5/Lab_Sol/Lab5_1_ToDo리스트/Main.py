import sys, os, json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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
        self.btnComplete.clicked.connect(self.makeComplete)     # 완료표시
        self.btnDelComplete.clicked.connect(self.delComplete)   # 완료된것삭제
        self.btnDelSelect.clicked.connect(self.delSelected)     # 선택된것삭제
        self.lstTodo.currentRowChanged.connect(self.lstTodo.setFocus)
        self.lstTodo.itemChanged.connect(self.lstTodo.mark)     # 아이템에 마우스로 체크를 했을때

    def mark(self, item):
        row = self.lstTodo.row(item)
        if item.checkState()==Qt.Checked: self.todo[row][1]=True
        else: self.todo[row][1]=False
        self.saveFile()

    def delSelected(self):
        row = self.lstTodo.currentRow()
        self.lstTodo.takeItem(row)
        # self.todo.remove(self.todo[row])
        del self.todo[row]
        self.saveFile()

    def delComplete(self):
        for i in range(self.lstTodo.count()-1,-1,-1):
            if self.lstTodo.item(i) == Qt.Checked:
                self.lstTodo.takeItem(1)
                del self.todo[i]
        self.saveFile()    

    def makeComplete(self):
        item = self.lstTodo.currentItem()
        item.setCheckState(Qt.Checked)
        self.todo[self.lstTodo.currentRow()][1] = True
        self.saveFile()

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
        name = self.lineEdit.text()
        self.todo.append([name, False])
        item = QListWidgetItem()
        item.setText(name)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)
        self.lstTodo.addItem(item)
        
        self.saveFile()

        self.lineEdit.setText('')
        self.lineEdit.setFocus()


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
