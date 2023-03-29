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

        self.setupUi(self)
        self.toolAlign = QToolButton()
        self.makeToolButton()
        self.setActionConnect()
        self.curFile = ''

    def makeToolButton(self):
        self.toolBar.insertWidget(self.actionClose, self.toolAlign)
        self.toolBar.insertSeparator(self.actionClose)
        self.toolAlign.setMenu(self.menu_Align)
        self.toolAlign.setDefaultAction(self.actionLeftAlign)
        self.toolAlign.setPopupMode(QToolButton.InstantPopup)

    def setActionConnect(self):
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSaveAs.triggered.connect(self.saveAsFile)
        self.actionClose.triggered.connect(self.exitProgram)
        self.actionCopy.triggered.connect(self.txtDocument.copy)
        self.actionCut.triggered.connect(self.txtDocument.cut)
        self.actionPaste.triggered.connect(self.txtDocument.paste)
        self.actionUndo.triggered.connect(self.txtDocument.undo)
        self.actionRedo.triggered.connect(self.txtDocument.redo)
        self.actionFont.triggered.connect(self.selectFont)
        self.actionBold.triggered.connect(self.setBold)
        self.actionItalic.triggered.connect(self.txtDocument.setFontItalic)
        self.actionUderline.triggered.connect(self.txtDocument.setFontUnderline)

        self.actionLeftAlign.triggered.connect(lambda: self.txtDocument.setAlignment(Qt.AlignLeft))
        self.actionCenterAlign.triggered.connect(lambda: self.txtDocument.setAlignment(Qt.AlignCenter))
        self.actionRightAlign.triggered.connect(lambda: self.txtDocument.setAlignment(Qt.AlignRight))
        self.actionJsutify.triggered.connect(lambda: self.txtDocument.setAlignment(Qt.AlignJustify))

        self.toolAlign.triggered.connect(self.toolAlign.setDefaultAction)

    def newFile(self):
        self.curFile = ''
        self.txtDocument.clear()
        self.setWindowTitle('Note Pad')

    def openFile(self):
        # dialog 이후
        filename, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'txt file(*.txt);;Python Files(*.py)')

        if filename:
            self.curFile = filename
            with open(filename, 'r') as file:
                self.setWindowTitle(QFileInfo(filename).fileName())
                txt = file.read()
                self.txtDocument.setText(txt)

            self.setWindowTitle(filename.split('/')[-1])

    def saveFile(self):
        if self.curFile:
            filename = self.curFile
            with open(filename, 'w') as file:
                file.write(self.txtDocument.toPlainText())
        else:
            self.saveAsFile()

        self.setWindowTitle(QFileInfo(self.curFile).fileName())

    def saveAsFile(self):
        filename, fileext = QFileDialog.getSaveFileName(self, 'Save File', '',
                                                        'txt file(*.txt);;Python Files(*.py)')
        if filename:
            self.curFile = filename
            self.setWindowTitle(QFileInfo(filename).fileName())

            with open(filename, 'w') as file:
                file.write(self.txtDocument.toPlainText())

    def exitProgram(self):
        QApplication.exit()

    def selectFont(self):
        font, result = QFontDialog().getFont()
        self.txtDocument.setFont(font) if result else None

    def setBold(self, bold):
        self.txtDocument.setFontWeight(QFont.Bold if bold else QFont.Normal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
