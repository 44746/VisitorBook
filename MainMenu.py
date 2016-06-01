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
		
		self.setWindowTitle("Main Menu")
		
		self.btnUserMenu = QPushButton("User menu")
		self.btnEmployee = QPushButton("Employees")
		self.btnBook = QPushButton("Visitor Book")
		self.btnBuilding = QPushButton("In Building")
		
		self.btnUserMenu.clicked.connect(self.ShowUserMenu)
		self.btnEmployee.clicked.connect(self.ShowEmployee)
		self.btnBuilding.clicked.connect(self.ShowBuilding)
		self.btnBook.clicked.connect(self.ShowBook)
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.btnUserMenu)
		self.layout.addWidget(self.btnBook)
		self.layout.addWidget(self.btnEmployee)
		self.layout.addWidget(self.btnBuilding)
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)
	
	def ShowUserMenu(self):
		self.menu = UserMenu(self)
		self.menu.show()
		self.menu.raise_()
		
	def ShowEmployee(self):
		self.Employee= EmployeeList(self)
		self.Employee.show()
		self.Employee.raise_()
		self.hide()
		
	def ShowBook(self):
		self.book = VisitorBook(self)
		self.book.show()
		self.book.raise_()
		self.hide()
	
	def ShowBuilding(self):
		self.building = InBuilding(self)
		self.building.show()
		self.building.raise_()
		self.close()
		