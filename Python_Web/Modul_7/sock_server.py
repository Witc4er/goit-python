import socket
import threading

PORT = 5050
HEADER = 64
HOST = socket.gethostbyname(socket.gethostname())
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT'


def handle_client(conn, addr):
    print(f'New connection {addr} connected')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'Received message from {addr} - {msg}')
            conn.send('OK'.encode(FORMAT))
    conn.close()


def listen(addr):
    print(f'SERVER listening on - {HOST}')
    with socket.socket() as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(addr)
        server.listen(1)
        while True:
            conn, addr = server.accept()
            try:
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
            except Exception as e:
                print(e)
                conn.close()


if __name__ == '__main__':
    print('START server')
    listen(ADDR)

