import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = 'localhost'
port = 5432
s.bind((host, port))
msg = '\nServidor : recebido'
print('Socket criado com sucesso!')
while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('\nServidor enviando Mensagem...')
        s.sendto(dados + (msg.encode()), end)