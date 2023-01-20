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


def main():
    ip1 = 'localhost'
    ip2 = 'localhost'
    port = '2121'

    banner1 = ret_banner(ip1, port)
    if banner1:
        print('{+} ' + ip1 + ': ' + banner1)

    banner2 = ret_banner(ip2, port)
    if banner2:
        print('{+}' + ip2 + ': ' + banner2)


if __name__ == '__main__':
    main()
