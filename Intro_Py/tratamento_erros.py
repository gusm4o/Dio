lista = [1]
try:
    div = 10 / 1
   # num = lista [10]
    x = a
except ZeroDivisionError:
    print("ERRO divisao por 0")
except IndexError:
    print("Erro Indice invalido")

except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))