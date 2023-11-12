import pandas as pd
from datetime import datetime, timezone, timedelta

class BaseOfUser:
  def __init__(self):
    self.dataUsers = pd.DataFrame()
  def toCSV(self):
    self.dataUsers.to_csv('./Users.csv', mode='a', index = False, header = False)
  def add(self, username, name):
    time = datetime.now(timezone(timedelta(hours=+3), 'MCK'))
    c_time = time.strftime('%H:%M:%S')
    c_date = time.strftime('%d.%m.%Y')
    dt =pd.DataFrame({"Ник":username, "Имя":name, "Время появления в сети":c_time, "Дата появления в сети":c_date}, index=[0])
    self.dataUsers = pd.concat([self.dataUsers, dt])
