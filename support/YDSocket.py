#!/usr/bin/python3
from socket import socket, AF_INET, SOCK_STREAM
from texttable import Texttable


class YDSocket:
    table = Texttable()
    table.set_cols_width([50, 10, 30])
    table.set_deco(table.BORDER | Texttable.HEADER | Texttable.VLINES)
    open_sockets = []
    bad_sockets = 0
    port = 443

    def __init__(self, host):
        self.host = host
        self.sock = socket(AF_INET, SOCK_STREAM)

    def __enter__(self):
        self.sock.connect((self.host, YDSocket.port))
        YDSocket.open_sockets.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for s in YDSocket.open_sockets:
            s.sock.close()

    @staticmethod
    def print_all_connections():
        YDSocket.table.header(['Hostnames', 'result', 'Good {0} / Bad {1} '.format(len(YDSocket.open_sockets),
                                                                                      YDSocket.bad_sockets)])
        print("\n" + YDSocket.table.draw() + "\n")
