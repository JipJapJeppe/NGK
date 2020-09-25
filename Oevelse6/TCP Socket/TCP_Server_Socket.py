import sys
import os
import socket
from lib import Lib
from os import scandir, walk

HOST = ""
PORT = 9000
BUFSIZE = 1000

def main(argv):
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(1)

    while 1:
        print("The server is ready to accept...")
        connectionSocket, addr = serverSocket.accept()
        print("Socket accept", addr)
        
        filename = ReadTextTCP(connectionSocket) #Modtager sti og filnavn fra client

        print("Message received from client:", filename)
        
        if check_File_Exists(filename) != 0      #Tjekker om filen ekstisterer
            file = open(filename,r)
            fileSize = getFileSizeTCP(connectionSocket)
            sendFile(fileName, fileSize, connectionSocket)
        else 
            writeTextTCP("File not found" connectionSocket)     #Sender error message til client
     
#  Hvis filen findes skal filens størrelse overføres til client som en tekststreng, hvorefter selve filen overføres fra server til client i segmenter på max.
# 1000 bytes ad gangen – indtil filen er overført fuldstændigt.
     

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
        
    writeTextTCP(fileSize)

    if fileSize > BUFSIZE
        buf = fileName
        sizebuf = fileSize
        i = 1000
        j = i-1000

        for sizebuf > 0
            if (sizebuf > 1000)
                writeTextTCP(fileName[j:i],conn)
                sizebuf -= i
                i += 1000

            else if sizebuf < 1000
                writeTextTCP(filename[sizebuf],conn)
    
if __name__ == "__main__":
   main(sys.argv[1:])
