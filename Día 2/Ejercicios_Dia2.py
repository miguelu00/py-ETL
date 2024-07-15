# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:12:25 2024

@author: miguel.fuentes.vale

EJERCICIOS Día 2 -- Formación PYTHON Nter
"""

## EJERCICIO 1 ##
# ¿Qué es un decorador y cómo se utiliza?
'''
    Se usan para pasar como argumentos de funciones otras funciones; se usan
    con el fin de extender la utilidad de una función ya creada agregando
    variaciones en su interior.
    
    Para usarlos, simplemente se debe colocar un @[metodo_decorador] delante del nombre de la
    función o método al que queramos extender funcionalidad. El metodo_decorador que llamemos
    será el que se ejecute antes y después de la ejecución del método decorado (donde se
    agregó el @)
'''

# ¿Qué es una función lambda?
'''
    Se trata de una función anónima, usada sobre todo como ayuda para la programación
    con funciones de orden superior. 
    Son capaces de, en una sola línea, recoger y transformar datos para su uso en la
    misma línea.
'''

# ¿Qué es un docstring?
'''
    Como este mismo comentario, son maneras de documentar métodos, clases y funciones
    (argumentos y uso de estas) en Python.
    Para crearlos, basta con insertar un comentario multilinea indentado de 
    Python (usando '' ó ""), indentado en la siguiente línea del nombre del 
    método / clase / función a documentar.
'''

# Explica el concepto de funciones de primera clase
'''
    Las funciones de orden superior son aquellas que se pueden pasar como argumento
    a otras funciones, variables... 
    Normalmente como argumentos reciben una expresión booleana o una colección/arreglo.
    Algunos ejemplos son .filter() .map() .reduce() ... y se suelen llamar
    de forma encadenada a otras funciones o métodos, ya que muchas las
    devuelven.
'''

## EJERCICIO 2 ##

'''
    Define una función que recoja un String y busque anagramas compatibles con ese string
    en una coleccion/contenedor, devolverlos en otro contenedor nuevo.
'''

# Primer intento
'''
def buscar_anagramas(palabra_orig, coleccion):
    output = []
    for palabra in coleccion:
        palabra.filter(palabra.matches() => )
'''

# Segundo intento, usado internet
def buscar_anagramas(palabra_orig, coleccion):
    res = False
    output = []
    for palabra in coleccion:
        if (sorted(palabra_orig) == sorted(palabra)):
            output.append(palabra);
            res = True
    
    if (res == False):
        print("No existen anagramas para la palabra introducida en esa coleccion!")
    else:
        print(output)
        
#Probar la funcion
pal = "holao"
arr = ["olaho", "holoa", "perro", "holup"]

buscar_anagramas(pal, arr)



## EJERCICIO 3 ## - Funciones lambda

# 1. Calcular el cuadrado de un número
exp = lambda a: a*a

print(str(exp(2))) # 4

# 2. Define una función lambda que devuelva True si el cuadrado de un número
#    es mayor que 999 si no devuelve False.

is_higher = lambda n: (n*n) > 999

print(is_higher(33))

# 3. Implementa una función en Python que invierta el orden de las palabras 
#    en una cadena dada, eliminando cualquier espacio adicional:

# TODO - arreglar esta lambda
contar_espacios = lambda palabra: int(str(palabra).strip().count(" "))
print(contar_espacios("hola  alo "))

strings = ["locura", "el cielo es azul", "  hola mundo  ", "un buen   ejemplo"]

def invertir_arrCadenas(strings):
    '''
    Invertirá un array con cadenas, eliminando los espacios extra que encuentre.
    
    Parameters
    ----------
    strings : LIST[str]
        DESCRIPTION.

    Returns
    -------
    salida : LIST[str]
        DESCRIPTION.

    '''
    salida = []
    for frase in strings:
        split = frase.strip().split(" ") #Split ya devuelve los espacios sin contenido...
        split.reverse()
        salida.append(" ".join(filter(lambda stri: stri != "", split))) #...por lo que solo faltaría filtrar aqui
    return salida


print(invertir_arrCadenas(strings))



## POO - Ejercicio 1 ##

# ¿Cuál es el propósito de la declaración if __name__ == "__main__":?
'''
    Creo que quiere comprobar si el meta-atributo de la clase llamada tiene
    como nombre main; esto es, que apunte al método main() de una clase.
    
    solución:
    Comprueba que el nombre de un módulo de python que se este ejecutando
    pertenece al módulo principal ejecutandose actualmente
    Cuando esto ocurre, el __name__ del módulo pasa a llamarse "(__main__)"
'''
# ¿Para qué sirve la función super() en Python?
'''
    En el constructor de una clase que hereda de otra, llamará a la clase
    padre, y desde este podremos llamar a otros métodos de dicho padre.
'''
# Describe el uso del decorador @staticmethod
'''
    Define que una función/método en una clase es estático, es decir, que 
    puede llamarse sin necesidad de crear una nueva instancia de la clase.
'''


## POO - EJERCICIO 2 ##

# Cree una clase Vehicle que reciba el nombre, velocidad máxima y el kilometraje.

class Vehicle:
    nombre = ""
    velMax = 90
    kms = 100000
    owner = ""

    def __init__(self, nombre, velMax, kms):
        self.nombre = nombre
        self.velMax = velMax
        self.kms = kms

    #Crea un método a Vehicle para imprimir por pantalla el nombre y la capacidad ( pasada por parametro )
    def mostrarCapacidad(self, capacidad):
        print(f"La capacidad del {self.nombre} es de {capacidad}")


# Cree una clase Bus que herede todos los métodos y variables de Vehicle.
class Bus(Vehicle):
    pass
    def mostrarCapacidad(capacidad = 50):
        print(f"La capacidad del {super().nombre} es de {capacidad}")


## EJERCICIO 3 ##

'''
    En este ejercicio, deberás implementar una clase Dni en Python que 
    represente un Documento Nacional de Identidad (DNI) español. 
    
    La clase debe validar el número del DNI y calcular su letra correspondiente:
'''

class DNI:
    
    numero = 12345678
    letra = "#" #por defecto, una almohadilla
    
    def __init__(self, num):
        self.numero = num
        self.letra = self.__calcular_letra() if self.__validarnumero(self.numero) == True else "#"
    
    
    def __calcular_letra(self):
        '''
        
        Devuelve la letra para el numero introducido en esta clase DNI
        Returns
        -------
        str

        '''
        letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
        return letras[self.numero%23]
    
    def __validarnumero(self, numero):
        if (len(str(numero)) == 8 and str(numero).isdigit()):
            return True
        else:
            self.numero = 00000000
            return False
    
    def __getNumero__(self):
        return self.numero
    

    def __setnumero__(self, num):
        self.numero = num

    def __getletra__(self):
        return self.letra
        


dni = DNI(20888746)

print(f"{dni.__getNumero__()}{dni.__getletra__()}")


## EJERCICIO 4 ##
from dataclasses import dataclass

@dataclass
class Empleado:
    
    nombre: str
    edad: int
    ciudad: str
    empresa: str = "Nter Tech Services"
    
    @staticmethod
    def calcular_salario(salario_base, hor_extras, coste_horas):
        return salario_base + (hor_extras * coste_horas)
    
    @classmethod
    def obtener_nombre_empresa(self):
        return self.empresa
    
    def __str__(self):
        return f"Empleado de {self.empresa}: {self.nombre} - {self.edad} años - {self.ciudad}"
    
print(Empleado.obtener_nombre_empresa())
# Crea una instancia e la clase Empleado y muestra su representación

emple = Empleado("GoofyGoober", 99, "Frankfurt")

print(Empleado.calcular_salario(1200, 20, 10))
print(emple)

'''
    Investiga sobre los slots y comenta este código
'''
class Dog:
    __slots__ = ["nombre", "edad"]

dog = Dog()
dog.name = "Bobby"
dog.edad = 3
dog.genero = "m"

'''
    Este código dará error, ya que no se puede acceder al nombre del obj. Dog
    con la propiedad "name"
'''



## EJERCICIO 6 - FICHEROS ##

# Explica el propósito de la declaración 'with'
'''
    Tiene como fin darle contexto a la llamada de un método, en concreto le da
    instrucciones iniciales y finales.
    
    Normalmente, se escribe antes de la palabra 'as', que especificará a qué
    variable agregar los cambios de dichas instrucciones.
    Por ejemplo, en ficheros se usa así:
        
        with open("fichero.txt", "r") as f:
            print(f.read())
'''

# ¿Cómo puedes realizar operaciones de entrada/salida de archivos en modo binario?
'''
    
'''
with open("AA instrucciones.txt", "r") as f:
    print(f.read())
# ¿Cómo serializas y deserializas objetos en Python?
'''
    
'''
import json

# EJEMPLO - Serializar/deserializar un objeto dict con varios tipos de dato
simple = dict(
        int_list=[1,2,3],
        text="string",
        number=3.44,
        boolean=True,
        none=None
)

#Abrir un fichero, para almacenar dicho dict usando formato json
with open("fichero_out.json", "w") as f:
    f.write(json.dumps(simple, indent=4))



## EJERCICIO 2 - TXT ##

#Escribir linea 1 en primerFichero.txt

linea1 = "Es mi primera linea."
linea2 = "Es mi segunda linea."
linea3 = "Es mi tercera linea."
linea4 = "Es el final del fichero!"

with open("primerFichero.txt", "w") as f:
    f.write(linea1)

# Crear un fichero vacío
with open("segundoFichero.txt", "w") as f:
    f.write("")

# Escribir linea2, 3 y 4 en el segundoFichero.txt, cada una en una línea
lineas = [linea2, linea3, linea4]

with open("segundoFichero.txt", "w") as f:
    for linea in lineas:
        f.write(linea + "\n")
        
with open("primerFichero.txt", "r") as f:
    linea = f.read()
    with open("segundoFichero.txt", "a") as fSeg:
        fSeg.write(linea)


## EJERCICIO 3 - CSV ##
# Lee el fichero estudiantes.csv, extrae y muestra la cabecera; convierte cada fila en un dict (la cabecera serán las claves);
#  muestra el fichero; abre el fichero y usa csv.DictReader para leerlo; muestra la info. de cada fila en un formato legible.
import csv
fichero = "estudiantes.csv"

# También habra que usar with
cabecera = ""
with open(fichero, "r") as lector_f:
    lectura = csv.reader(lector_f, delimiter=",") # skipinitialspace=True en la llamada a reader, saltaría el espacio despues del limitador
    for line in lectura:
        cabecera = line
        break

print(cabecera)
# Se puede pasar un string representando una cabecera, directamente a LIST
#  (si tiene el formato correcto)
lista_cabecera = list(cabecera)

dict_lineas2 = {}
with open(fichero, "r") as lector_f:
    # introducimos como cabecera la recogida en el List de arriba
    dict_lineas2 = csv.DictReader(lector_f, fieldnames=cabecera)
    print(dict_lineas2)



## EJERCICIO 4 - JSON ##

# Carga los datos de los productos existentes desde el archivo “productos.json”

import json

class Producto:
    
    nombreFichero = "productos.json"
    ficheroInventario = "inventario.json"
    
    def __init__(self):
        self.nombre = ""
        self.cantidad = 0
        self.precio = 10
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @staticmethod
    def __setNombreFichero(self, nombre):
        self.nombre = nombre
        
    @staticmethod
    def agregar_producto(nombre, cantidad, precio, nombreFichero):
        arrDatos = list(json.loads(nombreFichero))
        aux = {
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio
        }
        arrDatos.append(aux)
        jsonStr = json.dumps(arrDatos) # skipkeys se saltará aquellas claves cuyos tipos de dato saquen un error
        # Sobrescribir el fichero de datos con el array JSON recogido
        with open(nombreFichero, "w") as f:
            f.write(jsonStr)
    
    # JSON.DUMPS --> Recoge un DICT y devuelve un JSON string
    @staticmethod
    def escribir_fichero(inventario, ficheroInventario):
        jsonStr = json.dumps(inventario, indent=4)
        with open(ficheroInventario, "w") as f:
            f.write(jsonStr)
    
    # JSON.LOADS -> Recoge un JSON String y devuelve DICT o LIST, dependiendo de los datos
    @staticmethod
    def leer_FicheroProductos(nombreFichero):
        jsonStr = ""
        with open(nombreFichero, "r") as f:
            jsonStr += f.read()
        return json.loads(jsonStr)

prods = Producto.leer_FicheroProductos("productos.json")
print(prods)

Producto.escribir_fichero(prods, "inventario.txt")