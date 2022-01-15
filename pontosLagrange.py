from math import *

p = 1.e-7                           #precisão
it = 0

R = 1.5*10**11                      #raio do Sol até a Terra
m = 5.9736*10**24                   #massa da Terra
M = 1.989*10**30                    #massa do Sol 
w = 1.992*10**(-7)                  #velocidade angular da Terra e do objeto no ponto L1
G = 6.674*10**(-11)                 #constante gravitacional

x0 = R/2

def funcao(xi):                      #função para a distância do Sol até o ponto L1

    return G*M/xi**2 - G*m/(R - xi)**2 - xi*w**2 

def derivada(xi):                     #derivada da função anterior

    return -G*2*M/xi**3 - G*2*m/(R - xi)**3 - w**2

xi = x0 - funcao(x0)/derivada(x0)     #definendo o primeiro xi para começar o loop

while fabs(x0 - xi) > p and it < 100: #loop para a raiz da função 

    x0 = xi
    xi = x0 - funcao(x0)/derivada(x0)
    it += 1                           #contador de interações

print("Com %d interações, a distancia do Sol até o ponto L1 é %.4f" %(it, xi))
