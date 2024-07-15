# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:55:23 2024

@author: miguel.fuentes.vale
"""

## EJERCICIO 1 ##

# ¿Cual es la diferencia entre os.path.join() y os.path.abspath?

'''
    Os.path.abspath devuelve la ruta absoluta del fichero al que estemos apuntando, a
    partir de una ruta ya especificada por parámetro.
    
    Sin embargo, path.join() busca y trata de unir una o varias rutas de ficheros que 
    hayamos especificado, y permite trabajar con subcarpetas.
'''

# ¿Cuál es el propósito del módulo os? Da ejemplos de su uso.

'''
    En python, su propósito es trabajar con nombres de fichero
    y ficheros del sistema, cuyo tratamiento puede variar
    según el sistema operativo en uso (de ahí el nombre os, supongo)
'''

# ¿Cuál es el propósito del módulo logging? ¿Cómo se usa?

'''
    El módulo logging se usa para dar al usuario información sobre la ejecución
    de programas Python. Se puede usar para reportar errores, cambios
    en variables y ficheros, entre muchos otros...
    
    Se puede usar con cualquier librería e implementación de clases,
    así que sería muy flexible
'''


## EJERCICIO 2 ##

import random as rng
frutas = ['manzana', 'plátano', 'cereza', 'mango', 'piña', 'fresa']

print(frutas[rng.Random().randint(0, len(frutas)-1)])

# Mezcla la lista y devuelve las dos primeras frutas de la lista mezclada
rng.shuffle(frutas)
print(frutas[::-1])

# Saca una muestra de 3 frutas para decorar el batido
muestra = frutas[rng.Random().randint(0, len(frutas)-1)], frutas[rng.Random().randint(0, len(frutas)-1)], frutas[rng.Random().randint(0, len(frutas)-1)]

# Usa itertools para generar todas las combinaciones posibles de tres frutas.
import itertools

combis = list(itertools.combinations(frutas, 3))
itertools.
print(combis)


## EJERCICIO 3 ##
import os, json

# Usa os.listdir para obtener todos los archivos en el directorio actual.
listadoDir = os.listdir(os.getcwd())
print(listadoDir)

print(json.dumps(obj=listadoDir)) # usando json por diversion

# Abre cada archivo TXT y lee su contenido.
def leerFichero(nombreFichero):
    output = ""
    with open(nombreFichero, "r") as f:
        output += f.read + "\n"
    
    return output

for fichero in listadoDir:
    print(leerFichero(fichero) + "\n" if fichero.lower().endswith(".txt") else "")

# o usando list comprehension...
listadoCondicional = [f for f in listadoDir if f.lower().endswith(".txt")]


# Leer todo el listado de ficheros; solo sacar por pantalla las líneas con palabras que cumplan la expresión reg.
import re

patron = r'\b\w+!\s?' # matchear solamente las PALABRAS (\b) que incluyan CUALQUIER CARACTER 1+ veces (\w+) y termine con "!" o con un espacio("\s") y "!" y otro espacio
listadoDir = os.listdir(os.getcwd())
listadoCondicional = [f for f in listadoDir if f.lower().endswith(".txt")]

def leerFicheroRegex(nombreFichero, expresionReg):
    output = ""
    with open(nombreFichero, "r") as f:
        #lineas_Sep = str(f.read()).split("\n")
        lineas_Sep = f.readlines()
        for line in lineas_Sep:
            output += line if re.findall(patron, line) else "\n" # solo sacar lineas que cumplan con el patron

    return output

print("Lineas en ficheros que coincidan con la expresión regular (palabras acabadas en '!')")
for fichero in listadoCondicional:
    leido = leerFicheroRegex(fichero, patron)
    print(leido if leido!="" else "") # condicional para evitar vacios


## EJERCICIO 4 - logging ##

import logging as log

t4_logger = log.getLogger("t4_logger")

# Configurar el modo del logger a 'DEBUG' y los manejadores de ficheros que almacenarán los logs
t4_logger.setLevel(log.DEBUG)


# Dar formato a los fileHandler's mediante un objeto logging.Formatter
formateador = log.Formatter('%(asctime)s - %(levelname)s - %(message)s')


fhand_Warning = log.FileHandler("t4_warning.log")
fhand_Critical = log.FileHandler("t4_critical.log")

fhand_Warning.setFormatter(formateador)
fhand_Critical.setFormatter(formateador)

# Especificar nivel de los fileHandler's
fhand_Warning.setLevel(log.WARNING)
fhand_Critical.setLevel(log.CRITICAL)
# Aplicar el fileHandler a los logger's
t4_logger.addHandler(fhand_Critical)
t4_logger.addHandler(fhand_Warning)


try:
    t4_logger.log(log.CRITICAL, 32)
    t4_logger.warning("Esto se logeará, pero no loggear de autenticarse, loguear de reportar en un fichero este texto")
except:
    t4_logger.log(log.FATAL, "HA OCURRIDO UN ERROR IRRECUPERABLE AL CREAR EL LOG!")



## EXCEPCIONES ##

# ¿Cuál es el propósito de la declaración ‘raise’?
'''
    RAISE se usa para lanzar una excepción, predeterminada o personalizada,
    y hace que se pare el programa.
'''

# ¿Cómo puedes crear y usar una excepción personalizada?
'''
    Se puede crear una clase que herede de la clase Exception,
    en su constructor, podemos llamar al método especial super()
    con el fin de cambiar el mensaje o su constructor por defecto
'''

# Uso de la declaración ‘assert’
'''
    Assert se debe usar para recoger un booleano en función de
    que se cumpla la condición que indiquemos dentro de la llamada
    al método.
'''

## EJERCICIO 2 ##

# Implementa un programa que solicite al usuario que ingrese un número entero. 
#  Debes asegurar que el usuario ingresa un valor válido. Si el usuario 
#   ingresa un valor no numérico, se mostrará un mensaje de error y se le pedirá 
#    que lo intente nuevamente.
#
# Configura y utiliza un logger para ello

import logging as log

t4_logger = log.getLogger("t4_logger")

# Configurar el modo del logger a 'DEBUG' y los manejadores de ficheros que almacenarán los logs
t4_logger.setLevel(log.DEBUG)


# Dar formato a los fileHandler's mediante un objeto logging.Formatter
formateador = log.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fHandler = log.FileHandler(filename="ficheros/Ej3_datos.txt")
fHandler.setFormatter(formateador)
t4_logger.addHandler(fHandler)
t4_logger.setLevel(log.ERROR)

while (True):
    try:
        print("Introduzca un número entero:")
        numero = int(input())
        break
    except ValueError: #TODO - Buscar tipos de excepciones en python
        print("ERROR. Introduzca un entero VÁLIDO!!")

print(numero)


# Implementa una función para leer numeros de un fichero de texto
import re
import logging as log

t5_logger = log.getLogger("t5_logger")

# Dar formato a los fileHandler's mediante un objeto logging.Formatter
formateador = log.Formatter('%(levelname)s - %(asctime)s - %(message)s')

fHandler = log.FileHandler(filename="ficheros/data_analisis.log")
fHandler.setFormatter(formateador)
# Configurar el modo del logger a 'DEBUG' (todo) y los manejadores de ficheros que almacenarán los logs
t5_logger.addHandler(fHandler)
t5_logger.setLevel(log.DEBUG)

class InvalidDataError(Exception):
    pass


#print(float("3.20")) # Prueba por mi cuenta

def leerNumeros(nombreFichero):
    lineasFiltro = ""
    try:
        with open(nombreFichero, "r") as lectorF:
            lineasFiltro = lectorF.read()
            if (len(re.findall(r'[A-Za-z]+', lineasFiltro)) > 0):
                raise InvalidDataError
    except:
        print("ERROR! Se han leído datos no numéricos en el fichero!")
        t5_logger.error(msg="INVALID DATA ERROR!")
    else:
        # Si no ha saltado error, loggear y devolver lista de lineas
        t5_logger.log(level=log.INFO, msg="Fichero leído correctamente! :D")
        return lineasFiltro
    finally:
        #Aquí se cerraría el fichero abierto para lectura. Pero no es necesario
        print("Acabado. Output:")

print(leerNumeros("ficheros/Ej3_datos.txt"))

'''
    #Filtrar el list para sacar solo datos numéricos
    lineasFiltro = [ln for ln in lineas if re.match(r'^[0-9]+.?[0-9]*$', ln)]
'''

## Ejercicios CONCURRENCIA ##

# 1. ¿Qué es el Global Interpreter Lock (GIL)?
'''
    Es el sistema que se utiliza para evitar que más de un
    hilo este en ejecución a la vez
'''

# 2, Diferencias entre multithreading y multiprocessing
'''
    Multithreading es cuando una aplicación pone en marcha diversos
    hilos para repartir tareas específicas a cada uno de ellos,
    de esta manera se divide el tiempo en ejecutar cada uno.
    En Python, cada hilo se ejecuta en el mismo hilo principal,
    simulando el multihilado tradicional de otras aplicaciones.
    
    Multiprocessing por otro lado, es la práctica de usar un
    intérprete para cada hilo de procesamiento que lancemos.
    De esta manera, se soluciona el hecho de que realmente
    Python con sus librerías por defecto no pueden usar 
    multihilado correctamente
'''

## EJERCICIO 1 ##
import os
import threading

class FicheroNoValidoException(Exception):
    pass

def lector_archivos_multihilo(listadoRutasF):
    #Comprobar si hay algun directorio/nombre de fichero no válido
    listadoNoFicheros = [f for f in listadoRutasF if os.path.isfile(f) != True]
    if (len(listadoNoFicheros) > 0):
        raise FicheroNoValidoException
    
    #Iniciar, guardar, y esperar a que terminen cada hilo que esté leyendo los ficheros
    listaHilos = []
    for elemento in listadoRutasF:
        hilo = threading.Thread(target=leer_fichero, args={elemento,})
        listaHilos.append(hilo)
        hilo.start()
    
    for hilado in listaHilos:
        hilado.join()

def leer_fichero(rutaFichero):
    lectura = ""
    with open(rutaFichero, "r") as f:
        lectura = f.read()
        print("Terminado")
    return lectura

if __name__ == "__main__":
    listaRutas = ["Nuevo documento de texto.txt", "t4_critical.log", "holanovalido"]
    lector_archivos_multihilo(listaRutas)


## EJERCICIO 3 ##

import datetime as dtime
import multiprocessing

NUM_PROCESOS = 3
ITERACIONES = 3

NUM_OBJETIVO = 100000000

def suma_enesima(n):
    
    suma_total = sum(range(1+n))
    return print("Suma: " + str(suma_total))

def sumaN_sin_multiprocessing():
    print("Iniciando función sin multiprocessing.")
    for _ in range(ITERACIONES):
        suma_enesima(NUM_OBJETIVO)

def sumaN_multiproceso():
    #Guardar e iniciar los hilos de un array
    hilos = []
    
    for _ in range(1, NUM_PROCESOS):
        hilos.append(multiprocessing.Process(target=suma_enesima, args={NUM_OBJETIVO,}))
    
    #Igual que anteriormente, iniciar cada proceso y esperar a que terminen de ejecutarse, uno a uno
    for proc in hilos:
        proc.start()
    
    for proc in hilos:
        proc.join()

def main():
    # Marcar los tiempso Sin multiproceso y con multi
    print("Sumatoria sin multiproceso")
    inicio = dtime.datetime.now()
    sumaN_sin_multiprocessing()
    print("Ha tardado: " + str(dtime.datetime.now() - inicio))

    print("Sumatoria con multiprocesado:")
    inicio = dtime.datetime.now()
    sumaN_multiproceso()
    print("Ha tardado: " + str(dtime.datetime.now() - inicio))


if (__name__ == "__main__"):
    main()