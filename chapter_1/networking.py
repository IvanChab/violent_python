import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("localhost", 21))
ans = s.recv(1024)

print(ans)
