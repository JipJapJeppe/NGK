import sys
from socket import socket, AF_INET, SOCK_STREAM
from lib import Lib

PORT = 9000
serverName = "10.0.0.1"
BUFSIZE = 1000

def main(argv):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    print ("The client is trying to connect")
    clientSocket.connect((serverName, PORT))
    print("The client is connected")
    messagetoserver = input("Input command: ")
    #clientSocket.sendto(messagetoserver.encode(),(socket))
    receiveFile(messagetoserver, clientSocket)
    #Lib.writeTextTCP(, serverName)
    
    #text = Lib.readTextTCP(serverName)
    
    #messagefromserver = bytesAddresPair[0]
    #print(messagefromserver.decode())
    clientSocket.close()
    
    


    #img.saved.save()
def receiveFile(fileName,  conn):
	# TO DO Your Code
    print("Inside receiveFile")
    Lib.writeTextTCP(fileName, conn)
   
    print("After conn.sendto")
    #sendto(data: bytes, address: _Addresss)
    #bytesAddresPair = conn.recvfrom(2048)
    #number of bytes to be read from the TCP socket
    sizeOfFile = int(Lib.readTextTCP(conn))
    print(sizeOfFile)
    print("after sizeOfFile")
    if sizeOfFile == 0 :
        print("Der findes ikke nogen fil")
        return
    fileNameExtracted = Lib.extractFilename(fileName)
    fd = open(fileNameExtracted, 'wb')
   
    while sizeOfFile >= BUFSIZE:
        print("Inside receiveFile Inside while loop")
        var = Lib.readImageTCP(conn)
        fd.write(var)
        
        sizeOfFile-=BUFSIZE
        print("After fileLEngth -=")
    print("fd.close") 
    var = Lib.readImageTCP(conn)
    fd.write(var)
    fd.close()
      

if __name__ == "__main__":
   main(sys.argv[1:])
