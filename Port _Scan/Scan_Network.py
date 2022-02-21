
import nmap


scanner = nmap.PortScanner()

print('Welcome ')
print('-'*10)
endereco = input('Entre com o destino')
print ('O endereco digitado e :', endereco)
print(type(scanner))

menu = int(input('''\n Escolha o tipo de varredura:
            1- Tipo SYN
            2- Tipo UDP
            3- Tipo Intensa\n'''))

print('Escolha:', menu)

if menu == 1:
    #print('Versao do NMAP :', nmap.version())
    scanner.scan(endereco, '1-4000', '-v -sS')
    print(scanner.scaninfo())
    print('Status do IP ', scanner[endereco].state())
    print(scanner[endereco].all_protocols())
    print('')
    print('Portas abertas: ', scanner[endereco]['tcp'].keys())

elif menu == 2:
    #print('Versao do NMAP :', nmap.version())
    scanner.scan(endereco, '1-3000', '-v -sU')
    print(scanner.scaninfo())
    print('Status do IP ', scanner[endereco].state())
    print(scanner[endereco].all_protocols())
    print('')
    print('Portas abertas: ', scanner[endereco]['udp'].keys())

elif menu == 3:
    scanner.scan(endereco, '1-1000', '-v -sC')
    print('Status do IP', scanner[endereco].state())
    print(scanner[endereco].all_protocols())
    print('')
    print('Portas abertas: ',scanner[endereco]['tcp'].keys())

else:
    print('Opção inválida:')