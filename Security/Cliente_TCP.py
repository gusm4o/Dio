import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    except socket.error as e:
        print('erro de conexao')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso')

    h_alvo = input('Entre com o host:')
    porta_alvo = int(input('Entre com a porta:'))


    try:
        s.connect((h_alvo, porta_alvo))
        print('Cliente TCP conectado com sucesso no host: '+ h_alvo)
        s.shutdown(2)
    except socket.error as e:
        print('Impossivel conectar no host: ' + h_alvo)
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == '__main__':
    main()