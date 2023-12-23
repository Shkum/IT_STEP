# Завдання 2
# Реалізуйте клієнт-серверний додаток з можливістю надсилати файли.
# Один користувач ініціює надсилання файлу, другий
# підтверджує. Після підтвердження починається надсилання.
# Якщо відправка була вдалою, повідомте про це відправника.

# exit - exist script

# ready? - send file from client to server


from threading import Thread
from server import create_server
from client import create_client
from time import sleep

server = Thread(target=create_server)

client = Thread(target=create_client)

server.start()
sleep(1)
client.start()

