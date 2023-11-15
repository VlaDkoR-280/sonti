from telethon.sync import TelegramClient
import time
import os
import sys
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from scripts import data as db
from scripts import info
from multiprocessing import Process, Value
data = [info._NUM, info._API_ID, info._APP_HASH] # phone, api_id, api_hash
def Auth():
    client = TelegramClient(data[0], data[1], data[2])
    client.start()
    client.disconnect()
def Start():
    client = TelegramClient(os.path.join(os.path.expanduser('~'), '.telegram.session'), data[1], data[2])
    client.start()
    return client


def status(client, username):
	try:
		entity = client.get_entity(username)
		return entity.first_name, (str(entity.status)[:str(entity.status).find('(')])
	except Exception as e:
		print(f'Не удалось получить информацию о пользователе: {e}')

def watchOfUsers(usernames, cout):
	client = Start()
	breakLoop = Value('i', 0) 
	def LoopScan(breakLoop):
		while not(breakLoop.value):
			for username in usernames: #нужно добавить проверку на существование пользователя
				name, statusOfUser = status(client, username)
				if statusOfUser == 'UserStatusOnline':
					db.SaveToDB(username, name, cout)
				time.sleep(5)
		print("Выход из программы")
	def LoopInput(breakLoop):
		while(not(breakLoop.value)):
			line = os.read(0, 1024).decode()
			if line == 'q\n':
				breakLoop.value = 1
	try:
		processScan = Process(target=LoopScan, args=(breakLoop,))
		processInput = Process(target=LoopInput, args=(breakLoop,))
		processInput.start()		
		processScan.start()

		processInput.join()
		processScan.join()
		
	except Exception as e:
		print(f'Ошибка перебора: {e}')
		client.disconnect()
	client.disconnect()
