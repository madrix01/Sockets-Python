import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.110", 6969))

print(socket.gethostname())
while True:

    full_msg = ""
    new_msg = True

    while True:
        msg = s.recv(16) #message recieved

        if new_msg:
            #print(f"New message {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
        full_msg += msg.decode("utf-8")

        if len(full_msg) - HEADERSIZE == msglen:
            print(f"Message from server > {full_msg[HEADERSIZE:]}")
            new_msg = True
            full_msg = ""
    print(full_msg)

 