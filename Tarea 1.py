
import numpy as np
import math as mt
import pandas as pd
import matplotlib.pyplot as plt
from __future__ import print_function,division
def horner(coeffs,x):
    acc=0
    for c in reversed(coeffs):
        acc = acc*x + c
    return acc 
mt.factorial(0)
1
#Codigo mas Ineficiente
def evalupoly(coeff,x):
    acc = 0 
    for i,a in enumerate(coeff): #Esta funcion da el indice y el numero de ese indice 
        acc += (x**i)*a #i = 0,1,2... y a es igual los valores 
    return acc
evalupoly((-1,2,2,3,1),2)
51
#Metodo Iterativo
def poly_iter(A, x):
    p = 0 #Inializa las variables 
    xn = 1
    for a in A: #A son los coeficientes 
        p += xn * a # el primer coeficiente, y de ahi los demas 
        xn *= x #esto hara que tengamos los exponentes 
    return p
poly_iter((-1,2,2,3,1),2)
51
#La regla de Horner
def poly_horner(A, x): # A coeficiente en forma de lista []
    p = A[-1] #A[-1] es para que vaya del ultimo al primero 
    i = len(A) - 2 #len es para dar el tamaño de A 
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p
poly_horner((-1,2,2,3,1),2)
51
#Funcion conseno en serie de potencias
def cos(x,k):
    valor = 0
    A = []
    for i in range(k+1):
      p = (((-1)**i) * x**(2*i))/(mt.factorial(2*i))
      valor = valor + p 
    return (valor)
cos(7,1700)
0.7539022543432953
iteraciones = [10,20,50,100,1000]
valores_x = [0,5,8,16,32,60,80,100]
def tabla(a,b):
   val_x = [] 
   itera = []
   val_cos = []
   error_re = []
   cos_v = []
   for i in (a):
    for j in (b):
        val_x.append(i)
        itera.append(j)
        val_cos.append(cos(i,j))
        error_re.append((cos(i,j) - mt.cos(i))/mt.cos(i))
        cos_v.append(mt.cos(i))
        tabla = np.column_stack((val_x, itera,val_cos,cos_v,error_re))
        tabla_res = pd.DataFrame(tabla,columns=['X','Iteraiones','Suma',"cos",'Error'])
    
   
   
   return  tabla_res 

tabla(valores_x,iteraciones)

X	Iteraiones	Suma	cos	Error
0	0.0	10.0	1.000000e+00	1.000000	0.000000e+00
1	0.0	20.0	1.000000e+00	1.000000	0.000000e+00
2	0.0	50.0	1.000000e+00	1.000000	0.000000e+00
3	0.0	100.0	1.000000e+00	1.000000	0.000000e+00
4	0.0	1000.0	1.000000e+00	1.000000	0.000000e+00
5	5.0	10.0	2.836642e-01	0.283662	7.151709e-06
6	5.0	20.0	2.836622e-01	0.283662	1.761251e-15
7	5.0	50.0	2.836622e-01	0.283662	1.761251e-15
8	5.0	100.0	2.836622e-01	0.283662	1.761251e-15
9	5.0	1000.0	2.836622e-01	0.283662	1.761251e-15
10	8.0	10.0	-8.677416e-02	-0.145500	-4.036141e-01
11	8.0	20.0	-1.455000e-01	-0.145500	-4.784259e-13
12	8.0	50.0	-1.455000e-01	-0.145500	-7.611321e-14
13	8.0	100.0	-1.455000e-01	-0.145500	-7.611321e-14
14	8.0	1000.0	-1.455000e-01	-0.145500	-7.611321e-14
15	16.0	10.0	1.848709e+05	-0.957659	-1.930455e+05
16	16.0	20.0	-7.233984e-01	-0.957659	-2.446183e-01
17	16.0	50.0	-9.576595e-01	-0.957659	-1.164118e-10
18	16.0	100.0	-9.576595e-01	-0.957659	-1.164118e-10
19	16.0	1000.0	-9.576595e-01	-0.957659	-1.164118e-10
20	32.0	10.0	3.740488e+11	0.834223	4.483797e+11
21	32.0	20.0	7.511996e+11	0.834223	9.004777e+11
22	32.0	50.0	8.339676e-01	0.834223	-3.066086e-04
23	32.0	100.0	8.339676e-01	0.834223	-3.066124e-04
24	32.0	1000.0	8.339676e-01	0.834223	-3.066124e-04
25	60.0	10.0	1.356797e+17	-0.952413	-1.424589e+17
26	60.0	20.0	1.132192e+23	-0.952413	-1.188761e+23
27	60.0	50.0	1.826468e+19	-0.952413	-1.917727e+19
28	60.0	100.0	1.596800e+09	-0.952413	-1.676584e+09
29	60.0	1000.0	1.596800e+09	-0.952413	-1.676584e+09
30	80.0	10.0	4.470466e+19	-0.110387	-4.049803e+20
31	80.0	20.0	1.304690e+28	-0.110387	-1.181921e+29
32	80.0	50.0	8.442218e+31	-0.110387	-7.647820e+32
33	80.0	100.0	-8.643526e+16	-0.110387	7.830186e+17
34	80.0	1000.0	-8.643526e+16	-0.110387	7.830186e+17
35	100.0	10.0	3.958792e+21	0.862319	4.590868e+21
36	100.0	20.0	1.058262e+32	0.862319	1.227228e+32
37	100.0	50.0	5.330353e+41	0.862319	6.181417e+41
38	100.0	100.0	-3.771888e+25	0.862319	-4.374122e+25
39	100.0	1000.0	-4.023252e+25	0.862319	-4.665620e+25


#Datos Estrellas
from pylab import scatter,xlabel,ylabel,xlim,ylim,show
from numpy import loadtxt

data = loadtxt("stars.data.dat",float)
x = data[:,0]
y = data[:,1]

scatter(x,y)
xlabel("Temperature")
ylabel("Magnitude")
xlim(0,13000)
ylim(-5,20)
show()

#Reproduccion
#Ahora graficaremos con matplotlib

plt.scatter (x,y,c="yellow")
plt.grid(c="r")
plt.title("Stars")
xlabel("Temperature")
ylabel("Magnitude")
plt.style.use('dark_background')


#Alturas
ltura5 = loadtxt("altura5.dat",float)
altura6 = loadtxt("altura6.dat",float)
altura5[:,0]
altura6.shape
(100000,)
plt.plot(altura5[:,0],altura5[:,1],label = "Caso 1")
plt.plot(altura5[:,0],altura5[:,2],label = "Caso 2")
plt.plot(altura5[:,0],altura5[:,3],label = "Caso 3")
plt.legend()
xlabel("Altura")
ylabel("Frecuencia")
plt.style.use('default')

plt.boxplot(altura6)
plt.title('Boxplot')
plt.ylabel('Valor')
plt.grid()
plt.show()

import seaborn as sns
sns.violinplot(altura6)
plt.title('Violin Plot')
plt.show()