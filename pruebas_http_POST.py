# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 12:32:42 2024

@author: miguel.fuentes.vale
"""
import requests

#Conseguir datos de csv
def conectarYComprobar(url: str, parm: dict=None, headrs: dict=None):
    '''
    Hace una petición GET a la url indicada; devuelve la respuesta del servidor
    y hace print por pantalla del código HTTP devuelto tras hacer
    la petición.
    '''
    response = requests.get(url, params=parm, headers=headrs, verify=False)
    print(f"Código de respuesta de la petición: {response.status_code}")
    return response

def POST_conectarYComprobar(url: str, parm: dict=None, headrs: dict=None):
    '''
    
    Returns
    -------
    El objeto requests resultante tras hacer una petición POST

    '''
    
    res = requests.post(url, params=parm, headers=headrs, verify=False)
    print(f"Código de respuesta de la petición: {res.status_code}")
    return res

http_satelites = POST_conectarYComprobar("http://services-uswest2.sentinel-hub.com/api", parm={"input.data.type": "landsat-ot-l1"})
print(http_satelites)