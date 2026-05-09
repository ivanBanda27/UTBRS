from abc import ABC, abstractmethod

class MostrarInfo(ABC):
    @abstractmethod
    def mostrar_informacion(self):
        pass

class Usuario(MostrarInfo): #Permitir a los estudiantes acceder con su correo institucional.
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
        print(f" -- {self.nombre}")

profesor1 = Profesor("profesor 1")
profesor2 = Profesor("profesor 2")
profesor3 = Profesor("profesor 3")
profesor4 = Profesor("profesor 4")
profesor5 = Profesor("profesor 5")
profesor6 = Profesor("profesor 6")

profesor1.mostrar_informacion()
profesor2.mostrar_informacion()
profesor3.mostrar_informacion()
profesor4.mostrar_informacion()
profesor5.mostrar_informacion()
profesor6.mostrar_informacion()

seleccion_profe = int(input("\n Seleccione un profesor (1-6): "))

def menu_profesor(profesor):
    print(f"\nUTBRS                        | Mis Reseñas | {usuario1.correo} |\n")
    print(f"\nHas seleccionado: {profesor.nombre}\n")
    print("\n1. Ver reseñas")
    print("2. Publicar reseñas")
    opcion = int(input("\n Selecciona una opción: "))

    if opcion == 1:
        print("Ver reseñas")
    elif opcion == 2:
        print("Publicar reseñas")
    else:
        print("Opción inválida")


if seleccion_profe == 1:
    menu_profesor(profesor1)
elif seleccion_profe == 2:
    menu_profesor(profesor2)
elif seleccion_profe == 3:
    menu_profesor(profesor3)
elif seleccion_profe == 4:
    menu_profesor(profesor4)
elif seleccion_profe == 5:
    menu_profesor(profesor5)
elif seleccion_profe == 6:
    menu_profesor(profesor6)
else:
    print("Opción inválida")
