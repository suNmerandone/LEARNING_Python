# Import library
import socket
import sys
import time

# Field variables
clientHost = socket.gethostname()
clientPort = 9999

# Client Socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Client Connection
clientSocket.connect((clientHost, clientPort))

sentence = input("Input lowercase sentence: ")
clientSocket.send(sentence.encode())

msg = clientSocket.recv(1024)
print(" Recieved from EzServer: \n" + msg.decode())

clientSocket.close()
