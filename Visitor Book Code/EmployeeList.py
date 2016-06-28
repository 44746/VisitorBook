from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sqlite3
from Database import *
from AddEmployee import *

class EmployeeList(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent=parent
		#Setting the window title
		self.setWindowTitle("Employees")
		#Widget set up 
		self.btnBack =QPushButton("Back")
		self.btnDelete=QPushButton("Delete")
		self.btnAdd=QPushButton("New Employee")
		self.employeeList = QListWidget()
		self.vLayoutMAIN = QVBoxLayout()
		self.hLayout1 = QHBoxLayout()
		self.hLayout1.addWidget(self.btnBack)
		self.hLayout1.addWidget(self.btnDelete)
		self.hLayout1.addWidget(self.btnAdd)
		self.vLayoutMAIN.addWidget(self.employeeList)
		self.vLayoutMAIN.addLayout(self.hLayout1)
		
		self.widget = QWidget()
		self.widget.setLayout(self.vLayoutMAIN)
		self.setCentralWidget(self.widget)
		#Running the refresh list function to populate the list
		self.refresh_List()
		#Setting up push button connections
		self.btnBack.clicked.connect(self.btnBack_pushed)
		self.btnDelete.clicked.connect(self.btnDelete_pushed)
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
	#Returning to the parent window
	def btnBack_pushed(self):
		self.parent.show()
		self.parent.raise_()
		self.hide()
		
	def btnDelete_pushed(self):
		#Retrieving all employees from the database
		employees = g_database.GetAllEmployees()
		#Converting the selected item to text
		currentItem = self.employeeList.currentItem().text()
		count= 0
		#Calculating the length of the selected item
		while currentItem[count] != " ":
			count = count+1
		#Setting up a blank string
		forename = ""
		for each in range(count):
			#Adding each character to the string
			forename = forename+currentItem[each]
		#Incrementing the count variable to account for the space between forename and surname
		count = count +1
		count2 = 0
		#Working out where the surname ends
		while currentItem[count2] != "(":
			count2 +=1	
		#Setting up a blank string
		surname=""
		#Minus 1 to account for the space
		count2 -=1
		#Using the full name length minus the already calculated forename length to calculate the surname length 
		for each in range(count2-count):
			#Adding each character to the string
			surname = surname + currentItem[count]
			count = count +1
	
		#Adding 2 to account for the bracket and the space
		count2 +=2
		#Setting up a blank string
		department = ""
		for each in range(count2,(len(currentItem)-1)):
			department = department + currentItem[each]
		for employee in employees:
			#matching the chosen employee to its position in the database
			if forename == employee[1] and surname == employee[2] and department == employee[3]:
				#Locally assigning the visitor ID
				employeeID = employee[0]
				
				#Deleting that employee from the database
				g_database.DeleteEmployee(employeeID)
		#Running the refresh list function to re-populate the list to account for the recently deleted employee
		self.refresh_List()
		
	def btnAdd_pushed(self):
		#Calling the 'addEmployee' window
		self.Employee= addEmployee(self)
		self.Employee.show()
		self.Employee.raise_()
		self.close()
	
	def refresh_List(self):
		#Retrieving all employee entries from the database
		employees = g_database.GetAllEmployees()
		row = -1
		#clearing the current list
		self.employeeList.clear()
		#sorting through each individual employee
		for employee in employees:
			row = row+1
			#Creating a full name
			name = ""
			#Adding the employees name and department to the string
			name= name + (employee[1]) + " " +(employee[2]) + " (" + (employee[3]) + ")"
			#Adding the employees full name to the list
			self.employeeList.addItem(name)
		

		