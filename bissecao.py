'''
Programa que calcula a raiz de funções pelo método da bisseção
'''

from math import *


def funcao1(x):                  #função pedida pela questão

    return exp(-x) - sin(pi*x/2) #returna um valor para cada x

xmin = 0                        
xmax = 1
n = 100                          #número máximo de interações no loop
p = 1.e-7                        #presisão
it = 0                           #número de interações

fmax = funcao1(xmax)            
fmin = funcao1(xmin)

if fmax*fmin > 0:                #verificando se é possível utilizar a bisseção com os pontos dados

    print("Não é possivel achar a raiz com os pontos escolhidos")

while fabs(xmax - xmin) > p and it < n:   #loop de interações para a raiz da função

    xmedio = (xmin + xmax)/2
    fmedio = funcao1(xmedio)

    if fmin*fmedio < 0:           #verificando qual variável vai receber o valor médio 

        xmax = xmedio

    else: xmin = xmedio

    it += 1                       #contador de interações 


print("Com %d interações, a raiz da função é %.4f" %(it, xmedio))
