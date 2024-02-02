import socket
import threading

from redis_handler import MessageHandler

msg = MessageHandler()
redis_session = '01'


def print_all_messages(msgs):
    for i, v in msgs.items():
        print(i, v)


def client_handler(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            msg.save_message(redis_session, message)
            print_all_messages(msg.get_messages(session=redis_session))
            for client in clients:
                if client is not client_socket:
                    client.send(message)
        except ConnectionResetError:
            clients.remove(client_socket)
            client_socket.close()
            break


host = '127.0.0.1'
port = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []

print(f"Server is listening on {host}:{port}")

try:
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()
except KeyboardInterrupt:
    print("Server is shutting down.")
finally:
    server.close()
