import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSplashScreen, QProgressBar
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
from time import sleep

from WindowManager import WindowManager
from DataManager import DataManager
from Home import MainWindow
from Stalls import StallsWindow
from DateTimeInput import DateTimeInput
from OperatingHours import OperatingHoursWindow
import Data
import Stylesheet

# Coded by Jun Wei
# Methods are self-explanatory
class WindowCreator():
    
    def __init__(self):
        self.wm = WindowManager()
        data = Data.getData("data\\metadata.txt")
        self.data_manager = DataManager(data)

    
    def createInputDialog(self):
        window = QtWidgets.QMainWindow()
        window.setStyleSheet(Stylesheet.style_datetime)
        ui = DateTimeInput(window)
        ui.bindConfirmAction(self.wm.passInformation)
        ui.bindBackAction(self.wm.popUI)
        self.wm.addUI(ui)

    def createMainWindow(self):
        window = QtWidgets.QMainWindow()
        window.setStyleSheet(Stylesheet.style_home)
        ui = MainWindow(window)
        ui.bindExitAction(self.wm.exitProgram)
        ui.bindGoToStallsAction(self.createWindow_to_stalls)
        ui.bindGoToOperatingHoursAction(self.createOperatingHoursWindow)
        self.showSplashScreen(window, "img\splash.jpg")
        self.wm.addUI(ui)

    def createWindow_to_stalls(self):
        window = QtWidgets.QMainWindow()
        window.setStyleSheet(Stylesheet.style_stalls)
        ui = StallsWindow(window, self.data_manager)
        ui.bindBackAction(self.wm.popUI)
        ui.bindCustomAction(self.createInputDialog)
        self.wm.addUI(ui)
    
    def createOperatingHoursWindow(self):
        window = QtWidgets.QMainWindow()
        window.setStyleSheet(Stylesheet.style_opHours)
        ui = OperatingHoursWindow(window, self.data_manager)
        ui.bindBackAction(self.wm.popUI)
        self.wm.addUI(ui)

    def showSplashScreen(self, window, filename):
        pixmap = QPixmap(filename)
        splash = QSplashScreen(pixmap)
        splash.setWindowIcon(QIcon('img/app_icon.png')) 
        splash.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        splash.setEnabled(False)
        
        progressBar = QProgressBar(splash)
        progressBar.setMaximum(3)
        progressBar.setGeometry(20, splash.height() - 50, splash.width(), 20)

        splash.show()
        splash.showMessage("<h1><font color='green'>Welcome!</font></h1>", QtCore.Qt.AlignCenter, QtCore.Qt.black)
        
        for i in range(4):
            progressBar.setValue(i)
            sleep(0.1)
        
        sleep(0.25)
        splash.finish(window)