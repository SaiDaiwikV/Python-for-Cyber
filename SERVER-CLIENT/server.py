# server.py

import socket
import random
import string

# Creating a socket instance
server_object = socket.socket(family=socket.AF_INET, type = socket.SOCK_STREAM)

# connecting to the local host

ip = '127.0.0.1'
port = 5555

server_object.bind((ip,port))
server_object.listen()

# once the client connects to the particular port, the server starts to accept the request

connection_obj, _ = server_object.accept();

if connection_obj:
    # connected to client successfully
    print("SERVER CONNECTED TO CLIENT")

    # sending inital message to the client
    connection_obj.send(b"Hi there")

    # receiving message from the client
    data_rece = connection_obj.recv(1024)

    while data_rece != b'stop':
        print("{}: {}".format("CLIENT MESSAGE: ", data_rece.decode('utf-8')))
        server_input = random.choice(string.ascii_letters)
        connection_obj.send(server_input.encode('utf-8'))
        data_rece = connection_obj.recv(1024)