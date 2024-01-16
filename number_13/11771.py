from ipaddress import *
ip = ip_address('121.74.179.135')
net = ip_address('121.74.179.128')
for mask in range(33):
    network = ip_network(f'{ip}/{mask}', 0)
    if net == network.network_address:
        print(network.num_addresses)