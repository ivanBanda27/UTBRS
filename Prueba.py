from abc import ABC, abstractmethod

class MostrarInfo(ABC):
    @abstractmethod
    def mostrar_informacion(self):
        pass

class Usuario(MostrarInfo):
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Correo: {self.correo}")

    def validar_correo(self, dominio):
        while not self.correo.endswith(dominio):
            print("Ingrese un dominio válido.")
            self.nombre = input("Ingrese su nombre: ")
            self.apellido = input("Ingrese su apellido: ")
            self.correo = input("Ingrese su correo: ")

        self.mostrar_informacion()
        print(f"\n----- Bienvenido/a {self.nombre} -----\n")
        print(f"\nUTBRS                        | Mis Reseñas | {self.correo} |\n")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
correo = input("Ingrese su correo: ")

usuario1 = Usuario(nombre, apellido, correo)
usuario1.validar_correo("@utb.edu.co")

class Profesor(MostrarInfo):
    def __init__(self, nombre):
        self.nombre = nombre

    print("\n--- Lista de profesores ---\n")

    def mostrar_informacion(self):
        print(f"  --  {self.nombre}")

    def publicar_reseña(self, autor):
        texto = input("Escribe tu reseña: ")

        archivo = f"{self.nombre.lower().replace(' ', '')}.txt"

        try:
            with open(archivo, "r") as f:
                contenido = f.read()
                id_reseña = contenido.count("---") + 1
        except FileNotFoundError:
            id_reseña = 1

        with open(archivo, "a") as f:
            f.write(f"id:{id_reseña}\n")
            f.write(f"autor:{autor}\n")
            f.write(f"texto:{texto}\n")
            f.write("---\n")

        print(f"\nReseña publicada exitosamente.")

profesor1 = Profesor("Profesor 1")
profesor2 = Profesor("Profesor 2")
profesor3 = Profesor("Profesor 3")
profesor4 = Profesor("Profesor 4")
profesor5 = Profesor("Profesor 5")
profesor6 = Profesor("Profesor 6")

profesor1.mostrar_informacion()
profesor2.mostrar_informacion()
profesor3.mostrar_informacion()
profesor4.mostrar_informacion()
profesor5.mostrar_informacion()
profesor6.mostrar_informacion()

def menu_profesor(profesor):
    print(f"\nUTBRS                        | Mis Reseñas | {usuario1.correo} |\n")
    print(f"\nHas seleccionado: {profesor.nombre}\n")

    while True:
        print("\n1. Ver reseñas")
        print("2. Publicar reseñas")
        opcion = int(input("\n Selecciona una opción: "))

        if opcion == 1:
            print("Ver reseñas")
            break
        elif opcion == 2:
            profesor.publicar_reseña(usuario1.correo)
            break
        else:
            print("\nOpción inválida")


while True:
    seleccion_profe = int(input("\nSeleccione un profesor (1-6): "))

    if seleccion_profe == 1:
        menu_profesor(profesor1)
        break
    elif seleccion_profe == 2:
        menu_profesor(profesor2)
        break
    elif seleccion_profe == 3:
        menu_profesor(profesor3)
        break
    elif seleccion_profe == 4:
        menu_profesor(profesor4)
        break
    elif seleccion_profe == 5:
        menu_profesor(profesor5)
        break
    elif seleccion_profe == 6:
        menu_profesor(profesor6)
        break
    else:
        print("\nOpción inválida")