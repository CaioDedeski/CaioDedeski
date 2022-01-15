'''
Programa que faz um histograma com os dados do arquivo gravidade.dat
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy import loadtxt
    
a = loadtxt ("gravidade.dat")                      #array com os valores da lista
    
print("A média dos valores é: %.5f" %(np.mean(a))) #média dos valores
print("E o desvio padrão: %.5f" %(np.std(a)))      #desvio padrão dos valores

plt.subplot(1,2,1)                                 #função para plotar dois histogramas separados
plt.hist(a , bins=20, ec = "black", label = "20 bins")
plt.legend()
plt.subplot(1,2,2) 
plt.hist(a , bins=60,ec = "black", label = "60 bins") 
plt.tight_layout()
plt.legend()
plt.show() 
