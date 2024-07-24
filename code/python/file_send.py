import socket

sk = socket.socket()

sk.connect(('192.168.19.40', 9999))

with open("C:\\Users\\62497\\Downloads\\VSCodeUserSetup-x64-1.91.1.exe", "rb") as f:
    for i in f:
        sk.send(i)
        data = sk.recv(1024)
        if data != b'success':
            break

sk.send('quit'.encode())


