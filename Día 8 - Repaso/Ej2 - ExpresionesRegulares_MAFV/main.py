# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 11:30:58 2024

Comprobar, desde un fichero CSV y con expresiones regulares, 
que sus datos están bien formalizados en función de la
información que se pretende guardar.

Se guardará la siguiente información sobre usuarios:
    nombre de usuario, 
    un teléfono, 
    un correo electrónico y
    una URL de GitHub

@author: miguel.fuentes.vale
"""
import csv
import re

ficheroCSV = input("Nombre/ruta absoluta del fichero CSV a comprobar:")

dictCsv = []

try:
    with open(ficheroCSV, "r", encoding="UTF-8") as f:
        lectorCsv = csv.DictReader(f) #le paso al DictReader el iterable del fichero abierto
        for linea in lectorCsv:
            dictCsv.append(linea)
        
except OSError as fErr:
    print("ERROR. Fichero no encontrado!")
    print(fErr.strerror)


# A comprobar:
    
    # los nombres de usuario nunca deben empezar con números

    # los teléfonos serán un simbolo +, números de prefijo, y 9 dígitos [0-9]{9}
    
    # correo electrónico: letras/numeros @ servidor . com/es/org/net
    
    # URL de github: https://[usuario].github.com/[repo]
    
#Comprobar si las expresiones coinciden, una por una
for linea in dictCsv:
    razones = []
    if (len(re.findall(r'^[^\d][\w]{2,}$', linea["nombre_usuario"])) == 0):
        razones.append("""Nombre de usuario no válido! No puede contener espacios,
        ni números delante -> """ + linea["nombre_usuario"])
    if (len(re.findall(r'^\+\d{1,3}\d{9}$', linea["telefono"])) == 0):
        razones.append("Número de teléfono no válido! -> " + linea["telefono"])
    if (len(re.findall(r'^([a-z0-9_\.-]+\@[a-z._-]+\.edu)$', linea["correo_electronico"])) == 0):
        razones.append("Uno de los correos electrónicos no tiene un formato válido! -> " + linea["correo_electronico"])
    if (len(re.findall(r'^https://[w{3}.]*github\.com/[\w-]+/*[\w-]*', linea["GitHub_URL"])) == 0):
        razones.append(f"Una de las URL de GitHub no es válida -> {linea['GitHub_URL']}")
    
    for razon in razones:
        print(razon)