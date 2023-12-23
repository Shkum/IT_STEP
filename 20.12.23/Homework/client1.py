import socket
import threading
import json


def connect_to_server():
    host = 'localhost'
    port = 55555

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    message_handler(client)


def receive_message(client_socket):
    while True:
        try:
            message = json.loads(client_socket.recv(1024).decode('utf-8'))
            print(f"{message['user']}: {message['message']}\n->")
        except ConnectionResetError:
            print("Connection lost to server.")
            break
        except OSError:
            break


def message_handler(client):
    receive_thread = threading.Thread(target=receive_message, args=(client,))
    receive_thread.start()
    print("Connected to the server. You can start sending messages.")
    user = input("Enter your name: ")
    password = input("Enter your password: ")
    try:
        while True:
            message = input("->")
            message_to_send = json.dumps({
                "user": user,
                "password": password,
                "message": message
            })

            if message[:10] == r'\password=':
                password = message[10:]
                print('\nPassword successfully changed!\n')
                continue

            client.send(message_to_send.encode('utf-8'))
    except KeyboardInterrupt:
        print("You have exited the chat.")
    finally:
        client.close()


if __name__ == '__main__':
    connect_to_server()
