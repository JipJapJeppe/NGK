import sys
import os
from socket import socket, AF_INET, SOCK_STREAM
from lib import Lib

PORT = 9002
BUFSIZE = 1000
serverName = "10.0.0.1"

def main(argv):
    #Connect to socket
    s = socket(AF_INET,SOCK_STREAM)
    print("The client is connecting...")
    s.connect((serverName, PORT))
    print ("Client Connected")
    
    filename = input("Filename? -->")   #Enter filename
    print(filename)
    filesize = Lib.getFileSizeTCP(filename) #Get filesize
    print(filesize)
    
    if filename == 'q': 
        s.close()
    else:
        getFile(filename, filesize, s)
        
        
def getFile(fileName, fileSize, conn):
    print("getFile() called")
    with open(fileName, 'wb') as file1:
        print("receiving file: '",fileName, "' of size: ", fileSize, " Bytes")
        for i in range(fileSize):
            data = conn.recv(fileSize)
            if not data:
                print("done")
                break
            file1.write(data)
            
 
def getFiletoof(fileName, fileSize, s):
    s.send(filename.encode())
    data = s.recv(BUFSIZE)
    if (data[:6] == "EXISTS"):
        filesize = long(data[6:])
        message = input("File Exists, " + str(filesize) + "Bytes, download? (Y/N)? -> ")
        if (message == "Y"):
            s.send("OK")
            f = open('new_'+filename,'wb')
            data = s.recv(BUFSIZE)
            totalRecv = len(data)
            f.write(data)
            while(totalRecv < filesize):
                data = s.recv(BUFSIZE)
                totalRecv += len(data)
                f.write(data)
                print("{0:.2f}".format((totalRecv/float(filesize))*100 + "%Done"))
            print("Download Complete!")
        else:
            print("File does not exist!")
    s.close() 

          
if __name__ == "__main__":
   main(sys.argv[1:])