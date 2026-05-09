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
    def __init__(self, nombre, apellido, materia):
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia

    print("\n--- Lista de profesores ---\n")

    def mostrar_informacion(self):
        print(f"    {self.nombre} {self.apellido}")

profesor1 = Profesor("Yuranis", "Henriquez", "POO")
profesor2 = Profesor("Eder", "Barrios", "Cálculo Diferencial")
profesor3 = Profesor("Kelly", "Tarrá", "Inglés IV")


profesor1.mostrar_informacion()
profesor2.mostrar_informacion()
profesor3.mostrar_informacion()
