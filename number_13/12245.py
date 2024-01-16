from ipaddress import *

ip = '192.168.32.48'
mask = '255.255.255.240'
network = ip_network(f'{ip}/{mask}', 0)
#ip_network - создаёт объект сеть
#network = ip_network('192.168.32.48/255.255.255.240', 0)
k = 0

for net in network:
    print(net)
    if f"{net:b}".count('1') % 2 != 0:
        k += 1
''' if bin(int(net))[2:].count('1') % 2 != 0:
        k += 1'''

print(k)