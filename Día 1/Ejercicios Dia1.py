# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 11:58:31 2024

@author: miguel.fuentes.vale
"""
import math
## EJERCICIO 1 ## 

# 1. Explica el concepto de tipado dinámico en Python
'''
    A cada variable se le asigna un tipo de dato implícito,
    dependiendo del valor que esta variable tenga.
    
    Es implícito en este aspecto, pero fuertemente tipado
    ya que Python lanza un error cuando se intenta realizar
    una operación propia de un tipo de dato específico sobre otro
    no compatible.
'''

# 2. ¿Cuáles son los principales tipos de datos en Python?
'''
    int
    float
    bool
    str
    
    set
    tuple
    dict
'''

# 3. Describe la diferencia entre '==' e 'is'

'''
    Is es un comparador para punteros de memoria,
    mientras que == es un comparador general.
'''

## EJERCICIO 2 ## Operaciones con números enteros y complejos
# 4. Define dos numeros de tipo complejo
comp1 = 3 * 2j
comp2 = 1 + 1j

# 5. Muestra por pantalla la parte real del primer número definido en el punto 1.
print(str(comp1.real))

# 6. Muestra por pantalla la parte imaginaria del segundo ''' '' '''
print(str(comp2.imag))

# 7. Define la variable f con el resultado de la multiplicación de los dos números complejos
f = comp1 * comp2

# 8. Define una variable num con un número entero
num = 33

# 9. Utiliza el operador AND bit a bit para verificar si el número es par.
print(f"Num es par: {num&1 == 0}")


## EJERCICIO 3 ## Operaciones con STRING
# 10. Define una variable con un string con valor "  E.T., telefono, mi casa  "
string = "  E.T., telefono, mi casa  "

# 11. Muestra la longitud del string
print(len(string))

# 12. Elimina los caracteres con espacio en blanco al comienzo y al final
string = string.strip()
print(string)

# 13. Muestra el primer y penúltimo caracter del string
print(f"{string[0]} || {string[-2]}" )

# 14. Convierte la cadena a mayúsculas
string = string.upper()

# 15. Busca la posicion de la subcadena "mi" en la cadena
posMi = string.find("mi")
print (f"'mi' esta en la posición {posMi}")

# 16. Reemplaza la palabra 'casa' por 'coche'
string = string.lower().replace("casa", "coche")
print(string)

# 17. Divide la cadena en una lista de subcadenas utilizando la coma como delimitador
listaSubstr = string.split(",")
print(listaSubstr)

## EJERCICIO 4 ## F-STRINGS

#1. Incorpora variables en un string
nombre = "Alicia"
edad = 20

print(f"Hola! Mi nombre es {nombre} y tengo {edad} años")

#2. Operaciones aritméticas
a = 33
b = 10

print(f"Treinta y tres más diez es {a + b}")

#3. Formatea números
numPi = math.pi
print(str(numPi))
print(f"Pi redondeado es {numPi:.2f}")

# 4. Incluye expresiones condicionales
score = 55
print (f"Tu calificación es {'Aprobado' if score >= 50 else 'Suspenso'}")


'''
    APARTADO 2)
'''

## EJERCICIO 1 ##

# 1. Explica las diferencias entre una lista y una tupla
'''
    Una tupla es inmutable, mientras que en una lista podemos agregar,
    modificar y eliminar elementos como necesitemos.
    Una tupla es más eficiente en memoria debido a esto.
'''

# 2. ¿Como se puede invertir una lista en Python?

'''
    Se puede hacer mediante el método reverse()
'''
lista = [3, 2, 1];
lista.reverse()
print(lista)

# 3. ¿Cuál es la diferencia entre los métodos append y extend para listas?

'''
    A extend() solo se le puede pasar un elemento ITERABLE (es decir, otra lista, tupla, dict...)
    mientras que a Append() se le puede pasar también números sueltos u otros datos primitivos
    de Python.
'''

## EJERCICIO 2 ##

# Eliminar los elementos duplicados de una lista, ordenar los resultantes y mostrar el número de elementos únicos
## junto a la lista ordenada
nums = [1, 5, 5, 2, 1]
nums.sort()
nums_unicos = []
for i in nums:
    if i not in nums_unicos:
        nums_unicos.append(i)

print(f"Número de elementos no duplicados: {len(nums_unicos)} -> {nums_unicos}")

# Crea otra lista num2 con los valores [1, 1, 2]
## Encuentra los elementos que aparezcan en ambas listas y los elementos de la primera lista que no
### se encuentran en la segunda.

num2 = [1, 1, 2]

#Convertir a sets las dos colecciones
nums = set(nums)
num2 = set(num2)

#Encontrar los elementos en ambas listas y los discriminados de la segunda
numDiffs = nums.difference(num2) #discriminados
num4 = nums.intersection(num2) #coincidentes
num4 = nums.union(numDiffs) #Union de ambos sets; sobrescribe el set 'num4'
#num4.add(num3)

print(nums)
print(num2)
print(num4)



# 2. Para realizar este ejercicio tienes un diccionario con las claves: coche, motocicleta, camión y los
## valores 10, 20 y 30 respectivamente

diccionario_dict = dict(
     coche = 10,
     motocicleta = 20,
     camión = 30
)

#Usando sintaxis normal
diccionario = {
    "coche": 10,
    "motocicleta": 20,
    "camión": 30    
}

diccionario_zip = zip(
    ("coche", "motocicleta", "camión"),
    (10, 20, 30)
)

print(diccionario_dict)
print(diccionario)
print(list(diccionario_zip)) #hay que pasarlo a zip antes de seguir


# Muestra los valores y las claves del diccionario
print(diccionario_dict.values())
print(diccionario_dict.keys())

# Muestra el valor para la clave 'coche'
print(diccionario_dict["coche"])

# Agrega al diccionario ['avion': 100]
diccionario_dict["avion"] = 100

print("\n")
print(diccionario_dict.items())
print("\n")

## EJERCICIO 3 ##

# 1. ¿Cual es el propósito de la función 'enumerate' en Python?

'''
    Se usa enumerate para crear un elemento de tipo 'enum' en
    Python. Este puede recoger un arreglo (set, list, dict...)
    y convertirlo a este tipo de elemento.
'''

en = enumerate(diccionario)

print(list(en))

# 2. Explica el concepto de list comprehensions o comprensiones de listas
'''
    Es la capacidad de insertar colecciones dentro de otras en Python,
    pero de manera dinámica a través de estructuras de control.
    
    Normalmente, se realiza con un constructor de colección, y dentro
    se introduce una expresión que si se cumple, insertará el valor
    dentro de la colección que se está creando.
'''


# Ejercicio 2 - PALINDROMOS
words = ["Ana", "12321", "Una manzana", "radar", "No es palíndromo"]

words2 = [word.lower() for word in words]
words2 = [word.strip() for word in words2]

#print(words2[2][::-1]) #test para sacar la tercera palabra en orden invertido

palindromos = [word for word in words2 if word[::-1] == word]

print(palindromos)


# Ejercicio 3 - 

palabra_ejemplo = "marsupilami"

#Crear diccionario y recorrer letra a letra la palabra de ejemplo

#Especificar numero de ocurrencias para cada letra en contador1 (diccionario)
contador1 = dict()
for i in palabra_ejemplo:
    if i not in contador1.keys():
        contador1[i] = 1
    else:
        contador1[i] += 1
        
# Ordenar los valores del contador1
print(contador1)
letras_abc = list(contador1.values())
letras_abc.sort()
print(letras_abc)

#Usando defaultdict
from collections import defaultdict

palabra_ej2 = "manzaneo"
#Valor por defecto: string

#A diferencia del anterior, defaultdict no dará error si intentamos acceder a una clave inexistente
contador2 = defaultdict(int)
for i in palabra_ej2:
    contador2[i] += 1
    
#Ordenar los valores del contador2
letras_abc2 = list(contador2.values())
letras_abc2.sort()

print(letras_abc2)


#Usando Counter -- simplemente será pasar la palabra en formato de list (splitteada)
from collections import Counter
palabra_ej3 = "cocoliso"


contador3 = Counter(palabra_ej3)

#Mostrar por pantalla las letras, ordenadas por mayor num. de ocurrencias
print(contador3.most_common())

lista_claves = list(contador3.keys())
print(lista_claves)
lista_claves = lista_claves.sort()
#Ordenados alfabeticamente
print(lista_claves)

#Solución del pdf, mostrar en orden alfabético
for letra, frecuencia in sorted(contador3.items()):
    print(f"letra: {letra}: {frecuencia}")

from collections import deque
# Ejercicio 4


s = "()()()()()(["
s1 = "())()(){})()[]["

deq1 = deque(s)
deq2 = deque(s1)

#Define un diccionario brackets para mapear los paréntesis de apertura con sus cierres correspondientes
brackets = {"(": ")", "{": "}", "[": "]"}
balancing = {}

#Comprobar que ambos deques tienen datos, si tienen ir contando el peso de cada elemento en su interior
if (len(deq1) > 0 and len(deq2) > 0):
    resultado = [brack for brack in deq1 if (brack in brackets.keys() or brack in brackets.values())]
    
    for i in range(len(deq1)):
        if i+1 == len(deq1): # salir del bucle antes de mirar una posición fuera de rango
            break
        if deq1[i] in brackets.keys() and deq1[i+1] in brackets.values():
            if "primero" not in balancing.keys():
                balancing["primero"] = 1
            else:
                balancing["primero"] += 1
                
    #Igual para el deque 2
    for i in range(len(deq2)):
        if i+1 == len(deq2): # salir del bucle antes de mirar una posición fuera de rango
            break
        if deq2[i] in brackets.keys() and deq2[i+1] in brackets.values():
            if "segundo" not in balancing.keys():
                balancing["segundo"] = 1
            else:
                balancing["segundo"] += 1
                
    
    for clave, valor in balancing.items():
        print(f"String {clave}: {valor} paréntesis bien cerrados")
else:
    print("formato del array de brackets no válido!")
    
    
# 1) Recoger elementos del dict -> 2) Ordenarlos con Sorted() -> 3) Recoger el primer elemento (tras ordenarse, será el que tenga mayor valor)
mayor_balance = {}

print(f"El string mejor balanceado es {lista} {max(balancing.values())}")