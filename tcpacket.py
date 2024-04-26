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

dst_host = "127.0.0.1"
dst_port = 5432
payload = "W mans"

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