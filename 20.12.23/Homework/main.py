# Завдання 1
# Реалізуйте клієнт-серверний додаток, що дозволяє двом
# користувачам грати в гру «Хрестики — нулики». Один із
# гравців ініціює гру. Якщо другий гравець підтверджує, то
# гра починається. Гру можна припинити. Той хто припинив
# гру — програв. Після завершення гри можна ініціювати повторний матч.

from threading import Thread

from server import create_server
from client import create_client

server = Thread(target=create_server)
server.start()

client = Thread(target=create_client)
client.start()
