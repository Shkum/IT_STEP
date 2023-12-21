import socket


def create_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 55555))
    print("Connected to the server.")
    while True:
        message = input("\nEnter city name: ")
        client_socket.send(message.encode())
        if message.lower() == 'exit':
            break
        response = client_socket.recv(1024).decode()
        print(f"{response}")
    print("Conversation ended.")
    client_socket.close()
