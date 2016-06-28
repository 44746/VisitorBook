from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *

class Clarification(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		#Setting the window title
		self.setWindowTitle("Clear Table")
		#Widget set up
		self.label =QLabel("Are you sure you want to clear the table?")
		self.btnNo =QPushButton("No")
		self.btnYes=QPushButton("Yes")
		
		self.vLayout = QVBoxLayout()
		self.hLayout = QHBoxLayout()
		
		self.hLayout.addWidget(self.btnNo)
		self.hLayout.addWidget(self.btnYes)
		self.vLayout.addWidget(self.label)
		self.vLayout.addLayout(self.hLayout)
		self.widget = QWidget()
		self.widget.setLayout(self.vLayout)
		self.setCentralWidget(self.widget)
		#Setting up connections for both push buttons
		self.btnNo.clicked.connect(self.btnNo_pushed)
		self.btnYes.clicked.connect(self.btnYes_pushed)
	
	#Returning to the parent window
	def btnNo_pushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
		
	def btnYes_pushed(self):
		#Clearing the database
		g_database.DeleteVisitors()
		#Returning to the main menu without opening window upon window
		self.parent.btnBackPushed()
		self.close()