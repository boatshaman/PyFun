import socket

LOGTAG = "Net.Host"
class Host:
    def __init__(self):
        self.hostname = None
        self.ip = None
        self.ports = None

    def get_ip(self):
        try:
            if self.hostname:
                self.ip = socket.gethostbyname(self.hostname)
            else:
                raise Exception("No Hostname set for Host")
         except Exception as e:
            print(LOGTAG + ": error getting IP")
            print(LOGTAG + " error: " + str(e))

    def get_hostname(self):
        if self.hostname:
            return self.hostname
        try:
            if self.ip:
                self.hostname = socket.gethostbyaddr(self.ip)
                return self.hostname
            else:
                raise Exception("No IP set for Host")
        except Exception as e:
            print(LOGTAG + ": error getting hostname")
            print(LOGTAG + " error: " + str(e))

    def get_ports(self):
        if not self.ip:
            self.get_ip()
