# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 19:15:20 2024

@author: miguel.fuentes.vale
"""

import re
import pandas as pd

res = re.findall(pattern=r'^PC-', string="PC-1234")

df = pd.DataFrame([{1: "a", 2: "e"}, {1: "j", 2: "u"}])

print(df[df[1] == "a"])

print(type(res))
print(res)
print(len("res ".strip()))