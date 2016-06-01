from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
from Message import *

class addEmployee(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		self.setWindowTitle("Add employee")
		
		self.forename = QLineEdit()
		self.labelF = QLabel("Forename: ")
		self.surname = QLineEdit()
		self.labelS = QLabel("Surname: ")
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		
		self.VLayoutMAIN = QVBoxLayout()
		self.VLayout1 = QVBoxLayout()
		self.VLayout2 = QVBoxLayout()
		self.HLayout1 = QHBoxLayout()
		self.HLayout2 = QHBoxLayout()
		
		self.VLayout1.addWidget(self.labelF)
		self.VLayout1.addWidget(self.labelS)
		self.VLayout2.addWidget(self.forename)
		self.VLayout2.addWidget(self.surname)
		self.HLayout1.addLayout(self.VLayout1)
		self.HLayout1.addLayout(self.VLayout2)
		self.HLayout2.addWidget(self.btnCancel)
		self.HLayout2.addWidget(self.btnAdd)
		self.VLayoutMAIN.addLayout(self.HLayout1)
		self.VLayoutMAIN.addLayout(self.HLayout2)
		self.widget = QWidget()
		self.widget.setLayout(self.VLayoutMAIN)
		self.setCentralWidget(self.widget)
		
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
		
	def btnAdd_pushed(self):
		forename = self.forename.text()
		surname = self.surname.text()
		
		forename_valid = False
		surname_valid = False
		
		if forename != "" and surname != "":
			alphabet_lower = []
			alphabet_upper =[]
			for letter in map(chr, range(97, 123)):
				alphabet_lower.append(letter)
			for letter in map(chr, range(65,91)):
				alphabet_upper.append(letter)
			
			forename_valid = True
			count = -1
			for each in forename:
				count = count +1
				if count == 0:
					if forename[count] not in alphabet_upper:
						forename_valid = False
				else:
					if forename_valid == True and each not in alphabet_lower:
						forename_valid = False	
			if forename_valid == False:
				self.error = Message(self,"Please enter a valid Forename")
				self.error.show()
				self.error.raise_()
			
			if forename_valid == True:
				surname_valid = True
				count = -1
				for each in surname:
					count = count +1
					if count == 0:
						if surname[count] not in alphabet_upper:
							surname_valid = False
					else:
						if surname_valid == True and each not in alphabet_lower:
							surname_valid = False			
				if surname_valid == False:
					self.error = Message(self,"Please enter a valid Surname")
					self.error.show()
					self.error.raise_()	
				if surname_valid == True:
					g_database.AddEmployee(forename,surname)
					self.parent.show()
					self.parent.raise_()
					self.parent.refresh_List()
					self.close()
		
		else:
			self.error = Message(self,"Please enter data in every field")
			self.error.show()
			self.error.raise_()
		
	
	def btnCancel_pushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
		
	

