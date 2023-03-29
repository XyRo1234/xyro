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
        MainWindow.resize(484, 205)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cboFont = QtWidgets.QFontComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboFont.sizePolicy().hasHeightForWidth())
        self.cboFont.setSizePolicy(sizePolicy)
        self.cboFont.setObjectName("cboFont")
        self.horizontalLayout_3.addWidget(self.cboFont)
        self.linFontSize = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linFontSize.sizePolicy().hasHeightForWidth())
        self.linFontSize.setSizePolicy(sizePolicy)
        self.linFontSize.setObjectName("linFontSize")
        self.horizontalLayout_3.addWidget(self.linFontSize)
        self.chkBold = QtWidgets.QCheckBox(self.centralwidget)
        self.chkBold.setObjectName("chkBold")
        self.horizontalLayout_3.addWidget(self.chkBold)
        self.chkItalic = QtWidgets.QCheckBox(self.centralwidget)
        self.chkItalic.setObjectName("chkItalic")
        self.horizontalLayout_3.addWidget(self.chkItalic)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 462, 57))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblEng = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lblEng.setObjectName("lblEng")
        self.horizontalLayout.addWidget(self.lblEng)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 462, 57))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblKor = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lblKor.setStyleSheet("")
        self.lblKor.setObjectName("lblKor")
        self.horizontalLayout_2.addWidget(self.lblKor)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.btnApply = QtWidgets.QPushButton(self.centralwidget)
        self.btnApply.setObjectName("btnApply")
        self.horizontalLayout_4.addWidget(self.btnApply)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.linFontSize.setPlaceholderText(_translate("MainWindow", "Font 크기 입력"))
        self.chkBold.setText(_translate("MainWindow", "Bold"))
        self.chkItalic.setText(_translate("MainWindow", "Italic"))
        self.lblEng.setText(_translate("MainWindow", "The quick brown fox jumps over the lazy dog"))
        self.lblKor.setText(_translate("MainWindow", "다람쥐 헌 쳇바퀴에 타고파"))
        self.btnApply.setText(_translate("MainWindow", "적용"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
