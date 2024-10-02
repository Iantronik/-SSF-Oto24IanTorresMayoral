# %%
import numpy as np 
import matplotlib.pyplot as plt
import math as mt

# %% [markdown]
# # Tarea 2

# %%
#Integracion numerica
#a) usando regla del trapecio y con 6, 15 subintervalos.

# %% [markdown]
# $$
# \int_{-1}^{1} \frac{1}{\sqrt{2\pi}} e{\frac{{-x^2}}{2}} ,dx
# $$

# %%
#Definimos nuestra funcion del ejercicio 1
def fx(x):
    funcion = (1/(mt.sqrt(2*mt.pi)))*(mt.exp((-x**2)/2))
    return funcion 

# %% [markdown]
# Metodo del Trapecio 

# %%
#Definimos la funcion que corresponde al metodo del trapesio 
def trape(a,b,n,fun,valor_teorico): #a,b son los limites de integracion, n umero de intervalos,la funcion a integrar 
    suma = []
    intervalo = np.linspace(a,b,n+1)
    suma.append(float(fun(intervalo[0])))
    suma.append(float(fun(intervalo[-1])))
    h = (b-a)/n
    for i in (intervalo[1:-1]):
        suma.append(2*fun(float(i)))
    resultado = (h/2)*np.sum(suma)
    error = abs((resultado - valor_teorico)/valor_teorico)
    return float(resultado) , float(error)

# %% [markdown]
# Metodo Simpson 
# 

# %%
def simpson(a,b,n,fun,valor_teorico):    
    h = (b - a) / n
    intervalo = np.linspace(a, b, n + 1)
    fun = np.vectorize(fun)
    S = fun(intervalo[0]) + fun(intervalo[-1]) + 4 * np.sum(fun(intervalo[1:-1:2])) + 2 * np.sum(fun(intervalo[2:-2:2]))
    #intervalo[1:-1:2] representa los pares y intervalo[2:-2:2] los impares 
    resultado_s = (h / 3) * S
    error = abs((resultado_s - valor_teorico)/valor_teorico)
    return float(resultado_s) , float(error)
    

# %% [markdown]
# Metodo de Guass_legende

# %%
def gauss_legendre(a,b,n,fun,valor_teorico):
    xi, wi = np.polynomial.legendre.leggauss(n) #obtenemos los puntos y pesos de gauss legendre par n 
    entrada = (xi/2)*(b-a) + ((b+a)/2)
    fun = np.vectorize(fun) #vectorizamos la funcion 
    resultado_gl = ((b-a)/2) * np.sum(wi * fun(entrada))
    error = abs((resultado_gl - valor_teorico)/valor_teorico)
    return float(resultado_gl) , float(error)

# %%
print (f"Para metodo del trapecio con 6 subintervalos el resultado y error relativo es {trape(-1,1,6,fx,0.6826894921)} " )
print (f"Para metodo del trapecio con 15 subintervalos el resultado y error relativo es {trape(-1,1,15,fx,0.6826894921)}" )
print (f"Para metodo del trapecio con 50000 subintervalos el resultado y error relativo es {trape(-1,1,50000,fx,0.6826894921)}" )

print (f"Para el metodo de Simpson con 6 inervalos el resultado es y error relativo es  {simpson(-1, 1, 6,fx,0.6826894921)}")
print (f"Para el metodo de Simpson con 15 inervalos el rresultado y error relativo es{simpson(-1, 1, 15,fx,0.6826894921)}")
print (f"Para el metodo de Simpson con 16 inervalos el rresultado y error relativo es{simpson(-1, 1, 16,fx,0.6826894921)}")
print (f"Para el metodo de Simpson con 50000 inervalos el resultado y error relativo es{simpson(-1, 1, 50000,fx,0.6826894921)}")

print (f"Para el metodo de Gauss Legendre con 6 inervalos el resultado y error relativo es{gauss_legendre(-1, 1, 6,fx,0.6826894921)}")
print (f"Para el metodo de Gauss Legendren con 15 inervalos el resultado y error relativo es{gauss_legendre(-1, 1, 15,fx,0.6826894921)}")
print (f"Para el metodo de Gauss Legendren con 16 inervalos el resultado y error relativo es{gauss_legendre(-1, 1, 16,fx,0.6826894921)}")
print (f"Para el metodo de Gauss Legendre con 50000 inervalos el resultado y error relativo es{gauss_legendre(-1, 1, 5000,fx,0.6826894921)}")


# %% [markdown]
# ## Ejercicio 2 

# %% [markdown]
# $$
# \int_{0}^{3} \frac{ e^ {x} \sin(x)}{1 + {x^2}} , dx 
# $$

# %%
def fx2(y):
    funcion_2 = (mt.exp(y)*mt.sin(y))/(1+y**2)
    return funcion_2

