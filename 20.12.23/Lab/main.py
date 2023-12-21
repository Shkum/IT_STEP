# Завдання 3
# Створіть клієнтсько-серверний додаток, де клієнт
# надсилає рядок тексту або слово на сервер для
# перекладу на іншу мову. Сервер повертає переклад і
# відправляє його клієнту. Наприклад, клієнт надсилає
# рядок "Hello, how are you?" на сервер, а сервер повертає
# переклад цього рядка на вказану мову. Скористайтеся
# бібліотекою googletrans.


from server import create_server
from client import create_client
from threading import Thread


server = Thread(target=create_server)
client = threaded = Thread(target=create_client)
server.start()
client.start()

