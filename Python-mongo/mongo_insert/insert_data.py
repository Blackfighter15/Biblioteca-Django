from config import get_database

def insertar_usuario(nombre, correo, edad):
    db = get_database()
    coleccion = db["usuarios"]

    nuevo_usuario = {
        "nombre": nombre,
        "correo": correo,
        "edad": edad
    }

    resultado = coleccion.insert_one(nuevo_usuario)
    print(f"Usuario insertado con ID: {resultado.inserted_id}")
