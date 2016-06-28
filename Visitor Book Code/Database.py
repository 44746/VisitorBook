import sqlite3
class Database:
	def __init__(self,db_name):
		self._db_name=db_name
		#Running the CreateDatabase function
		self.CreateDatabase()
	#Creating tables with all relevant variables
	def CreateDatabase(self):
		sql = """create table if not exists Visitor
			 (VisitorID integer,
			 forename text,
			 surname text,
			 reg text,
			 whom text,
			 date text,
			 inTime text,
			 outTime text,
			 primary Key(VisitorID))"""
		#Running the execute_sql function passing in the sql	 
		self.execute_sql(sql)
		
		sql ="""create table if not exists Employee
			 (EmployeeID integer,
			 forename text,
			 surname text,
			 department text,
			 primary Key(EmployeeID))"""
		#Running the execute_sql function passing in the sql	 
		self.execute_sql(sql)	 
	def execute_sql(self, sql):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute(sql)
			db.commit()
			
	def GetAllEntries(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Visitor ")
			entries = cursor.fetchall()
			return entries
	def GetAllEmployees(self):
		with sqlite3.connect(self._db_name) as db:
			cursor = db.cursor()
			cursor.execute("select * from Employee ")
			employees = cursor.fetchall()
			return employees
		
	def AddVisitor(self,forename,surname,reg,whom,date,inTime,outTime):
		with sqlite3.connect(self._db_name) as db:
				cursor = db.cursor()
				sql = "insert into Visitor(VisitorID,forename,surname,reg,whom,date,inTime,outTime) values ((SELECT max(VisitorID) FROM Visitor)+1,'{0}', '{1}', '{2}','{3}','{4}','{5}','{6}')".format(forename,surname,reg,whom,date,inTime,outTime)
				cursor.execute(sql)
				db.commit()
	def AddEmployee(self,forename,surname,department):
		with sqlite3.connect(self._db_name) as db:
				cursor = db.cursor()
				sql = "insert into Employee(EmployeeID,forename,surname,department) values ((SELECT max(EmployeeID) FROM Employee)+1,'{0}', '{1}','{2}')".format(forename,surname,department)
				cursor.execute(sql)
				db.commit()
	def DeleteEmployee(self,employeeID):
		sql = "DELETE from Employee WHERE EmployeeID = {0}".format(employeeID)
		self.execute_sql(sql)
		
	def SignOut(self,VisitorID,outTime):
		sql = "UPDATE Visitor set outTime = '{0}' where visitorID == {1}".format(outTime,VisitorID)
		self.execute_sql(sql)
		
	def DeleteVisitors(self):
		sql = "DELETE from Visitor"
		self.execute_sql(sql)
		
g_database = Database("Visitor_Database.db")