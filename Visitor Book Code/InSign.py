from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 
from Database import *
import datetime
from Message import *
import os

class InSign(QMainWindow):
	def __init__(self,parent):
		super().__init__(parent)
		self.parent=parent
		#Setting the window title
		self.setWindowTitle("Sign In")
		#Widget set up
		self.forename = QLineEdit()
		self.labelF = QLabel("Forename: ")
		self.surname = QLineEdit()
		self.labelS = QLabel("Surname: ")
		self.reg = QLineEdit()
		self.labelR = QLabel("Car registration: ")
		self.labelE = QLabel("Visiting: ")
		self.EmployeeCombo = QComboBox()
		self.PopulateEmployeeComboBox()
		self.btnSignIn = QPushButton("Sign in")
		self.btnCancel = QPushButton("Cancel")
		#Using two & symbols to make it show up on the button
		self.btnTC = QPushButton("T&&C's")
		self.labelTC = QLabel("I have read and agree to the T&C's:")
		self.tick =QCheckBox()
		
		self.VLayoutMAIN = QVBoxLayout()
		self.VLayout1 = QVBoxLayout()
		self.VLayout2 = QVBoxLayout()
		self.HLayout1 = QHBoxLayout()
		self.HLayout2 = QHBoxLayout()
		self.HLayout3 = QHBoxLayout()
		
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
		self.HLayout2.addWidget(self.btnTC)
		self.HLayout2.addWidget(self.btnSignIn)
		self.HLayout3.addWidget(self.labelTC)
		self.HLayout3.addWidget(self.tick)
		self.VLayoutMAIN.addLayout(self.HLayout1)
		self.VLayoutMAIN.addLayout(self.HLayout3)
		self.VLayoutMAIN.addLayout(self.HLayout2)
		self.widget = QWidget()
		self.widget.setLayout(self.VLayoutMAIN)
		self.setCentralWidget(self.widget)
		
		#Setting up push button connections
		self.btnSignIn.clicked.connect(self.btnSignIn_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
		self.btnTC.clicked.connect(self.btnTC_pushed)
	
	
	
	def PopulateEmployeeComboBox(self):
		#Retrieving all employess from the database
		employees = g_database.GetAllEmployees()
		#Creating a blank list
		name_list = []
		for employee in employees:
			#Creating a full name
			name= ""
			#Adding the employee's name and department to the string
			name= name+ (employee[2]) + " " + (employee[1][0])+ " (" + (employee[3])+")"
			#Adding the full name to the drop down box
			name_list.append(name)
		#Sorting the list into alphabetical order
		name_list.sort()
		#Sorting through each employee
		for employee in name_list:
			#Adding the employee to the drop down box in alphabetical order
			self.EmployeeCombo.addItem(employee)
	
	def btnTC_pushed(self):
		#Starting the file called 'text.txt' using operating system commands
		os.startfile("text.txt")
		
	def btnSignIn_pushed(self):
		#Obtaining the selected index
		indexEmployee = self.EmployeeCombo.currentIndex()
		#Retrieving all the employee entries from the database
		employees = g_database.GetAllEmployees()
		#Assigning 'employee' to its data in the database
		employee = employees[indexEmployee]
		name= ""
		#Adding the forname initial and a space to the string
		name= name+(employee[1][0])+ " "
		#Adding the surname to the string
		name= name+(employee[2])
		#Re-assigning 'employee' to the variable 'name'
		employee = name
		#Obtaining the current date and time
		time = datetime.datetime.now()
		#Obtaining just the time in the format hour:minute
		inTime =time.strftime('%H:%M')
		#Obataining just the date in the format day/month/year
		inDate = time.strftime('%d/%m/%Y')
		#Assigning 'outTime' to "N/A" as the user hasnt signed out
		outTime = "N/A"
		
		
		#Validation
		#Converting the users input to text
		forename = self.forename.text()
		surname = self.surname.text()
		registration = self.reg.text()
		forename_valid = True
		surname_valid = True
		reg_valid = False
		
		#Checking if the line edit has been left blank
		if forename != "" and surname != "" and registration != "":
			#Converting the forename and surname to lower case for easier validation
			forename = forename.lower()
			surname = surname.lower()
			#Setting up blank lists to append the alphabet into 
			alphabet = ['-']
			#Creating the alphabet from ascii characters 
			for letter in map(chr, range(97, 123)):
				#Adding the character to the blank list
				alphabet.append(letter)
			count = -1
			#Sorting through each character in 'forename'
			for each in forename:
				#Checking to see if its in the alphabet
				if each not in alphabet:
					forename_valid = False
			#Sorting through each character in 'surname'
			for each in surname:
				#Checking to see if its in the alphabet
				if each not in alphabet:
					surname_valid = False
			
			if forename_valid == False:
				#Calling the message window, passing in the message to display
				self.error = Message(self,"Please enter a valid Forename")
				#Showing the window
				self.error.show()
				#Raising the window the front of the screen
				self.error.raise_()
			if surname_valid == False:
					#Calling the message window, passing in the message to display
					self.error = Message(self,"Please enter a valid Surname")
					#Showing the window
					self.error.show()
					#Raising the window the front of the screen
					self.error.raise_()	
			
			#Making the initial upper case
			initial = forename[0].upper()
			count = 1
			#Adding the rest of the 'forename' to the new string
			for each in range(len(forename)-1):
				initial= initial + forename[count]
				count +=1
			forename = initial
			
			#Making the initial upper case
			initial = surname[0].upper()
			count = 1
			#Adding the rest of the 'forename' to the new string
			for each in range(len(surname)-1):
				initial= initial + surname[count]
				count +=1
			surname = initial
			
			#Converting all of registration to upper case to format it correctly
			registration= registration.upper()
			#Checking that the registration number is less than or equal to 7
			if len(registration) <= 7:
				reg_valid = True
			else:
				#Calling the message window, passing in the message to display
				self.error = Message(self,"Please enter a valid Registration Number ('N/A' if not applicable)")
				#Showing the window
				self.error.show()
				#Raising the window the front of the screen
				self.error.raise_()
		

			if reg_valid == True and forename_valid == True and surname_valid == True:
					#Checking if the tick box is checked
					if self.tick.isChecked():
						#Adding the entered validated data to the database
						g_database.AddVisitor(forename,surname,registration,employee,inDate,inTime,outTime)
						self.parent.show()
						self.parent.raise_()
						#Calling the message window, passing in the message to display
						self.message=Message(self,"Please see a Receptionist to obtain your Visitor Pass")
						self.message.show()
						self.message.raise_()
						self.close()
		
					else:
						#Calling the message window, passing in the message to display
						self.error = Message(self,"Please read and agree to the terms and conditions")
						self.error.show()
						self.error.raise_()
				
		else:
			if forename == "" and surname == "" and registration =="":
				self.error = Message(self,"Please enter a forename, a surname and a registration number")
				self.error.show()
				self.error.raise_()
			elif forename == "" and surname=="":
				self.error = Message(self,"Please enter a forename and a surname")
				self.error.show()
				self.error.raise_()
			elif forename=="" and registration == "":
				self.error = Message(self,"Please enter a forename and a registration number")
				self.error.show()
				self.error.raise_()
			elif surname=="" and registration == "":
				self.error = Message(self,"Please enter a surname and a registration number")
				self.error.show()
				self.error.raise_()
			elif forename == "":
				self.error = Message(self,"Please enter a forename")
				self.error.show()
				self.error.raise_()
			elif surname =="":
				self.error = Message(self,"Please enter a surname")
				self.error.show()
				self.error.raise_()
			elif registration == "":
				self.error = Message(self,"Please enter a registration number ('N/A' if not applicable)")
				self.error.show()
				self.error.raise_()
	#Returning to the parent window	
	def btnCancel_pushed(self):
		self.parent.show()
		self.close()
		
			
			