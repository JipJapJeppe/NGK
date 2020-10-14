#!/usr/bin/python3
import sys
import socket
from lib import Lib
from socket import socket, AF_INET, SOCK_STREAM

HOST = ""
PORT = 9919
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code

    serverSocket = socket(AF_INET, SOCK_STREAM)
    #socket has 2 parameters domain and type
    # two ways stream is picked
    serverSocket.bind((HOST,PORT))
    serverSocket.listen(1)
    #defines amount of queue members
    while 1:
        print("The server is ready to accept a connection")
        connectionSocket, addr = serverSocket.accept()
        # accept()-> Tuple[socket, _RetAddress]
        # connectionSocket it is the destination to the client who got accepted

        print("Socket is accepted", addr)
        
        #decode text into filedestination
        filedestination = Lib.readTextTCP(connectionSocket)

        print("filedestination requested is ",filedestination)
        
        #extract the file name to textFileName
        textFileName = Lib.extractFilename(filedestination)

        #Return size of file into fileSize
        fileSize = Lib.check_File_Exists(textFileName)
        
        
        #sep=' ' 
        #Call sendFile
        sendFile(textFileName,fileSize, connectionSocket)    
        connectionSocket.close()  
        

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
    Lib.writeTextTCP(str(fileSize), conn)
    fo = open(fileName, "rb")

    print("sendFile out of while")
    while  fileSize >= BUFSIZE :
        print("sendFile inside of while")
        var = fo.read(BUFSIZE)
        conn.send(var)
        
        fileSize -= BUFSIZE
    var = fo.read(BUFSIZE)
    conn.send(var)
    fo.close()

if __name__ == "__main__":
   main(sys.argv[1:])