from ipaddress import *

ip = '192.168.32.160'
mask = '255.255.255.240'

network = ip_network(f'{ip}/{mask}', 0)

print(network.netmask)
print(network.broadcast_address)
print(network.network_address)