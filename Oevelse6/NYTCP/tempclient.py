import sys
import os
from socket import socket, AF_INET, SOCK_STREAM
from lib import Lib

<<<<<<< HEAD
PORT = 9006
=======
PORT = 9004
>>>>>>> 1c3dcd13cc5d1ad558b9565a6287a0e968eaf7a7
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
    Lib.writeTextTCP(filename,s)
    
    #filesize = Lib.getFileSizeTCP(filename) #Get filesize
    #print(filesize)
    
    if filename == 'q': 
        s.close()
    else:
        #getFile(filename, filesize, s)
        getFile(filename,s)
    s.close()
    
    
def getFile1(fileName, fileSize, conn):
    print("getFile() called")
    with open(fileName, 'wb') as file1:
        print("receiving file: '",fileName, "' of size: ", fileSize, " Bytes")
        for i in range(fileSize):
            data = conn.recv(1024)
            if not data:
                print("done")
                break
            file1.write(data)
    conn.close()        
    
def getFile(fileName, conn):
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
   
#    while sizeOfFile >= BUFSIZE:
#        print("Inside receiveFile Inside while loop")
#        var = Lib.readImageTCP(conn)
#        fd.write(var)
#        
#        sizeOfFile -= BUFSIZE
#        print("After fileLEngth -=")
#    print("fd.close") 
#    var = Lib.readImageTCP(conn)
    i = 1
    #databuf = b""
    while sizeOfFile > 0:
        
        print("receiving datapacket: ", i)
        if sizeOfFile >= 1000:
            data = conn.recv(BUFSIZE)
            #databuf += data
            sizeOfFile -= BUFSIZE
            i += 1
            print("data received: ", data)
        
        elif sizeOfFile < BUFSIZE:
            data = conn.recv(sizeOfFile)
            print("data received: ", data)
            sizeOfFile -= sizeOfFile
        fd.write(data)
            
            
    fd.close()
            
 
#def getFiletoof(fileName, fileSize, s):
#    s.send(filename.encode())
#    data = s.recv(BUFSIZE)
#    if (data[:6] == "EXISTS"):
#        filesize = long(data[6:])
#        message = input("File Exists, " + str(filesize) + "Bytes, download? (Y/N)? -> ")
##        if (message == "Y"):
#           s.send("OK")
#            f = open('new_'+filename,'wb')
#            data = s.recv(BUFSIZE)
#            totalRecv = len(data)
#            f.write(data)
#            while(totalRecv < filesize):
#                data = s.recv(BUFSIZE)
#                totalRecv += len(data)
#                f.write(data)
#                print("{0:.2f}".format((totalRecv/float(filesize))*100 + "%Done"))
#            print("Download Complete!")
#        else:
#            print("File does not exist!")
#    s.close() 

          
if __name__ == "__main__":
   main(sys.argv[1:])