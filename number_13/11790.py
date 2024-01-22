from ipaddress import *

ip = ip_address('152.65.245.132')

for mask in range(33):
    network = ip_network(f'{ip}/{mask}', 0)
    if ip not in [network.network_address, network.broadcast_address]:
            if all(f'{ip:b}'[:16].count('0') >= f'{ip:b}'[16:].count('0')
                for ip in network):
                print(network.netmask)