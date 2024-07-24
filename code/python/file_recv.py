import socket

sk = socket.socket()

sk.bind(('127.0.0.1', 9999))

sk.listen(5)

conn, address = sk.accept()

print("文件开始接受")

while True:
    with open('file', "ab") as f:
        data = conn.recv(1024)
        if data == b'quit':
            break
        f.write(data)
        conn.send('success'.encode())
print('文件接受完成')
sk.close()
