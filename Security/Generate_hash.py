import hashlib
cont = 0
while cont ==0 :
    palavra = input('Digite uma palavra:')

    menu = int(input('''####### ESCOLHA O TIPO DE HASH ######
    
                    1)MD5
                    2)SHA1
                    3)SHA256
                    4)SHA512
                    5)SAIR'''))
    if menu == 1:
        resultado = hashlib.md5(palavra.encode('utf-8'))
        print('Hash MD5 da palavra ',palavra,'é :',resultado.hexdigest())

    elif menu == 2:
        resultado = hashlib.sha1(palavra.encode('utf-8'))
        print('Hash SHA1 da palavra ',palavra,'é :',resultado.hexdigest())

    elif menu == 3:
        resultado = hashlib.sha256(palavra.encode('utf-8'))
        print('Hash  SHA256 da palavra ',palavra,'é :',resultado.hexdigest())

    elif menu == 4:
        resultado = hashlib.sha512(palavra.encode('utf-8'))
        print('Hash SHA512 da palavra ',palavra,'é :',resultado.hexdigest())

    else:
        cont = 1