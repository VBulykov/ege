from ipaddress import *

mask = '255.255.252.0'

for A in range(256):
    ip_net = ip_network(f'183.192.{A}.0/{mask}', 0)

    if all([True if bin(int(net))[18:].count('1') > 3 else False for net in ip_net]):
        print('A=', A)
        break