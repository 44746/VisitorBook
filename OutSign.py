from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
from Message import *
from OutClarification import *
import datetime
class OutSign(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		self.setWindowTitle("Sign Out")
		
		
		self.searchTerm = QLineEdit("")
		self.btnSearch = QPushButton("Search")
		self.searchList = QListWidget()
		self.btnBack = QPushButton("Back")
		self.btnOut = QPushButton("Sign Out")
		self.labelT = QLabel("Please enter your surname:")
		self.vLayoutMAIN = QVBoxLayout()
		self.hLayout1 = QHBoxLayout()
		self.hLayout2 = QHBoxLayout()
		
		
		self.hLayout1.addWidget(self.searchTerm)
		self.hLayout1.addWidget(self.btnSearch)
		self.hLayout2.addWidget(self.btnBack)
		self.hLayout2.addWidget(self.btnOut)
		self.vLayoutMAIN.addWidget(self.labelT)
		self.vLayoutMAIN.addLayout(self.hLayout1)
		self.vLayoutMAIN.addWidget(self.searchList)
		self.vLayoutMAIN.addLayout(self.hLayout2)
		self.widget = QWidget()
		self.widget.setLayout(self.vLayoutMAIN)
		self.setCentralWidget(self.widget)
		
		self.btnSearch.clicked.connect(self.btnSearch_pushed)
		self.btnBack.clicked.connect(self.btnBack_pushed)
		self.btnOut.clicked.connect(self.btnOut_pushed)
		
	def btnSearch_pushed(self):
		self.searchList.clear()
		visitors = g_database.GetAllEntries()
		term = self.searchTerm.text()
		termFound = False
		for visitor in visitors:
			if term == visitor[2] and visitor[7] == "N/A":
				name = ""
				name= name + (visitor[1]) + " "
				name = name + (visitor[2])
				self.searchList.addItem(name)
				termFound = True
		if termFound == False:
			self.message=Message(self,"No entries found, please search again")
			self.message.show()
			self.message.raise_()
			
	def btnBack_pushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
		
	def btnOut_pushed(self):
		currentItem = self.searchList.currentItem().text()
		self.clarification = Clarification(self,currentItem)
		self.clarification.show()
		self.clarification.raise_()
		self.close()
				
				
				