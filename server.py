import socket
import time

HEADERSIZE = 10

msg = "Welcome to the header"
print(f'{len(msg):<10}' + msg)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.180", 6969))

s.listen(5)


while True:
    clientSocket, adress = s.accept()
    print(f"Connected {adress}")

    while True:
        msg = input("> ")
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientSocket.send(bytes(msg, "utf-8"))
