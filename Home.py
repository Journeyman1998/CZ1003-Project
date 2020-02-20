from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *


import Time
import Stylesheet

class MainWindow(object):

    def __init__(self, window):
        self.window = window
        self.setupUI(self.window)
    
    def setupUI(self, MainWindow):
        self.setWindowProperties(MainWindow)
        self.addBackgroundLabel(MainWindow)
        self.addLogoLabel(MainWindow)
        self.addTextLabel(MainWindow)
        self.addTemporalLabel(MainWindow)
        self.addGoStallsButton(MainWindow)
        self.addOperatingHoursButton(MainWindow)
        self.addExitButton(MainWindow)  
        
    # Helper functions for setupUI()
    # Coded by YongZhi

    def setWindowProperties(self, window):
        window.setWindowIcon(QIcon('img/app_icon.png'))
        window.setWindowTitle("North Spine Canteen Viewer")
        window.setFixedSize(700, 700)
    
    def addBackgroundLabel(self, window):
        window.bglabel =QtWidgets.QLabel(window)
        window.bglabel.setPixmap(QtGui.QPixmap('img/welcome background image.jpg'))
        window.bglabel.move (150,150)
        window.bglabel.setGeometry (0,0,700,700)

    def addLogoLabel(self, window):
        window.Logolabel = QtWidgets.QLabel(window)
        window.Logolabel.setStyleSheet("background-image: url(img/NTU_Logo.png)")
        window.Logolabel.move (220,250)
        window.Logolabel.resize(200,85)

    def addTextLabel(self, window):
        window.Textlabel =QtWidgets.QLabel(window)
        window.Textlabel.setStyleSheet("background-color:white; font-size: 21px;")
        window.Textlabel.setText("  Welcome to North Spine \n Canteen Viewer Application")
        window.Textlabel.move (420,250)
        window.Textlabel.resize(280,85)
    
    def addTemporalLabel(self, window):
        window.Time_Date_Label = QtWidgets.QLabel(window)
        window.Time_Date_Label.setObjectName("Time_Date_Label")
        now_t= Time.getTime()
        now_d = Time.getDate()
        window.Time_Date_Label.move (220, 350)
        window.Time_Date_Label.resize(480,30)
        window.Time_Date_Label.setText("Date: " + str(now_d) + "   Time: " + str(now_t))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateTime) # Updates time automatically every second
        self.timer.start(1000)
    
    def addOperatingHoursButton(self, window):
        window.operatingHours_button = QtWidgets.QPushButton(window)
        window.operatingHours_button.move (300,480) 
        window.operatingHours_button.resize(300,50)
        window.operatingHours_button.setText("Operating Hours")

    def addGoStallsButton(self, window):
        window.stall_button=QtWidgets.QPushButton(window)
        window.stall_button.move (300,420) 
        window.stall_button.resize(300,50)
        window.stall_button.setText("View The Stalls")

    def addExitButton(self, window):
        window.button_exit=QtWidgets.QPushButton(window)
        window.button_exit.setObjectName("button_exit")
        window.button_exit.move (300,555) 
        window.button_exit.resize(300,50)
        window.button_exit.setText("Exit")

    #End of helper functions


    def updateTime(self):
        self.window.Time_Date_Label.setText("Date: " + str(Time.getDate()) + "   Time: " + str(Time.getTime()))
        
    
    def bindExitAction(self, method):
        self.window.button_exit.clicked.connect(method)

    def bindGoToStallsAction(self, method):
        self.window.stall_button.clicked.connect(method)
    
    def bindGoToOperatingHoursAction(self, method):
        self.window.operatingHours_button.clicked.connect(method)
