import socket


class Udp:
    def __init__(self, targetIp, port, message):
        self.target = targetIp
        self.port = port
        self.message = message.encode()
    def sendPacketUdp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self.message, (self.target, self.port))
bool = True
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
while bool == True:
    ip = str(input("to what ip would you like to send a packet to?\n"))
    if ip == "":
        bool = False
    else:
        pt = int(input("what port should it be send to?\n"))
        ms = input("what should the message be?\n")
        transmit1 = Udp(ip, pt, ms)
        transmit1.sendPacketUdp()
        print(f"Udp packet with message: {ms} send to {ip}:{pt}")
print("Quitting program...")
