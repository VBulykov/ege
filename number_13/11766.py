from ipaddress import *


ip = ip_address('132.243.87.85')

network = ip_address('132.243.64.0')

for mask in range(33):
    net = ip_network(f"{ip}/{mask}", 0)
    #net.network_address - адрес сети
    #net.broadcast_address - широковещательный 
    #net.hosts
    if net.network_address == network:
        print(bin(int(net.netmask))[2:].zfill(32).count('0'))
        break

    bin(int(net.netmask))[2:].zfill(32)[:16]
    bin(int(net.netmask))[2:].zfill(32)[16:]