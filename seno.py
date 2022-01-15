from math import *
import numpy as np
import matplotlib.pyplot as plt

print("Este programa calcula o seno de um numero usando a série de Taylor \n")
x = float(input("Digite o valor desejado\n"))
N = int(input("Digite o número de termos\n"))

def serieT(x, N):

   senox = 0
   x0 = 0
   
   for n in range(0,N):             #loop para o somatório, variando n de 0 até 5, em passos de 1

      fat = 1
      num = (x - x0)**(2*n + 1)         #numerador
      den = (2*n + 1)                   #deniminador
   
      for d in range(den,0,-1):         #loop para o fatorial do denominador, variando dele mesmo, para cada n, até 1, em passos de -1

         fat = fat*d                    #calculo do fatorial

      senox += (-1)**n*num/fat          #somatorio da série
      
   return senox                         #retorna o valor do somatório

y = serieT(x, N)

print("O seno de %.6f é aproximadamente igual a %.8f \n" %(x, y))
print("A soma do valor obtido com o valor dado pela biblioteca: %.8f" %(y))
print("A diferença do valor obtido com o valor dado pela biblioteca: %.8f" %(sin(x) - y))

xs = np.arange(0, 3*pi/2, 0.1)          #array com angulos 
ydxs = np.sin(xs)                       #array com os senos dos angulos

plt.plot(xs, ydxs, 'r')                 #gráfico com os senos dados pela função sin
plt.xlabel("angulo (0 a 3/2 pi)")
plt.ylabel("seno(x)")
plt.title("Série de Taylor - sen(x)")
plt.ylim(-1.5, 1.5)                     #limites no eixo y
plt.grid()

for n in range(2, 6):                   #loop para plotar com os n termos

   ys = serieT(xs, n)
   plt.plot(xs, ys)
   
plt.legend(['sen(x)','n = 2','n = 3','n = 4','n = 5'])
plt.show()


