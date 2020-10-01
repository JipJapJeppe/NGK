import sys
import os
from socket import socket, AF_INET, SOCK_STREAM
from lib import Lib

PORT = 9000
BUFSIZE = 1000
serverName = "10.0.0.1"

def main(argv):
	# TO DO Your Code
	s = socket(AF_INET,SOCK_STREAM)
	print("The client is connecting...")
	clientSocket.connect((serverName, PORT))
	print ("Client Connected")
    filename = input("Filename? -> ")
	
    if (filename != "q"):
        s.send(filename.encode())
        data = s.recv(1024)
        if (data[:6] == "EXISTS"):
            filesize = long(data[6:])
            message = input("File Exists, " + str(fielsize) + "Bytes, download? (Y/N)? -> ");
            if (message == "Y"):
                s.send("OK")
                f = open('new_'+filename,'wb')
                data = s.recv(1024)
                totalRecv = len(data)
                f.write(data)
                while(totalRecv < filesize):
                    data = s.recv(1024)
                    totalRecv += len(data)
                    f.write(data)
                    print("{0:.2f}".format((totalRecv/float(filesize))*100 + "%Done"));
                	print("Download Complete!")

        else:
            print("File does not exist!");	


clientSocket.close()

if __name__ == "__main__":
   main(sys.argv[1:])
