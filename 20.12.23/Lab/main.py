# Завдання 2
# Реалізуйте клієнт-серверний додаток погоди. Клієнт
# звертається до сервера із зазначенням країни та міста.
# Сервер, отримавши запит, видає погоду на тиждень для
# вказаної місцевості. Використовуйте для реалізації додатку багатопотокові механізми.
# Дані про погоду мають бути наперед визначеними та взяті з файлу


from threading import Thread

from server import create_server
from client import create_client

server = Thread(target=create_server)
client = Thread(target=create_client)
server.start()
client.start()
