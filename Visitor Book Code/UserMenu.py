from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 
from InSign import *
from OutSign import *

class UserMenu(QMainWindow):
	def __init__(self,parent) :
		super().__init__(parent)
		self.parent=parent
		#Settting the window title
		self.setWindowTitle("Menu")
		#Widget set up
		self.btnIn = QPushButton("Sign in")
		self.btnOut = QPushButton("Sign Out")
		
		self.logo = QLabel()
		#Using 'Pixmap' to add an image, in this case the company logo
		self.logo.setPixmap(QPixmap("logo.png"))
	
		self.vLayout=QVBoxLayout()
		self.hLayout = QHBoxLayout()
		
		self.vLayout.addWidget(self.logo)
		self.hLayout.addWidget(self.btnIn)
		self.hLayout.addWidget(self.btnOut)	
		self.vLayout.addLayout(self.hLayout)
		
		self.widget=QWidget()
		self.widget.setLayout(self.vLayout)
		self.setCentralWidget(self.widget)
		#Setting up push button connections
		self.btnIn.clicked.connect(self.signIn)
		self.btnOut.clicked.connect(self.signOut)
		
		
	def signIn(self):
		#Calling the sign in window
		self.signIn = InSign(self)
		#Showing the window
		self.signIn.show()
		#Rasing the window to the front of the screen
		self.signIn.raise_()
		#Closing the current window
		self.close()
	
	def signOut(self):
		#Calling the sign out window
		self.signOut = OutSign(self)
		#Showing the window
		self.signOut.show()
		#Raising the window to the front of the screen
		self.signOut.raise_()
		#Closing the current window
		self.close()
	