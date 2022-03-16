import os
def ping_unitario():
    host = input('Digite o endereco do host:')

    os.system('ping -n {}'.format(host))

def ping_multiplo():
    with open('/home/gusmao/Documents/Dev/PycharmProjects/Dio/Security/host.txt') as file:
        dump = file.read()
        dump = dump.splitlines()
        for hosts in dump:
            os.system('ping -w 4 '+ hosts)
            print(hosts)
        file.close()


ping_multiplo()