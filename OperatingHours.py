#UI Written by Seah Yong Zhi
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import Time
import sys

# Coded by YongZhi
class OperatingHoursWindow(object):

    def __init__(self, window, data_manager):
        self.window = window
        self.dataManager = data_manager
        self.setupUI(self.window)
    
    def setWindowProperties(self, window):
        window.setWindowIcon(QIcon('img/app_icon.png'))
        window.setWindowTitle("North Spine Canteen Viewer")
        window.setGeometry (0 ,0, 900, 900)
        window.setFixedSize(1100, 700)

    def addBackgroundLabel(self, window):
        window.bglabel = QtWidgets.QLabel(window)
        window.bglabel.setPixmap(QtGui.QPixmap('img/operatingbg.jpg'))
        window.bglabel.move (150,150)
        window.bglabel.setGeometry (0,0,1100,700)

    def addOperatingHeader(self, window):
        window.operatingHeaderLabel = QtWidgets.QLabel(window)
        window.operatingHeaderLabel.setObjectName("operatingHeader")
        window.operatingHeaderLabel.setText("Operating Hours")
        window.operatingHeaderLabel.setAlignment(Qt.AlignCenter)
        window.operatingHeaderLabel.setFont(QFont("Algerian",weight=QFont.Bold)) #change font type
        window.operatingHeaderLabel.move(300, 150)
        window.operatingHeaderLabel.resize(500, 100)

    def addBackButton(self, window):
        window.back_button = QtWidgets.QPushButton(window)
        window.back_button.setObjectName("backButton")
        window.back_button.move (930,640) #(horizontal vs vertical)
        window.back_button.resize(100,50)
        window.back_button.setFont(QFont("Roboto")) #change font type
        window.back_button.setText("Back")

    def addComboBox(self, window):
        window.stall_comboBox = QtWidgets.QComboBox(window)
        window.stall_comboBox.view().setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        window.stall_comboBox.resize(190,30)
        window.stall_comboBox.move(520, 100)
        window.stall_comboBox.currentIndexChanged[str].connect(self.on_click)#call function when change is detected

        stallList = self.dataManager.getStallList()
        for key,value in stallList.items():
            window.stall_comboBox.addItem(value)
    
    def addOperatingHoursDisplayLabel(self, window):
        window.operatingTimeDisplayLabel = QtWidgets.QLabel(window)
        window.operatingTimeDisplayLabel.move(570, 300)
        window.operatingTimeDisplayLabel.resize(300, 500)

    def addOperatingDaysDisplayLabel(self, window):
        window.operatingDayDisplayLabel = QtWidgets.QLabel(window)
        window.operatingDayDisplayLabel.move(220, 300)
        window.operatingDayDisplayLabel.resize(300, 500)
        
    def addStallLabel(self, window):
        window.stall_label = QtWidgets.QLabel(window)
        window.stall_label.setObjectName("stallLabel")
        window.stall_label.resize(100,30)
        window.stall_label.setText("Select stall")
        window.stall_label.move(380,100)

    def setupUI(self, window):
        self.setWindowProperties(window)
        self.addBackgroundLabel(window)
        self.addOperatingHeader(window)
        self.addOperatingHoursDisplayLabel(window)
        self.addOperatingDaysDisplayLabel(window)
        self.addBackButton(window)
        self.addStallLabel(window)
        self.addComboBox(window)
        

    def bindBackAction(self, method):
        self.window.back_button.clicked.connect(method)

    def on_click(self, name):
        textString = self.dataManager.getStallOperatingHoursString(name)

        dayText = ""
        timeText = ""

        for i in range(len(textString)):
            dayText += textString[i][0] + ":\t\n\n"
            timeText += textString[i][1] + "\n\n"

        self.window.operatingDayDisplayLabel.setText(dayText)
        self.window.operatingTimeDisplayLabel.setText(timeText)

        self.window.operatingDayDisplayLabel.setAlignment(Qt.AlignRight)
        self.window.operatingTimeDisplayLabel.setAlignment(Qt.AlignLeft)
