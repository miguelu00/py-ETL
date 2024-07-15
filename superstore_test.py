# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 14:35:55 2024

@author: miguel.fuentes.vale
"""
import pandas as pd

ruta_superstore = "C:/Users/miguel.fuentes.vale/Documents/Pentaho/superstore.txt"

#Conseguir datos PUROS del fichero SUPERSTORE.TXT
try:
    df_superstore = pd.read_csv(ruta_superstore, sep=";", encoding="ISO-8859-1")
except FileNotFoundError as e:
    print("Fichero SUPERSTORE.TXT no encontrado en la ruta especificada!")
    print(f"Ruta: {e.filename}")

print(df_superstore.columns)

df_superstore["DES_APELLIDOS"] = df_superstore["DES_1_APELLIDO"] + " " + df_superstore["DES_2_APELLIDO"]
#print(df_superstore[["ID_PEDIDO", "ID_FECHA_PEDIDO", "ID_CLIENTE", "DES_NOMBRE", "DES_APELLIDOS"]].head(5))

df_superstore["FECHA_PEDIDO"] = df_superstore["ID_FECHA_PEDIDO"].astype('string')
df_superstore["FECHA_PEDIDO"] = df_superstore["FECHA_PEDIDO"].str[0:4] + "/" + df_superstore["FECHA_PEDIDO"].str[4:6] + "/" + df_superstore["FECHA_PEDIDO"].str[6::]

print(df_superstore[["ID_PEDIDO", "FECHA_PEDIDO", "ID_CLIENTE", "DES_NOMBRE", "DES_APELLIDOS"]].head(5))

df_superstore["FECHA_PEDIDO"] = pd.to_datetime(df_superstore["FECHA_PEDIDO"])

print(df_superstore["FECHA_PEDIDO"].tail(5))


## Ver los pedidos entre dos fechas
df_query = df_superstore.query("`FECHA_PEDIDO` > '2016-01-01' and `FECHA_PEDIDO` < '2019-05-15'")
df_query = df_query[["ID_PEDIDO", "FECHA_PEDIDO", "DES_NOMBRE", "DES_APELLIDOS"]].reset_index()
df_query = df_query.drop(columns=["index"])
print(df_query.head(5))

## Ver los pedidos que tengan una fecha inferior a la fecha actual
df_query = df_query[df_query["FECHA_PEDIDO"] < pd.Timestamp.now()] ## (se pueden poner condicionales *dentro* de los selectores [])

print(df_query.tail(5))

df_query.shape ## tupla con (FILAS, COLUMNAS)


##borrar columnas no necesarias, y exportar a .xlsx
df_superstore_done = df_superstore.drop(columns=["ID_FECHA_PEDIDO", "DES_1_APELLIDO", "DES_2_APELLIDO"])

print(df_superstore_done.head(5).to_string())