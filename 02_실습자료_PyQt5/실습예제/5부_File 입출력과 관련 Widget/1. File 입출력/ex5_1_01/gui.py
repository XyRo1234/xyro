# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(377, 137)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(10, 10, 111, 23))
        self.btnNew.setObjectName("btnNew")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setEnabled(False)
        self.btnAdd.setGeometry(QtCore.QRect(10, 40, 111, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 40, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.btnRead = QtWidgets.QPushButton(self.centralwidget)
        self.btnRead.setGeometry(QtCore.QRect(10, 70, 111, 23))
        self.btnRead.setObjectName("btnRead")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnNew.setText(_translate("MainWindow", "새 파일 만들기"))
        self.btnAdd.setText(_translate("MainWindow", "현재 파일에 추가"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "파일에 추가할 문자열 입력"))
        self.btnRead.setText(_translate("MainWindow", "파일 읽어 오기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
