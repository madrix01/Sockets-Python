import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 6969))

s.listen(5)


while True:
    clientSocket, adress = s.accept()
    print(f"Connected {adress}")
    clientSocket.send(bytes("Welcome to the server", "utf-8"))
