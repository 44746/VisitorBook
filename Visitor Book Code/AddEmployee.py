from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
#Importing all required relations
from Database import *
from Message import *

class addEmployee(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		#Setting the window title
		self.setWindowTitle("Add employee")
		#Widget set up
		self.forename = QLineEdit()
		self.labelF = QLabel("Forename: ")
		self.surname = QLineEdit()
		self.labelS = QLabel("Surname: ")
		self.btnAdd = QPushButton("Add")
		self.btnCancel = QPushButton("Cancel")
		self.labelD = QLabel("Department:")
		self.department = QComboBox()
		
		#Adding the departments
		self.department.addItem("Marketing")
		self.department.addItem("Production")
		self.department.addItem("Sales")
		self.department.addItem("R&D")
	
		self.VLayoutMAIN = QVBoxLayout()
		self.VLayout1 = QVBoxLayout()
		self.VLayout2 = QVBoxLayout()
		self.HLayout1 = QHBoxLayout()
		self.HLayout2 = QHBoxLayout()
		
		self.VLayout1.addWidget(self.labelF)
		self.VLayout1.addWidget(self.labelS)
		self.VLayout1.addWidget(self.labelD)
		self.VLayout2.addWidget(self.forename)
		self.VLayout2.addWidget(self.surname)
		self.VLayout2.addWidget(self.department)
		self.HLayout1.addLayout(self.VLayout1)
		self.HLayout1.addLayout(self.VLayout2)
		self.HLayout2.addWidget(self.btnCancel)
		self.HLayout2.addWidget(self.btnAdd)
		self.VLayoutMAIN.addLayout(self.HLayout1)
		self.VLayoutMAIN.addLayout(self.HLayout2)
		self.widget = QWidget()
		self.widget.setLayout(self.VLayoutMAIN)
		self.setCentralWidget(self.widget)
		
		#Setting up button connections, to run functions when the buttons are pushed
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		self.btnCancel.clicked.connect(self.btnCancel_pushed)
	
	def btnAdd_pushed(self):
		#Converting the entries to text
		forename = self.forename.text()
		surname = self.surname.text()
		#Obtaining the selected index
		index = self.department.currentIndex()
		if index == 0:
			department = "Marketing"
		elif index == 1:
			department = "Production"
		elif index == 2:
			department = "Sales"
		elif index == 3:
			department = "R&D"
		
		forename_valid = True
		surname_valid = True
		#Checking if the line edit has been left blank
		if forename != "" and surname != "":
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
			
			if forename_valid == True and surname_valid == True:
				#Running the 'AddEmployee' function in the database to add the data to the database
				g_database.AddEmployee(forename,surname,department)
				#Showing the window
				self.parent.show()
				#Raising the window the front of the screen
				self.parent.raise_()
				#Refreshing the 'refresh_List' in the parent window to show the new addition 
				self.parent.refresh_List()
				#Closing the current window
				self.close()
					
		else:
			if forename =="" and surname == "":
				#Calling the message window, passing in the message to display
				self.error = Message(self,"Please enter a Forename and Surname")
				#Showing the window
				self.error.show()
				#Raising the window the front of the screen
				self.error.raise_()
			elif forename == "":	
				#Calling the message window, passing in the message to display
				self.error = Message(self,"Please enter a Forename")
				#Showing the window
				self.error.show()
				#Raising the window the front of the screen
				self.error.raise_()
			elif surname=="":
				#Calling the message window, passing in the message to display
				self.error = Message(self,"Please enter a Surname")
				#Showing the window
				self.error.show()
				#Raising the window the front of the screen
				self.error.raise_()
			
		
	#Returning the to the parent window 
	def btnCancel_pushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
		
	

