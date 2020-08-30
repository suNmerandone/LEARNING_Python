# Import library
import socket
import sys
import time

# Define a close method
def EzServerClose():
    print("===== The EzServer is shut down =====")
    connectSocket.shutdown(socket.SHUT_RDWR)
    connectSocket.close()
    sys.exit()

# Field variables
serverHost = socket.gethostname()
serverPort = 9999

# Server Socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverHost, serverPort))
serverSocket.listen(1)
print("===== The EzServer is ready for receiving =====")

# Server Listener
while True:
    connectSocket, addr = serverSocket.accept()     # Create a socket and accept the request from client
    print(" Accepted a connection from " + str(addr) + " at " + time.ctime())
    
    recvByte = connectSocket.recv(1024)             # Set the max data byte lengh
    sentence = recvByte.decode()                    # To decode byte to string

    if sentence == "SHUTDOWN":                      # Handle the shut down request from client
        EzServerClose()

    capitalizedSentence = sentence.upper()          # Do someting: Turn the lowercase to uppercase

    msg = " Welcome to EzServer: " + capitalizedSentence
    print(" Responed a largecase sentence to client: " + msg)
    connectSocket.send(msg.encode())                # Send the responds to client
    connectSocket.close()                           # Close this connected socket
