import matplotlib.pylab as plt
import scipy as sp
import math
from numpy import*

# phi = numero de oro (proporción aurea)
phi= (1+ sqrt(5))/2

# q = numeros irracionales tipicos
q = [math.pi , math.e , phi]

# q2 = cuadrado de los numeros irracionales calculados en calculadora
q2 = [9.86960440109 , 7.38905609893 , 2.61803398875]

# luego calculamos los cuadrados de los mismos números pero utilizando float64
# y float32 para luego comparar los errores

float64 = []
for i in q:
    q3 = sp.float64(i**2)
    float64.append(q3)

float32 = []
for i in q:
    q4 = sp.float32(i**2)
    float32.append(q4)

#Error 64:
error64 = []
while i in range(2):
    error = ((float64[i] - q2[i])/q2[i])
    error64.append(error)
    i += 1

#Error 32:
error32 = []
while i in range(2):
    error = ((float32[i] - q2[i])/q2[i])
    error32.append(error)
    i +=1
