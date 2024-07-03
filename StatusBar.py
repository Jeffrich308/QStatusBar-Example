# -------------------------------------------------------------------------------
# Name:             StatusBar.py
# Purpose:          Simplify Example of QStatusBar use
#
# Author:           Jeffreaux
#
# Created:          03July24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QAction,
    QStatusBar,
    QLineEdit,
)
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("StatusBar_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.btnPrint = self.findChild(QPushButton, "btnPrint")
        self.actExit = self.findChild(QAction, "actExit")
        self.statusbar = self.findChild(QStatusBar, "statusbar")
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        self.actExit.triggered.connect(self.closeEvent)
        self.btnPrint.clicked.connect(self.print_to_status)
        # Will connect when enter is pressed
        self.lineEdit.returnPressed.connect(self.print_to_status)

        # Show the app
        self.show()

    def print_to_status(self):
        # self.statusbar.showMessage("Hello there!!")
        self.statusbar.showMessage(self.lineEdit.text())  # Sends message to StatusBar
        self.lineEdit.clear()  # Clears input box after printing to StatusBar

    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
