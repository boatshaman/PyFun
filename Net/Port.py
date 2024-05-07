import socket
import Host

class Port:

    def __init__(self, host, port_number):
        self.host = host
        self.port_number = port_number

    def scan(self, proto="TCP"):
        # returns non-zero if successful
        if proto=="TCP":
            return self.tcp_scan()

    def tcp_scan(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
            socket_tcp.settimeout(5)
            if (socket_tcp.connect_ex((self.host.ip, self.port_number))==0):
                return 1


    def print_status(self):



