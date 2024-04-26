import socket
import time

print(
"""
▄▄▄█████▓ ▄████▄   ██▓███   ▄▄▄       ▄████▄   ██ ▄█▀▓█████▄▄▄█████▓
▓  ██▒ ▓▒▒██▀ ▀█  ▓██░  ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀▓  ██▒ ▓▒
▒ ▓██░ ▒░▒▓█    ▄ ▓██░ ██▓▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███  ▒ ▓██░ ▒░
░ ▓██▓ ░ ▒▓▓▄ ▄██▒▒██▄█▓▒ ▒░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄░ ▓██▓ ░ 
  ▒██▒ ░ ▒ ▓███▀ ░▒██▒ ░  ░ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒ ▒██▒ ░ 
  ▒ ░░   ░ ░▒ ▒  ░▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░ ▒ ░░   
    ░      ░  ▒   ░▒ ░       ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░   ░    
  ░      ░        ░░         ░   ▒   ░        ░ ░░ ░    ░    ░      
         ░ ░                     ░  ░░ ░      ░  ░      ░  ░        
         ░                           ░                              
"""
)

dst_host = str(input("\u001b[35m[?]\u001b[0m\thost? "))
dst_port = int(input("\u001b[35m[?]\u001b[0m\tport? "))
payload = str(input("\u001b[35m[?]\u001b[0m\tpayload? "))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((dst_host, dst_port))
print(f"\u001b[32m[!]\u001b[0m\tConnected to {dst_host}:{dst_port}")
payload = payload.encode("UTF-8")
s.send(payload)
print(f"\u001b[32m[!]\u001b[0m\tPayload send")
data = s.recv(1024)
s.close()
print(f"\u001b[32m[!]\u001b[0m\tReceived: {data}")
time.sleep(10)