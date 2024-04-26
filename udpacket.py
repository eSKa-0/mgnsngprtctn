import socket

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
class Udp:
    def __init__(self, targetIp, port, message):
        self.target = targetIp
        self.port = port
        self.message = message.encode()
    def sendPacketUdp(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(self.message, (self.target, self.port))
bool = True

while bool == True:
    ip = str(input("\u001b[35m[?]\u001b[0m\thost? "))
    if ip == "":
        bool = False
    else:
        pt = int(input("\u001b[35m[?]\u001b[0m\tport? "))
        ms = input("\u001b[35m[?]\u001b[0m\tpayload? ")
        transmit1 = Udp(ip, pt, ms)
        transmit1.sendPacketUdp()
        print(f"Udp packet with message: {ms} send to {ip}:{pt}")
print("Quitting program...")
