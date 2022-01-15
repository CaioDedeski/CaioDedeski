from math import *

N = 5                               
senox = 0
x = 1.2
n = 0

print("Este programa calcula o seno de 1.2 usando a série de Taylor \n")
print("Para n = 5 \n")


for n in range(n,N + 1):             #loop para o somatório, variando n de 0 até 5, em passos de 1

   fat = 1
   num = (-1)**n                     #numerador
   den = (2*n + 1)                   #deniminador
   
   for d in range(den,0,-1):         #loop para o fatorial do denominador, variando dele mesmo, para cada n, até 1, em passos de -1

       fat = fat*d                   #calculo do fatorial

   senox = senox + (num*x**den)/fat  #somatorio da série


print("O seno de 1.2 é aproximadamente igual a %.8f \n" %(senox))   
print(sin(1.2))                      #valor de sin(1.2) da bibliotéca math
