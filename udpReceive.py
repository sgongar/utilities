# coding=utf-8

import socket


def main():
    ip = ''
    port = 57009
    UDPsocket = socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)
    UDPsocket.bind((ip, port))

    while True:
        data, addr = UDPsocket.recvfrom(1024)

        print data
        print "\n"


if __name__ == '__main__':
    main()
