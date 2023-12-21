import socket
from translate import get_translated

def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 55555))
    server_socket.listen()
    print("Waiting for connection...")
    while True:
        client_socket, address = server_socket.accept()
        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == 'exit':
                break
            print(message)
            response = input("\nServer: ")
            response = get_translated(response, 'en', 'uk')
            client_socket.send(response.encode())
        print("Connection closed")
        client_socket.close()
        break
