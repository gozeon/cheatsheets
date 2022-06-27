## python 实现文件传输

``` python title="client.py"
import socket
import sys
import time


# python client.py xxx.file
file_name = sys.argv[1]
addr = ("127.0.0.1", 6000)
# bytes
buf = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('send file name', file_name)
s.sendto(file_name.encode(), addr)
f = open(file_name, "rb")
data = f.read(buf)
print('send file content', file_name)
while(data):
    if s.sendto(data, addr):
        data = f.read(buf)
        time.sleep(0.02) # server save time

s.close()
f.close()

```

``` python title="server.py"
import socket
import time

start = time.process_time()

addr = ("127.0.0.1", 6000)
# bytes
buf = 1024 * 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr)

file_name, addr = s.recvfrom(buf)
print('receive file name', file_name)
if file_name:
    file_name = file_name.strip()

f = open(b"out/"+ file_name, "wb")

data, addr = s.recvfrom(buf)
print('receive file content', file_name)

try:
    while(data):
        f.write(data)
        s.settimeout(1)
        data, addr = s.recvfrom(buf)
except socket.timeout:
    f.close()
    s.close()
    print("File Downloaded")
    

    
print(time.process_time() - start)
```

## go demo

``` go title="clent.go"
package main

import (
	"fmt"
	"net"
)

func main() {
	sip := net.ParseIP("127.0.0.1")
	srcAddr := &net.UDPAddr{IP: net.IPv4zero, Port: 0}
	dstAddr := &net.UDPAddr{IP: sip, Port: 6001}
	conn, err := net.DialUDP("udp", srcAddr, dstAddr)
	if err != nil {
		fmt.Println(err)
	}
	defer conn.Close()
	conn.Write([]byte("hello"))
	fmt.Printf("<%s>\n", conn.RemoteAddr())
}

```

``` go title="server.go"
package main

import (
	"fmt"
	"log"
	"net"
)

func main() {
	listener, err := net.ListenUDP("udp", &net.UDPAddr{IP: net.ParseIP("127.0.0.1"), Port: 6001})
	if err != nil {
		log.Fatal(err)
		return
	}

	fmt.Printf("local: <%s> \n", listener.LocalAddr().String())

	data := make([]byte, 1024)

	for {
		n, remoteAddr, err := listener.ReadFromUDP(data)
		if err != nil {
			fmt.Printf("error during read: %s", err)
		}

		fmt.Printf("<%s> %s\n", remoteAddr, data[:n])

		_, err = listener.WriteToUDP([]byte("world"), remoteAddr)

		if err != nil {
			fmt.Printf(err.Error())
		}
	}
}

```