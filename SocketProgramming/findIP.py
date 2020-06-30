import nmap
import socket

class Network(object):
    def __init__(self, ip=''):
        # ip = input("Please enter IP. Default is 192.168.1.1/192.168.0.1 ")
        # ip = '192.168.43.103'
        # ip = '192.168.43.251'
        ip = self.get_ip()
        self.ip = ip
    
    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

    def networkscanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        else:
            network = self.ip + '/24'
        print("Scanning please wait")

        nm = nmap.PortScanner()
        nm.scan(hosts=network, arguments='-sn')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        neighbours = []
        for host, status in hosts_list:
            if host != self.ip:
                # print("Host\t{}".format(host))
                # print(host, len(host))
                neighbours.append(host)
        return self.ip, neighbours

if __name__ == "__main__":
    D = Network()
    D.networkscanner()