import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file = ''
        self.setupUi(self)

        self.txtEditor1.cursorPositionChanged.connect(self.highlight_current_line)
        self.btnLoad.clicked.connect(self.load_file)
        self.btnSetDoc.clicked.connect(self.set_doc)
        self.btnClear.clicked.connect(self.clear_edit)
        self.doc = self.txtEditor1.document()

        self.txtEditor1.blockCountChanged.connect(lambda x: print('blockCountChanged', x))
        self.txtEditor1.copyAvailable.connect(lambda x: print('copyAvailable', x))
        self.txtEditor1.redoAvailable.connect(lambda x: print('redoAvailable', x))
        self.txtEditor1.undoAvailable.connect(lambda x: print('undoAvailable', x))
        self.txtEditor1.selectionChanged.connect(lambda: print('selectionChanged'))
        self.txtEditor1.modificationChanged.connect(lambda x: print('modificationChanged', x))

    def highlight_current_line(self):
        selection = QTextEdit.ExtraSelection()
        color = QColor(Qt.yellow).lighter()
        selection.format.setBackground(color)
        selection.format.setProperty(QTextFormat.FullWidthSelection, True)
        selection.cursor = self.txtEditor1.textCursor()
        self.txtEditor1.setExtraSelections([selection])

    def load_file(self):
        with open('Main.py', 'rt', encoding='utf-8') as f:
            s = f.read()
            self.doc.setPlainText(s)
            self.doc.setModified(False)

    def set_doc(self):
        self.txtEditor2.setDocument(self.doc)

    def clear_edit(self):
        self.txtEditor1.clear()
        self.doc.setModified(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    app.installEventFilter(w)
    w.show()
    sys.exit(app.exec_())
