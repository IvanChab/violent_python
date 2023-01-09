import socket
socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("localhost", 2121))
ans = s.recv(1024)

ans = ans.decode()
ans = ans.strip()
ans = ans[4:]

if "FreeFloat Ftp Server (Version 1.00)" in ans:
    print("{+} FreeFloat FTP Server is vulnerable.")
elif "3Com 3CDaemon FTP Server Version 2.0" in ans:
    print("{+} 3CDaemon FTP Server is vulnerable.")
elif "Ability Server 2.34" in ans:
    print("{+} Ability FTP Server is vulnerable.")
elif "Sami FTP Server 2.0.2" in ans:
    print("{+} Sami FTP Server is vulnerable.")
else:
    print("{-} FTP Server is not vulnerable.")
