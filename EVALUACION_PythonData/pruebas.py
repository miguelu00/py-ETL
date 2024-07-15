# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 09:32:59 2024

@author: miguel.fuentes.vale
"""

import requests as req
import zipfile as zipf
import pandas as pd
import logging as logg

#Librerias extra que también uso:
import os
import io

## Primero, obtendremos de la API el .zip requerido
### Para ello, usaremos una petición GET (y aprovecho una función que ya tenía guardada del Día 9 (uso de APIs))

def conectarYComprobar(url: str, parm: dict=None, headrs: dict=None):
    '''
    Hace una petición GET a la url indicada; devuelve la respuesta del servidor
    y hace print por pantalla del código HTTP devuelto tras hacer
    la petición.
    '''
    if (parm is not None and headrs is not None):
        response = req.get(url, params=parm, headers=headrs)
    elif (parm is not None):
        response = req.get(url, parm)
    else:
        response = req.get(url)
    print(f"Codigo de respuesta para {url}: {response.status_code}")
    return response

# La API es la siguiente:<b> https://portal.mineco.gob.es/economiayempresa/EconomiaInformesMacro/Documents/bdsicecsv.zip </b>
api_url = "https://portal.mineco.gob.es/economiayempresa/EconomiaInformesMacro/Documents/bdsicecsv.zip"
resp = conectarYComprobar(api_url)

from unidecode import unidecode
print("código".isascii())
unidecod = unidecode("código")
print(unidecod)

print(float("3,22444".replace(",", ".")))
