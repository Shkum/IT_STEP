# Завдання 1
# Реалізуйте клієнт-серверний додаток з можливістю
# зворотного обміну повідомленнями. Для початку спілкування встановіть з’єднання. Після з’єднання використайте текстовий формат. У бесіді беруть участь лише дві
# особи. Після завершення спілкування сервер переходить
# до очікування нового учасника розмови

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 55555))
print("Connected to the server.")
while True:
    message = input("You: ")
    client_socket.send(message.encode())
    if message.lower() == 'exit':
        break
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")
print("Conversation ended.")
client_socket.close()
