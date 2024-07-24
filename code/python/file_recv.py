import socket

BUFFER_SIZE = 1024 * 1024

sk = socket.socket()

sk.bind(('192.168.19.40', 9999))

sk.listen(5)

conn, address = sk.accept()

while True:
    with open('file', "ab") as f:
        data = conn.recv(BUFFER_SIZE)
        print(len(data))
        if not data:
            break
        f.write(data)
sk.close()

