import socket
import time

HOST = '127.0.0.1'    # The remote host
PORT = 65432              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
check = 'start'
while check != 'stop':
    sendData = input("Sensor value: " '\n')
    s.sendall(str(sendData))
    check = s.recv(1024).decode()
    print check, '\n'

s.close()
