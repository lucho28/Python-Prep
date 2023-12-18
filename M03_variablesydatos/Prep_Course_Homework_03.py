#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:
a = 28



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:
print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1


# In[8]:

print(type(a))



# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = "Luis Gonzalez"



# 5) Crear una variable que contenga un número complejo

# In[3]:

complejo = 28 + 2j



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

print(type(complejo))



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?


# In[3]:

var1 = "True"
var2 = True

#son distintos tipos de datos

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print("el tipo de dato de var1 es: " , type(var1), "y el de var2 es: " , type(var2))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma = 28 + 5.6



# 11) Realizar una operación de suma de números complejos

# In[2]:

suma_complejo = (14 + 5j) + (28 + 10j)
print(suma_complejo)


# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:

suma_real_complejo = (28 + 5j ) + 3.5
print(suma_real_complejo)



# 13) Realizar una operación de multiplicación

# In[5]:

multiplicar = 25 * 25



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

potencia = 2**8
print(potencia)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

cociente = 27/4
print(cociente)
print(27/4)


# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

cociente_parte_entera = 27//4
print(27//4)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:


cociente_resto=27%4
print(cociente_resto)


# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:


resultado = (cociente_parte_entera + cociente_resto) * 3
print(resultado)


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

nombre_apellido = "luis" + "gonzalez"
print(nombre_apellido)


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

probar_tipo = "2" + 2
#no son del mismo tipo, una es una cadena y el otro es un entero, por eso al sumarla, da error.



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

probar_tipo= int("2") + 2

print(probar_tipo)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

a = float("3,8")
print(a)
#por el separador de decimales, porque el separador seria el punto y no la coma


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

x = 3
x-=1
print(x)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

print(1<<2)
# 1 equivale a 1 * 2**2
print(1<<3)
#equivale a 1 * 2**3 corresponde a desplazar bits a la izquierda en el numero binario.


# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

operacion = 2 + '2'
#en realidad no son del mismo tipo, uno es una cadena (string) y el otro es un entero
print(type('2'))
print(type(2))



# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:


operacion = 2 + int('2')
print(operacion)
# %%
