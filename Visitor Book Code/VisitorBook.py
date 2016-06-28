from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
from clearClarification import *
from Message import *

class VisitorBook(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		#Setting the window title
		self.setWindowTitle("Visitor Book")
		#Widget set up
		self.table = QTableWidget()
		self.refreshTable()
		self.btnBack = QPushButton("Back")
		self.btnClear = QPushButton("Clear")
		
		self.labelS = QLabel("Search:")
		self.searchTerm = QLineEdit("")
		self.btnSearch = QPushButton("Search")
		
		self.Hlayout1 = QHBoxLayout()
		self.VlayoutMAIN = QVBoxLayout()
		self.Vlayout = QVBoxLayout()
		self.Hlayout= QHBoxLayout()
		self.Vlayout.addWidget(self.table)
		self.Hlayout.addWidget(self.btnBack)
		self.Hlayout.addWidget(self.btnClear)
		self.Hlayout1.addWidget(self.labelS)
		self.Hlayout1.addWidget(self.searchTerm)
		self.Hlayout1.addWidget(self.btnSearch)
		self.VlayoutMAIN.addLayout(self.Hlayout1)
		self.VlayoutMAIN.addLayout(self.Vlayout)
		self.VlayoutMAIN.addLayout(self.Hlayout)
		self.widget = QWidget()
		self.widget.setLayout(self.VlayoutMAIN)
		self.setCentralWidget(self.widget)
		
		#Setting up push button connections
		self.btnBack.clicked.connect(self.btnBackPushed)
		self.btnClear.clicked.connect(self.btnClearPushed)
		self.btnSearch.clicked.connect(self.btnSearchPushed)
		
		
		
		
	def refreshTable(self):
		#Retrieving all visitor entries from the database
		entries = g_database.GetAllEntries()
		#Setting the row count to the number of entries so that there are no empty rows
		self.table.setRowCount(len(entries))
		#Setting the coloumn count to 8
		self.table.setColumnCount(8) 
		#Setting the header labels
		self.table.setHorizontalHeaderLabels(["ID","Forename","Surname","Reg","Visiting","Date","Time In","Time Out"])
		row = -1
		#Sorting through each entry
		for entry in entries:
			column = 0
			row += 1
			#Sorting through each field in each entry
			for field in entry:
				#Adding each field to the table
				self.table.setItem(row,column,QTableWidgetItem(str(field)))
				column += 1 
	
	def btnSearchPushed(self):
		#Clearing the table
		self.table.clear()
		#Converting the users input to text
		term = self.searchTerm.text()
		#converting the term to lower case to allow for user input error
		term = term.lower()
		
		#Checking if the user actually entered something
		if term == "":
			#Running the 'refreshTable' function
			self.refreshTable()
		else:
			
			#Retrieving all visitor entries from the database
			entries = g_database.GetAllEntries()
			RowCount = 0
			#Setting the row count
			self.table.setRowCount(RowCount)
			#Setting the coloumn count
			self.table.setColumnCount(8) 
			#Setting the table headers
			self.table.setHorizontalHeaderLabels(["ID","Forename","Surname","Reg","Visiting","Date","Time In","Time Out"])
			row = -1
			#Sorting through each entry in the database
			#Setting the variable to True
			table_empty =True
			for entry in entries:
				#Obtaining the forename from the database
				forename = entry[1]
				#converting the forename to lower case to allow for user input error
				forename=forename.lower()
				#Obtaining the surname from the database
				surname = entry[2]
				#converting the surname to lower case to allow for user input error
				surname = surname.lower()
				#Converting the id intger to a string so it can be compared to the term, as the term is text
				ID = str(entry[0])
				#Obtaining the registration number from the database
				reg = entry[3]
				#converting the registration number to lower case to allow for user input error
				reg = reg.lower()
				##Obtaining the employee being visited from the database
				visiting = entry[4]
				#converting visiting to lower case to allow for user input error
				visiting = visiting.lower()
				#Checking to see if the term matches any of the fields in the database
				if term == ID or term == forename or term == surname or term == reg or term == visiting or term == entry[5] or term == entry[6] or term == entry[7]:
					RowCount +=1
					#Resetting the row count to allow the program to add the found visitor
					self.table.setRowCount(RowCount)
					column = 0
					row += 1
					#Sorting through each field in that entry
					for field in entry:
						#Adding the field to the table
						self.table.setItem(row,column,QTableWidgetItem(str(field)))
						column += 1 
					#Changing table_empty to False if an entry has been entered into the table
					table_empty = False
			if table_empty == True:
				#Calling the message window, passing in the message to display
				self.error = Message(self,"No entries found, please try again")
				self.error.show()
				self.error.raise_()
				self.refreshTable()
	#Returning to the parent window		
	def btnBackPushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
	
	def btnClearPushed(self):
		#Calling the clarification window
		self.clear = Clarification(self)
		#Showing the window
		self.clear.show()
		#Raising the window to the front of the screen
		self.clear.raise_()
		#Closing the current window
		self.close()

		