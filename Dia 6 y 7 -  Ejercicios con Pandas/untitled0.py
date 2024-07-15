# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 10:51:58 2024

@author: miguel.fuentes.vale
"""

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = dict(zip(languages, versions)) #Zip outputs: [('Java', 14), ('Python', 3), ('JavaScript', 6)]
print(result)

# Output result : {'Java': 14, 'Python': 3, 'JavaScript': 6}

import pandas as pd
inventario = pd.read_json(path_or_buf="../Día 8 - Repaso/Ejercicio 1 - Inventario/productos.json")

print(inventario[inventario["id"] == 'PC-GPTJLR'])
print(inventario.items)

print(0 == "0")

import os
import pandas as pd
import json

print(os.listdir())

df = pd.DataFrame(data=[{'id': "hola", 'nombre': "si", 'cantidad': "aberlo"}, {'id': "hola2", 'nombre': "si2", 'cantidad': "aberlo2"}], index=None)
print(dict(df))
with open("json.json", "w") as f:
    pass

os.unlink("json.json")
df.to_json("json.json", indent=4, orient="records")


df2 = pd.read_json("productos.json")
df2.to_json("json2.json", indent=4, orient="records")

print(df2)