import socket
from game import *
from time import sleep


def create_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 55555))
    print("Connected to the server.")
    sleep(1)
    play()
    while True:
        message = input("You: ")

        x = get_x(message)
        while x in dic:
            print('Position occupied')
            message = input("You: ")
            x = get_x(message)
        if not message.isdigit():
            print('\nYou lose!\n')
            client_socket.send('YOU WIN'.encode())
            break
        if x == -1:
            break
        else:
            dic[x] = 'X'
            draw_game(dic)

            client_socket.send(message.encode())
            res = check_win(dic)
            if res:
                print(res)
                break

        if message.lower() == 'exit':
            break
        message = client_socket.recv(1024).decode()
        print(f"Server: {message}")

        o = get_o(message)
        if o == -1:
            break
        else:
            dic[o] = '0'
            draw_game(dic)
            res = check_win(dic)
            if res:
                print(res)
                break
    print("Conversation ended.")
    client_socket.close()


if __name__ == '__main__':
    create_client()
