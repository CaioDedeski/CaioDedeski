'''
Programa que plota o gráfico de funções
'''

from math import pi
import matplotlib.pyplot as plt
import numpy as np


def funcao1(x):                  #função pedida pela questão

    return np.exp(-x) - np.sin(pi*x/2) #utilização do "np." para trata-lo como array 

x = np.arange(0, 4, 0.1)           #definendo o intervalo da curva e o passo entre cada ponto  
y = funcao1(x)

plt.plot(x, y, 'r')                #plot da função
plt.grid()
plt.show()
