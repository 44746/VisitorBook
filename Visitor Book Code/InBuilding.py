from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
import datetime

class InBuilding(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		#Setting the window title
		self.setWindowTitle("In Building")
		#Widget set up
		self.table = QTableWidget()
		#Running the 'refreshTable' function to populate the table
		self.refreshTable()
		self.btnBack = QPushButton("Back")
		

		
		self.VlayoutMAIN = QVBoxLayout()
		self.Vlayout = QVBoxLayout()
		self.Hlayout= QHBoxLayout()
		self.Vlayout.addWidget(self.table)
		self.Hlayout.addWidget(self.btnBack)
		self.VlayoutMAIN.addLayout(self.Vlayout)
		self.VlayoutMAIN.addLayout(self.Hlayout)
		self.widget = QWidget()
		self.widget.setLayout(self.VlayoutMAIN)
		self.setCentralWidget(self.widget)
		
		#Setting up push button connection
		self.btnBack.clicked.connect(self.btnBackPushed)
		
	def refreshTable(self):
		#Getting the current date and time
		time = datetime.datetime.now()
		#Obtaining just the date in the format date/month/year
		inDate = time.strftime('%d/%m/%Y')
		#Retrieving all visitor entries from the database
		entries = g_database.GetAllEntries()
		number = 0
		#Setting the row count to the variable 'number'
		self.table.setRowCount(number)
		#Setting the column count to 8  as there is 8 headers
		self.table.setColumnCount(8) 
		#Setting the header labels
		self.table.setHorizontalHeaderLabels(["ID","Forename","Surname","Reg","Visiting","Date","Time In","Time Out"])
		row = -1
		for entry in entries:
			#Sorting through all entries to find entries that signed in on todays date and havent signed out
			if entry[7] == "N/A" and entry[5] == inDate:
				#Adding another row to the table
				number +=1
				self.table.setRowCount(number)
				column = 0
				row += 1
				#Adding the visitor to the table
				for field in entry:
					#Adding each field of that entry to the table under the correct heading
					self.table.setItem(row,column,QTableWidgetItem(str(field)))
					column += 1 
	#Returning to the parent window
	def btnBackPushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
	