# %%
print (f"Para metodo del trapecio con 6 subintervalos el resultado y error relativo es {trape(0,3,6,fx2,2.88164)} " )
print (f"Para metodo del trapecio con 15 subintervalos el resultado y error relativo es {trape(0,3,15,fx2,2.88164)}" )
print (f"Para metodo del trapecio con 16 subintervalos el resultado y error relativo es {trape(0,3,16,fx2,2.88164)}" )
print (f"Para metodo del trapecio con 20 subintervalos el resultado y error relativo es {trape(0,3,20,fx2,2.88164)}" )

print (f"Para el metodo de Simpson con 6 inervalos el resultado es y error relativo es  {simpson(0,3, 6,fx2,2.88164)}")
print (f"Para el metodo de Simpson con 15 inervalos el rresultado y error relativo es{simpson(0,3, 15,fx2,2.88164)}")
print (f"Para el metodo de Simpson con 16 inervalos el rresultado y error relativo es{simpson(0,3, 16,fx2,2.88164)}")
print (f"Para el metodo de Simpson con 20 inervalos el resultado y error relativo es{simpson(0,3, 20,fx2,2.88164)}")

print (f"Para el metodo de Gauss Legendre con 6 inervalos el resultado y error relativo es{gauss_legendre(0,3, 6,fx2,2.88164)}")
print (f"Para el metodo de Gauss Legendren con 15 inervalos el resultado y error relativo es{gauss_legendre(0,3, 15,fx2,2.88164)}")
print (f"Para el metodo de Gauss Legendren con 16 inervalos el resultado y error relativo es{gauss_legendre(0,3, 16,fx2,2.88164)}")
print (f"Para el metodo de Gauss Legendre con 20 inervalos el resultado y error relativo es{gauss_legendre(0,3, 20,fx2,2.88164)}")

# %% [markdown]
# # Ejercicio 3

# %% [markdown]
# Repetir el problema 2. pero considerando los límites en (-2, 0)

# %%
print (f"Para metodo del trapecio con 6 subintervalos el resultado y error relativo es {trape(-2,0,6,fx2,-0.256471)} " )
print (f"Para metodo del trapecio con 15 subintervalos el resultado y error relativo es {trape(-2,0,15,fx2,-0.256471)}" )
print (f"Para metodo del trapecio con 16 subintervalos el resultado y error relativo es {trape(-2,0,16,fx2,-0.256471)}" )
print (f"Para metodo del trapecio con 20 subintervalos el resultado y error relativo es {trape(-2,0,20,fx2,-0.256471)}" )

print (f"Para el metodo de Simpson con 6 inervalos el resultado es y error relativo es  {simpson(-2,0, 6,fx2,-0.256471)}")
print (f"Para el metodo de Simpson con 15 inervalos el rresultado y error relativo es{simpson(-2,0, 15,fx2,-0.256471)}")
print (f"Para el metodo de Simpson con 16 inervalos el rresultado y error relativo es{simpson(-2,0, 16,fx2,-0.256471)}")
print (f"Para el metodo de Simpson con 20 inervalos el resultado y error relativo es{simpson(-2,0, 20,fx2,-0.256471)}")

print (f"Para el metodo de Gauss Legendre con 6 inervalos el resultado y error relativo es{gauss_legendre(-2,0, 6,fx2,-0.256471)}")
print (f"Para el metodo de Gauss Legendren con 15 inervalos el resultado y error relativo es{gauss_legendre(-2,0, 15,fx2,-0.256471)}")
print (f"Para el metodo de Gauss Legendren con 16 inervalos el resultado y error relativo es{gauss_legendre(-2,0, 16,fx2,-0.256471)}")
print (f"Para el metodo de Gauss Legendre con 20 inervalos el resultado y error relativo es{gauss_legendre(-2,0, 20,fx2,-0.256471)}")

# %% [markdown]
# # Ejercicio 4

# %% [markdown]
# $$
# f(x) = \frac{e^{x}}{x}
# $$
# $$
# g(x) = \frac{1-e^{x}}{x}
# $$
# $$

# %%
#Definimos las nuevas funciones 
def fx3(x):
    return mt.exp(x)/x

def fx4(x):
    return (1-mt.exp(x))/x

# %% [markdown]
# En este caso utilizaremos el metodo de gauss-legendre en intervalos de 10,100,1000

# %%
print(f"El resultado con el metodo de gauss-legendre {gauss_legendre(0,5, 10,fx3,-0.256471)}")
print(f"El resultado con el metodo de gauss-legendre {gauss_legendre(0,5, 1000,fx3,-0.256471)}")
print(f"El resultado con el metodo de gauss-legendre {gauss_legendre(0,5, 9000,fx3,-0.256471)}")

# %%
print(f"El resultado con el metodo de gauss-legendre {gauss_legendre(0,5, 10,fx4,-37.9986)}")
print(f"El resultado con el metodo de gauss-legendre {gauss_legendre(0,5, 100,fx4,-37.9986)}")
print(f"El resultado con el metodo de gauss-legendre {gauss_legendre(0,5, 9000,fx4,-37.9986)}")

# %% [markdown]
# 