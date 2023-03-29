# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_sol.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(246, 119)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.radioMale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioMale.setGeometry(QtCore.QRect(60, 50, 51, 17))
        self.radioMale.setChecked(True)
        self.radioMale.setObjectName("radioMale")
        self.grpGender = QtWidgets.QButtonGroup(MainWindow)
        self.grpGender.setObjectName("grpGender")
        self.grpGender.addButton(self.radioMale)
        self.radioFemale = QtWidgets.QRadioButton(self.centralwidget)
        self.radioFemale.setGeometry(QtCore.QRect(120, 50, 51, 17))
        self.radioFemale.setObjectName("radioFemale")
        self.grpGender.addButton(self.radioFemale)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 31, 16))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 31, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.radio2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio2.setGeometry(QtCore.QRect(120, 20, 61, 17))
        self.radio2.setObjectName("radio2")
        self.grpYear = QtWidgets.QButtonGroup(MainWindow)
        self.grpYear.setObjectName("grpYear")
        self.grpYear.addButton(self.radio2)
        self.radio3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio3.setGeometry(QtCore.QRect(180, 20, 61, 17))
        self.radio3.setObjectName("radio3")
        self.grpYear.addButton(self.radio3)
        self.radio1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radio1.setGeometry(QtCore.QRect(60, 20, 51, 17))
        self.radio1.setChecked(True)
        self.radio1.setObjectName("radio1")
        self.grpYear.addButton(self.radio1)
        self.btnOK = QtWidgets.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.btnOK.setObjectName("btnOK")
        self.lblMsg = QtWidgets.QLabel(self.centralwidget)
        self.lblMsg.setGeometry(QtCore.QRect(30, 90, 111, 21))
        self.lblMsg.setStyleSheet("color: rgb(0, 0, 255);")
        self.lblMsg.setObjectName("lblMsg")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioMale.setText(_translate("MainWindow", "남자"))
        self.radioFemale.setText(_translate("MainWindow", "여자"))
        self.label.setText(_translate("MainWindow", "성별:"))
        self.label_2.setText(_translate("MainWindow", "학년:"))
        self.radio2.setText(_translate("MainWindow", "2학년"))
        self.radio3.setText(_translate("MainWindow", "3학년"))
        self.radio1.setText(_translate("MainWindow", "1학년"))
        self.btnOK.setText(_translate("MainWindow", "확인"))
        self.lblMsg.setText(_translate("MainWindow", "1학년 남자입니다"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
