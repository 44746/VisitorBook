from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from Database import *
import datetime

class InBuilding(QMainWindow):
	def __init__(self,parent):
		super().__init__()
		self.parent = parent
		self.setWindowTitle("In Building")
		
		self.table = QTableWidget()
		self.refreshTable()
		self.btnBack = QPushButton("Back")
		
		
		self.btnBack.clicked.connect(self.btnBackPushed)
		
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
				
	def refreshTable(self):
		time = datetime.datetime.now()
		inDate = time.strftime('%d/%m/%Y')
		entries = g_database.GetAllEntries()
		self.table.setRowCount(len(entries))
		self.table.setColumnCount(7) 
		self.table.setHorizontalHeaderLabels(["ID","Forename","Surname","Reg","Visiting","Date","Time In","Time Out"])
		row = -1
		for entry in entries:
			if entry[7] == "N/A" and entry[5] == inDate:
				column = 0
				row += 1
				for field in entry:
					self.table.setItem(row,column,QTableWidgetItem(str(field)))
					column += 1 
				
	def btnBackPushed(self):
		self.parent.show()
		self.parent.raise_()
		self.close()
	