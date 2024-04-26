import socket
import time

host = "127.0.0.1"
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print(f"\u001b[32m[!]\u001b[0m\tListening on port {port}")

while 1:
    data, client = s.recvfrom(1024)
    src_host = client[0]
    src_port = client[1]
    if not data:
        print(f"\u001b[36m[!]\u001b[0m\tPacket received from {src_host}:{src_port}")
    else:
        data = data.decode("UTF-8")
        print(f"\u001b[36m[!]\u001b[0m\t{data} received from {src_host}:{src_port}")
