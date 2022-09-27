import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://ibarake:mDBe5MmpaRxhE2M6@tcp-chat.siia2mv.mongodb.net/?retryWrites=true&w=majority")
db = cluster["tcpchat"]
collection = db["port"]

query = collection.find({"_id": 0})
for x in query:
    port = x['Aport']
    print("Attempting to connect port: ", x['Aport'])

import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('4.tcp.ngrok.io', port))

def receive():
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == 'NICK':
                client.send(nickname.encode("ascii"))
            else:
                print(message)
        except:
            print('error!')
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode("ascii"))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()