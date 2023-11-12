import pandas as pd
from datetime import datetime, timezone

class BaseOfUser:
  def __init__(self):
    self.dataUsers = pd.DataFrame()
  def toCSV(self):
    self.dataUsers.to_csv('./Users.csv', mode='a', index = False)
  def add(self, username, name):
    time = datetime.now(timezone.utc)
    dt =pd.DataFrame({"Ник":username, "Имя":name, "В какое время был в сети":time}, index=[0])
    self.dataUsers = pd.concat([self.dataUsers, dt])
