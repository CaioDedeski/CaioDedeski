print("Este programa retorna a soma dos elementos de uma lista\n")

def mysum(x):

    s = x[0]                   # a variável s recebe o primeiro elemento da lista

    for i in range(1, len(x)): # o loop vai do segundo elemento da lista até o último

        s += x[i]              # somatório dos elementos da lista

    return s                   # retorna o valor desse somatório

print(mysum([1, 2, 3]))
print(mysum(["Hello, ", "World!"]))
print(mysum([[1,2], [3, 4]]))
