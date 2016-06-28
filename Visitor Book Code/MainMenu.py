from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys 
from UserMenu import *
from EmployeeList import *
from VisitorBook import *
from InBuilding import *

class MainMenu(QMainWindow):
	def __init__(self):
		super().__init__()
		#Setting the window title
		self.setWindowTitle("Main Menu")
		#Widget set up
		self.btnUserMenu = QPushButton("User menu")
		self.btnEmployee = QPushButton("Employees")
		self.btnBook = QPushButton("Visitor Book")
		self.btnBuilding = QPushButton("In Building")
		
	
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.btnUserMenu)
		self.layout.addWidget(self.btnBook)
		self.layout.addWidget(self.btnEmployee)
		self.layout.addWidget(self.btnBuilding)
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)
		
		#Setting up push button connections
		self.btnUserMenu.clicked.connect(self.ShowUserMenu)
		self.btnEmployee.clicked.connect(self.ShowEmployee)
		self.btnBuilding.clicked.connect(self.ShowBuilding)
		self.btnBook.clicked.connect(self.ShowBook)
		
	def ShowUserMenu(self):
		#Calling the 'UserMenu' window
		self.menu = UserMenu(self)
		#Showing the window
		self.menu.show()
		#Raising the window to the front of the screen
		self.menu.raise_()
		
	def ShowEmployee(self):
		#Calling the 'EmployeeList' window
		self.employee= EmployeeList(self)
		#Showing the window
		self.employee.show()
		#Raising the window to the front of the screen
		self.employee.raise_()
		#Closing the current window
		self.close()
		
	def ShowBook(self):
		#Calling the 'VisitorBook' window
		self.book = VisitorBook(self)
		#Showing the window
		self.book.show()
		#Raising the window to the front of the screen
		self.book.raise_()
		#Closing the current window
		self.close()
	
	def ShowBuilding(self):
		#Calling the 'InBuilding' window
		self.building = InBuilding(self)
		#Showing the window
		self.building.show()
		#Raising the window to the front of the screen
		self.building.raise_()
		#Closing the current window
		self.close()
		