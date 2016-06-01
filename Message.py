from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class Message(QMainWindow):
	def __init__(self,parent,message):
		super().__init__()
		self.parent = parent
		self.message = message
		self.setWindowTitle("Message")
		
		self.message = QLabel(self.message)
		self.btnOk = QPushButton("OK")

		self.layout = QVBoxLayout()
		self.layout.addWidget(self.message)
		self.layout.addWidget(self.btnOk)
		self.widget = QWidget()
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)
		
		self.btnOk.clicked.connect(self.back)

	def back(self):
		self.close()
