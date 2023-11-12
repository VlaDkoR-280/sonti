from telethon.sync import TelegramClient
import time
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import databaseT
data = ["Null", "Null", "Null"] # phone, api_id, api_hash

def Start():
    with open('info.txt', 'r') as f:
        for i in range(3):
            data[i] = f.readline().split('\n')[0]

    client = TelegramClient(data[0], data[1], data[2])
    client.start()
    return client

def status(client, username):
	print('Наш пользователь: ', username)
	try:
		entity = client.get_entity(username)
		return entity.first_name, (str(entity.status)[:str(entity.status).find('(')])
	except Exception as e:
		print(f'Не удалось получить информацию о пользователе: {e}')

def watchOfUsers(usernames):
	client = Start() 
	try: 
		while (1):
			for username in usernames: #нужно добавить проверку на существование пользователя
				print('Проверка пользователя: ', usernames)
				name, statusOfUser = status(client, username)
				if statusOfUser == 'UserStatusOnline':
					databaseT.SaveToDB(username, name)
			time.sleep(10)
	except Exception as e:
		print(f'Ошибка перебора: {e}')
		client.disconnect()
	client.disconnect()
	
