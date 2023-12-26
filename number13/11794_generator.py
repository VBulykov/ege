from ipaddress import *
mask = '255.255.255.192'

for A in range(256):
    ip = f'223.167.{A}.167'
    network = ip_network(f"{ip}/{mask}", 0)
    k = 0

    for net in network:
        bin_net = bin(int(net))[2:]

        if bin_net[:16].count('0') <= bin_net[16:].count('0'):
            k += 1
   
    if k == len([net for net in network]):
        print(A)