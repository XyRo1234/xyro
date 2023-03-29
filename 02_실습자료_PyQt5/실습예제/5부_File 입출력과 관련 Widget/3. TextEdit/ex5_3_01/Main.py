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

        self.textEdit.cursorPositionChanged.connect(self.textEdit.setFocus)
        self.textEdit.textChanged.connect(self.textEdit.setFocus)

        self.textEdit.installEventFilter(self)

        self.btnChange.clicked.connect(self.select_change)
        self.btnImage.clicked.connect(self.insert_image)
        self.btnImage2.clicked.connect(self.insert_image2)
        self.btnImage3.clicked.connect(self.insert_image3)
        self.btnTable.clicked.connect(self.insert_table)
        self.btnList.clicked.connect(self.insert_list)
        self.btninsert.clicked.connect(self.insert_frame)

        self.btnMovePos.clicked.connect(self.move_pos)
        self.btnSetPos.clicked.connect(self.set_pos)

        with open('Main.py', 'rt', encoding='utf-8') as f: self.textEdit.setText(f.read())

    def move_pos(self):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.Down, QTextCursor.KeepAnchor, 3)
        self.textEdit.setTextCursor(cursor)

    def set_pos(self):
        cursor = self.textEdit.textCursor()
        cursor.setPosition(10, QTextCursor.MoveAnchor)
        cursor.setPosition(20, QTextCursor.KeepAnchor)
        self.textEdit.setTextCursor(cursor)

    def select_change(self):
        cursor = self.textEdit.textCursor()
        fmt = QTextCharFormat()
        fmt.setForeground(Qt.red)
        fmt.setBackground(Qt.yellow)
        fmt.setFontItalic(True)
        cursor.mergeCharFormat(fmt)
        cursor.clearSelection()
        self.textEdit.setTextCursor(cursor)

    def insert_frame(self):
        cursor = self.textEdit.textCursor()
        fmt = QTextFrameFormat()
        fmt.setBorder(QTextFrameFormat.BorderStyle_Solid)
        fmt.setWidth(50)

        cursor.insertFrame(fmt)

    def insert_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, '이미지 추가', ".",
                                                  "이미지 파일 (*.png *.xpm *.jpg *.bmp *.gif)")
        if not filename:
            QMessageBox.critical(self, "이미지 파일 오류", "이미지 파일을 선택해 주세요")
        else:
            image = QImage(filename)
            self.textEdit.document().addResource(QTextDocument.ImageResource, QUrl('pic1'), image)
            cursor = self.textEdit.textCursor()
            fmt = QTextImageFormat()
            fmt.setName('pic1')
            fmt.setWidth(40)
            fmt.setHeight(40)
            cursor.insertImage(fmt)

    def insert_image2(self):
        cursor = self.textEdit.textCursor()
        filename, _ = QFileDialog.getOpenFileName(self, '이미지 추가', ".",
                                                  "이미지 파일 (*.png *.xpm *.jpg *.bmp *.gif)")
        if not filename:
            QMessageBox.critical(self, "이미지 파일 오류", "이미지 파일을 선택해 주세요")
        else:
            cursor.insertImage(QImage(filename), name='pic2')

    def insert_image3(self):
        cursor = self.textEdit.textCursor()
        r = self.textEdit.document().resource(QTextDocument.ImageResource, QUrl('pic1'))
        if r:
            cursor.insertImage('pic1')

    def insert_table(self):
        cursor = self.textEdit.textCursor()
        pad = 5
        space = 0
        fmt = QTextTableFormat()
        fmt.setCellPadding(pad)
        fmt.setCellSpacing(space)

        fmt.setWidth(self.textEdit.width() - 10)
        len = []
        len.append(QTextLength(QTextLength.PercentageLength, 25))
        len.append(QTextLength(QTextLength.PercentageLength, 25))
        len.append(QTextLength(QTextLength.PercentageLength, 25))
        len.append(QTextLength(QTextLength.PercentageLength, 25))
        fmt.setColumnWidthConstraints(len)

        cursor.insertTable(3, 4, fmt)

    def insert_list(self):
        cursor = self.textEdit.textCursor()

        fmt = QTextListFormat()
        fmt.setNumberPrefix('제')
        fmt.setNumberSuffix('장')
        fmt.setStyle(QTextListFormat.ListDecimal)
        cursor.insertList(fmt)

        # cursor.createList(QTextListFormat.ListCircle)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    app.installEventFilter(w)
    w.show()
    sys.exit(app.exec_())
