from WindowCreator import WindowCreator
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# Windows will recognise this program as separate from a normal Python process
# Hence, the app icon in taskbar will change
import ctypes
myappid = u'cz1003.canteenviewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


def start():
    app = QtWidgets.QApplication([])
    wc = WindowCreator()
    wc.createMainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start()
