import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print("{-} " + filename + "does not exist")
        exit(0)
    if not os.access(filename, os.R_OK):
        print("{-} " + filename + "access denied")
        exit(0)
    print("{+} Reading Vulnerabilities From: " + filename)

import socket
import os
import sys


def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
