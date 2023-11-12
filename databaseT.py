import pandas as pd
from datetime import datetime, timezone

class BaseOfUser:
	def __init__(self):
		self.dic = {"Ник","Имя","В какое время был в сети"}
		self.dateUsers = pd.DataFrame(self.dic)
	def toCSV(self):
		self.dateUs.to_csv('./Users.csv', index = False)
	def add(self, username, name):
		time = datetime.now(timezone.utc)
		self.dateUsers.append(pd.DataFrame({username, name, time}))


