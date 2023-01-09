import socket


def ret_banner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return


def check_vulns(banner):
    if 'FreeFloat Ftp Server (Version 1.00)' in banner:
        print('{+} FreeFloat FTP Server is vulnerable.')
    elif '3Com 3CDaemon FTP Server Version 2.0' in banner:
        print('3Com 3CDaemon FTP Server is vulnerable.')
    elif 'Ability Server 2.34' in banner:
        print('{+} Ability FTP Server is vulnerable.')
    elif 'Sami FTP Server 2.0.2' in banner:
        print('{+} Sami FTP Server is vulnerable.')
    else:
        print('{-} FTP Server is not vulnerable.')
    return


def main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    ip3 = '192.168.95.150'
    port = 21
    banner1 = ret_banner(ip1, port)
    if banner1:
        print('{+} ' + ip1 + ': ' + banner1.strip('\n'))
        check_vulns(banner1)
    banner2 = ret_banner(ip2, port)
    if banner2:
        print('[+] ' + ip2 + ': ' + banner2.strip('\n'))
        check_vulns(banner2)
    banner3 = ret_banner(ip3, port)
    if banner3:
        print('[+] ' + ip3 + ': ' + banner3.strip('\n'))
    check_vulns(banner3)
    if __name__ == '__main__':
        main()
