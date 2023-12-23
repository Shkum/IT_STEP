import socket
import threading
import json

host = 'localhost'
port = 55555

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print(f"Server is listening on '{host}:{port}'\n")

passwords = ['1', '2', '3', 'admin']


def client_handler(client_socket):
    while True:
        try:
            message = json.loads(client_socket.recv(1024).decode('utf-8'))
            if message['password'] in passwords:
                for client in clients:
                    if client is not client_socket:
                        client.send(json.dumps(message).encode('utf-8'))
            else:
                message['message'] = 'You can not send messages due to wrong password!'
                client_socket.send(json.dumps(message).encode('utf-8'))
        except ConnectionResetError:
            clients.remove(client_socket)
            client_socket.close()
            break


def start_server():
    try:
        while True:
            client_socket, addr = server.accept()
            print(f"Accepted connection from {addr}\n")
            clients.append(client_socket)
            client_thread = threading.Thread(target=client_handler, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server.close()


if __name__ == '__main__':
    start_server()
