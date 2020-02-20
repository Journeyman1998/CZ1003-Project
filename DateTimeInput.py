from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QCalendarWidget, QWidget, QLabel, QTimeEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon

import Time

# Coded by YongZhi
class DateTimeInput():

    def __init__(self, window):
        self.window = window
        self.createInputDialog(self.window)

    def createInputDialog(self, window):
        self.setWindowProperties(window)
        self.addCalendarWidget(window)
        self.addTimeWidget(window)
        self.addConfirmButton(window)
        self.addBackButton(window)


    # Helper functions for createInputDialog()
        
    def setWindowProperties(self, window):
        window.setObjectName("window")
        window.setWindowIcon(QIcon('img/app_icon.png'))
        window.setWindowTitle("North Spine Canteen Viewer")
        window.setGeometry (0,0,700,700)
        window.setFixedSize(450, 600)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

    def addCalendarWidget(self, window):
        window.calendar = QCalendarWidget(window)
        window.calendar.setGridVisible(True)
        window.calendar.move(30, 30)
        window.calendar.resize(380,300)
        window.calendar.clicked[QtCore.QDate].connect(self.updateDate)
        date = window.calendar.selectedDate()

        window.calendar_label = QtWidgets.QLabel(window)
        window.calendar_label.setObjectName("calendar_label")
        window.calendar_label.setText(" Chosen Date: "+ date.toString())
        window.calendar_label.resize(305, 30)
        window.calendar_label.move(70, 350)

    def updateDate(self, date):
        self.window.calendar_label.setText(" Chosen Date: "+ date.toString())

    def addTimeWidget(self, window):
        window.timeWidget = QTimeEdit(window)
        window.timeWidget.setObjectName("timeWidget")
        window.timeWidget.move(100, 410)
        window.timeWidget.resize(240, 70)

    def addBackButton(self, window):
        window.backButton = QtWidgets.QPushButton(window)
        window.backButton.move(245, 535)
        window.backButton.resize(120, 45)
        window.backButton.setText("Back")
    
    def addConfirmButton(self, window):
        window.confirmButton = QtWidgets.QPushButton(window)
        window.confirmButton.move(85, 535)
        window.confirmButton.resize(120, 45)
        window.confirmButton.setText("Confirm")
    
    def bindConfirmAction(self, method):
        self.window.confirmButton.clicked.connect(method)
    
    def bindBackAction(self, method):
        self.window.backButton.clicked.connect(method)
    
    def getInfo(self):
        time = self.window.timeWidget.time()
        date = self.window.calendar.selectedDate()

        return {"time": time, "date": date}
        
        