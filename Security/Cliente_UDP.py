import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,0)
host = 'localhost'
porta = 5432
msg = 'Hello'

try:
    print('Cliente : ' + msg)
    s.sendto(msg.encode(), (host, 5432))
    dados, servidor = s.recvfrom(1024)

    dados = dados.decode()
    print('\nCliente : ' + dados)
finally:
    print('\nCliente: Fechando a conexao')
    s.close()