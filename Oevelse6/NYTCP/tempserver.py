import sys
import os
from socket import socket, AF_INET, SOCK_STREAM
from lib import Lib #import klassen Lib

HOST = ""
PORT = 9002
BUFSIZE = 1000

def main(argv):
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    serverSocket.listen(1)
    
    while 1:
        print("The server is ready to accept...")
        connectionSocket, addr = serverSocket.accept()
        print("Socket accept", addr)
        
        fileName = Lib.readTextTCP(connectionSocket) #Modtager sti og filnavn fra client

        print("Message received from client:", fileName)
        
        if Lib.check_File_Exists(fileName) != 0: 
            file = open(fileName,'rb') #opens file without truncation
            file2 = file.read(all)
            fileSize = Lib.getFileSizeTCP(connectionSocket)
            sendFile(file2, fileSize, connectionSocket)
        else:
            Lib.writeTextTCP("File not found", connectionSocket)    #Sender error message til client
     
#  Hvis filen findes skal filens størrelse overføres til client som en tekststreng, hvorefter selve filen overføres fra server til client i segmenter på max.
# 1000 bytes ad gangen – indtil filen er overført fuldstændigt.

def sendFile(file,  fileSize,  conn):
	# TO DO Your Code
    with open(file, 'rb') as file1:
        for i in range(fileSize):
            bytes_read = file1.read(BUFSIZE)
            if not bytes_read:
                break
            conn.sendall(bytes_read)

def sendFile1(file,  fileSize,  conn):
	# TO DO Your Code
        
    Lib.writeTextTCP(fileSize, conn)

    if fileSize > BUFSIZE:
        sizebuf = fileSize
        i = 1000
        j = i-1000

        while sizebuf > 0:
            if sizebuf > 1000:
                conn.sendFile(file[j:i],conn)
                sizebuf -= i
                i += 1000

            elif sizebuf < 1000:
                conn.sendFile(file[sizebuf],conn)
    conn.close
        
    
if __name__ == "__main__":
   main(sys.argv[1:])
