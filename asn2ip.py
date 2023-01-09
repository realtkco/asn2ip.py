import socket
import struct

def cidr_to_ip_range(cidr):
    network, net_bits = cidr.split('/')
    host_bits = 32 - int(net_bits)
    net = struct.unpack('!I', socket.inet_aton(network))[0]
    start = (net >> host_bits << host_bits) + 1
    end = net | (1 << host_bits) - 1
    return [socket.inet_ntoa(struct.pack('!I', i)) for i in range(start, end)]

with open('asns.txt', 'r') as asntxt:
    for cidr in asntxt:
        with open('ipaddresses.txt', 'a') as f:
            for item in cidr_to_ip_range(cidr):
                f.write(item + '\n')
                # degrade performance by 57.4% :lul: real  with: 0m0.990s  without: 0m0.416s
                # print(item)
