import socket
from game import *


def create_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 55555))
    server_socket.listen()
    print("Waiting for connection...")
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection with '{address}' established!")
        play()
        while True:
            message = client_socket.recv(1024).decode()
            if message.lower() == 'exit':
                break
            print("Client: ", message)

            x = get_x(message)
            if x == -1:
                break
            dic[x] = 'X'
            draw_game(dic)
            res = check_win(dic)
            if res:
                print(res)
                break

            response = input("Server: ")

            o = get_x(response)
            while o in dic:
                print('Position occupied')
                response = input("Server: ")
                o = get_x(response)
            if not response.isdigit():
                print('\nYou lose!\n')
                client_socket.send('YOU WIN'.encode())
                break
            if o == -1:
                break
            dic[o] = '0'
            draw_game(dic)
            client_socket.send(response.encode())
            res = check_win(dic)
            if res:
                print(res)
                break

        print("Connection closed")
        client_socket.close()
        exit()


if __name__ == '__main__':
    create_server()
