# client.py
import socket

client_obj = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

ip = '127.0.0.1'
port = 5555

#  instance requesting for connection to the specified address and port

client_obj.connect((ip,port))

# receiving response from server
data_rece = client_obj.recv(1024)

# if response is not null
if data_rece:
    print("CLIENT CONNECTED TO SERVER")
    print(data_rece.decode('utf-8'))

    while data_rece:
        client_inp = input().encode('utf-8')

        # sending request to the server
        client_obj.send(client_inp)

        # receiving response from the server
        data_rece = client_obj.recv(1024)
        if data_rece:
            print("{}: {}".format("SERVER",data_rece.decode('urf-8')))