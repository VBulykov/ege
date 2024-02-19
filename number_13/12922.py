from ipaddress import *

ip = ip_address('136.36.240.16')
mask = '255.255.255.248'

k = 0
ip_net = ip_network(f'{ip}/{mask}', 0)

for net in ip_net:
    ip_bin = bin(int(net))[2:]
    if '101' not in ip_bin:
        k += 1

print(k)