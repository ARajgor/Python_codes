import socket

def client_program():

    client_socket = socket.socket()  # instantiate
    client_socket.connect(('localhost', 80))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'stop':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        if data.lower().strip() == 'stop':
            print("Disconnected")
            break
        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
