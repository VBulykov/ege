from ipaddress import *

ip_first_1 = ip_address('167.77.194.47')
ip_first_2 = ip_address('167.77.194.37')
ip_second  = ip_address('167.77.200.25')

k = 0

for i in range(12, 32):
    ip_network_1 = ip_network(f'{ip_first_1}/{i}', 0)
    ip_network_1_2 = ip_network(f'{ip_first_2}/{i}', 0)

    ip_network_2 = ip_network(f'{ip_second}/{i}', 0)

    if (
        ip_first_1 in ip_network_1 and
        ip_first_1 in ip_network_1_2 and 
        ip_first_2 in ip_network_1 and
        ip_first_2 in ip_network_1_2 and
        ip_second in ip_network_2
    ):
        k += 1
    
print(k)