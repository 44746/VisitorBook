from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 

from InSign import *
from OutSign import *

class UserMenu(QMainWindow):
	def __init__(self,parent) :
		super().__init__(parent)
		self.parent=parent
		
		self.setWindowTitle("Menu")
		self.btnIn = QPushButton("Sign in")
		self.btnOut = QPushButton("Sign Out")
		
		self.logo = QLabel()
		self.logo.setPixmap(QPixmap("logo.png"))
		
		
		self.btnIn.clicked.connect(self.signIn)
		self.btnOut.clicked.connect(self.signOut)
		
		self.vLayout=QVBoxLayout()
		self.hLayout = QHBoxLayout()
		
		self.vLayout.addWidget(self.logo)
		self.hLayout.addWidget(self.btnIn)
		self.hLayout.addWidget(self.btnOut)	
		self.vLayout.addLayout(self.hLayout)
		
		self.widget=QWidget()
		self.widget.setLayout(self.vLayout)
		self.setCentralWidget(self.widget)
		
	def signIn(self):
		self.signIn = InSign(self)
		self.signIn.show()
		self.signIn.raise_()
		self.close()
	
	def signOut(self):
		self.signOut = OutSign(self)
		self.signOut.show()
		self.signOut.raise_()
		self.close()
	