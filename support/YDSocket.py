from socket import (
    socket, getaddrinfo, AF_INET, SOCK_STREAM, IPPROTO_TCP, timeout, gaierror
)
from texttable import Texttable
from OpenSSL.SSL import WantReadError, Error


class YDSocket:
    table = Texttable()
    table.set_cols_width([50, 10, 30])
    table.set_deco(table.BORDER | Texttable.HEADER | Texttable.VLINES)
    open_sockets = 0
    bad_sockets = 0
    port = 443

    def __init__(self, host):
        self.host = host
        self.sock = socket(AF_INET, SOCK_STREAM)

    def __enter__(self):
        """
            The getaddrinfo() call can throw a GAI Error, if hostname cannot resolve to an IP address
            The connect() can throw
        :return: self
        """
        self.sock.setblocking(True)
        getaddrinfo(self.host, YDSocket.port, proto=IPPROTO_TCP)
        self.sock.connect((self.host, YDSocket.port))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        return True

    @staticmethod
    def handle_socket_errors(host, error):
        YDSocket.bad_sockets += 1
        if issubclass(error, timeout):
            YDSocket.table.add_row([host, 'fail', 'timeout'])
        elif issubclass(error, gaierror):
            YDSocket.table.add_row([host, 'fail', 'get_address_info() error'])
        elif issubclass(error, WantReadError):
            YDSocket.table.add_row([host, 'fail', 'WantReadError. Generated by Socket that hadn\'t issued a connect()'])
        elif issubclass(error, Error):
            YDSocket.table.add_row([host, 'fail', 'OpenSSL error, from Connection.do_handshake()'])
        else:
            YDSocket.table.add_row([host, 'fail', 'Socket error. unhandled'])

    @staticmethod
    def print_all_connections():
        YDSocket.table.header(['Hostnames', 'Socket', 'Good {0} / Bad {1} '.format(YDSocket.open_sockets,
                                                                                   YDSocket.bad_sockets)])
        print("\n" + YDSocket.table.draw() + "\n")
