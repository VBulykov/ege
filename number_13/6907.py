from ipaddress import *

ip = '140.19.96.0'
mask = '255.255.248.0'
network = ip_network(f'{ip}/{mask}')
k = 0

for net in network:
    ip_net = bin(int(net))[2:]
    if (
        ip_net[0:8].count('1') == 
        ip_net[8:16].count('1') == 
        ip_net[16:24].count('1') == 
        ip_net[24:32].count('1')
    ):
        k += 1

print(k)