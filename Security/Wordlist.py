import itertools

str_permut = input('String a ser permutada:')
result =itertools.permutations(str_permut, len(str_permut))

cont = 0

for i in result:
    cont +=1
    print('' .join(i))
print('',cont)