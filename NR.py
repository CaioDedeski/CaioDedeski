'''
Programa que calcula a raiz de funções pelo método de Newton-Raphson
'''

from math import *


x0 = 0                                    #valor inicial de x
p = 1.e-7                                 #precisão
it = 0                                    #interações

def funcao1(xi):

    return exp(-xi) - sin(pi*xi/2)        #função que ser´s encontrada a raiz


def derivada(xi):

    return -exp(-xi) - cos(pi*xi/2)*pi/2  #derivada da função

xi = x0 - funcao1(x0)/derivada(x0)        #primeira interação do método de Newton-Raphson


while fabs(x0 - xi) > p and it < 100:     #loop para as interações do método

    x0 = xi
    xi = x0 - funcao1(x0)/derivada(x0)
    it += 1

print("Com %d interações, a raiz da função é %.4f" %(it + 1, xi))  
