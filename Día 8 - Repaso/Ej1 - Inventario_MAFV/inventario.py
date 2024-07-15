# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:35:34 2024

Clases Inventario y Producto; la primera se usa para gestionar
instancias y eliminar/modificar entidades de Producto en un
fichero JSON. 
La segunda (Producto) se usa para dar forma a dichas entidades
Producto, incluye un generador de campos ID

@author: miguel.fuentes.vale
"""
import pandas as pd
import random as rng
import json
import re
import os


class Inventario():
    '''
        Clase para gestionar una lista (inventario) de diccionarios
        (producto)
    '''
    listado_productos = pd.DataFrame()
    lista_list = list()
    inventarioJson = "lista_inventario.json"
    
    def __init__(self, inventarioJson = "lista_inventario.json"):
        '''
        Se sobrescribe el constructor para que busque
        primero si existen productos en el fichero JSON.
        Si los encuentra, actualizar el listado de productos local.
        '''
        #Crear el fichero json si no existe
        if (inventarioJson not in os.listdir()):
            with open(inventarioJson, "w") as f:
                f.writelines("[]")
            
        self.inventarioJson = inventarioJson
        self.listado_productos = pd.read_json(self.inventarioJson)
    
    def listar_ids_inventario(self):
        '''
        Actualizará la lista de productos, y recuperar un objeto 
        Series con los ID de todos los productos.

        Returns
        -------
        pd.Series
            Listado de IDs como un obj. Series de Pandas.

        '''
        self.recuperar_todos()
        return self.listado_productos.id
    
    def listar_ids(self):
        ''' TODO - ARREGLAR ESTE MÉTODO
        Consultar el JSON de inventario de esta clase, y sacar
        un obj. Series con la columna ID

        Parameters
        ----------
        inventarioJson : TYPE
            DESCRIPTION.

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        productos = pd.read_json(path_or_buf=self.inventarioJson)
        if (productos.empty):
            return pd.Series(None)
        else:
            return productos.id
    
    def leerFichero(self):
        with open(self.inventarioJson, "r") as f:
            print(f.read())
    
    def get_productoID(self):
        id_o_nombre = input("Introduce el ID o Nombre de producto a consultar: ").strip()
        if (len(re.findall(pattern=r'^PC-', string=id_o_nombre)) >= 1):
            res = self.listado_productos.query(f"id == '{id_o_nombre}'")
        else:
            res = self.listado_productos.query(f"nombre == '{id_o_nombre}'")
        if (res.empty != True):
            print(res)
        else:
            print("El producto con ID/Nombre indicado no se ha encontrado!")
    
    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario
    
        Args:
            · producto (dict): El diccionario con los detalles del producto a agregar.
            (Se entiende que se quiere almacenar una lista [list] de diccionarios
             [dict])
        """
        self.lista_list.append(producto)
        if (self.guardar_cambios()):
            print(f"Producto agregado: {producto['nombre']}")
        else:
            print("ERROR al almacenar el producto deseado!")

    def exportar_EXCEL(self):
        nombreExcel = input("Nombre del fichero EXCEL: ")
        excelSheet = input("Nombre hoja principal: ")
        hecho = self.listado_productos.to_excel(excel_writer=nombreExcel, sheet_name=excelSheet)
        if (hecho):
            print("Fichero excel EXPORTADO correctamente!")
        else:
            print("ERROR al exportar el inventario actual a excel!")
    
    def exportar_MSserver(self):
        from sqlalchemy import create_engine
        nombreServer = input("Nombre del servidor SQL Server:")
        nombreDB = input("Nombre de la base de datos:")
        
        conn_db = create_engine(f"mssql+pyodbc://{nombreServer}/{nombreDB}?driver=ODBC+Driver+17+for+SQL+Server")
        
        sql_str = f"""
            CREATE TABLE [inventario] (
                ID VARCHAR(8) NOT NULL,
                nombre VARCHAR(255),
                cantidad int,
                precio float
            )
        """
        try:
            self.listado_productos.to_sql("inventario", conn_db, if_exists="fail")
        except ValueError as e:
            print("La tabla ya existe! Seguro que desea sobrescribir sus datos?")
            if (input("[y/n]: ") == "y"):
                hecho = self.listado_productos.to_sql("inventario", conn_db, if_exists="replace")
            else:
                print("Exportación cancelada!")
                return
        print(f"Hecho! Datos guardados en la tabla 'inventario' de la bbdd {nombreDB}")

    def recuperar_todos(self) -> pd.DataFrame:
        self.listado_productos = pd.read_json(path_or_buf=self.inventarioJson)
        return self.listado_productos
    
    def eliminar_producto(self) -> bool:
        id_o_nombre = input("Introduce un nombre o ID de producto a eliminar: ")
        
        try:
            if (len(re.findall(pattern=r'^PC-', string=id_o_nombre)) >= 1):
                res = self.listado_productos[self.listado_productos['id'] == id_o_nombre]
                self.lista_list.pop(res.index[0]) #eliminar, primero de la lista local
            else:
                res = self.listado_productos[self.listado_productos['nombre'] == id_o_nombre]
                self.lista_list.pop(res.index[0]) #eliminar, primero de la lista local
            if (res.empty != True):
                # Eliminar producto POR ÍNDICE si se ha encontrado...
                self.listado_productos = self.listado_productos.drop(res.index)
                self.guardar_cambios() #... y después del DataFrame guardado. Se guardan los cambios en el fichero JSON externo
                
                print(f"Producto {id_o_nombre} eliminado correctamente!")
                return True
            else:
                # Si no, mostrar un error
                print("No se ha podido encontrar el producto indicado")
                return False
        except Exception as e:
            print("ERROR! No se ha podido encontrar el producto indicado")

    def guardar_cambios(self):
        # Convertir self.lista_ids (lista de diccionarios) a self.listado_productos (DataFrame)
        self.listado_productos = pd.DataFrame(self.lista_list)
        
        # Eliminar el archivo JSON existente
        if os.path.exists(self.inventarioJson):
            os.unlink(self.inventarioJson)
        
        # Guardar el DataFrame en un archivo JSON con el formato adecuado
        self.listado_productos.to_json(self.inventarioJson, indent=4, orient="records")
        
        print("Cambios guardados.")
        return True
    
    def cargar_fichero(self):
        with open(self.inventarioJson, "r") as f:
            self.lista_list = json.load(fp=f)
        
        self.listado_productos = pd.read_json(path_or_buf=self.inventarioJson)
        print("Fichero cargado correctamente!")
        print(self.listado_productos)
        
    @staticmethod
    def pedir_continuar():
        input("Enter para continuar...")

