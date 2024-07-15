# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:26:22 2024

@author: miguel.fuentes.vale
"""

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 90)
df1 = pd.read_csv("Ejercicio EPA/data/vehicles.csv")
df1.dropna

df1.dtypes[::-1]

print(df1.isna().sum().sum())

df_filtro = df1[["guzzler"]]
print(df_filtro)