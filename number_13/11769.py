from ipaddress import *
ip =  ip_address('157.17.164.129')
net = ip_address('157.17.128.0')

for A in range(33):
    network = ip_network(f"{ip}/{A}", 0)
    #print(bin(int(network.broadcast_address))[2:].zfill(32))
    #print(bin(int(network.network_address))[2:].zfill(32))
    
    if net == network.network_address:
        #print(A)
        print(network.netmask)
        break