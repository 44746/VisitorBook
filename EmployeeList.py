from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sqlite3
from Database import *
from AddEmployee import *

class EmployeeList(QMainWindow):
	def __init__(self,parent):
		super().__init__(parent)
		self.parent=parent
		
		self.setWindowTitle("Employees")
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
		
		self.refresh_List()
		self.btnBack.clicked.connect(self.btnBack_pushed)
		self.btnDelete.clicked.connect(self.btnDelete_pushed)
		self.btnAdd.clicked.connect(self.btnAdd_pushed)
		
	def btnBack_pushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
		
	def btnDelete_pushed(self):
		employees = g_database.GetAllEmployees()
		currentItem = self.employeeList.currentItem().text()
		count= 0
		while currentItem[count] != " ":
			count = count+1
		forename = ""
		for each in range(count):
			forename = forename+currentItem[each]
		count = count +1
		surname=""
		for each in range(len(currentItem)-count):
			surname = surname + currentItem[count]
			count = count +1
		
		for employee in employees:
			if forename == employee[1] and surname == employee[2]:
				employeeID = employee[0]
				g_database.DeleteEmployee(employeeID)
			
		self.refresh_List()
		
	def btnAdd_pushed(self):
		self.Employee= addEmployee(self)
		self.Employee.show()
		self.Employee.raise_()
		self.close()
	
	def refresh_List(self):
		employees = g_database.GetAllEmployees()
		row = -1
		self.employeeList.clear()
		for employee in employees:
			row = row+1
			name = ""
			name= name + (employee[1]) + " "
			name = name + (employee[2])
			self.employeeList.addItem(name)
		

		