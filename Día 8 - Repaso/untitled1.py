# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:10:34 2024

@author: miguel.fuentes.vale
"""
import pandas as pd

lista_ids = pd.read_json("../Ejercicio 1 - Inventario/productos.json").id
print(lista_ids)

# booleano para ver si existe o no el id
print("PC-GPTJLR" in lista_ids.values)

query_id = lista_ids.where(lambda x: x=="PC-GPTJLRd")[0]
print(query_id)