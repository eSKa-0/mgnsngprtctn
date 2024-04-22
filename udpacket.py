import socket

class Udp:
    def __init__(self, targetIp, port, message):
        self.target = targetIp
        self.port = port
        self.message = message
    def sendPacketUdp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self.message, (self.target, self.port))
        print(f"Udp packet with message: {self.message} send to {self.target}:{self.port}")

transmit1 = Udp("10.10.10.90", 5005, b"hello world")
transmit1.sendPacketUdp()