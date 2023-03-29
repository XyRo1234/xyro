import sys, os
from PyQt5.QtWidgets import *

GUI_FILE_NAME = 'gui'
os.system('python -m PyQt5.uic.pyuic -x ' + GUI_FILE_NAME + '.ui -o ' + GUI_FILE_NAME + '.py')

from gui import Ui_MainWindow


class Form(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.groupAction = QActionGroup(self)
        self.setupUi(self)
        self.initToolButton()
        self.setActionConnect()

    def initToolButton(self):
        # self.groupAction.addAction(self.actionLeftAlign)
        # self.groupAction.addAction(self.actionRightAlign)
        # self.groupAction.addAction(self.actionCenterAlign)
        # self.groupAction.addAction(self.actionJustAlign)

        self.toolButton.addAction(self.actionLeftAlign)
        self.toolButton.addAction(self.actionRightAlign)
        self.toolButton.addAction(self.actionCenterAlign)
        self.toolButton.addAction(self.actionJustAlign)

        self.toolBar.addWidget(self.toolButton)
        self.toolBar.addWidget(self.menuTool)

        self.menuTool.setMenu(self.menu)
        self.menuTool.setDefaultAction(self.actionLeftAlign)
        self.toolButton.setDefaultAction(self.actionLeftAlign)

    def setActionConnect(self):
        self.actionLeftAlign.triggered.connect(self.alignLeft)
        self.actionRightAlign.triggered.connect(self.alignRigth)
        self.actionCenterAlign.triggered.connect(self.alignCenter)
        self.actionJustAlign.triggered.connect(self.alignJustify)
        self.toolBar.actionTriggered.connect(self.setDefaultAction)

    def setDefaultAction(self, action):
        self.toolButton.setDefaultAction(action)
        self.menuTool.setDefaultAction(action)

    def alignLeft(self):
        print('alignLeft')

    def alignRigth(self):
        print('alignRigth')

    def alignCenter(self):
        print('alignCenter')

    def alignJustify(self):
        print('alignJustify')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Form()
    w.show()
    sys.exit(app.exec_())
