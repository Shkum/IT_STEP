import socket
from translate import get_translated

def create_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 55555))
    print("Connected to the server.")
    while True:
        message = input("\nClient: ")
        if message.lower() != 'exit':
            message = get_translated(message, 'en', 'uk')
            client_socket.send(message.encode())
        if message.lower() == 'exit':
            client_socket.send(message.encode())
            break
        response = client_socket.recv(1024).decode()
        print(f"{response}")
    print("Conversation ended.\n")
    client_socket.close()
