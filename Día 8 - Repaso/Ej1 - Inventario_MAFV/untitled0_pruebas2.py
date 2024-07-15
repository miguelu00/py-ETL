# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 12:50:28 2024

@author: miguel.fuentes.vale
"""

import pandas as pd
import sqlalchemy as sql
import json

class Excepcion(Exception):
    juan = "aguayo al ataque"

try:
    raise Excepcion
    df = pd.read_clipboard(sep=',')
    print(df)
except Excepcion as E:
    print("O NO: " + E.juan)

DATABASE = "AdventureWorks2022"
SERVER = "localhost\\SQLEXPRESS"

conn = sql.create_engine(f"mssql+pyodbc://{SERVER}/{DATABASE}?driver=ODBC+Driver+17+for+SQL+Server")

df2 = pd.read_sql("SELECT BusinessEntityID, NationalIDNumber, JobTitle, BirthDate, SUBSTRING(MaritalStatus, 1, 2) AS MaritalStatus FROM HumanResources.Employee", conn)

print(df2)

datos = None
with open("lista_inventario.json", "r") as f:
    datos = json.load(f)

print(datos)
print(datos[0])
print(type(datos[0]))

df3 = pd.read_sql("SELECT TOP 10 NationalIDNumber FROM HumanResources.Employee", conn)

print(df3)