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
        MainWindow.resize(242, 194)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnPush = QtWidgets.QPushButton(self.centralwidget)
        self.btnPush.setEnabled(True)
        self.btnPush.setGeometry(QtCore.QRect(10, 10, 111, 81))
        self.btnPush.setIconSize(QtCore.QSize(32, 32))
        self.btnPush.setObjectName("btnPush")
        self.btnToggle = QtWidgets.QPushButton(self.centralwidget)
        self.btnToggle.setEnabled(True)
        self.btnToggle.setGeometry(QtCore.QRect(10, 100, 111, 81))
        self.btnToggle.setCheckable(True)
        self.btnToggle.setObjectName("btnToggle")
        self.lblColor = QtWidgets.QLabel(self.centralwidget)
        self.lblColor.setGeometry(QtCore.QRect(130, 10, 91, 81))
        self.lblColor.setFrameShape(QtWidgets.QFrame.Box)
        self.lblColor.setText("")
        self.lblColor.setAlignment(QtCore.Qt.AlignCenter)
        self.lblColor.setObjectName("lblColor")
        self.lblState = QtWidgets.QLabel(self.centralwidget)
        self.lblState.setGeometry(QtCore.QRect(130, 100, 91, 81))
        self.lblState.setStyleSheet("")
        self.lblState.setFrameShape(QtWidgets.QFrame.Box)
        self.lblState.setText("")
        self.lblState.setAlignment(QtCore.Qt.AlignCenter)
        self.lblState.setObjectName("lblState")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Push Button Test"))
        self.btnPush.setText(_translate("MainWindow", "색상 변경"))
        self.btnPush.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.btnToggle.setText(_translate("MainWindow", "OFF"))
        self.btnToggle.setShortcut(_translate("MainWindow", "Ctrl+P"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
