import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
class Connection:
    def __init__(self, src_host, src_port, dst_host, dst_port):
        self.src_host = src_host
        self.src_port = src_port
        self.dst_host = dst_host
        self.dst_port = dst_port
    def bind(self):
        s.bind((self.src_host, self.src_port))
        print(f"\u001b[36m[!]\u001b[0m\tListening on port {self.src_port}")
    def send(self):
        self.message = str(input("\u001b[35m[?]\u001b[0m\tmessage? ")).encode("UTF-8")
        s.sendto(self.message,(self.dst_host, self.dst_port))
    def check(self):
        data, client = s.recvfrom(1024)
        sender_ip = client[0]
        sender_port = client[1]
        print(f"\u001b[36m[!]\u001b[0m\t{data.decode("UTF-8")} received from {sender_ip}:{sender_port}")
src_host= str(input("\u001b[35m[?]\u001b[0m\tsource adress? "))
src_port= int(input("\u001b[35m[?]\u001b[0m\tsource port? "))
dst_host= str(input("\u001b[35m[?]\u001b[0m\ttarget adress? "))
dst_port= int(input("\u001b[35m[?]\u001b[0m\ttarget port? "))
c = Connection(src_host, src_port, dst_host, dst_port)
c.bind()
while True:
	c.send()
	c.check()