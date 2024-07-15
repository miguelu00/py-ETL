# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:34:50 2024

Aplicación simple con menú para simular una gestión 
de un fichero JSON representando el Inventario de una empresa.

@author: miguel.fuentes.vale
"""

from inventario import Inventario, Producto

def mostrarMenu():
    '''
    GESTIÓN DE INVENTARIO PYTHON - Miguel Angel FV
    
    Introduzca un número para realizar la acción deseada:
        1) Agregar producto
        2) Mostrar producto por ID o Nombre
        3) Ver todos los productos
        4) Eliminar producto por ID/Nombre
        5) Leer el fichero CSV (raw)
        6) Exportar a EXCEL
        7) Exportar a SQL SERVER (preguntar BBDD)
    
        0) GUARDAR Y SALIR
    '''
    print("""
    GESTIÓN DE INVENTARIO PYTHON - Miguel Angel FV
    
    Introduzca un número para realizar la acción deseada:
        1) Agregar producto
        2) Mostrar producto por ID o Nombre
        3) Ver todos los productos
        4) Eliminar producto por ID/Nombre
        5) Leer el fichero CSV (raw)
        6) Exportar a EXCEL
        7) Exportar a SQL SERVER (preguntar BBDD)
    
        0) GUARDAR Y SALIR
    """)

# Aquí creo la instancia de Inventario para usar sus métodos
inventario = Inventario()
inventario.cargar_fichero()

while (True):
    
    try:
        mostrarMenu()
        opcion = int(input("Opción: "))
        
        # Coloco los métodos en un diccionario; esto es similar
        ## a usar un SWITCH en cualquier otro lenguaje
        ### Sacado de aquí https://codedamn.com/news/python/switch-case-statement
        opciones = {
            0: "salir",
            1: Producto.pedirProducto,
            2: inventario.get_productoID,
            3: inventario.cargar_fichero,
            4: inventario.eliminar_producto,
            5: inventario.leerFichero,
            6: inventario.exportar_EXCEL,
            7: inventario.exportar_MSserver
        }
            
        if (opcion not in opciones):
            print("Introduzca una opción que esté en la lista!")
            continue
        
        if (opcion == 0):
            inventario.guardar_cambios()
            break
        
        # Ejecutar la acción, pasandole como índice la opc. seleccionada.
        if (opcion == 1):  # Si se trata de la primera opción, le deberé pasar como argumento el objeto Inventario creado al inicio
            opciones[opcion](inventario)
        else:
            opciones[opcion]()
        
        Inventario.pedir_continuar()
    except ValueError: #Ignoro este error sacado por un df.query() en la opción de buscar por ID; TODO -> Arreglarlo
        print()
    except Exception as e:
        print("El valor introducido no es válido o está vacío, inténtelo de nuevo!")
        print(repr(e))