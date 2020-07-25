import socket
import time

HEADERSIZE = 10

msg = "Welcome to the header"
print(f'{len(msg):<10}' + msg)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6969))

s.listen(5)


while True:
    clientSocket, adress = s.accept()
    print(f"Connected {adress}")

    while True:
        time.sleep(3)
        msg = f"The time is {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        clientSocket.send(bytes(msg, "utf-8"))
