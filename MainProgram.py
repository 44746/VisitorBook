from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

from MainMenu import *

       
if __name__ == "__main__":
    ##Create new applicatin
    app = QApplication(sys.argv)
    ##instantiate window
    window = MainMenu()
    window.show()
    window.raise_()
    app.exec_()
