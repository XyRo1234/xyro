import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class myDelegate(QItemDelegate):

    def __init__(self, data=None):
        super().__init__()
        trans = list(map(set, zip(*data[1:])))
        self.brand = sorted(list(trans[1]))
        self.star = QPixmap('star.png')
        self.lstar = QPixmap('lstar.png')
        self.rstar = QPixmap('rstar.png')

    def createEditor(self, parent, option, index):
        if index.column() == 0:
            editor = QSpinBox(parent)
            editor.setMinimum(0)
            editor.setMaximum(10000)
            return editor
        if index.column() == 1:
            editor = QComboBox(parent)
            editor.addItems(self.brand)
            return editor
        return super().createEditor(parent, option, index)

    def setEditorData(self, obj, index):
        value = index.model().data(index, Qt.EditRole)
        if index.column() == 0:
            obj.setValue(int(value))
        elif index.column() == 1:
            obj.setCurrentText(value)
        else:
            super().setEditorData(obj, index)

    def setModelData(self, obj, model, index):
        if index.column() == 0:
            value = obj.value()
        elif index.column() == 1:
            value = obj.currentText()
        else:
            value = obj.text()
            super().setModelData(obj, model, index)
        model.setData(index, value, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        print(option)
        editor.setGeometry(option.rect)

    def paint(self, painter, option, index):
        if index.column() != 5:
            super().paint(painter, option, index)
        else:
            model = index.model()
            if model.data(index, Qt.DisplayRole).replace('.', '', 1).isdigit():
                rating = int(float(model.data(index, Qt.DisplayRole)) * 2)
                width = self.lstar.width()
                height = self.lstar.height()
                x = option.rect.x()
                y = option.rect.y() + (option.rect.height() / 2) - (height / 2)
                img = [self.lstar, self.rstar]

                for i in range(0, rating):
                    painter.drawPixmap(x, y, img[i % 2])
                    x += width
            else:
                super().paint(painter, option, index)


class TableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self.contents = data or []

    def data(self, index, role):
        if index.row() >= len(self.contents) - 1:
            return QVariant()
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.contents[index.row() + 1][index.column()]
        return QVariant()

    def setData(self, index, any, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            self.contents[index.row() + 1][index.column()] = any
        return True

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return QVariant()
        if orientation == Qt.Horizontal:
            return self.contents[0][section]
        else:
            return section + 1

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable

    def rowCount(self, index):
        return len(self.contents) - 1

    def columnCount(self, index):
        return len(self.contents[0])


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.data = None
        self.setupUi(self)
        self.data = None
        self.loadFile()
        self.model = TableModel(self.data)
        self.tableView.setModel(self.model)
        self.delegate = myDelegate(self.data)
        self.tableView.setItemDelegate(self.delegate)

    def loadFile(self):
        with open('ramen.csv', 'r') as f:
            self.data = [line.split(',') for line in f.read().splitlines()]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
