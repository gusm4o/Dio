import hashlib

arq1 = '/home/gusmao/Documents/Dev/PycharmProjects/Dio/Security/x1.txt'
arq2 = '/home/gusmao/Documents/Dev/PycharmProjects/Dio/Security/x2.txt'


hash1 = hashlib.new('md5')
hash1.update(open(arq1, 'rb').read())
hash2 = hashlib.new('md5')
hash2.update(open(arq2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'o arquivo: {arq1}  é diferente do arquivo : {arq2}')
else:
    print(f'o arquivo:  {arq1} é igual ao arquivo : {arq2}')