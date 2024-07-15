import json
import random
import string
from typing import List, TypedDict


class Producto(TypedDict):
    id: str
    nombre: str
    cantidad: int
    precio: float


def generate_custom_id() -> str:
    """
    Genera un ID único para un producto.

    El ID tiene el formato 'PC-XXXXXX' donde 'XXXXXX' es una combinación
    de 6 caracteres aleatorios que pueden ser letras mayúsculas o dígitos.

    Returns:
        str: El ID generado.
    """
    random_chars = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"PC-{random_chars}"


def escribir_fichero(
    inventario: List[Producto], filename: str = "productos.json"
) -> None:
    """
    Escribe el inventario en un archivo JSON.

    Args:
        inventario (List[Producto]): La lista del inventario.
        filename (str): El nombre del archivo donde se guardará el inventario.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(inventario, file, indent=4)


def cargar_inventario(filename: str = "productos.json") -> List[Producto]:
    """
    Carga el inventario desde un archivo JSON.

    Args:
        filename (str): El nombre del archivo desde donde se cargará el inventario.

    Returns:
        List[Producto]: La lista del inventario.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def agregar_producto(
    inventario: List[Producto], nombre: str, cantidad: int, precio: float
) -> None:
    """
    Agrega un producto al inventario.

    Args:
        inventario (List[Producto]): La lista del inventario.
        nombre (str): El nombre del producto a agregar.
        cantidad (int): La cantidad del producto a agregar.
        precio (float): El precio del producto a agregar.
    """
    producto: Producto = {
        "id": generate_custom_id(),
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio,
    }
    inventario.append(producto)
    print(f"Producto agregado: {producto['nombre']} (ID: {producto['id']})")
    escribir_fichero(inventario)


def eliminar_producto(inventario: List[Producto], consulta: str) -> None:
    """
    Elimina un producto del inventario por su ID o nombre.

    Args:
        inventario (List[Producto]): La lista del inventario.
        consulta (str): El ID o nombre del producto a eliminar.
    """
    for producto in inventario:
        if producto["id"] == consulta or producto["nombre"].lower() == consulta.lower():
            inventario.remove(producto)
            print(f"Producto eliminado: {producto['nombre']}")
            escribir_fichero(inventario)
            break
    else:
        print("Producto no encontrado.")


def mostrar_inventario(inventario: List[Producto]) -> None:
    """
    Muestra todos los productos en el inventario.

    Args:
        inventario (List[Producto]): La lista del inventario.
    """
    if not inventario:
        print("El inventario está vacío.")
    else:
        for producto in inventario:
            print(
                f"ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']} €"
            )


def consultar_producto(inventario: List[Producto], consulta: str) -> None:
    """
    Consulta un producto en el inventario por su ID o nombre.

    Args:
        inventario (List[Producto]): La lista del inventario.
        consulta (str): El ID o nombre del producto a consultar.
    """
    for producto in inventario:
        if producto["id"] == consulta or producto["nombre"].lower() == consulta.lower():
            print(
                f"Producto encontrado: ID: {producto['id']}, Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']} €"
            )
            break
    else:
        print("Producto no encontrado.")


def mostrar_menu() -> None:
    menu = """
    ## Bienvenido al Sistema de Inventario ##
    1. Agregar producto al inventario
    2. Eliminar producto del inventario
    3. Mostrar inventario
    4. Consultar producto
    5. Salir
    """
    print(menu)


def main():
    inventario = cargar_inventario()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").lower()

        match opcion:
            case "1" | "agregar" | "a":
                nombre = input("Nombre del producto: ")
                while True:
                    try:
                        cantidad = int(input("Cantidad del producto: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico para la cantidad.")
                while True:
                    try:
                        precio = float(input("Precio del producto: "))
                        break
                    except ValueError:
                        print("Por favor, ingrese un valor numérico para el precio.")
                agregar_producto(inventario, nombre, cantidad, precio)
            case "2" | "eliminar" | "e":
                consulta = input("ID o nombre del producto a eliminar: ")
                eliminar_producto(inventario, consulta)
            case "3" | "mostrar" | "m":
                mostrar_inventario(inventario)
            case "4" | "consultar" | "c":
                consulta = input("ID o nombre del producto a consultar: ")
                consultar_producto(inventario, consulta)
            case "5" | "salir" | "q" | "quit":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Por favor, elige una opción correcta.")


if __name__ == "__main__":
    main()
