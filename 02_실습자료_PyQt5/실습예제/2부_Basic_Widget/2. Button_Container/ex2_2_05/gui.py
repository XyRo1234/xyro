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
        MainWindow.resize(329, 157)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 311, 71))
        self.groupBox.setObjectName("groupBox")
        self.chkC = QtWidgets.QCheckBox(self.groupBox)
        self.chkC.setGeometry(QtCore.QRect(20, 20, 82, 17))
        self.chkC.setTristate(False)
        self.chkC.setObjectName("chkC")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.setExclusive(False)
        self.buttonGroup.addButton(self.chkC)
        self.chkCpp = QtWidgets.QCheckBox(self.groupBox)
        self.chkCpp.setGeometry(QtCore.QRect(180, 20, 82, 17))
        self.chkCpp.setTristate(False)
        self.chkCpp.setObjectName("chkCpp")
        self.buttonGroup.addButton(self.chkCpp)
        self.chkJava = QtWidgets.QCheckBox(self.groupBox)
        self.chkJava.setGeometry(QtCore.QRect(20, 40, 82, 17))
        self.chkJava.setTristate(False)
        self.chkJava.setObjectName("chkJava")
        self.buttonGroup.addButton(self.chkJava)
        self.chkPython = QtWidgets.QCheckBox(self.groupBox)
        self.chkPython.setGeometry(QtCore.QRect(180, 40, 82, 17))
        self.chkPython.setTristate(False)
        self.chkPython.setObjectName("chkPython")
        self.buttonGroup.addButton(self.chkPython)
        self.lblMsg = QtWidgets.QLabel(self.centralwidget)
        self.lblMsg.setGeometry(QtCore.QRect(20, 90, 281, 20))
        self.lblMsg.setStyleSheet("color: rgb(0, 0, 255);")
        self.lblMsg.setObjectName("lblMsg")
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(240, 120, 75, 23))
        self.btnOK.setObjectName("btnOK")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.chkC, self.chkCpp)
        MainWindow.setTabOrder(self.chkCpp, self.chkJava)
        MainWindow.setTabOrder(self.chkJava, self.chkPython)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "나는 할 수 있다"))
        self.chkC.setText(_translate("MainWindow", "C"))
        self.chkCpp.setText(_translate("MainWindow", "C++"))
        self.chkJava.setText(_translate("MainWindow", "Java"))
        self.chkPython.setText(_translate("MainWindow", "Python"))
        self.lblMsg.setText(_translate("MainWindow", "나는 C, C++, Java, Python 언어를 사용할 수 있다"))
        self.btnOK.setText(_translate("MainWindow", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
