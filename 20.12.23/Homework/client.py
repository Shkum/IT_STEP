import socket
from threading import Thread
from fileops import open_file
from time import sleep

def create_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 55555))
    print("Connected to the server.")
    sleep(1)
    while True:

        message = input("You: ")
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break





        response = client_socket.recv(1024).decode()
        print(f"Server: {response}\n")


        if response == 'ready!':
            file = open_file()
            with open(file, 'rb') as f:
                l = f.read(1024)
                while l:
                    client_socket.send(l)
                    l = f.read(1024)
                print('\nSending completed\n')

            client_socket.send('end'.encode())

            response = client_socket.recv(1024).decode()
            print(f"Server: {response}\n")
    sleep(1)
    print("Conversation ended.")
    client_socket.close()
    exit()


if __name__ == '__main__':
    t = Thread(target=create_client)
    t.start()
    t.join()

