import os
import socket
import sys

if len(sys.argv) == 2:
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        print("{-} " + file_name + "does not exist")
        exit(0)
    if not os.access(file_name, os.R_OK):
        print("{-} " + file_name + "access denied")
        exit(0)
    print("{+} Reading Vulnerabilities From: " + file_name)


def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def check_vulnerabilities(banner, file_name):
    f = open(file_name, 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print("{+} Server is vulnerable: " + banner.strip('\n'))


def main():
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        if not os.path.isfile(file_name):
            print("{-} " + file_name + "does not exist")
            exit(0)
        if not os.access(file_name, os.R_OK):
            print("{-} " + file_name + "access denied")
            exit(0)
    else:
        print('{-} Usage: ' + str(sys.argv[0]) + "<vuln file_name>")
        exit(0)
        file_name = sys.argv[1]
        port_list = [21, 22, 25, 80, 110, 443]
        for x in range(147, 150):
            ip = '192.168.95.' + str(x)
            for port in port_list:
                banner = ret_banner(ip, port)
                if banner:
                    print("{+} " + ip + ": " + banner)
                    check_vulnerabilities(banner, file_name)


if __name__ == '__main__':
    main()
