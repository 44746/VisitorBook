from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
import datetime


class Clarification(QMainWindow):
	def __init__(self,parent,fullName):
		super().__init__()
		#reassinging the variables so that they can be used in the class
		self.parent = parent
		self.fullName = fullName
		#Setting the window title
		self.setWindowTitle("Sign Out")
		#Widget set up
		#Using 'format' to add a variable into the label
		self.label=QLabel("Sign out {0}?".format(fullName))
		self.btnBack = QPushButton("Cancel")
		self.btnOut = QPushButton("Sign Out")
		
		self.hLayout = QHBoxLayout()
		self.vLayoutMain = QVBoxLayout()
		
		self.hLayout.addWidget(self.btnBack)
		self.hLayout.addWidget(self.btnOut)
		self.vLayoutMain.addWidget(self.label)
		self.vLayoutMain.addLayout(self.hLayout)
		self.widget = QWidget()
		self.widget.setLayout(self.vLayoutMain)
		self.setCentralWidget(self.widget)
		#Setting up the push button connections
		self.btnBack.clicked.connect(self.btnBackPushed)
		self.btnOut.clicked.connect(self.btnOutClicked)
	#returning to the parent window
	def btnBackPushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
	#Signing out the chosen visitor
	def btnOutClicked(self):
		#retrieving all visitors in the database
		visitors = g_database.GetAllEntries()
		count= 0
		#Splitting 'self.fullName' into forename and surname
		#Working out how many characters are in the forename
		while self.fullName[count] != " ":
			count = count+1
		#Setting up a blank string
		forename = ""
		#Adding each character to the string
		for each in range(count):
			forename = forename+self.fullName[each]
		#Incrementing the count variable to account for the space between forename and surname
		count = count +1
		#Setting up a blank string
		surname=""
		#Using the full name length minus the already calculated forename length to calculate the surname length 
		for each in range(len(self.fullName)-count):
			#Adding each character to the string
			surname = surname + self.fullName[count]
			count = count +1
		for visitor in visitors:
			#matching the chosen visitor to its position in the database
			if forename == visitor[1] and surname == visitor[2]:
				#Locally assigning the visitor ID
				visitorID = visitor[0]
		#Obtaining the current date and time		
		time = datetime.datetime.now().time()
		#Selecting just the time
		outTime =time.strftime('%H:%M')
		#Appending the database to add a sign out time to the chosen user
		g_database.SignOut(visitorID,outTime)
		#Returning the user menu without opening window upon window
		self.parent.btnBack_pushed()
		self.close()
		
				