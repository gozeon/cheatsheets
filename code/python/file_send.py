import socket

BUFFER_SIZE = 1024 * 1024
sk = socket.socket()

sk.connect(('192.168.19.40', 9999))

with open("C:\\Users\\62497\\Downloads\\VSCodeUserSetup-x64-1.91.1.exe", "rb") as f:
    while True:
       d = f.read(BUFFER_SIZE)
       if not d:
           break
       sk.sendall(d)
sk.send('quit'.encode())


