from ipaddress import *

ip = '192.168.32.45'
mask = '255.255.255.240'
network = ip_network(f'{ip}/{mask}', 0)
k = 0

for net in network:
    if f"{net:b}".count('1') % 2 != 0:
        k += 1
''' if bin(int(net))[2:].count('1') % 2 != 0:
        k += 1'''

print(k)