import Port
import socket
class Ports:
    TOTALPORTS = 65535
    RESERVEDPORTS = 1024
    def __init__(self, host):
        self.host = host
        self.ports = {}


    def port_scan(self):
        for port_number in range(self.RESERVEDPORTS):
            new_port = Port(self.host, port_number)
            if new_port.scan():
                self.ports[port_number] = new_port

    def print_ports(self):
        for port_number, port in self.ports.items():
            print("Port %i:" + port.status)

    def get_proto(self, port_number, proto="TCP"):
        return socket.getservbyport(port_number, proto)


    def get_protos(self, start_port=0, end_port=TOTALPORTS, proto="TCP"):
        for i in range(start_port, end_port):
            try:
                res = socket.getservbyport(i, proto)
                print(proto+ " Port " + str(i) + " : " + res)
