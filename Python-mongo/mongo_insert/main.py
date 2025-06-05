from insert_data import insertar_usuario

if __name__ == "__main__":
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    edad = int(input("Edad: "))

    insertar_usuario(nombre, correo, edad)
