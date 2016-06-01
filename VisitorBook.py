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
		
		self.btnBack.clicked.connect(self.btnBackPushed)
		self.btnClear.clicked.connect(self.btnClearPushed)
		
		self.VlayoutMAIN = QVBoxLayout()
		self.Vlayout = QVBoxLayout()
		self.Hlayout= QHBoxLayout()
		self.Vlayout.addWidget(self.table)
		self.Hlayout.addWidget(self.btnBack)
		self.Hlayout.addWidget(self.btnClear)
		self.VlayoutMAIN.addLayout(self.Vlayout)
		self.VlayoutMAIN.addLayout(self.Hlayout)
		self.widget = QWidget()
		self.widget.setLayout(self.VlayoutMAIN)
		self.setCentralWidget(self.widget)
		
		
		
		
	def refreshTable(self):
		entries = g_database.GetAllEntries()
		self.table.setRowCount(len(entries))
		self.table.setColumnCount(7) 
		self.table.setHorizontalHeaderLabels(["ID","Forename","Surname","Reg","Visiting","Time In","Time Out"])
		row = -1
		for entry in entries:
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
		