import csv
import re


def extract_user(URL):
    github_user = ""
    url = URL.strip()

    """
    # Opción 1 usando removeprefix:
    github_user = url.removeprefix("https://github.com/")

    
    #Opción 2: Usando search y extrayando información con grupos
    matches = re.search(r"^https?://(?:www\.)?github\.(?:.+)/(.+)$", url, re.IGNORECASE)
    if matches:
        return matches.group(1) 

    """
    # Opción 3: Usando el operador walrus
    if matches := re.search(
        r"^https?://(?:www\.)?github\.(?:.+)/(.+)$", url, re.IGNORECASE
    ):
        return matches.group(1)
    return github_user


def validar_username(username):
    return re.fullmatch(r"[A-Za-z][A-Za-z0-9_.]{4,19}", username) is not None


def validar_telefono(telefono):
    telefono_sin_prefijo = re.sub(r"\+\s?34", "", telefono)
    telefono_limpio = re.sub(r"[^\d]", "", telefono_sin_prefijo)
    return re.match(r"[9|6|7|8][0-9]{8}$", telefono_limpio) is not None


def validar_email(email):
    # HTML Estandar: r"/^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/"
    return re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE)


def leer_usuarios_validos(archivo_entrada):
    campos = ["username", "telefono", "email", "github_username"]
    usuarios_validos = []

    try:
        with open(archivo_entrada, mode="r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo, fieldnames=campos)
            next(lector)
            for usuario in lector:
                if (
                    validar_username(usuario["username"])
                    and validar_telefono(usuario["telefono"])
                    and validar_email(usuario["email"])
                ):
                    usuario["github_username"] = extract_user(
                        usuario["github_username"]
                    )
                    usuarios_validos.append(usuario)
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo_entrada}")
        return

    return usuarios_validos


if __name__ == "__main__":
    usuarios_validos = leer_usuarios_validos("usuarios_db.csv")
    if usuarios_validos:
        print("Los siguientes usuarios son válidos:")
        for usuario in sorted(
            usuarios_validos, key=lambda usuario: usuario["username"]
        ):
            print(
                f"El usuario {usuario["username"]} con email {usuario["email"]}, es válido"
            )
    else:
        print("No se encontraron usuarios válidos para guardar.")
