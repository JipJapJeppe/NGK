import socket

SERVER = '127.0.1.1'
PORT = 5050
BUFSIZE = 1000
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
PORT = 5050
BUFSIZE = 1000
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ADDR))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (BUFSIZE - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(BUFSIZE).decode(FORMAT))

send("Hello World!")
send("Hello Me!")
send("Hello You!")
send(DISCONNECT_MESSAGE)
