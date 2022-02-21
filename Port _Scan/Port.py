import socket

ip = input('Entre endereco:\n')
list_ports = []
cont = 0
while cont < 2 :
    list_ports.append(int(input('Digite a porta alvo:\n')))
    cont +=1

for port_number in list_ports:
    cliente_conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente_conexao.settimeout(0.05)
    code =cliente_conexao.connect_ex((ip,port_number))
    print(code)
    if code == 0:
        print(str(port_number),'Porta aberta')

    else:
        print(str(port_number),'Porta fechada')
