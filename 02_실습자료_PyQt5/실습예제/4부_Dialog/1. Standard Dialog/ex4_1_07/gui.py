# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(236, 122)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblmin = QtWidgets.QLabel(self.centralwidget)
        self.lblmin.setObjectName("lblmin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblmin)
        self.editMin = QtWidgets.QLineEdit(self.centralwidget)
        self.editMin.setObjectName("editMin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editMin)
        self.lblMax = QtWidgets.QLabel(self.centralwidget)
        self.lblMax.setObjectName("lblMax")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblMax)
        self.editMax = QtWidgets.QLineEdit(self.centralwidget)
        self.editMax.setObjectName("editMax")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editMax)
        self.lblMinDuration = QtWidgets.QLabel(self.centralwidget)
        self.lblMinDuration.setObjectName("lblMinDuration")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblMinDuration)
        self.editMinDuration = QtWidgets.QLineEdit(self.centralwidget)
        self.editMinDuration.setObjectName("editMinDuration")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.editMinDuration)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 2)
        self.btnDownLoadModal = QtWidgets.QPushButton(self.centralwidget)
        self.btnDownLoadModal.setObjectName("btnDownLoadModal")
        self.gridLayout.addWidget(self.btnDownLoadModal, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lblmin.setText(_translate("MainWindow", "최소값"))
        self.editMin.setText(_translate("MainWindow", "0"))
        self.lblMax.setText(_translate("MainWindow", "최대값"))
        self.editMax.setText(_translate("MainWindow", "10"))
        self.lblMinDuration.setText(_translate("MainWindow", "minDuration"))
        self.editMinDuration.setText(_translate("MainWindow", "0"))
        self.btnDownLoadModal.setText(_translate("MainWindow", "Modal Progress"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
