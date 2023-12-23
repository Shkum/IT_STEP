import socket
from threading import Thread
from fileops import save_file



def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 55555))
    server_socket.listen()
    print("Waiting for connection...")
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection with '{address}' established!")
        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == 'exit':
                break
            if message == 'ready?':
                print("Client: ", message)
                file = save_file()
                client_socket.send('ready!'.encode())

                with open(file, 'wb') as f:
                    l = client_socket.recv(1024)
                    while l:
                        if l != b'end':
                            f.write(l)
                            l = client_socket.recv(1024)
                        else:
                            print('\nReceiving completed\n')
                            client_socket.send('Completed!'.encode())
                            break
                continue




            print("Client: ", message)
            response = input("Server: ")
            client_socket.send(response.encode())
        print("Connection closed")
        client_socket.close()
        exit()


if __name__ == '__main__':
    t = Thread(target=create_server)
    t.start()
    t.join()

