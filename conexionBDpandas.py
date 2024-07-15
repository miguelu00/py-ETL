# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:10:22 2024

@author: miguel.fuentes.vale
@docs: ["https://refactoring.guru/es/design-patterns/singleton/python/example#example-1",
        "https://datamanagement.es/2019/10/13/proceso-etl-con-python-desde-cero-y-paso-a-paso/",
        "http://datamanagement.es/Recursos/python_parserXML.zip"]
"""
from sqlalchemy import create_engine
from threading import Lock, Thread
import urllib
import pandas as pd


class ConnectionSingleton(type):
    """
    CLASE USADA PARA IMPLEMENTAR SINGLETON SOBRE LA CLASE PRINCIPAL
    This is a thread-safe implementation of Singleton.
    Español: Implementación del Singleton a prueba de hilos
    
    Más específicamente, sincronizará los hilos que vayan inicializando
    instancias de esta clase.
    """

    _instances = {}

    _lock: Lock = Lock()
    """
    We now have a lock object that will be used to synchronize threads during
    first access to the Singleton.
    """

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        with cls._lock:
            # The first thread to acquire the lock, reaches this conditional,
            # goes inside and creates the Singleton instance. Once it leaves the
            # lock block, a thread that might have been waiting for the lock
            # release may then enter this section. But since the Singleton field
            # is already initialized, the thread won't create a new object.
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class conexionBDpandas(metaclass=ConnectionSingleton):
    '''
        CLASE PRINCIPAL

        Notifica a los demás hilos de su existencia a través de la clase
        "ConnectionSingleton" creada más arriba, especificada
        como metaclase en la declaración
    '''
    SERVER = "localhost\\SQLEXPRESS"
    DATABASE = "AdventureWorks2022"

    #Creacion de parámetros
    params = urllib.parse.quote_plus(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes")

    #Creacion de la cadena para conectarse
    conn_str = f"mssql+pyodbc:///?odbc_connect={params}"
    conn = None
    
    def __init__(self):
        if (self.conn is None):
            self.conn = create_engine(self.conn_str)
        else:
            None

    def sql_toDF(self, sqlStr):
        return pd.read_sql(sqlStr, self.conn)