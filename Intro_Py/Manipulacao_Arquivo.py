def escrever_arquivos(texto):
    diretorio ='/home/gusmao/Documents/Dev'
    arquivo= open('novo.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('novo.txt','a')
    arquivo.write(texto)
    arquivo.close()

def  ler_arquivo(nome):
    arquivo= open(nome, 'r')
    texto= arquivo.read()
    print(texto)

def media_notas(nome):
    arquivo = open(nome, 'r')
    aluno_nota = aquivo.read()
    print(aluno_nota)
    for x in aluno_nota:
        print(x)

if __name__ == '__main__':
    ent = None
    ent = input("Digite um texto para inserir no arquivo {}" .format(ent))
    atualizar_arquivo(ent)
    #escrever_arquivos(ent)
    ler_arquivo('novo.txt')