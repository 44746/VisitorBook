from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 
from Database import *
import datetime
from Message import *

class InSign(QMainWindow):
	def __init__(self,parent):
		super().__init__(parent)
		self.parent=parent
		self.setWindowTitle("Sign In")
		
		self.forename = QLineEdit()
		self.labelF = QLabel("Forename: ")
		
		self.surname = QLineEdit()
		self.labelS = QLabel("Surname: ")
		
		self.reg = QLineEdit()
		self.labelR = QLabel("Reg #: ")
		
		self.labelE = QLabel("Visiting: ")
		self.EmployeeCombo = QComboBox()
		self.PopulateEmployeeComboBox()
		self.btnSignIn = QPushButton("Sign in")
		self.btnCancel = QPushButton("Cancel")
		
		self.VLayoutMAIN = QVBoxLayout()
		self.VLayout1 = QVBoxLayout()
		self.VLayout2 = QVBoxLayout()
		self.HLayout1 = QHBoxLayout()
		self.HLayout2 = QHBoxLayout()
		
		self.VLayout1.addWidget(self.labelF)
		self.VLayout1.addWidget(self.labelS)
		self.VLayout1.addWidget(self.labelR)
		self.VLayout1.addWidget(self.labelE)
		self.VLayout2.addWidget(self.forename)
		self.VLayout2.addWidget(self.surname)
		self.VLayout2.addWidget(self.reg)
		self.VLayout2.addWidget(self.EmployeeCombo)
		self.HLayout1.addLayout(self.VLayout1)
		self.HLayout1.addLayout(self.VLayout2)
		self.HLayout2.addWidget(self.btnCancel)
		self.HLayout2.addWidget(self.btnSignIn)
		self.VLayoutMAIN.addLayout(self.HLayout1)
		self.VLayoutMAIN.addLayout(self.HLayout2)
		self.widget = QWidget()
		self.widget.setLayout(self.VLayoutMAIN)
		self.setCentralWidget(self.widget)
		
		self.btnSignIn.clicked.connect(self.btnSignIn_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
	
	
	
	def PopulateEmployeeComboBox(self):
		employees = g_database.GetAllEmployees()
		for employee in employees:
			name= ""
			name= name+(employee[1][0])+ " "
			name= name+(employee[2])
			
			self.EmployeeCombo.addItem(name)
		
	def btnSignIn_pushed(self):
		indexEmployee = self.EmployeeCombo.currentIndex()
		employees = g_database.GetAllEmployees()
		employee = employees[indexEmployee]
		name= ""
		name= name+(employee[1][0])+ " "
		name= name+(employee[2])
		employee = name
		time = datetime.datetime.now().time()
		inTime =time.strftime('%H:%M')
		outTime = "N/A"
		
		
		forename = self.forename.text()
		surname = self.surname.text()
		registration = self.reg.text()
		forename_valid = False
		surname_valid = False
		reg_valid = False
		
		if forename != "" and surname != "" and registration != "":
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
				if forename_valid==True and surname_valid == True:
					if len(registration) <= 7:
						reg_valid = True
					else:
						self.error = Message(self,"Please enter a valid Registration Number")
						self.error.show()
						self.error.raise_()	
			if reg_valid == True:
				g_database.AddVisitor(forename,surname,registration,employee,inTime,outTime)
				self.parent.show()
				self.parent.raise_()
		
				self.message=Message(self,"Please see a Receptionist to obtain your Visitor Pass")
				self.message.show()
				self.message.raise_()
				self.close()
		else:
			self.error = Message(self,"Please enter data in every field")
			self.error.show()
			self.error.raise_()
		
	def btnCancel_pushed(self):
		self.parent.show()
		self.close()
		
			
			