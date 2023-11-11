from telethon.sync import TelegramClient
import csv

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

data = ["Null", "Null", "Null"] # phone, api_id, api_hash

def Start():
    with open('info.txt', 'r') as f:
        for i in range(3):
            data[i] = f.readline().split('\n')[0]

    client = TelegramClient(data[0], data[1], data[2])

    client.start()

    result = client(GetDialogsRequest(offset_date=None, offset_id=0, offset_peer=InputPeerEmpty(), limit=200, hash = 0))
    chats = []

    chats.extend(result.chats)
    return chats

def status(username):
	data = ["Null", "Null", "Null"]
	with open('info.txt', 'r') as f:
		for i in range(3):
			data[i] = f.readline().split('\n')[0]
	client = TelegramClient(data[0], data[1], data[2])
	client.start()
	entity = client.get_entity(username)
	try:
		entity = client.get_entity(username)
		print(str(entity.status)[:str(entity.status).find('(')])
	except Exception as e:
		print(f'Не удалось получить информацию о пользователе: {e}')
	client.disconnect()
