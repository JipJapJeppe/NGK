import sys
import os
from socket import socket, AF_INET, SOCK_DGRAM

HOST = ""
PORT = 12000

def main(argv):
    UDPServerSocket = socket(AF_INET, SOCK_DGRAM)
    UDPServerSocket.bind((HOST, PORT))

    print("server is running")

    while 1:
        bytesAddressPair = UDPServerSocket.recvfrom(2048)
        message = bytesAddressPair[0]
        clientAddress = bytesAddressPair[1]
        print("Message recieved from client", clientAddress,": ", message.decode())
        message = message.Upper()
        UDPServerSocket.sendto(message, clientAddress)

if __name__ == "__main__":
    main(sys.argv[1:])