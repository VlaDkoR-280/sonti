from telethon.sync import TelegramClient
import csv

from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

data = ["Null", "Null", "Null"] # phone, api_id, api_hash

with open('info.txt', 'r') as f:
    for i in range(3):
        data[i] = f.readline().split('\n')[0]

client = TelegramClient(data[0], data[1], data[2])

client.start()

