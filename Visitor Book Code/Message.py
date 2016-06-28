from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class Message(QMainWindow):
	def __init__(self,parent,message):
		super().__init__()
		#Reassigning the variables for local use
		self.parent = parent
		self.message = message
		#Setting the window title 
		self.setWindowTitle("Message")
		#Widget setting
		self.message = QLabel(self.message)
		self.btnOk = QPushButton("OK")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.message)
		self.layout.addWidget(self.btnOk)
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)
		#Setting up push button connection
		self.btnOk.clicked.connect(self.back)
	#Closing the window
	def back(self):
		self.close()
		