class Producto():
    
    def __init__(self, nombre: str, cantidad: int, precio: float, inventario: Inventario):
        self.id = self.generarIdUnico(inventario)
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def generarIdUnico(self, inventario) -> str:
        '''
        Tratará de generar un ID único con el siguiente formato
        PC-12345, donde "12345" pueden ser tanto números como letras,
        en cualquier orden.

        Parameters
        ----------
        inventario : TYPE
            DESCRIPTION.

        Returns
        -------
        str
            DESCRIPTION.

        '''
        #Primero, revisar los IDs que ya existan en el sistema
        ids = inventario.listar_ids()
        id_unico = "PC-" + self.__generarLetras()
        while (id_unico in ids.values):
            id_unico = "PC-" + self.__generarLetras()
        return id_unico
    
    def __generarLetras(self) -> str:
        # Coloco números en la lista, ya que en el ejemplo también se usan para identificar a los productos
        letras = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        salida = ""
        rand = rng.Random()
        for i in range(1, 6):
            salida += letras[rand.randint(0, len(letras))]
        return salida

    @staticmethod
    def pedirProducto(inventario: Inventario) -> None:
        nombre = input("Nombre del producto: ")
        cantidad = input("Stock disponible: ")
        precio = input("Precio del producto: ")
        
        try:
            if (nombre.strip() == "" or cantidad.strip() == "" or precio.strip() == ""):
                raise Exception
            else:
                # Si se introducen bien los datos, crear un nuevo objeto Producto, y 
                #  pasarle los datos introducidos + un ID nuevo generado automáticamente
                prod = Producto(nombre, int(cantidad), float(precio), inventario)
                
                producto = {
                    "id": prod.__getid__(),
                    "nombre": prod.__getnombre__(),
                    "cantidad": prod.__getcantidad__(),
                    "precio": prod.__getprecio__()
                }
                
                inventario.agregar_producto(producto)
            
        except Exception as e:
            print(str(e))
            print("Los datos introducidos no son válidos!")
        else:
            print("Producto introducido correctamente!")

    def __getid__(self):
        return self.id
    
    def __getnombre__(self):
        return self.nombre
    
    def __getcantidad__(self):
        return self.cantidad

    def __getprecio__(self):
        return self.precio
    
    def __setnombre__(self, nombre):
        self.nombre = nombre
    
    def __setcantidad__(self, cantidad):
        self.cantidad = cantidad
    
    def __setprecio__(self, precio):
        self.precio = precio
        
    def __str__(self):
        return f"Producto ID. {self.id} -- {self.nombre} | Cantidad: {self.cantidad} | Precio: {self.precio}"