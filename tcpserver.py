import socket
import time

host = str(input("\u001b[35m[?]\u001b[0m\thost? "))
port = int(input("\u001b[35m[?]\u001b[0m\tport? "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
print(f"\u001b[32m[!]\u001b[0m\tBinded to {host}:{port}")
s.listen()
print(f"\u001b[32m[!]\u001b[0m\tListening to {host}:{port}")
c, src_host = s.accept()
print(f"\u001b[32m[!]\u001b[0m\tConnected to {src_host}")

while True:
    data = c.recv(1024)
    if not data:
        print(f"\u001b[31m[!]\u001b[0m\tNo data received!!!")
        break
    print(f"\u001b[32m[!]\u001b[0m\tData received: {data}")
    c.send(data)
c.close()
time.sleep(6)