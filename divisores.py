print("Este programa calcula o numero de divisores de um número qualquer inteiro positivo")

n = int(input("Digite seu número \n"))
i = 1
j = 1

print("Divisores: \n")
          
while n != i:
    if n%i == 0:
        j = j + 1           # contador dos divisores
        print("%d" %(i))    # imprime o divisor
    i = i + 1               # contador do loop

print("%d" %(n))            # todo numero é divisor dele mesmo
print("Total de divisores: %d \n" %(j))
    
    
        
          

          
