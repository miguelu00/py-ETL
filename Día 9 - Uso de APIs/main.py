# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:24:28 2024

# Ejercicio - iTUNES

Aplicación para conectarse a una API de música de iTunes.
Se le deben pasar dos argumentos: un termino de búsqueda, y
un número que represente el límite de resultados a obtener
@author: miguel.fuentes.vale
"""
import sys
import json
import requests as req

#recoger parametros pasados por consola
params_cli = sys.argv

if (len(params_cli) != 3):
    print("No se ha especificado un término de busqueda, y número de resultados")
    sys.exit(2) # salir del programa. Si indicamos otro número que no sea 2, saldra devolviendo un Error

def conectarYComprobar(url: str, parm: dict=None, headrs: dict=None):
    if (parm is not None and headrs is not None):
        response = req.get(url, params=parm, headers=headrs)
    elif (parm is not None):
        response = req.get(url, parm)
    else:
        response = req.get(url)
    print(f"Codigo de respuesta para {url}: {response.status_code}")
    return response

#por defecto, buscar canciones
respuesta = conectarYComprobar("https://itunes.apple.com/search",
                   {"term": params_cli[1], #el parametro con index 0 está "reservado" así que empezamos a comprobamos el indice 1
                    "entity": "song",
                    "media": "music",
                    "limit": params_cli[2]
                    },
                   {"Accept": "application/json"}
                   )

#print(respuesta.json()) #debug

""" ## ejemplo de respuesta JSON:
{'resultCount': 1, 'results': [{'wrapperType': 'track', 'kind': 'song', 
                                'artistId': 1564638435, 'collectionId': 1723854461,
                                'trackId': 1723854462, 'artistName': 'Juan Bravo',
                                'collectionName': 'Autorias del Pasado - EP',
                                'trackName': 'Cantautores del pasado (feat. Juan Aguayo)',
                                'collectionCensoredName': 'Autorias del Pasado - EP',
                                'trackCensoredName': 'Cantautores del pasado (feat. Juan Aguayo)',
                                'artistViewUrl': 'https://music.apple.com/us/artist/juan-bravo/1564638435?uo=4',
                                'collectionViewUrl': 'https://music.apple.com/us/album/cantautores-del-pasado-feat-juan-aguayo/1723854461?i=1723854462&uo=4',
                                'trackViewUrl': 'https://music.apple.com/us/album/cantautores-del-pasado-feat-juan-aguayo/1723854461?i=1723854462&uo=4',
                                'previewUrl': 'https://audio-ssl.itunes.apple.com/itunes-assets/AudioPreview116/v4/49/81/52/49815262-5af6-40ae-c07b-867373a6f596/mzaf_12396238132471444266.plus.aac.p.m4a',
                                'artworkUrl30': 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/9a/9e/11/9a9e1155-2157-9c51-7afb-52f6c73c375b/artwork.jpg/30x30bb.jpg', 'artworkUrl60': 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/9a/9e/11/9a9e1155-2157-9c51-7afb-52f6c73c375b/artwork.jpg/60x60bb.jpg', 'artworkUrl100': 'https://is1-ssl.mzstatic.com/image/thumb/Music116/v4/9a/9e/11/9a9e1155-2157-9c51-7afb-52f6c73c375b/artwork.jpg/100x100bb.jpg', 'collectionPrice': 4.95, 'trackPrice': 0.99, 'releaseDate': '2024-01-02T12:00:00Z',
                                ...
                                'collectionExplicitness': 'notExplicit', 'trackExplicitness': 'notExplicit', 'discCount': 1, 'discNumber': 1, 'trackCount': 5, 'trackNumber': 1, 'trackTimeMillis': 239412, 'country': 'USA', 'currency': 'USD', 'primaryGenreName': 'Urbano latino', 'isStreamable': True}]}
"""


 # Recibir el numero de resultados obtenidos, y el elemento results del JSON
total_resultados = respuesta.json()["resultCount"]
dict_resultado = respuesta.json()["results"]

i = 0
 # Resultados
for result in dict_resultado:
    i += 1
    print(str(i) + ". " + result["artistName"] + " - " + result["trackName"] + " (" + result["releaseDate"][0:4] + ")\nPreview " + str(i) + "\t" + result["previewUrl"])