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
		#Setting the window title
		self.setWindowTitle("Sign Out")
		#Widget set up
		self.searchTerm = QLineEdit("")
		self.btnSearch = QPushButton("Search")
		self.searchList = QListWidget()
		self.btnBack = QPushButton("Back")
		self.btnOut = QPushButton("Sign Out")
		self.labelT = QLabel("Please enter your Surname:")
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
		#Setting up push button connections
		self.btnSearch.clicked.connect(self.btnSearch_pushed)
		self.btnBack.clicked.connect(self.btnBack_pushed)
		self.btnOut.clicked.connect(self.btnOut_pushed)
		
	def btnSearch_pushed(self):
		#Clearing the list
		self.searchList.clear()
		#Retrieving all visitors from the database
		visitors = g_database.GetAllEntries()
		#Converting the users entry to text
		term = self.searchTerm.text()
		#converting the term to lower to allow for user input error
		term = term.lower()
		termFound = False
		for visitor in visitors:
			#Obtaing the surname from the database
			surname = visitor[2]
			#converting the surname to lower to allow for user input error
			surname = surname.lower()
			#Checking the search term matches the term in the database and the visitor isnt signed out
			if term == surname and visitor[7] == "N/A":
				#Creating a full name
				name = ""
				#Adding the forename and a space to the string
				name= name + (visitor[1]) + " "
				#Adding a surname
				name = name + (visitor[2])
				#Adding the full name to the list
				self.searchList.addItem(name)
				termFound = True
		#If the term isnt found
		if termFound == False:
			#Calling the error window, passing in the message to display
			self.message=Message(self,"No entries found, please search again")
			#Showing the window
			self.message.show()
			#Raising the window the front of the screen
			self.message.raise_()
	
	#Returning the to the parent window 		
	def btnBack_pushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
		
	def btnOut_pushed(self):
		#Converting the users selected item to text
		currentItem = self.searchList.currentItem().text()
		#Calling the clarification window, passing in the users selected name
		self.clarification = Clarification(self,currentItem)
		self.clarification.show()
		self.clarification.raise_()
		self.close()
				
				
				