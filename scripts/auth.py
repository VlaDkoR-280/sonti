from telethon.sync import TelegramClient
import time
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from scripts import data as db
from scripts import info
data = [info._NUM, info._API_ID, info._API_HASH] # phone, api_id, api_hash

def Start():
    client = TelegramClient(data[0], data[1], data[2])
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
	try: 
		while (1):
			for username in usernames: #нужно добавить проверку на существование пользователя
				name, statusOfUser = status(client, username)
				if statusOfUser == 'UserStatusOnline':
					db.SaveToDB(username, name, cout)
			time.sleep(10)
	except Exception as e:
		print(f'Ошибка перебора: {e}')
		client.disconnect()
	client.disconnect()
