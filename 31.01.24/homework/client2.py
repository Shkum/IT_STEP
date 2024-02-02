import socket
import threading
import json


def receive_message(client_socket):
    while True:
        try:
            message = json.loads(client_socket.recv(1024).decode('utf-8'))
            print(f"{message['user']}: {message['message']}")
        except ConnectionResetError:
            print("Connection lost to server.")
            break
        except OSError:
            break


host = '127.0.0.1'
port = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

receive_thread = threading.Thread(target=receive_message, args=(client,))
receive_thread.start()

print("Connected to the server. You can start sending messages.")

user = input("Enter your name: ")

try:
    while True:
        message_to_send = json.dumps({
            "user": user,
            "message": input("Enter your message:\n")
        })

        client.send(message_to_send.encode('utf-8'))
except KeyboardInterrupt:
    print("You have exited the chat.")
finally:
    client.close()