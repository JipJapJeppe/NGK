import socket
import threading

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 5050
BUFSIZE = 1000
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((ADDR))

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(BUFSIZE).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                
            print(f"[{addr}] says -> {msg}")
            conn.send("Msg receiced".encode(FORMAT))

    conn.close()

def start():
    serverSocket.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() -1}")

print("[Starting] server is starting")
start()
