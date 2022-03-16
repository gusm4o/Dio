def Cont_letras (lista_palavras):
    contador= []
    for x in lista_palavras:
        quant = len(x)
        contador.append(quant)
    return contador
if __name__ == '__main__':
    lista = ['cachorros', 'papagaio']
    print(Cont_letras(lista))