import ipaddress

ip = '192.168.1.1'

endereco = ipaddress.ip_address(ip)

print (endereco + 5000)

ip2 = '10.1.1.0/24'

rede = ipaddress.ip_network(ip2)
print (rede)
for ip in rede:
    print(ip)

