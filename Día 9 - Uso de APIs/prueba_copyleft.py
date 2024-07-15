import sys
import json
import requests as req
import pandas as pd

def conectarYComprobar(url: str, parm: dict=None, headrs: dict=None):
    if (parm is not None and headrs is not None):
        response = req.get(url, params=parm, headers=headrs)
    elif (parm is not None):
        response = req.get(url, parm)
    else:
        response = req.get(url)
    print(f"Codigo de respuesta para {url}: {response.status_code}")
    return response

respuesta2 = conectarYComprobar(url="https://api.opensource.org/licenses/copyleft")

res_obj = json.dumps(respuesta2.json(), indent=4)

print(res_obj)

res_obj = json.JSONDecoder().decode(res_obj)
#Pasar esta información JSON, a un DATAFRAME

datos_series = list()
for licencia in res_obj:
    
    links = list()
    for link in licencia["links"]:
        links.append(link["url"])
    
    texts = list()
    for texto in licencia["text"]:
        texts.append(texto["url"])
    
    identifiers = list()
    for ident in licencia["identifiers"]:
        identifiers.append(ident)
    
    serie = pd.Series({
        "id": licencia["id"],
        "identifiers": str(identifiers),
        "links": str(links),
        "name": licencia["name"],
        "other_names": licencia["other_names"],
        "superseded": licencia["superseded_by"],
        "keywords": str(licencia["keywords"]),
        "urls": str(texts)
    })
    datos_series.append(serie)

df = pd.DataFrame()
if (len(datos_series) > 0):
    df = pd.DataFrame(datos_series)
    
print(df.head(10))