from ipaddress import *

mask = '255.255.255.192'
k = 0

for A in range(256):
    ip_net = ip_network(f'207.0.{A}.167/{mask}', 0)
    if all([
        True if bin(int(ip))[2:18].count('0') > bin(int(ip))[18:].count('0')
        else False for ip in ip_net
    ]):
        k += 1

print(k)