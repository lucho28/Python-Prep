#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

variable = 28
if (variable < 0):
    print("Es meno que cero !")
else:
    print("Es Mayor que cero !")


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
var1 = 2
var2 = "2"

if(type(var1) == type(var2)):
    print("Son del mismo tipo")
else:
    print("Son de tipos diferentes")




# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1,20):
    if(i%2 == 0):
        print("el valor: ", i , "es par")
    else:
        print("el valor: ", i , "es impar")




# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:
for i in range(0,5):
    print(i**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:
cont = 10
for i in range(0,cont):
    print("ciclo numero: ", i)




# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
factor = 5
factorial = 1
if (factor > 0):
    while (factor >0):
        factorial = factorial * factor
        factor -=1

print(factorial)


# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:
cont = 10
while (cont > 0):
    for i in range(1,3):
        print("Bucle for iteracion Nro: ", i)
    cont -=1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
cont = 5
for i in range(1,10):
    while(cont > 0):
        print("Bucle while iteracion Nro: ", cont)
        cont -=1





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for i in range(2,31):
    cont = 0
    d=1
    while(d<=i):
        if(i % d == 0):
            cont+=1
        d+=1
    if(cont == 2):
        print("el numero ", i , "es primo")



# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
for i in range(2,31):
    cont = 0
    d=1
    while(d<=i):
        if(i % d == 0):
            cont+=1
            if(cont > 2):
                break
        d+=1
    if(cont == 2):
        print("el numero ", i , "es primo")




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

#se optimizo en las iteracion que se producian en el bucle while, si el cont era mayor a 2 ya no servia de nada continuar verificando.


# In[57]:




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:
i=100
while(i<=300):
    if(i % 12 != 0):
        i+=1
        continue
    print(i)
    i+=1
    



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:
for i in range(2,31):
    cont = 0
    d=1
    while(d<=i):
        if(i % d == 0):
            cont+=1
            if(cont > 2):
                break
        d+=1
    if(cont == 2):
        print("el numero ", i , "es primo, presione Enter para continuar")
        input()

    


# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6


# In[75]:
i=100
while(i<=300):
    if (i % 3 == 0 & i % 6 == 0):
        print("El primer multipli de 3 y 6 entre 100 y 300 es: ", i)
        break
    i+=1


# %%
