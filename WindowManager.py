import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Time

# Coded by Jun Wei
class WindowManager():

    def __init__(self):
        self.stack = Stack() # store the windows opened in a stack and pop when retrieving them
        self.currentUI = None
    
    # Push the opened ui to the stack
    def addUI(self, ui):
        if self.currentUI != None:
            self.currentUI.window.hide()
            self.stack.push(self.currentUI)

        self.currentUI = ui
        self.currentUI.window.show()

    # Remove the current ui and show the previous one
    def popUI(self):
        self.currentUI.window.close()
        self.currentUI = self.stack.pop()
        self.currentUI.window.show()

    def exitProgram(self):
        sys.exit()

    # Current UI must implement getInfo() and previous UI must implement receiveInfo()
    # Else Error and UI is closed normally -> no information propagation
    def passInformation(self):
        try:
            raw_info = self.currentUI.getInfo()
        except:
            msg = "{} is not programmed to pass information!".format(type(self.currentUI))
            print(msg)

            f = open("log.txt", "a")
            f.write(msg)
            f.close()
        finally:
            self.popUI()

        try:
            self.currentUI.receiveInfo(raw_info)
        except:
            msg = "{} is not programmed to receive information!".format(type(self.currentUI))
            print(msg)
            
            f = open("log.txt", "a")
            f.write(msg)
            f.close()



class Stack():

    def __init__(self):
        self.arr = []
    def peek(self):
        return self.arr[-1]
    def pop(self):
        return self.arr.pop()
    def push(self, element):
        self.arr.append(element)
    def length(self):
        return len(self.arr)
    def isEmpty(self):
        return not self.length()