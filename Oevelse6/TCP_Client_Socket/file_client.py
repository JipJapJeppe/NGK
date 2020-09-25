import sys
import os
from socket import socket, AF_INET, SOCK_STREAM
from lib import Lib

PORT = 9000
BUFSIZE = 1000
serverName = "10.0.0.1"

def main(argv):
	# TO DO Your Code
	clientSocket = socket(AF_INET,SOCK_STREAM)
	print("The client is connecting...")
	clientSocket.connect((serverName, PORT))
	print ("Client Connected")
	# WriteTextTCP()

	#readTextTCP or getFileSizeTCP() 
	
	# 

def receiveFile(fileName,  conn):
	# TO DO Your Code


clientSocket.close()

if __name__ == "__main__":
   main(sys.argv[1:])
