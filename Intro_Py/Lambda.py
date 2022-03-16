contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b : a+b
print(soma(10,2))
sub = lambda a, b : a-b
print(sub(10,2))
div = lambda a, b : a/b
print(div(10,2))
mul = lambda  a, b : a*b
print(mul(10,2))

calculadora = {
    'soma' : lambda a, b : a+b,
    'subt' : lambda a, b : a-b,
    'divi' : lambda a, b : a/b,
    'mult' : lambda  a, b : a*b,

}
soma = calculadora['soma']
print(soma(25,5))