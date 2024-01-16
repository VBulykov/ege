from ipaddress import *
#255 = 11111111
ip =      ip_address('175.184.52.103')
#                     255.255. x.0
ad_seti = ip_address('175.184.48.0')

#наибольшее количество единиц в записи маски
print(bin(int(ip))[18:26])
print(bin(int(ad_seti))[18:26])
print(bin(255)[2:])