from math import *

print("Este programa calcula funções de segundo grau, usando bhaskara \n")
a = float(input("Digite o valor do coeficiente a da equação \n"))
b = float(input("Digite o valor do coeficiente b da equação \n"))
c = float(input("Digite o valor do coeficiente c da equação \n"))

if a == 0:
    print("Não é uma equação de segundo grau \n")

delta = b**2 - 4*a*c                     # calculo do delta

if delta > 0:
    print("A equação %.3fx**2 + %.3fx + %.3f" %(a,b,c))
    print("Possui duas raizes reais \n")

    x1 = (- b + sqrt(delta))/(2.*a)      # calculo das raizes
    x2 = (- b - sqrt(delta))/(2.*a)
    
    print("As raizes são: %.3f %.3f" %(x1,x2))

if delta == 0:
    print("A equação %.3fx**2 + %.3fx + %.3f" %(a,b,c))
    print("Possui uma raiz real \n")

    x = - b/(2.*a)                       # calculo da raiz

    print("A raiz é: %.3f" %(x))

if delta < 0:
    print("A equação %.3fx**2 + %.3fx + %.3f" %(a,b,c))
    print("Possui duas raizes complexas \n")
    print("Com uma parte real e uma parte imaginária \n")

    real = - b/2.*a
    imag = ((- 1*delta)**(1/2))/(2.*a)  # parte imaginaria da raiz
                                        # para possibilitar o cálculo, multipliquei por -1

    print("%.3f +- %.3fi" %(real,imag)) # evidencio a parte imaginária
    

    

    
    
    
    


