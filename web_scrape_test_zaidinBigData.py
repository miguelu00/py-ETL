# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Script para comprobar si en la página web de Zaidín-Vergeles
(con las palabras clave "Big+Data") hay novedades.
Esto se comprueba de manera superficial, comparando la fecha actual
con la fecha que ponga en cualquier <td> con la clase CSS "price-col".

[Así es como en la página se almacena la fecha de la última publicación,
 en el momento de la realización de este script].
 Que lo disfrute el Aguayo, aplausosss aplausos
"""

import tkinter as tk
from tkinter import messagebox
import requests as req
import datetime as dtime, time
import locale
locale.setlocale(locale.LC_TIME, 'es_ES')

#1. Conectar a la página web, y sacar su contenido HTML
def conectarYComprobar(url: str, parm: dict=None, headrs: dict=None):
    '''
    Hace una petición GET a la url indicada; devuelve la respuesta del servidor
    y hace print por pantalla del código HTTP devuelto tras hacer
    la petición.
    '''
    if (parm is not None and headrs is not None):
        response = req.get(url, params=parm, headers=headrs, verify=False)
    elif (parm is not None):
        response = req.get(url, parm, verify=False)
    else:
        response = req.get(url, verify=False)
    print(f"Codigo de respuesta para {url}: {response.status_code}")
    return response

resp = conectarYComprobar("https://www.ieszaidinvergeles.org/blog/?s=big+data")

#guardar como texto el HTML (solo la parte con body ya que solo queremos buscar ahi actualizaciones)
respuesta = resp.text

#2. Comprobar si hay una entrada en el html con la fecha actual del sistema

#antes, se formatea así la fecha actual para adaptarse a la que se pone en la página web
fecha_actual = dtime.datetime.now()
formateada = fecha_actual.strftime("%d, %b %Y")
formateada = formateada.replace(".", "")

particion = formateada.split(" ")
particion[1] = particion[1].capitalize()
fech_formateada = " ".join(particion)

print(fech_formateada)

# Crear una instancia de la ventana principal
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

if (respuesta.count('<td class="price-col">{fech_formateada}</td>') >= 1):
    messagebox.showinfo("NOVEDADES!", "HAY NOTICIAS NUEVAS PARA BIG DATA!! Chequea la página:\n" +
          "https://www.ieszaidinvergeles.org/blog/?s=big+data")
    print("HAY NOTICIAS NUEVAS PARA BIG DATA!! Chequea la página:\n" +
          "https://www.ieszaidinvergeles.org/blog/?s=big+data")
else:
    print("Nada nuevo por aquí...")
    messagebox.showinfo("Nada nuevo...", "Nada nuevo por aqui...")

# Cerrar la ventana principal
root.destroy()