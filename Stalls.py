from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QPushButton, QApplication, QCalendarWidget, QWidget, QLabel, QTextEdit, \
                            QListWidget, QListWidgetItem, QMessageBox, QScrollArea, QToolTip, QFrame,\
                            QHBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap, QFont
import Time
import os

class StallsWindow(object):

    def __init__(self, window, data_manager):
        self.window = window
        self.time = None
        self.temp_time = None    #current time set by user
        self.date = None
        self.temp_date = None    #current date set by user
        self.id = 0         #current id of stall selected by user
        self.dataManager = data_manager
        self.setupUI(self.window)
        self.updateList()   #initialise list to show all stalls
    
    # Setup UI when window first starts
    def setupUI(self, window):
        self.setWindowProperties(window)
        self.addBackButton(window)
        self.addCustomButton(window)
        self.addNowButton(window)
        self.addGoButton(window)
        self.addDateTimeTextBox(window)
        self.addResetButton(window)
        self.addListWidget(window)
        self.addMessageBoxButton(window)
        self.addQueueLengthTextBox(window)
        self.addMenuBackground(window)
        self.addMenuArea(window)

    # Helper functions for setupUI()
    # Coded by YongZhi
    def setWindowProperties(self, window):
        window.setObjectName("window")
        window.setWindowIcon(QIcon('img/app_icon.png')) 
        window.setWindowTitle("North Spine Canteen Viewer") 
        window.setFixedSize(1000, 700)
        window.setWindowFlags(window.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)

    def addBackButton(self, window):
        window.backButton = QPushButton(window)
        window.backButton.setObjectName("backButton")
        window.backButton.move(225, 10)
        window.backButton.resize(60,30)
        window.backButton.setText("Back")

    def addCustomButton(self, window):
        window.customButton = QPushButton(window)
        window.customButton.setObjectName("customButton")
        window.customButton.move(5, 10)
        window.customButton.resize(60, 30)
        window.customButton.setText("Custom")
    
    def addNowButton(self, window):
        window.nowButton = QPushButton(window)
        window.nowButton.setObjectName("nowButton")
        window.nowButton.move(75, 10)
        window.nowButton.resize(60, 30)
        window.nowButton.setText("Now")
        window.nowButton.clicked.connect(self.clickNowButton)
    
    def addGoButton(self, window):
        window.goButton = QPushButton(window)
        window.goButton.setObjectName("goButton")
        window.goButton.move(155, 10)
        window.goButton.resize(60, 30)
        window.goButton.setText("Go")
        window.goButton.clicked.connect(self.updateList)
        window.goButton.setDisabled(True)

    def addDateTimeTextBox(self, window):
        window.dtTextBox = QTextEdit(window)
        window.dtTextBox.setObjectName("dtTextBox")
        window.dtTextBox.setDisabled(True)
        window.dtTextBox.move(5, 55)
        window.dtTextBox.resize(130, 30)
    
    def addResetButton(self, window):
        window.resetButton = QPushButton(window)
        window.resetButton.setObjectName("resetButton")
        window.resetButton.move(155, 55)
        window.resetButton.resize(130,30)
        window.resetButton.setText("Reset")
        window.resetButton.setDisabled(True)
        window.resetButton.clicked.connect(self.clickResetButton)

    def addListWidget(self, window):
        window.listWidget = QListWidget(window)
        window.listWidget.setObjectName("listWidget")
        window.listWidget.move(5, 100)
        window.listWidget.resize(280, 510)
        window.listWidget.setSortingEnabled(True)
        window.listWidget.itemClicked.connect(self.getItemClicked)

    def addMessageBoxButton(self, window):
        window.msgButton = QPushButton(window)
        window.msgButton.move(5, 630)
        window.msgButton.resize(120,40)
        window.msgButton.setText("Get Queue Time")
        window.msgButton.clicked.connect(lambda: self.showQueueTimeMessage(window))
        window.msgButton.setDisabled(True)

    def addQueueLengthTextBox(self, window):
        window.queueLengthTextBox = QTextEdit(window)
        window.queueLengthTextBox.setObjectName("queueTextBox")
        window.queueLengthTextBox.move(140, 630)
        window.queueLengthTextBox.resize(145, 40)
        window.queueLengthTextBox.setDisabled(True)

    def addMenuBackground(self, window):
        window.menuArea = QLabel(window)
        window.menuArea.setObjectName("menuArea")
        window.menuArea.move(300, 0)
        window.menuArea.resize(700, 695)
        window.menuArea.setPixmap(QtGui.QPixmap('img/menubg2.jpg'))
        window.menuArea.setAlignment(Qt.AlignCenter)

        self.addMealNameLabel(window, window.menuArea)
    
    def addMealNameLabel(self, window, menuBackground):
        window.mealNameLabel = QLabel(menuBackground)
        window.mealNameLabel.setObjectName("mealNameLabel")
        window.mealNameLabel.move(300, 10)
        window.mealNameLabel.resize(100, 30)
        window.mealNameLabel.setText("")
        window.mealNameLabel.setAlignment(Qt.AlignCenter)

    def addMenuArea(self, window):
        window.scrollArea = QScrollArea(window)
        window.scrollArea.setFrameShape(QFrame.NoFrame)
        window.scrollArea.move(430, 310)
        window.scrollArea.resize(480, 360)
    
    #End of Helper functions


    # Binds methods passed from WindowManager
    # Coded by Jun Wei
    def bindBackAction(self, method):
        self.window.backButton.clicked.connect(method)
    
    def bindCustomAction(self, method):
        self.window.customButton.clicked.connect(method)


    # Receives and handles Time, Date object (stored in dict) passed from DateTimeInput
    # Coded by Jun Wei
    def receiveInfo(self, raw_info):

        # Sets Time object. Handles KeyError
        try:
            raw_time = raw_info["time"]
            self.temp_time = Time.getTime(raw_time.hour(), raw_time.minute(), raw_time.second())
        except:
            self.temp_time = None

        # Sets Date object. Handles KeyError
        try:
            raw_date = raw_info["date"]
            self.temp_date = Time.getDate(raw_date.year(), raw_date.month(), raw_date.day())
        except:
            self.temp_date = None

        # Once info is received, the time, date have changed. Allows user to reset date, time. 
        self.window.resetButton.setDisabled(False)
        self.updateDateTimeTextBox()
        self.window.goButton.setDisabled(False)

        if self.temp_time == None and self.temp_date == None:
            self.window.goButton.setDisabled(True)


    # Set date, time to NOW
    # Coded by Jun Wei
    def clickNowButton(self):
        # no parameters -> default is current date, time
        self.temp_time = Time.getTime() 
        self.temp_date = Time.getDate()
        self.updateDateTimeTextBox()
        self.window.resetButton.setDisabled(False)
        self.window.goButton.setDisabled(False)
    

    # Set everything back to default, but menuArea is still left showing food
    # Coded by Jun Wei
    def clickResetButton(self):
        self.time = None
        self.date = None
        
        self.temp_time = None
        self.temp_date = None
        self.id = 0

        self.window.resetButton.setDisabled(True)
        self.window.queueLengthTextBox.setText("")
        self.window.queueLengthTextBox.setDisabled(True)
        self.window.msgButton.setDisabled(True)
        self.window.goButton.setDisabled(True)

        self.updateDateTimeTextBox()
        self.updateList()
        self.resetMenu()
        

    # Stores ID of stall for later use. Updates menu based on stall clicked (and date, time)
    # Coded by Jun Wei
    def getItemClicked(self, item):
        self.id = item.id
        self.updateMenu(self.id)
        self.window.msgButton.setDisabled(False)
        self.window.queueLengthTextBox.setDisabled(False)


    # Updates stalls available based on date, time
    # Coded by Jun Wei
    def updateList(self):
        self.time = self.temp_time
        self.date = self.temp_date
        self.temp_time = None
        self.temp_date = None
        
        self.window.listWidget.clear()
        if self.time == None and self.date == None: # Show all stalls
            stall = self.dataManager.getStallList()
        else:
            stall = self.dataManager.getStallList(self.date, self.time)
        
        for key, value in stall.items():
                i = ListItem(key, value)
                self.window.listWidget.addItem(i)

        self.window.goButton.setDisabled(True)

        # Nothing is selected, so user cannot check queue length
        self.window.queueLengthTextBox.setDisabled(True)
        self.window.msgButton.setDisabled(True)
        self.window.queueLengthTextBox.setText("")


    # Updates date_time_textbox based on date, time
    # Coded by Jun Wei
    def updateDateTimeTextBox(self):
        if self.temp_time != None and self.temp_date != None:
            self.window.dtTextBox.setText(Time.getDateTimeString(self.temp_date, self.temp_time))
        else:
            self.window.dtTextBox.setText("")


    #Shows menu of the stall at the given date, time, id     
    # Coded by Jun Wei   
    def updateMenu(self, id):

        if self.time != None:
            mealName = self.getMealName(id, self.time)
            self.window.mealNameLabel.setText(mealName)
        else:
            self.window.mealNameLabel.setText("")

        menu = self.dataManager.getMenu(id, self.date, self.time)
        vbox = QtWidgets.QVBoxLayout()
        
        for food in menu:
            hbox = QtWidgets.QHBoxLayout()
            foodLabel = QLabel()
            foodLabel.setFixedSize(200, 80)
            foodLabel.setText(food["name"])
            foodLabel.setAlignment(Qt.AlignLeft)
            
            hbox.addWidget(foodLabel)

            priceLabel = QLabel()
            priceLabel.setFixedSize(220, 80)
            priceLabel.setText("$%.2f" %(food["price"]))
            priceLabel.setAlignment(Qt.AlignRight)
            hbox.addWidget(priceLabel)

            miniWidget = QWidget()
            miniWidget.setLayout(hbox)
            vbox.addWidget(miniWidget)

            # Sets tooltip
            filename = 'img/food/' + str(self.id) + "/" + food["id"] + ".png"
            if os.path.exists(filename):
                miniWidget.setToolTip("<b>%s : $%.2f</b><br><img src='%s'/>" %(food["name"], food["price"], filename))
            elif os.path.exists('img/default.jpg'):
                miniWidget.setToolTip("<b>%s : $%.2f</b><br><img src='img/default.jpg'/>" %(food["name"], food["price"]))

        scrollWidget = QWidget()
        scrollWidget.setStyleSheet("background-color: #15120d;")
        scrollWidget.setLayout(vbox)
        self.window.scrollArea.setWidget(scrollWidget)

    # Mealname to display on MenuArea
    # Coded by Jun Wei
    def getMealName(self, id, time):
        mealTimeDict = self.dataManager.getMealTimeDict(id)

        #Use TimeInt to avoid converting to TimeObject many times
        timeInt = Time.convertTimeToInt(time)
        prevMealName = "Error" #Default
        for key,value in mealTimeDict.items():
            if timeInt < value:
                break
            else:
                prevMealName = key
        return prevMealName.capitalize()

    # Resets menu when Reset button is pressed
    # Coded by Jun Wei
    def resetMenu(self):
        tempLabel = QLabel()
        self.window.scrollArea.setWidget(tempLabel)
        self.window.mealNameLabel.setText("")

    # Opens a message dialog, informing user of queue time
    # Coded by Jun Wei
    def showMessageBox(self, window, message, title="MessageBox"):
        box = QMessageBox(window)
        box.setFixedSize(100, 100)
        box.setText(message)
        box.setWindowTitle(title)
        box.exec_()

    def showQueueTimeMessage(self, window):
        message, title = self.checkInfo(self.id)
        self.showMessageBox(window, message, title)
    
    # Returns message(string), title(string)
    # Coded by Xuege
    def checkInfo(self, id):
        text = self.window.queueLengthTextBox.toPlainText()
        
        if text.isdigit():
            queueTime = self.dataManager.getQueueTime(id, int(text))
            return "The waiting time is {} mins.\t".format(queueTime), "Waiting Time", 
        else:
            return "Please enter a valid number!", "Error", 

    
# Custom ListWidgetItem. Contains information of stall ID
# Coded by Jun Wei
class ListItem(QListWidgetItem):
    def __init__(self, id, name):
        super().__init__()
        self.id = id
        self.name = name
        self.setFont(QFont ("Helvetica [Cronyx]", 16))
        self.setText(name)
    
    def __str__(self):
        return self.name
    
#See Custom Widget List Item
# https://stackoverflow.com/questions/25187444/pyqt-qlistwidget-custom-items




# For UI testing:
from DataManager import DataManager
import Data
import Stylesheet
import sys
if __name__ == "__main__":
    app = QApplication([])
    window = QtWidgets.QMainWindow()
    window.setStyleSheet(Stylesheet.style_stalls)
    ui = StallsWindow(window, DataManager(Data.getData("data\\metadata.txt")))
    window.show()

    sys.exit(app.exec_())