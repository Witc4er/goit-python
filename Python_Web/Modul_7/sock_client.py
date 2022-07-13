import socket

PORT = 5050
HEADER = 64
DISCONNECT_MESSAGE = 'DISCONNECT'
SERVER = '192.168.88.218'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048))


if __name__ == '__main__':
    while True:
        send_msg(msg=input('>>> '))