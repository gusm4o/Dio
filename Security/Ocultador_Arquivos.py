import ctypes

oculta_arq = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('/home/gusmao/Documents/Dev/PycharmProjects/Dio/Security/oculto.txt' , oculta_arq)


if retorno:
    print('Arquivo ocultado')

else:
    print('Arquivo nao ocultado')