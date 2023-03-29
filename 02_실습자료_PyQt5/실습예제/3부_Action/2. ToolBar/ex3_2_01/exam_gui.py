# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exam_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(145, 90)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(30, 20, 75, 23))
        self.btnNew.setObjectName("btnNew")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 145, 20))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setTearOffEnabled(False)
        self.menu_File.setSeparatorsCollapsible(False)
        self.menu_File.setToolTipsVisible(False)
        self.menu_File.setObjectName("menu_File")
        self.menu_Edit = QtWidgets.QMenu(self.menubar)
        self.menu_Edit.setObjectName("menu_Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action_New = QtWidgets.QAction(MainWindow)
        self.action_New.setChecked(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/File/images/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_New.setIcon(icon)
        self.action_New.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.action_New.setIconVisibleInMenu(True)
        self.action_New.setPriority(QtWidgets.QAction.LowPriority)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/File/images/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon1)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/File/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon2)
        self.action_Save.setObjectName("action_Save")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/File/images/save_as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon3)
        self.actionSave_As.setObjectName("actionSave_As")
        self.action_Close = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/File/images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Close.setIcon(icon4)
        self.action_Close.setObjectName("action_Close")
        self.actionCu_t = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Edit/images/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCu_t.setIcon(icon5)
        self.actionCu_t.setObjectName("actionCu_t")
        self.action_Copy = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Edit/images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Copy.setIcon(icon6)
        self.action_Copy.setObjectName("action_Copy")
        self.action_Paste = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Edit/images/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Paste.setIcon(icon7)
        self.action_Paste.setObjectName("action_Paste")
        self.action_Print = QtWidgets.QAction(MainWindow)
        self.action_Print.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/File/images/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Print.setIcon(icon8)
        self.action_Print.setObjectName("action_Print")
        self.action_Undo = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/Edit/images/edit_undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Undo.setIcon(icon9)
        self.action_Undo.setObjectName("action_Undo")
        self.action_Redo = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Edit/images/edit_redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Redo.setIcon(icon10)
        self.action_Redo.setObjectName("action_Redo")
        self.action_Font = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/Edit/images/font.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Font.setIcon(icon11)
        self.action_Font.setObjectName("action_Font")
        self.action_Bold = QtWidgets.QAction(MainWindow)
        self.action_Bold.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Bold.setIcon(icon12)
        self.action_Bold.setObjectName("action_Bold")
        self.action_Italic = QtWidgets.QAction(MainWindow)
        self.action_Italic.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/Edit/images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Italic.setIcon(icon13)
        self.action_Italic.setObjectName("action_Italic")
        self.action_Uderline = QtWidgets.QAction(MainWindow)
        self.action_Uderline.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/Edit/images/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Uderline.setIcon(icon14)
        self.action_Uderline.setObjectName("action_Uderline")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/Edit/images/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon15)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionSave_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Print)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Close)
        self.menu_Edit.addAction(self.action_Copy)
        self.menu_Edit.addAction(self.actionCu_t)
        self.menu_Edit.addAction(self.action_Paste)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Undo)
        self.menu_Edit.addAction(self.action_Redo)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.action_Font)
        self.menu_Edit.addAction(self.action_Bold)
        self.menu_Edit.addAction(self.action_Italic)
        self.menu_Edit.addAction(self.action_Uderline)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionAbout)
        self.menu_Edit.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Note Pad"))
        self.btnNew.setText(_translate("MainWindow", "newFile"))
        self.menu_File.setToolTip(_translate("MainWindow", "testest"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Edit.setTitle(_translate("MainWindow", "&Edit"))
        self.action_New.setText(_translate("MainWindow", "&New"))
        self.action_New.setIconText(_translate("MainWindow", "New"))
        self.action_New.setStatusTip(_translate("MainWindow", "New"))
        self.action_New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
        self.action_Open.setStatusTip(_translate("MainWindow", "Open"))
        self.action_Open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindow", "&Save"))
        self.action_Save.setStatusTip(_translate("MainWindow", "Save"))
        self.action_Save.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save &As..."))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save As"))
        self.action_Close.setText(_translate("MainWindow", "&Close"))
        self.action_Close.setStatusTip(_translate("MainWindow", "Exit"))
        self.action_Close.setShortcut(_translate("MainWindow", "Ctrl+F4"))
        self.actionCu_t.setText(_translate("MainWindow", "Cu&t"))
        self.actionCu_t.setStatusTip(_translate("MainWindow", "Cut"))
        self.actionCu_t.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.action_Copy.setText(_translate("MainWindow", "&Copy"))
        self.action_Copy.setStatusTip(_translate("MainWindow", "Copy"))
        self.action_Copy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.action_Paste.setText(_translate("MainWindow", "&Paste"))
        self.action_Paste.setStatusTip(_translate("MainWindow", "Paste"))
        self.action_Paste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.action_Print.setText(_translate("MainWindow", "&Print(P)"))
        self.action_Print.setStatusTip(_translate("MainWindow", "Print"))
        self.action_Print.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.action_Undo.setText(_translate("MainWindow", "Undo"))
        self.action_Undo.setStatusTip(_translate("MainWindow", "Undo"))
        self.action_Undo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.action_Redo.setText(_translate("MainWindow", "Redo"))
        self.action_Redo.setStatusTip(_translate("MainWindow", "Redo"))
        self.action_Redo.setShortcut(_translate("MainWindow", "Ctrl+Y"))
        self.action_Font.setText(_translate("MainWindow", "&Font"))
        self.action_Font.setStatusTip(_translate("MainWindow", "Font"))
        self.action_Font.setShortcut(_translate("MainWindow", "Ctrl+F"))
        self.action_Bold.setText(_translate("MainWindow", "&Bold"))
        self.action_Bold.setStatusTip(_translate("MainWindow", "Bold"))
        self.action_Italic.setText(_translate("MainWindow", "&Italic"))
        self.action_Italic.setStatusTip(_translate("MainWindow", "Italic"))
        self.action_Uderline.setText(_translate("MainWindow", "&Uderline"))
        self.action_Uderline.setStatusTip(_translate("MainWindow", "Uderline"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionAbout.setStatusTip(_translate("MainWindow", "About"))
import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
