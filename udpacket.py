import socket


class Udp:
    def __init__(self, targetIp, port, message):
        self.target = targetIp
        self.port = port
        self.message = message.encode()
    def sendPacketUdp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self.message, (self.target, self.port))

class Tcp:
    def __init__(self, targetIp, port, message):
        self.target = targetIp
        self.port = port
        self.message = message.encode(utf-8)
    def sendPacketTcp(self):
        sock = socket.socket(socket.AF_INET, socket.TCP_STREAM)
        sock.sendto(self.message, (self.target, self.port))

print(
    """
     █    ██ ▓█████▄  ██▓███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████▄▄▄█████▓
     ██  ▓██▒▒██▀ ██▌▓██░  ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀▓  ██▒ ▓▒
    ▓██  ▒██░░██   █▌▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███  ▒ ▓██░ ▒░
    ▓▓█  ░██░░▓█▄   ▌▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄░ ▓██▓ ░ 
    ▒▒█████▓ ░▒████▓ ▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒ ▒██▒ ░ 
    ░▒▓▒ ▒ ▒  ▒▒▓  ▒ ▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░   
    ░░▒░ ░ ░  ░ ▒  ▒ ░▒ ░       ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░   ░    
     ░░░ ░ ░  ░ ░  ░ ░░         ░   ▒   ░        ░ ░░ ░    ░    ░      
       ░        ░                   ░  ░░ ░      ░  ░      ░  ░        
              ░                         ░                              
    """)
md = int(input("Would you like to send a TCP or an UDP packet? (1/2)\n")
if md == 1:
    ip = str(input("to what ip would you like to send a packet to?\n"))
    pt = int(input("what port should it be send to?\n"))
    ms = input("what should the message be?\n")
    transmit = Udp(ip, pt, ms)
    transmit.sendPacketUdp()
    print(f"UDP packet with message: {ms} send to {ip}:{pt}")
if md == 2:
    ip = str(input("to what ip would you like to send a packet to?\n"))
    pt = int(input("what port should it be send to?\n"))
    ms = input("what should the message be?\n")
    transmit = Tcp(ip, pt, ms)
    transmit.sendPacketTcp
    print(f"TCP packet with message: {ms} send to {ip}:{pt}")
print("Quitting program...")
