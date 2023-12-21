import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 55555))
server_socket.listen()
print("Waiting for connection...")
while True:
    client_socket, address = server_socket.accept()
    print(f"Connection with '{address}' established!")
    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'exit':
            break
        print("Client: ", message)
        response = input("Server: ")
        client_socket.send(response.encode())
    print("Connection closed")
    client_socket.close()