from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
class VisitorBook(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		self.setWindowTitle("Visitor Book")
		
		self.table = QTableWidget()
		self.refreshTable()
		self.btnBack = QPushButton("Back")
		self.btnClear = QPushButton("Clear")
		
		self.labelS = QLabel("Search:")
		self.searchTerm = QLineEdit("")
		self.btnSearch = QPushButton("Search")
		
		self.btnBack.clicked.connect(self.btnBackPushed)
		self.btnClear.clicked.connect(self.btnClearPushed)
		self.btnSearch.clicked.connect(self.btnSearchPushed)
		
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
		
		
		
		
	def refreshTable(self):
		entries = g_database.GetAllEntries()
		self.table.setRowCount(len(entries))
		self.table.setColumnCount(8) 
		self.table.setHorizontalHeaderLabels(["ID","Forename","Surname","Reg","Visiting","Date","Time In","Time Out"])
		row = -1
		for entry in entries:
			column = 0
			row += 1
			for field in entry:
				self.table.setItem(row,column,QTableWidgetItem(str(field)))
				column += 1 
	
	def btnSearchPushed(self):
		self.table.clear()
		term = self.searchTerm.text()
		entries = g_database.GetAllEntries()
		RowCount = 0
		self.table.setRowCount(RowCount)
		self.table.setColumnCount(8) 
		self.table.setHorizontalHeaderLabels(["ID","Forename","Surname","Reg","Visiting","Date","Time In","Time Out"])
		row = -1
		for entry in entries:
			if term == entry[0] or term == entry[1] or term == entry[2] or term == entry[3] or term == entry[5] or term == entry[6] or term == entry[7]:
				RowCount +=1
				self.table.setRowCount(RowCount)
				column = 0
				row += 1
				for field in entry:
					self.table.setItem(row,column,QTableWidgetItem(str(field)))
					column += 1 
					
	def btnBackPushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
	
	def btnClearPushed(self):
		g_database.DeleteVisitors()
		self.parent.show()
		self.parent.raise_()
		self.close()
		