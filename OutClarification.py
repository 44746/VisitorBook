from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
import datetime


class Clarification(QMainWindow):
	def __init__(self,parent,fullName):
		super().__init__()
		self.parent = parent
		self.fullName = fullName
		self.setWindowTitle("Sign Out")
		
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
		
		self.btnBack.clicked.connect(self.btnBackPushed)
		self.btnOut.clicked.connect(self.btnOutClicked)
		
	def btnBackPushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
	
	def btnOutClicked(self):
		visitors = g_database.GetAllEntries()
		count= 0
		while self.fullName[count] != " ":
			count = count+1
		forename = ""
		for each in range(count):
			forename = forename+self.fullName[each]
		count = count +1
		surname=""
		for each in range(len(self.fullName)-count):
			surname = surname + self.fullName[count]
			count = count +1
		for visitor in visitors:
			if forename == visitor[1] and surname == visitor[2]:
				visitorID = visitor[0]
				
		time = datetime.datetime.now().time()
		outTime =time.strftime('%H:%M')
		g_database.SignOut(visitorID,outTime)
		
		self.parent.btnBack_pushed()
		self.close()
		
				